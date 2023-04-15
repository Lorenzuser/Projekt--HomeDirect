# Projekttagebuch

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
  >mit Workaround gelöst (15.4)
- Lidar ansteuerbar mit 'ros2 launch hls_lfcd_lds_driver hlds_laser.launch' wenn im '/launch' Directory per 'cd'
   >Lidardaten nicht per RViz anzeigbar
