# Projektdokumentation Tagebuch 2023

## Samstag 18.2

- erstes gemeinsames Meeting

## Samstag 25.2

-

## Donerstag 2.3

- Meeting
- Projektname gewählt

## Montag 6.3

- Meeting
- Tabele Marktrecherche

## Mittwoch 8.3

- Ubuntu und ROS2(Lorenz) auf PC installiert

## Freitag 10.3

## Sonntag 12.3

- ROS2 "Hello world"
- Meeting.
- ROS leicht besprochen.
- Außerdem haben wir uns für unseren Prototyp-Roboter entschieden, der wahrscheinlich Thema unseres gesamten Projektes sein wird. Unsere Wahl ist auf den Turtlebot3 Burger gefallen. Dieser wird von der Open Robotics Foundation als offizieller Education, Research und Prototyping Roboter vermarktet. Deshalb haben wir den Vorteil mit diesem Kit, besonders im Vergleich zu der Alternative, einen Roboter von Grund auf zusammenzustellen und zu entwickeln, dass dessen Software-Entwicklung besser dokumentiert ist und wir weniger Zeit für die Hardware-Entwicklung investieren müssen. Ab jetzt beginnt das allgemeine Arbeitspaket: 'Prototyp Turtle'

# **Prototyp Turtle:**
>
> **Aufgabenpakete:**
>
>1. Betriebssystem auswählen
>1. Treiber installieren und testen
>1. Workspace/Environment schaffen
>1. Auf SLAM basierend fahren können
>1. Premapping und SLAM kombinieren und benutzerfreundlich und transportabel gestalten.
>1. Zusätzliche Patienten-Hilfe und Funktionen implementieren
>
## Montag 13.3

- 'turtlesim' ausprobiert

## Donnerstag 17.3

- Roboter angekommen und aufgebaut

## Samstag 18.3.23 *(Punkt 1.)*

- Da der Turtlebot 2016 realeased wurde, hat der LDS-01 Sensor keine offizielle Unterstützung für die neueste ROS2-Version "Humble Hawksbill". Somit werden wir zu Beginn die vorherige LTS-Version "Foxy Fitzroy" mindestens auf dem Turtlebot(Pi) verwenden.

## Sonntag 19.3.23 *(Punkt 2.)*

-Heute konnte ich feststellen, da ich die Treibern und die Distribution von Source installiert habe, dass es wahrscheinlch möglich wäre zur neueren ROS2 Distribution "Humble Hawksbill" zu migrieren. Trotzdem habe ich die Installation wie im [offiziellen e-manual](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/) beschrieben, vorgenommen um zu Beginn des Projektes Zeit zu sparen.

## 20-26.3

- Etablierung WiFi Verbindung Roboter mit Pc per Linux (ssh)
- SetUp OpenCr

## 20-27.3  

- Bringup
- Teleoperation funktionsfähig
  - Controler (DS4)-Support in Arbeit
- Simulation Fuktionsfähig
  - Map erstellbar
  - Position des Roboters auf Map vermerkbar -> wird geupdatet
  - Roboter kann zu Position fahren (inkonsistente Erfolgsrate)
- Probleme in Kommunikation zwischen PC und TurtleBot3 beim *topic monitor* und *SLAM*
  - "ros2 topic list" funtioniert nur auf Roboter, aber nicht per "ssh ubuntu@ubuntu"

## 28.3-1.4

- Probleme in Kommunikation 'TB3 zu PC' festgestellt
  - Teleoperation hat aufgehört zu funktionieren
  - SLAM-Node(vorgefertigt) wird nicht korrekt ausgeführt (keine Karte wird erstellt)

## 2-9.4

- Problem in Komunikation u.a. von Netzwerkkonfiguration verursacht (!)
  - Problem identifiziert und Lösungsweg gefunden (' "StackOverflow-Link" hier einfügen')
- Lidar-Sensor hängt mit SLAM-Problem zusammen
  - es wird keine gemeinsame Kommunikation aufgebaut

## 10.4-16.4

- Problematiken mit Schulnetzwerk im Zusammenhang zu unserer Gerätekommunikation festgestellt
  - Problem gelöst: "hgoIntern" als nutzbar anzunehmen
