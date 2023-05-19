#!/usr/bin/env python3
# Import rclpy which is referenced in package.xml as a dependency
import rclpy
# Import the Node by using the from keyword with the rclpy.node module
from rclpy.node import Node

# Create a new class which is a subclass of the Node class
class MyNode(Node):

    # The constructor ~~AI comment unclear here
    def __init__(self):
        super().__init__("first_node")
        # Create timer
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)

    # Create callback function for the timer
    def timer_callback(self):
        # Print "Hello + counter, which depends on the timer"
        self.get_logger().info("Hello " + str(self.counter_))
        # Increment the counter
        self.counter_ += 1

# The main function
def main(args=None):
    # Initialize the rclpy library
    rclpy.init(args=args)
    # Create the node
    node = MyNode()
    # Keep the node alive
    rclpy.spin(node)
    # Destroy the node explicitly
    rclpy.shutdown()

# If the python file is executed directly
if __name__ == '__main__':
    main()
