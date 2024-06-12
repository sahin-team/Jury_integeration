import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class DogfightListener(Node):
    def __init__(self):
        super().__init__('dogfight_listener')
        self.subscription = self.create_subscription(
            String,
            'dogfight_data',
            self.callback,
            10
        )

    def callback(self, data):
        self.get_logger().info('Received data: %s' % data.data)

def main():
    rclpy.init()
    node = DogfightListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()