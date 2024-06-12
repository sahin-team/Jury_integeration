import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class JsonTelemetryListener(Node):
    def __init__(self):
        super().__init__('telemetry_listener')
        self.telemetry_subscription = self.create_subscription(
            String,
            'json_telemetry',
            self.telemetry_listener_callback,
            10)
        
        self.dogfight_subscription = self.create_subscription(
            String,
            'dogfight_data',
            self.dogfight_listener_callback,
            10)

    def telemetry_listener_callback(self, msg):
        # Extract JSON string from the message
        json_str = msg.data
        
        # Parse the JSON string into a dictionary
        telemetry_data = json.loads(json_str)
        
        # Log the received data
        # self.get_logger().info(f'Received JSON data: {telemetry_data}')
        
    def dogfight_listener_callback(self, msg):
        json_str = msg.data
        dogfight_data = json.loads(json_str)
        
        self.get_logger().info(f'Received dogfight data: {dogfight_data}')
    
        


def main(args=None):
    rclpy.init(args=args)
    listener = JsonTelemetryListener()
    rclpy.spin(listener)
    
    # Shutdown the listener
    listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
