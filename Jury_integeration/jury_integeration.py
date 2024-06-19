import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import requests

class JsonTelemetryListener(Node):
    
    BASE_URL = 'http://localhost:5000'
    
    
    def __init__(self):
        super().__init__('data_listener')
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
        self.dedection_subscription = self.create_subscription(
            String,
            'detection_data',
            self.dedection_listener_callback,
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
        
        
        ENDPOINT = '/api/otonom_kilitlenme'
        payload = dogfight_data
        response = requests.post(f'{JsonTelemetryListener.BASE_URL}{ENDPOINT}', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        print(response.status_code)
        print(response.json())
        
        
        
    def dedection_listener_callback(self, msg):
        json_str = msg.data
        dedection_data = json.loads(json_str)
        
        # self.get_logger().info(f'Received dedection data: {dedection_data}')
    
        


def main(args=None):
    rclpy.init(args=args)
    listener = JsonTelemetryListener()
    rclpy.spin(listener)
    
    # Shutdown the listener
    listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
