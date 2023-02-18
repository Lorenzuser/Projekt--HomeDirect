# Planung des Roboters

## Features des Robotors
### Demente Personen zum Zimmer bringen
* mehrere Zielpunkte: Tür erkennen (2-3)
* mehrere Startpunkte möglich
    * Möglicherweise Problembereitend, da es schwierig wird zu Beginn erkennen, wo 
    * der Roboter sich als Startpunkt befindet. Vllt. Fester Startpunkt, von dem man aus Abholt 
    * Oder mit Bodenmarkieren gesamter Raum eingrenzbar...

### Zuküntig mögliche Erweiterungen
* Roboter kann ins Zimmer der Patienten fahren

### Spezififierung der Zielgruppe
* nicht mobile Demenz-Patienten
* mit Hilfsmitteln(z.B.: Krückstock) mobile Demenz-Patienten
* mobile Demenz-Patienten


### Mögliche Techniche Umsetung
#### Raum-Orientierung:
* Der Roboter erkennt mithilfe eines 360° Laserscanner(Lidar/ToF) Modules seine Umgebung:
Er sollte mithilfe aller Messpunkte eine Karte seiner Umgebung erstellen und dadurch seine 
eigene Position herausfinden und analysieren, wo er hinfahren soll.
* Zuvor macht der Roboter eine Analysefahrt, um die Umgebung zu analysieren und damit man die Türen 
der Bewohner einspeichern kann. 
    * Alternativ könnte man mit Markierungen an den Türen, Wänden oder Boden arbeiten.
    * Essenzieller, schwierig umsetbarer Teil des Projekts, Umgehen des Problemes gilt schwierig

#### Personen-Erkennung
* Mit einem RFID-Chip wird erkannt um welche Person es sich handelt.
