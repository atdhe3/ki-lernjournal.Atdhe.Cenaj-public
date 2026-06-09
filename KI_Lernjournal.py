import os
from datetime import datetime
import sqlite3

import pandas as pd
import streamlit as st
from google import genai


DB_FILE = "lernjournal.db"


st.set_page_config(
    page_title="KI-Lernjournal",
    page_icon="📘",
    layout="wide"
)


def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        st.error("Gemini API Key wurde nicht gefunden.")
        st.info('Setze den Key im Terminal mit: $env:GEMINI_API_KEY="DEIN_API_KEY"')
        st.stop()

    return genai.Client(api_key=api_key)


client = get_gemini_client()


def ask_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        return response.text
    except Exception as e:
        st.error("Fehler bei der Verbindung mit Gemini.")
        st.write(e)
        return None


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reflexionen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datum TEXT,
            name TEXT,
            projekt TEXT,
            ziel TEXT,
            was_lief_gut TEXT,
            was_war_schwierig TEXT,
            was_wurde_gelernt TEXT,
            vertiefung TEXT,
            zusammenfassung TEXT,
            feedback TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_entry(entry):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO reflexionen (
            datum,
            name,
            projekt,
            ziel,
            was_lief_gut,
            was_war_schwierig,
            was_wurde_gelernt,
            vertiefung,
            zusammenfassung,
            feedback
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        entry["datum"],
        entry["name"],
        entry["projekt"],
        entry["ziel"],
        entry["was_lief_gut"],
        entry["was_war_schwierig"],
        entry["was_wurde_gelernt"],
        entry["vertiefung"],
        entry["zusammenfassung"],
        ""
    ))

    conn.commit()
    conn.close()


def load_data():
    conn = sqlite3.connect(DB_FILE)
    data = pd.read_sql_query("SELECT * FROM reflexionen", conn)
    conn.close()

    if data.empty:
        return None

    return data


def save_feedback(reflexion_id, feedback):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE reflexionen
        SET feedback = ?
        WHERE id = ?
    """, (feedback, reflexion_id))

    conn.commit()
    conn.close()


init_db()


st.title("KI-Lernjournal für Lernende")

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Bereich auswählen",
    [
        "Dashboard Lernende",
        "Neue Reflexion",
        "Lernjournal",
        "Berufsbildner Dashboard"
    ]
)


if menu == "Dashboard Lernende":
    st.header("Dashboard Lernende")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Willkommen, Sara")
        st.write("Hier kannst du eine neue Reflexion starten oder dein Lernjournal ansehen.")
        st.info("Wähle links in der Navigation den Bereich 'Neue Reflexion'.")

    with col2:
        st.subheader("Dein Fortschritt")

        data = load_data()

        if data is not None:
            st.metric("Gespeicherte Reflexionen", len(data))
            st.metric("Projekte", data["projekt"].nunique())
        else:
            st.metric("Gespeicherte Reflexionen", 0)
            st.metric("Projekte", 0)

    st.divider()

    st.subheader("Letzte Reflexionen")

    data = load_data()

    if data is not None:
        st.dataframe(data.tail(3)[["datum", "name", "projekt", "zusammenfassung"]])
    else:
        st.info("Noch keine Reflexionen vorhanden.")


elif menu == "Neue Reflexion":
    st.header("Neue Reflexion starten")

    st.write("Beantworte zuerst die Fragen. Danach erstellt die KI Rückfragen und eine Zusammenfassung.")

    name = st.text_input("Name der lernenden Person", "Sara Meier")
    projekt = st.text_input("Projektname", "Website-Projekt")

    st.subheader("Schritt 1: Reflexionsfragen")

    antwort_1 = st.text_area("Was war das Ziel deiner Projektphase?")
    antwort_2 = st.text_area("Was lief gut?")
    antwort_3 = st.text_area("Was war schwierig?")
    antwort_4 = st.text_area("Was hast du gelernt?")

    if st.button("KI-Rückfragen erstellen"):
        if not antwort_1 or not antwort_2 or not antwort_3:
            st.warning("Bitte beantworte zuerst mindestens die ersten drei Fragen.")
        else:
            prompt = f"""
Du bist ein KI-Lernjournal für Lernende im Bereich Digital Business.

Die lernende Person hat eine Projektphase reflektiert.
Erstelle 2 bis 3 einfache Rückfragen, damit die Reflexion konkreter wird.

Die Rückfragen sollen:
- einfach verständlich sein
- nicht zu lang sein
- zur Ausbildung als Entwicklerin oder Entwickler Digital Business passen
- helfen, genauer über Learnings und Schwierigkeiten nachzudenken

