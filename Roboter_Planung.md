# Planung des Roboters

## Features des Roboters
### Demente Personen zum Zimmer bringen
* mehrere Zielpunkte: Tür erkennen (2-3)
* mehrere Startpunkte möglich
    * Möglicherweise Problem bereitend, da es schwierig wird zu Beginn erkennen, wo 
    * der Roboter sich als Startpunkt befindet. Vllt. fester Startpunkt, von dem man den Roboter 
    * aus Abholt oder mit Bodenmarkieren gesamter Raum eingrenzbar...

### Zukünftig mögliche Erweiterungen
* Roboter kann ins Zimmer der Patienten fahren

### Spezififizierung der Zielgruppe
* nicht mobile Demenz-Patienten
* mit Hilfsmitteln(z.B.: Krückstock) mobile Demenz-Patienten
* mobile Demenz-Patienten

### Mögliche Technische Umsetzung  
#### Raum-Orientierung:
* Der Roboter erkennt mithilfe eines 360° Laserscanner(Lidar/ToF) Modules seine Umgebung:
Er sollte mithilfe aller Messpunkte eine Karte seiner Umgebung erstellen und dadurch seine 
eigene Position herausfinden und analysieren, wo er hinfahren soll. Die Software dazu, soll aus Basis 
von Ros 2 (Robot Operating System) entwickelt werden.
Am besten unterstützt und am weitesten verbreitet in der günstigen Preisklasse sind die Sensoren von RPLidar.
Das günstigste Modell, der "A1M8" kostet auf den ersten Blick so 120-140€. Je nach Budget kann man es sicherlich auch
mit selbstgebauten Sensoren oder Ersatzteilen/Ausschlachtungen von Saugrobotern probieren.
* Zuvor macht der Roboter eine Analysefahrt, um die Umgebung zu analysieren und damit man die Türen 
der Bewohner einspeichern kann. 
    * Alternativ könnte man mit Markierungen an den Türen, Wänden oder Boden arbeiten.
    * Ros 2 kann man relativ einfach mit der opencv-Library ergänzen.
    * Essenzieller, schwierig umsetzbarer Teil des Projekts, Umgehen des Problems gilt schwierig.

<!---
##### Benötigte Navigationsdaten
* "Orientierungspunkte" : 

   -Kreuzungen  
   -Abbiegungen  
   -dead ends
   -Startpunkte  
   -Zielpunkte  

 * Entfernung zischen "Orientierungspunkten"

 * Kreuzungsausgänge    
--->
#### Gestaltung des Roboters:
* Wir tendieren dazu, den Roboter mit zwei Hard- und Software-Instanzen zu gestalten. 
Das bedeutet genauer, dass wir einen Raspberry Pi/Jetson Nano oder anderen Single-Board-Computer, oder 
sogar alternativ auf Home-Servern die komplexere Sensordatenverarbeitung und das Kartographieren laufen lassen, 
und auf einem Arduino/Esp/Microcontroller die Motoren steuern und Sensordaten aufzunehmen.
Die Kommunikation könnte über I2C, UART/USB, oder wahrscheinlich weniger praktisch für den Arduino SPI funktionieren.
* Der Roboter sollte einen sicheren, gut manövrierbaren Aufbau haben und er muss in seiner natürlichen Umgebung 
keine großen Hindernisse überfahren können. Ob Meccanum-Wheels oder Omni-Directional-Wheels von Vorteil sind
gilt es herauszufinden. Aber wahrscheinlich würde eine simple Panzersteuerung mit 4 Rädern oder Ketten am besten funktionieren.
Denkbar wäre auch die Nutzung von zwei Rädern für besseres Wenden/Drehen.
* Aus Gründen der Sichtbarkeit für die Nutzer und schnelleren Entwicklung und späteren Ergänzungen kann der Roboter
problemlos etwas größer sein. Eine Grundfläche von 0.25 qm könnte man anpeilen, obwohl mit der Größe auch weitere
Anforderungen an Material und Motoren hinzukommen. Voraussichtlich arbeiten wir größtenteils mit 
3D-Druck Plastik Komponenten. Für das Grundchassis und Schrauben/Muttern oder vergleichbares könnten andere Materialien genutzt werden.
* Um ein stabiles Fahrverhalten gewährleisten zu können, sollten Motoren und Akkus am tiefsten gelegt sein. Der 360° Lidar 
sollte für bessere Sicht an wichtigen Objekten und eine gesamte Umsicht ganz oben, an der "Spitze" des Roboters
befestigt sein. 
* (es ist denkbar sich an modernen Staubsaugerobotern zu orientieren)
#### Personen-Erkennung
* Mit einem RFID-Chip wird erkannt, um welche Person es sich handelt.


# Materialliste  

* 360° Lidar/Laser/ToF Sensor. Idee: RPLidar A1M8, sonst alternative DIY-Lösungen suchen
* RFID Leser und Transponder *(Wir haben einen in der Schule)*
* Motoren (Enocoder, Stepper?) *(Stepper ebenfalls, obwohl ich glaube, dass Gleichstrom-Motoren mit Encoder besser geeignet sind)*
* Akku, ggf. Ladegerät
* Single-Board-Computer (Jetson Nano, Raspberry Pi), vielleicht auch mit uhs-1 64er SD-Karte, obwohl ich 32er habe.
* Microcontroller/Erweiterter Microcontroller, *(Auch teilweise in Schule)*
* gy 521/mpu 6050 als Beispiel für günstiges Gyroskop/Beschleunigungssensor
* *Weitere Sensoren als Ergänzung für den Lidar, zum Beispiel Tiefgelegte Leisten mit Buttons oder Kameras.
Auch während der Entwicklung neue Dinge, welche hilfreich sind, wie Displays, Switches, Dinge für Nutzerinteragierung usw., neue Ideen werden folgen...*
* Räder

