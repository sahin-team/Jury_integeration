import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class ResponseListener(Node):
    def __init__(self):
        super().__init__('response_listener')
        self.subscription = self.create_subscription(
            String,
            'target_telemetry',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        response_data = json.loads(msg.data)
        self.get_logger().info(response_data)

def main(args=None):
    rclpy.init(args=args)
    response_listener = ResponseListener()
    rclpy.spin(response_listener)
    response_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()