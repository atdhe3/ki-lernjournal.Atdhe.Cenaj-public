# KI-Lernjournal für Lernende

## Projektbeschreibung

Das KI-Lernjournal ist ein Prototyp für Lernende im Bereich Digital Business. Die Anwendung unterstützt Lernende dabei, ihre Projektphasen besser zu reflektieren.

Die lernende Person beantwortet zuerst Reflexionsfragen zu einer Projektphase. Danach erstellt Google Gemini passende Rückfragen, damit die Reflexion konkreter und weniger oberflächlich wird. Anschliessend erstellt die KI eine strukturierte Zusammenfassung. Diese Reflexion wird lokal gespeichert und kann später im Lernjournal oder im Berufsbildner-Dashboard angezeigt werden.

Der Prototyp zeigt den zentralen Ablauf der Lösung: Reflexion starten, KI-Rückfragen erhalten, Zusammenfassung erstellen, Reflexion speichern und Feedback durch den Berufsbildner erfassen.

---

## Verwendete Tools und Technologien

- Python
- Streamlit
- Google Gemini API
- SQLite
- Pandas
- Git
- GitHub
- Visual Studio Code

---

## Features

### Dashboard Lernende

Die lernende Person sieht eine einfache Startseite mit einer Übersicht über gespeicherte Reflexionen und Projekte.

### Neue Reflexion

Die lernende Person kann eine neue Reflexion starten und mehrere Fragen beantworten, zum Beispiel:

- Was war das Ziel deiner Projektphase?
- Was lief gut?
- Was war schwierig?
- Was hast du gelernt?

### KI-Rückfragen

Google Gemini erstellt auf Basis der Antworten passende Rückfragen. Diese helfen der lernenden Person, genauer über ihre Erfahrungen, Schwierigkeiten und Learnings nachzudenken.

### KI-Zusammenfassung

Aus den Antworten und den Ergänzungen erstellt Gemini eine strukturierte Zusammenfassung mit folgender Struktur:

1. Was lief gut?
2. Was war herausfordernd?
3. Was wurde gelernt?
4. Nächster Schritt

### Persönliches Lernjournal

Gespeicherte Reflexionen werden im Lernjournal angezeigt. Die lernende Person kann frühere Einträge ansehen und ihre Entwicklung nachvollziehen.

### Berufsbildner-Dashboard

Der Berufsbildner kann gespeicherte Reflexionen ansehen, eine lernende Person auswählen und Feedback zu einer Reflexion erfassen.

### Feedback-Funktion

Der Berufsbildner kann direkt im Prototyp Feedback schreiben. Dieses Feedback wird gespeichert und bei der Reflexion angezeigt.

### Lokale Speicherung

Die Reflexionen werden lokal in einer SQLite-Datenbank gespeichert. Die Datenbankdatei wird automatisch erstellt.


---

## Setup-Anleitung

### 1. Projekt herunterladen oder klonen

Das Repository kann über GitHub heruntergeladen oder mit Git geklont werden:

```bash
git clone <repository-link>
cd ki-lernjournal
```

Alternativ kann das Projekt als ZIP-Datei heruntergeladen und in Visual Studio Code geöffnet werden.

---

### 2. Benötigte Pakete installieren

Falls eine Datei `requirements.txt` vorhanden ist, können die Pakete so installiert werden:

```bash
pip install -r requirements.txt
```

Falls keine `requirements.txt` vorhanden ist, können die Pakete auch direkt installiert werden:

```bash
pip install streamlit pandas google-genai
```

---

### 3. Gemini API-Key setzen

Für die KI-Funktion wird ein Google Gemini API-Key benötigt.

In Windows PowerShell kann der API-Key so gesetzt werden:

```powershell
$env:GEMINI_API_KEY="DEIN_API_KEY"
```

Wichtig: Der API-Key darf nicht direkt im Code gespeichert und nicht auf GitHub hochgeladen werden.

Ob der API-Key gesetzt ist, kann mit folgendem Befehl geprüft werden:

```powershell
echo $env:GEMINI_API_KEY
```

---

### 4. App starten

Die Anwendung wird mit folgendem Befehl gestartet:

```bash
python -m streamlit run KI_Lernjournal.py
```

Danach öffnet sich die App normalerweise automatisch im Browser.

Falls sich der Browser nicht automatisch öffnet, kann die lokale Adresse manuell geöffnet werden, zum Beispiel:

```text
http://localhost:8501
```

---

## Nutzung des Prototyps

1. App starten.
2. Links in der Navigation den Bereich **Neue Reflexion** auswählen.
3. Name der lernenden Person und Projektname eingeben.
4. Reflexionsfragen beantworten.
5. Auf **KI-Rückfragen erstellen** klicken.
6. Die Rückfragen der KI lesen.
7. Ergänzende Antworten zu den Rückfragen eingeben.
8. Auf **Zusammenfassung erstellen** klicken.
9. Die KI-Zusammenfassung prüfen.
10. Auf **Im Lernjournal speichern** klicken.
11. Im Bereich **Lernjournal** die gespeicherte Reflexion ansehen.
12. Im Bereich **Berufsbildner Dashboard** eine lernende Person auswählen.
13. Feedback schreiben und speichern.

