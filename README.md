# Sternzeichen Matching – Mehrsprachige Sternzeichen-Kompatibilitätsanwendung

#### Author1: Euijoon Lee / [2219038]
#### Video: https://youtube.com/shorts/kNLxoHt7Hc8?feature=share
#### Description:

## Projektüberblick

Zodiac Match ist eine webbasierte Anwendung, die mit Python und dem Flask-Framework entwickelt wurde. Ziel des Projekts ist es, eine interaktive Plattform zu erstellen, auf der Nutzer ihr Sternzeichen bestimmen, die Kompatibilität mit einem Partner überprüfen und eine passende Person empfohlen bekommen können.

Die Anwendung unterstützt drei Sprachen: Englisch, Deutsch und Koreanisch. Die Sprache der Benutzeroberfläche passt sich automatisch an die Browsersprache des Nutzers an. Dadurch wird eine bessere Benutzerfreundlichkeit erreicht und gleichzeitig das Konzept der Internationalisierung (i18n) demonstriert.

Das Projekt kombiniert Backend-Logik, algorithmische Auswertung von Kompatibilität und eine benutzerfreundliche Weboberfläche in einer strukturierten Flask-Anwendung.

---

## Funktionen

### 1. Bestimmung des Sternzeichens

Nach Eingabe von Name und Geburtsdatum wird automatisch das entsprechende Sternzeichen berechnet. Anschließend zeigt das System:

- Das eigene Sternzeichen
- Drei besonders kompatible Sternzeichen
- Drei weniger kompatible Sternzeichen

Die Logik zur Bestimmung der Sternzeichen befindet sich in `zodiac.py`.

---

### 2. Partner-Kompatibilitätsprüfung

Die erste Hauptfunktion ermöglicht es, die Kompatibilität mit einer bestimmten Person zu überprüfen.

Nach Eingabe von:
- Name des Partners
- Geburtsdatum des Partners

berechnet das System die Kompatibilität zwischen beiden Sternzeichen und generiert eine entsprechende Ergebnisnachricht. Die Berechnung erfolgt in `compatibility.py`.

Die Ausgabe wird mithilfe des Templates `result.html` dynamisch dargestellt :contentReference[oaicite:0]{index=0}.

---

### 3. Zufällige Empfehlung einer kompatiblen Person

Die zweite Funktion empfiehlt eine Person aus einer gespeicherten Liste von Profilen.

Dabei:
- wird die Kompatibilität mit allen gespeicherten Personen berechnet,
- die höchste Kompatibilitätsstufe ermittelt,
- und zufällig eine Person unter den besten Treffern ausgewählt.

Diese Funktion demonstriert einfache Bewertungs- und Auswahlalgorithmen.

---

### 4. Mehrsprachigkeit (Internationalisierung)

Die Übersetzungslogik ist in `i18n.py` implementiert. Alle Texte der Benutzeroberfläche werden dynamisch abhängig von der Browsersprache geladen.

Ein Beispiel dafür ist das Eingabefeld für das Geburtsdatum: Das Anzeigeformat passt sich automatisch der Sprache des Browsers an. Wenn der Browser beispielsweise auf Koreanisch eingestellt ist, erscheint die Datumsanzeige entsprechend in koreanischer Form.

Diese Designentscheidung verbessert die Benutzerfreundlichkeit und zeigt die praktische Umsetzung von Internationalisierung.

---

## Dateistruktur und Aufgaben der einzelnen Dateien

### `app.py`

Diese Datei enthält die Hauptanwendung. Sie:
- definiert die Routen,
- verarbeitet Formulareingaben,
- verbindet die Logik aus den anderen Modulen,
- rendert die HTML-Templates.

Sie fungiert als zentrale Steuerungseinheit der Anwendung.

---

### `zodiac.py`

Diese Datei enthält:
- die Logik zur Bestimmung des Sternzeichens,
- Definitionen kompatibler und inkompatibler Sternzeichen.

Die Auslagerung dieser Logik verbessert die Übersichtlichkeit und Modularität.

---

### `compatibility.py`

Hier befindet sich:
- die Berechnung der Kompatibilität,
- die Bewertungslogik,
- der Empfehlungsalgorithmus.

Durch die Trennung vom Hauptprogramm bleibt der Code strukturiert und wartbar.

---

### `i18n.py`

Diese Datei verwaltet:
- Übersetzungsdaten,
- Sprachzuordnung,
- dynamische Textausgabe.

Das modulare Konzept ermöglicht eine einfache Erweiterung um weitere Sprachen.

---

### `result.html`

Dieses Template:
- zeigt das Ergebnis der Berechnung an,
- verwendet dynamische Platzhalter,
- enthält ein modernes, kartenbasiertes Design mit CSS,
- bietet Navigationsoptionen zurück zur vorherigen Seite oder zur Startseite :contentReference[oaicite:1]{index=1}.

Das Design wurde bewusst minimalistisch und benutzerfreundlich gestaltet.

---

## Designentscheidungen

1. **Modularer Aufbau**  
   Die Trennung in mehrere Python-Dateien verbessert Wartbarkeit und Lesbarkeit.

2. **Trennung von Logik und Darstellung**  
   Die Backend-Logik wird in Python implementiert, während die Darstellung durch HTML-Templates erfolgt. Dies orientiert sich am MVC-Prinzip.

3. **Internationalisierung statt fest kodierter Texte**  
   Alle Texte werden dynamisch geladen, was die Anwendung erweiterbar und professioneller macht.

4. **Einfache, nachvollziehbare Algorithmen**  
   Das Kompatibilitätssystem basiert auf regelbasierten Bewertungen. Ziel war nicht astrologische Genauigkeit, sondern eine saubere algorithmische Umsetzung.

5. **Benutzerfreundliches Interface**  
   Die Anwendung nutzt ein klares Layout mit Kartenstruktur und Farbverlauf-Hintergrund, um eine moderne Benutzeroberfläche zu schaffen.

---

## Mögliche Weiterentwicklungen

- Integration einer Datenbank statt statischer Profillisten
- Benutzerkonten und Login-System
- Erweiterung des Kompatibilitätsalgorithmus
- REST-API-Version der Anwendung
- Unterstützung weiterer Sprachen

---

## Fazit

Dieses Projekt demonstriert:

- Webentwicklung mit Flask
- Strukturierte Python-Programmierung
- Internationalisierung (i18n)
- Algorithmische Bewertungssysteme
- Trennung von Backend- und Frontend-Logik

Die Anwendung verbindet technische Konzepte mit einer benutzerfreundlichen Oberfläche und zeigt grundlegende Prinzipien moderner Softwareentwicklung.