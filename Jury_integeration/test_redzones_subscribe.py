import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class RedzoneSubscriber(Node):
    def __init__(self):
        super().__init__('redzone_subscriber')
        self.subscription = self.create_subscription(
            String,
            'redzones',
            self.redzone_callback,
            10)
        self.subscription  # prevent unused variable warning

    def redzone_callback(self, msg):
        redzones = json.loads(msg.data)
        self.get_logger().info('Received redzones: "%s"' % redzones)

def main(args=None):
    rclpy.init(args=args)
    redzone_subscriber = RedzoneSubscriber()
    rclpy.spin(redzone_subscriber)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    redzone_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()