- Teleoperation wieder funktionsfähig
- Treiberprobleme des Lidars festgestellt
  - [Treiber](https://github.com/ROBOTIS-GIT/hls_lfcd_lds_driver) scheinen trotz Instalation nicht direkt abrufbar zu sein  
  >mit Workaround gelöst* (15.4)
- Lidar ansteuerbar mit 'ros2 launch hls_lfcd_lds_driver hlds_laser.launch' wenn im '/launch' Directory per 'cd'
   >Lidardaten nicht per RViz anzeigbar(, 'Fixed Frame-Error' per RViz manuell)![Fehler: vorgefertigte Launch-File](Bilder\RVizError_inProgramm-15.4.png)

## 21.4

- Gemeinsames Meeting
- Ursache von Lidarproblemen weiter spezifiziert
- ~~vermutliche Datei zum Wechseln von Launchparametern des Lidars gefunden~~

## 28.4

- Gemeinsames Meeting
- (Neukonfigurieren des TB3 vorgeschlagen)

## 04.05

- Lidar-Error in 'bringup' behoben
- Ubuntu auf Laptop von Lorenz als Dualboot installiert.
- Sensor gibt korrekt Werte aus und published über OpenWrt-Reiserouter Werte zum Laptop, wo sie visualisiert werden können.
![Bild aus RViz, ausführen von SLAM-Demo_Node](https://github.com/Lorenzuser/Projekt--HomeDirect/blob/17e1c41fca42d6a0e66bb64d89665e6b644c044f/Bilder/4.5-RViz.png)

## 5.5

- Die SLAM-Node zum erstellen der Karte funktioniert sehr gut. Man könnte ggf. als Enhancement eine Funktion zur Unterstützung von einem Controller hinzufügen
- Die Navigation funktioniert *out of the box* nicht. Als nächsten Schritt probiere ich unabhängig vom [Emanual](https://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/#navigation) die Navigation zu schreiben.
- Erstellung einer Gazebo-World auf VirtualBox versucht, jedoch Probleme mit Leistung festgestellt

## 6.5

- ~~Ubuntu auf Desktop-Pc von Alex als Dualboot installiert (nvm :(  )~~

## 7.5

- Fake Node Simulation-Tutorial abgeschlossen (A)

## 11.5

- RFID RC 522 mit zweitem Raspberry Pi verkabelt
- TurtleBot-Image auf Raspberry kopiert
- Änderung an 'config-5.4.0-1028-raspi' unten angehängt (Abweichung vom Tutorial):  
device_tree_param=spi=on  
dtoverlay=spi-bcm2708

## 12.5

- raspi-config auf Pi (Alex) installiert um evtl. SPI für RFID zu aktivieren  
Funktionsfähigkeit noch unklar

## 13.5

- Dependencys für 'raspi-config' und anderes auf dem Pi gefixt ('sudo apt --fix broken install')
- Programm Lesen und Schreiben RFID für Pi mit Python geschrieben dank [Tutorial](https://pimylifeup.com/raspberry-pi-rfid-rc522/)

## 14.5

- Ubuntu 22.4 auf Desktop-Pc von Alex als Dualboot installiert
  - ROS2 Humble installiert (debian) sowie TB3 und Nav2 Packages)

## 15.5

- [ROS2-Documentation Tutorial für Colcon](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html) fortgeführt bis "Creating a workspace"

# 16.5

- ROS2 Workspace lokal auf Alex's Desktop konfiguriert
- Übungs- ROS2-Package sowie Node erstellt

# Projektdokumentation: Problemlösung

## Lidar Sensor

### 'bringup' error: Lidar Sensor wird nicht gestartet  ![siehe](Bilder\ScreenshotBringupUpperHalf.png)

#### mögliche Ursachen

1. Probleme mit dem USB-Port ()

##### Lösungsversuche

    - Umstecken des USB Kabels vom Sensor 
      (von obenLinks nach obenRechts)
    > Gescheitert
      (... nach untenLinks dazu MotorControl umgesteckt)
    > Gescheitert , TeleOp scheint nicht zu gehen
    - sudo chmod a+rw /dev/ttyUSB0 (es wird angenommen dass 'USB0' der gewünschte Port ist)
    > Gescheitert
    - Ändern von "port: /dev/ttyUSB2" zu "/ttyUSB0" in '/tmp/launch_params_uuc1pnvx' (es wird laut 'bringup'-logs angenommen, dass dies die Datei mit den Einstellungen für den Lidar-Launch sind)
    > Änderung vom System verweigert
    - hlds_laser.launch.py bearbeiten: ttyUSB0 -> ttyUSB2; laser -> base_scan
    > Gescheitert

2. Allgemeine Komplikationen mit der Launchdatei von 'bringup' (als Ursache identifiziert)

#### Lösungsversuche  

    - '/turtlebot3_bringup/share/turtlebot3_bringup/launch' bearbeiten (bei GitHub-Repo des Roboters 
    auffindbar)
    > ~~nicht auf Ubuntu des Roboters auffindbar~~
    > Funktioniert
    - Roboter mit neuer SD-Karte in Ruhe nach Anleitung neu konfigurieren

#### - Workaround

1. Per 'cd' zum Directory: '/launch' navigieren
2. Launch Datei ('ros2 launch hls_lfcd_lds_driver hlds_laser.launch') starten, die nicht per 'bringup' gestartet worden konnte

- ![/scan topic](Bilder\rqt\rqtLidarRunning-19.4.png) wird ausgegeben
- RViz ist nicht in der Lage die Daten des Sensors auszugeben ![siehe](Bilder\RVizError_inProgramm-15.4.png)
  >Error: "fixed-frame missing"  