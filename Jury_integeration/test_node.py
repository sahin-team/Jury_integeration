import rclpy
from rclpy.node import Node
#!/usr/bin/env python3


class TestNode(Node):
    def __init__(self):
        super().__init__('test_node')
        self.get_logger().info('Test Node Started1')
        # Add your code here

def main(args=None):
    rclpy.init(args=args)

    node = TestNode()

    print("Hello, World!")
    # rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()