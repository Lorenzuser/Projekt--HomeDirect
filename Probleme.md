# Probleme

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