Projekt: {projekt}

Ziel der Projektphase:
{antwort_1}

Was lief gut:
{antwort_2}

Was war schwierig:
{antwort_3}

Was wurde gelernt:
{antwort_4}
"""

            rueckfragen = ask_gemini(prompt)

            if rueckfragen:
                st.session_state["rueckfragen"] = rueckfragen
                st.success("KI-Rückfragen wurden erstellt.")

    if "rueckfragen" in st.session_state:
        st.subheader("Schritt 2: KI-Rückfragen")
        st.write(st.session_state["rueckfragen"])

        vertiefung = st.text_area("Ergänze deine Antworten zu den Rückfragen:")

        if st.button("Zusammenfassung erstellen"):
            prompt = f"""
Du bist ein KI-Lernjournal für Lernende im Bereich Digital Business.

Erstelle aus den folgenden Antworten eine kurze und klare Zusammenfassung.
Schreibe in einfachem Schweizer Standarddeutsch.

Verwende genau diese Struktur:

1. Was lief gut?
2. Was war herausfordernd?
3. Was wurde gelernt?
4. Nächster Schritt

Die Zusammenfassung soll für die lernende Person und den Berufsbildner verständlich sein.

Name: {name}
Projekt: {projekt}

Ziel der Projektphase:
{antwort_1}

Was lief gut:
{antwort_2}

Was war schwierig:
{antwort_3}

Was wurde gelernt:
{antwort_4}

Ergänzungen durch Rückfragen:
{vertiefung}
"""

            zusammenfassung = ask_gemini(prompt)

            if zusammenfassung:
                st.session_state["zusammenfassung"] = zusammenfassung
                st.session_state["entry"] = {
                    "datum": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "name": name,
                    "projekt": projekt,
                    "ziel": antwort_1,
                    "was_lief_gut": antwort_2,
                    "was_war_schwierig": antwort_3,
                    "was_wurde_gelernt": antwort_4,
                    "vertiefung": vertiefung,
                    "zusammenfassung": zusammenfassung
                }

    if "zusammenfassung" in st.session_state:
        st.subheader("Schritt 3: Zusammenfassung")
        st.write(st.session_state["zusammenfassung"])

        if st.button("Im Lernjournal speichern"):
            save_entry(st.session_state["entry"])
            st.success("Die Reflexion wurde im Lernjournal gespeichert.")


elif menu == "Lernjournal":
    st.header("Persönliches Lernjournal")

    data = load_data()

    if data is not None:
        st.write("Hier werden alle gespeicherten Reflexionen angezeigt.")

        st.dataframe(data[["datum", "name", "projekt", "zusammenfassung", "feedback"]])

        st.subheader("Detailansicht")

        selected_project = st.selectbox(
            "Projekt auswählen",
            data["projekt"].unique()
        )

        selected_data = data[data["projekt"] == selected_project].tail(1).iloc[0]

        st.write("Projekt:", selected_data["projekt"])
        st.write("Datum:", selected_data["datum"])
        st.write("Zusammenfassung:")
        st.write(selected_data["zusammenfassung"])

        if selected_data["feedback"]:
            st.write("Feedback Berufsbildner:")
            st.write(selected_data["feedback"])
        else:
            st.info("Noch kein Feedback vorhanden.")

    else:
        st.info("Noch keine Reflexionen gespeichert.")


elif menu == "Berufsbildner Dashboard":
    st.header("Dashboard Berufsbildner")

    data = load_data()

    if data is not None:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Anzahl Reflexionen", len(data))

        with col2:
            st.metric("Anzahl Lernende", data["name"].nunique())

        with col3:
            st.metric("Anzahl Projekte", data["projekt"].nunique())

        st.subheader("Lernende auswählen")

        selected_name = st.selectbox(
            "Lernende Person",
            data["name"].unique()
        )

        filtered = data[data["name"] == selected_name]

        st.subheader(f"Reflexionen von {selected_name}")
        st.dataframe(filtered[["id", "datum", "projekt", "zusammenfassung", "feedback"]])

        st.subheader("Feedback schreiben")

        selected_reflexion_id = st.selectbox(
            "Reflexion auswählen",
            filtered["id"].tolist()
        )

        feedback = st.text_area("Feedback des Berufsbildners")

        if st.button("Feedback speichern"):
            save_feedback(selected_reflexion_id, feedback)
            st.success("Feedback wurde gespeichert.")
            st.write("Feedback:")
            st.write(feedback)

    else:
        st.info("Noch keine gespeicherten Reflexionen vorhanden.")