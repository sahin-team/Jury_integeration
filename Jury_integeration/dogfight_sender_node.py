import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class dogfightPubliher(Node):
    def __init__(self):
        super().__init__('example_publisher')
        self.dogfight_publisher = self.create_publisher(String, 'dogfight_data', 10)
        self.timer = self.create_timer(3, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        dogfight_data = {
            "source": "dogfight",
            "subject": "look_completed",
            "format": "object",
            "data": {
                "lockoutStartTime": {
                    "time": 11,
                    "minute": 40,
                    "seconds": 51,
                    "milliseconds": 478,
                },
                "lockoutEndTime": {
                    "time": 11,
                    "minute": 41,
                    "seconds": "03",
                    "milliseconds": 141,
                },
                "autonomous_lockout": 1,
            },
        }

        dogfight_json = json.dumps(dogfight_data)
        dogfight_json_msg = String()
        dogfight_json_msg.data = dogfight_json

        self.dogfight_publisher.publish(dogfight_json_msg)
 

def main(args=None):
    rclpy.init(args=args)
    node = dogfightPubliher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
