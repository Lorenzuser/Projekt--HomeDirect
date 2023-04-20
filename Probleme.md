# Probleme

## Lidar Sensor

### 'bringup' error: Lidar Sensor wird nicht gestartet ( [siehe](Bilder\ScreenshotBringupUpperHalf.png) )  

#### - Workaround:
1. Per 'cd' zum Directory: '/launch' navigieren 
2. Launch Datei ('ros2 launch hls_lfcd_lds_driver hlds_laser.launch') starten, die nicht per 'bringup' gestartet worden konnte
- [/scan topic](Bilder\rqt\rqtLidarRunning-19.4.png) wird ausgegeben 
- RViz ist nicht in der Lage die Daten des Sensors auszugeben ([siehe]()) 
  >Error: "fixed-frame missing"  