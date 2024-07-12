import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class detectionPublisher(Node):
    def __init__(self):
        super().__init__('detection_sender')
        self.dogfight_publisher = self.create_publisher(String, 'detection_data', 10)
        self.timer = self.create_timer(3, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        detection_data = {
            "source": "image_processing",
            "subject": "detection",
            "format": "object",
            "data": {
                "x": 100,
                "y": 200,
                "width": 50,
                "height": 50,
                "frameWidth": 640,
                "frameHeight": 480
            }
        }


        detection_json = json.dumps(detection_data)
        dogfight_json_msg = String()
        dogfight_json_msg.data = detection_json

        self.dogfight_publisher.publish(dogfight_json_msg)
 

def main(args=None):
    rclpy.init(args=args)
    node = detectionPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
