#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

# Create a new class which is a subclass of the Node class
class DrawCircle(Node):

    def __init__(self):
        super().__init__("draw_circle")
        # Create punlisher:
        #  node . publisher = node . "create publisher command"(data type, topic name, queue size)


        self.cmv_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        # Create timer
        self.timer_ = self.create_timer(0.5, self.send_velocity_command)
        # Print something
        self.get_logger().info("Draw circle node has been started")

    # Create a function to send the velocity command
    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        # Publish the message:
        # node . publisher which was alread created above] . publish(message)
        self.cmv_vel_pub_.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    node = DrawCircle()
    rclpy.spin(node)
    rclpy.shutdown()