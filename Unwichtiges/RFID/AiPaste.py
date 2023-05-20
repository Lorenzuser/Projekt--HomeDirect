#ACHTUNG: Kopierter, nicht angepasster, unvollständig Kommentierter Code !
# SetUP für RFID Modell RC522
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
#Erlaube 'string' für ROS2 per Package
from std_msgs.msg import String
#Fähigkeit zu Erstellung von nodes ect.
import rclpy

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('rc522_reader')

    pub = node.create_publisher(String, 'rfid_tag', 10)

    reader = SimpleMFRC522()

    try:
        while True:
            id, text = reader.read()
            msg = String()
            msg.data = str(id)
            pub.publish(msg)
            node.get_logger().info('Tag ID: %s' % id)
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
