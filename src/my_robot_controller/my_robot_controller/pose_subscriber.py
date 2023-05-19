#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriber(Node):

    def __init__(self):
        super().__init__("pose_subscriber")
        # Create subscriber
        # (data type, topic name, callback function, queue size)
        self.pose_subscriber_ = self.create_subscription(
            # Whenever a message is received, the callback function is called
            Pose, "/turtle1/pose", self.pose_callback, 10 )

    # Create callback function
    # Paramneter: message to be received (do whatever you want with it)
    def pose_callback(self, msg: Pose):
        # Print with nicer formatting
        # OMG, sinus function reference
        self.get_logger().info("(" + str(msg.x) + ", " + str(msg.y) + ")")

def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriber()
    # Keep the node alive
    rclpy.spin(node)
    rclpy.shutdown()