---

## Screenshots des Prototyps

### Dashboard Lernende

Das Dashboard zeigt der lernenden Person eine Übersicht über gespeicherte Reflexionen und Projekte. Von hier aus kann sie eine neue Reflexion starten oder das Lernjournal öffnen.

![Dashboard Lernende](screenshots/Screenshot%20Dashboard%20Lernende.png)

---

### Neue Reflexion starten

In diesem Screen gibt die lernende Person ihren Namen, den Projektnamen und die Antworten auf die Reflexionsfragen ein. Die Fragen helfen dabei, die Projektphase strukturiert zu reflektieren.

![Neue Reflexion starten](screenshots/Screenshot%20Neue%20Reflexion.png)

---

### KI-Rückfragen

Nachdem die ersten Antworten eingegeben wurden, erstellt Google Gemini passende Rückfragen. Diese helfen der lernenden Person, ihre Reflexion zu vertiefen.

![KI-Rückfragen](screenshots/Screenshot%20KI%20Rückfragen.png)

---

### Ergänzende Antworten

Die lernende Person ergänzt ihre Antworten zu den Rückfragen der KI. Dadurch wird die Reflexion genauer und persönlicher.

![Ergänzende Antworten](screenshots/Screenshot%20KI%20Rückfragen%20ergänzungen.png)

---

### Zusammenfassung

Aus den Antworten erstellt Gemini eine strukturierte Zusammenfassung. Diese enthält die wichtigsten Punkte: Was lief gut, was war herausfordernd, was wurde gelernt und was der nächste Schritt ist.

![KI-Zusammenfassung](screenshots/Screenshot%20KI%20Lernjournal%20Zusammenfassung.png)

---

### Reflexion speichern

Die fertige Zusammenfassung kann im Lernjournal gespeichert werden. Nach dem Speichern zeigt die App eine Bestätigung an.

Screenshots\Screenshot Reflexion gespeichert.png

---

### Persönliches Lernjournal Dashboard

Im Lernjournal werden alle gespeicherten Reflexionen angezeigt. Die lernende Person kann frühere Einträge ansehen und die Zusammenfassung nochmals lesen.

Screenshots\Screenshot Dashboard Lernende.png

---

### Detailansicht im Lernjournal

In der Detailansicht sieht die lernende Person die vollständige Zusammenfassung einer gespeicherten Reflexion sowie vorhandenes Feedback.

Screenshots\Screenshot Lernjournal Detailansicht.png

---

### Berufsbildner Dashboard

Im Berufsbildner-Dashboard sieht der Berufsbildner wichtige Kennzahlen, gespeicherte Reflexionen und die Auswahl der Lernenden.

Screenshots\Screenshot Berufsbildner Dashboard.png

---

### Feedback speichern

Der Berufsbildner kann zu einer Reflexion Feedback schreiben. Dieses Feedback wird gespeichert und später im Lernjournal angezeigt.

Screenshots\Screenshot Feedback Speichern.png

---


## Hinweise zur Nutzung

- Der Prototyp läuft lokal auf dem eigenen Computer.
- Für die KI-Funktion ist ein gültiger Gemini API-Key notwendig.
- Der API-Key darf nicht direkt im Code gespeichert werden.
- Die Daten werden lokal in einer SQLite-Datenbank gespeichert.
- Im Prototyp sollten keine echten sensiblen Daten eingegeben werden.
- Der Prototyp ist noch nicht für den produktiven Einsatz gedacht, sondern dient zur Demonstration der Idee und des Ablaufs.

---

## Datenschutz-Hinweis

Reflexionen können persönliche Informationen enthalten. Deshalb sollten im Prototyp nur Testdaten verwendet werden.

Für eine spätere echte Umsetzung müssten zusätzliche Datenschutzmassnahmen umgesetzt werden, zum Beispiel:

- Benutzerlogin
- Rollenrechte für Lernende und Berufsbildner
- sichere Speicherung der Daten
- klare Regeln zur Sichtbarkeit der Reflexionen
- Schutz des API-Keys
- Löschmöglichkeit für gespeicherte Einträge

---

## Prototyp-Typ

Der Prototyp ist ein horizontaler und explorativer Prototyp.

Er zeigt mehrere zentrale Bereiche der Anwendung, ohne dass alle Funktionen vollständig produktiv umgesetzt sind. Im Fokus stehen der Ablauf, die Nutzerführung und die Verständlichkeit der Idee.

Der Prototyp eignet sich, um früh Feedback von Lernenden und Berufsbildnern einzuholen.

---

## Mögliche Weiterentwicklungen

- Login für Lernende und Berufsbildner
- Rollen- und Rechtekonzept
- Export der Reflexionen als PDF
- bessere Filter- und Suchfunktionen
- Fortschrittsübersicht über mehrere Projektphasen
- automatische Erkennung von Schwierigkeiten und Learnings
- Benachrichtigung, wenn Feedback vorhanden ist
- sicherere Speicherung in einer externen Datenbank

---

## Autor

Atdhe Cenaj