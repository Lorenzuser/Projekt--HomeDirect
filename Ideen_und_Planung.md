# Planung des Roboters und mögliche Ideen:

## Features des Roboters
### Ein Roboter bringt demente Personen zum Zimmer. Das beinhaltet:
* mehrere Zielpunkte werden angefahren: (Tür erkennen (2-3))
* mehrere Startpunkte sind möglich.
* Es wird mit dem Nutzer interagiert.
    <!---
    * Möglicherweise Problem bereitend, da es schwierig wird zu Beginn erkennen, wo 
    * der Roboter sich als Startpunkt befindet. Vllt. fester Startpunkt, von dem man den Roboter 
    * aus abholt oder mit Bodenmarkieren gesamter Raum eingrenzbar...
    --->
### Zukünftig mögliche Erweiterungen
* Roboter kann ins Zimmer der Patienten fahren
* Roboter transportiert Gegenstände
* Roboter interagiert **sozial** mit Patienten

### Spezifizierung der Zielgruppe
* mobile Demenz-Patienten 
* mobile Demenz-Patienten mit Hilfsmitteln(z.B. Krückstock, Rollator)
* *(nicht mobile Demenz-Patienten)*

# Mögliche technische Umsetzungen  
## Raum-Orientierung:
### Option A:
* Der Roboter erkennt mithilfe eines 360° Laserscanner(Lidar/ToF)-Modules seine Umgebung:
Er sollte mithilfe aller Messpunkte eine Karte seiner Umgebung erstellen und dadurch seine 
eigene Position herausfinden und analysieren, wo er hinfahren soll. Die Software dazu, soll auf Basis 
von Ros 2 (Robot Operating System) entwickelt werden.
Am besten unterstützt und am weitesten verbreitet in der günstigen Preisklasse sind die Sensoren von RPLidar.
Das günstigste Modell, der "A1M8" kostet auf den ersten Blick so 120-140€. Je nach Budget kann man es sicherlich auch
mit selbstgebauten Sensoren oder Ersatzteilen/Ausschlachtungen von Saugrobotern probieren.
* Zuvor macht der Roboter eine Analysefahrt, um die Umgebung zu analysieren und damit man die Türen der Bewohner einspeichern kann. 
    * Alternativ könnte man mit Markierungen an den Türen, Wänden, Decke oder Boden arbeiten.
    * Ros 2 kann man relativ einfach mit der opencv-Library ergänzen.
    
### Option B:
* Vor Verwendung des Roboters werden Markierungen auf dem Boden angebracht. Diese könnten auf Basis kontrastreicher Linien aufbauen. Der Roboter orientiert sich anhand dieser, um den Weg zu den Räumen zu finden. Als Sensoren werden Farbsensoren oder Helligkeitssensoren verwendet.
* Der Roboter könnte eine Analysefahrt machen, um auch bei komplexer werdenden räumlichen Gegebenheiten, den kürzesten Weg zu finden. 

### Option C
* Es werden ähnliche Markierungen auf dem Boden oder der Decke angebracht. Diese werden mithilfe einer optischen Kamera, anstatt punktueller Sensoren erkannt. 

### Option D
* Markierungen am Boden, wie B,jedoch mit zusätzlichen kleineren Markierugen an Kreuzungen, die jeweils die richtige Route zum Zimmer angeben (Verlässlichkeit varriiert).
# Chassis des Roboters:
## Anforderungen:
- Es sollte gut erkennbar für seine Nutzer sein.
    > *Könnte möglicherweise auch als Gehhilfe dienen.*
- Es sollte ein gutes Fahrverhalten auf ebenen Flächen haben.
- Sollte Motoren-Encoder zur Positionsbestimmung haben.
## Mögliche Umsetzungen:
> **Denkbar sind alle Möglichkeiten mit der Nutzung von 2/4 Rad-Motorisierung oder Ketten. Immer wird eine Panzersteuerung verwendet. Als Ergänzung ist die Möglichkeit der Nutzung von Meccanum-Wheels oder Omni-Wheels heranziebar.**
### Option A:
- Aus 3D-Druck-Plastik-Komponenten könnte ein mehretagiger Roboter gebaut werden, der den jeweiligen Anforderungen entspricht. Die Räder und ggf. Schrauben/Muttern und andere Hardware werden ergänzend hinzugezogen.
### Option B:
- Die Hardware wird auf einem Roboter-Bauset angebracht und ggf. ergänzt.
> Diese Version des Roboters währe mehr als Prototy zu sehen, mit dessen Hilfe die Grundsätzliche Funtktionsweise eines möglichen weiter entwickelten Roboters demonstriert wird. 
### Option C:
- Ein Rollator wird motorisiert und entsprechend den Anforderungen umgebaut. 
> siehe z.B.: Räder von E-Scootern
### Option D:
- Design mit Ähnlichkeiten zu Robotern, die menschliche Anwesenheit emulieren sollen, mit evtl. denkbaren Display sowie Personenhöhe
> Problematik Kosten
### Option E:
- Modifizierter Servicebot
> Problematik Kosten
### Oprion F:
- Modifizierter Staubsaugerroboter mit bereits vorhandenen Sensoren zur Orienttierung
> Problematik: Erkennbarkeit

## Hardware-Gestaltung des Roboters
### Idee 1:
- Der Roboter besteht aus zwei Hard- und Software-Instanzen. 
Das bedeutet genauer, dass wir einen Raspberry Pi/Jetson Nano oder anderen Single-Board-Computer für komplexe Anwendungen nutzen und mit einem Arduino/Esp/Microcontroller die Motoren steuern und Sensordaten aufnehmen. Die Kommunikation könnte über I2C, UART/USB oder SPI funktionieren. 
### Idee 2:
- Alternativ könnte komplexe und rechenintensive Aufgaben auf Home-Servern laufen, sowie ggf. komplexere Sensordatenverarbeitung und das Kartographieren. Weiterhin würde das direkte interagieren mit Sensoren/Motoren auf einem Arduino/Esp/Microcontroller geschehen.
### Idee 3:
- Wir könnten die gesamte Software und Hardware-Interaktion so simpel gestalten, dass wir alles über einen oder mehren Arduino/Esp/Microcontroller verarbeiten.

## Personen-Erkennung
### Option 1
- Mit einem RFID-Chip wird erkannt, um welche Person es sich handelt.
### Option 2
- Gesichtserkennung



# Materialliste mit möglichen Teilen:

* 360° Lidar/Laser/ToF Sensor. Idee: RPLidar A1M8, sonst alternative DIY-Lösungen suchen
* Farb- oder Helligkeitssensoren
* RFID Leser und Transponder *(Wir haben einen in der Schule)*
* Motoren (Enocoder, Stepper?) *(Stepper ebenfalls, obwohl ich glaube, dass Gleichstrom-Motoren mit Encoder besser geeignet sind)*
* Akku, ggf. Ladegerät *(Gute 7.4 V Akkus gibt es in der Schule)*
* Single-Board-Computer (Jetson Nano, Raspberry Pi), vielleicht auch mit uhs-1 64er SD-Karte, obwohl ich 32er habe.
* Microcontroller/Erweiterter Microcontroller, *(Auch teilweise in Schule)*
* gy 521/mpu 6050 als Beispiel für günstiges Gyroskop/Beschleunigungssensor
* *Weitere Sensoren als Ergänzung für den Lidar, zum Beispiel Tiefgelegte Leisten mit Buttons oder Kameras.
Auch während der Entwicklung neue Dinge, welche hilfreich sind, wie Displays, Switches, Dinge für Nutzerinteraktion usw., neue Ideen werden folgen...*

