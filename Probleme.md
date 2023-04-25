# Probleme

## Lidar Sensor

### 'bringup' error: Lidar Sensor wird nicht gestartet  ![siehe](Bilder\ScreenshotBringupUpperHalf.png)  

#### - mögliche Ursachen:

1. Probleme mit dem USB-Port ()

##### Lösungsversuche:

    - Umstecken des USB Kabels vom Sensor (von obenLinks nach obenRechts)
    > Gescheitert
    - sudo chmod a+rw /dev/ttyUSB0 (es wird angenommen dass 'USB0' der gewünschte Port ist)
    > Gescheitert
    - Ändern von "port: /dev/ttyUSB2" zu "/ttyUSB0" in '/tmp/launch_params_uuc1pnvx' (es wird laut 'bringup'-logs angenommen, dass dies die Datei mit den Einstellungen für den Lidar-Launch sind)
    > Änderung vom System verweigert

#### - Workaround:

1. Per 'cd' zum Directory: '/launch' navigieren 
2. Launch Datei ('ros2 launch hls_lfcd_lds_driver hlds_laser.launch') starten, die nicht per 'bringup' gestartet worden konnte

- ![/scan topic](Bilder\rqt\rqtLidarRunning-19.4.png) wird ausgegeben 
- RViz ist nicht in der Lage die Daten des Sensors auszugeben ![siehe](Bilder\RVizError_inProgramm-15.4.png)
  >Error: "fixed-frame missing"  