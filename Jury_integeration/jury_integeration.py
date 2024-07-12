import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import requests

class JuryIntegration(Node):
    
    BASE_URL = 'http://localhost:5000'
    
    
    def __init__(self):
        super().__init__('data_listener')
        self.detection_data = None
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

        self.detection_subscription = self.create_subscription(
            String,
            'detection_data',
            self.detection_listener_callback,
            10)
        
        
        # self.publish_redzones()
        
        

        
    
    def telemetry_listener_callback(self, msg):
        # Extract JSON string from the message
        json_str = msg.data
        
        # Parse the JSON string into a dictionary
        telemetry_data = json.loads(json_str)
        
        # Log the received data
        
        
        ENDPOINT = '/api/telemetri_gonder'
        
        if self.detection_data is None:
            payload = telemetry_data["data"]
        else:
            
            payload = {
            "takim_numarasi": 1,
            "iha_enlem": telemetry_data["data"]["iha_enlem"],
            "iha_boylam": telemetry_data["data"]["iha_boylam"],
            "iha_irtifa": telemetry_data["data"]["iha_irtifa"],
            "iha_dikilme": telemetry_data["data"]["iha_dikilme"],
            "iha_yonelme": telemetry_data["data"]["iha_yonelme"],
            "iha_yatis": telemetry_data["data"]["iha_yatis"],
            "iha_hiz": telemetry_data["data"]["iha_hiz"],
            "iha_batarya": telemetry_data["data"]["iha_batarya"],
            "iha_otonom": telemetry_data["data"]["iha_otonom"],
            "iha_kilitlenme": 1,
            "hedef_merkez_X": self.detection_data["data"]["x"],
            "hedef_merkez_Y": self.detection_data["data"]["y"],
            "hedef_genislik": self.detection_data["data"]["width"],
            "hedef_yukseklik": self.detection_data["data"]["height"],
            "gps_saati": telemetry_data["data"]["gps_saati"]
        }
        
        
        self.get_logger().info(f'Received JSON data: {payload}')
        
        # response = requests.post(f'{JuryIntegration.BASE_URL}{ENDPOINT}', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        # print(response.status_code)
        # print(response.json())
        
    def dogfight_listener_callback(self, msg):
        
        json_str = msg.data
        dogfight_data = json.loads(json_str)
        
        self.get_logger().info(f'Received dogfight data: {dogfight_data}')
        
        
        ENDPOINT = '/api/otonom_kilitlenme'
        payload = dogfight_data
        response = requests.post(f'{JuryIntegration.BASE_URL}{ENDPOINT}', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        print(response.status_code)
        print(response.json())
    
        
        
        
    def detection_listener_callback(self, msg):
        json_str = msg.data
        self.detection_data = json.loads(json_str)
        
        self.get_logger().info(f'Received detection data: {self.detection_data}')
        
        # Check if the message is empty for two seconds
        if not msg.data:
            self.detection_data = None
        
    
    
    # def publish_redzones(self):
    #         redzone_publisher = self.create_publisher(String, 'redzones', 10)
            
    #         response = requests.get(f'{self.BASE_URL}/api/redzones')
    #         if response.status_code == 200:
    #             print("Redzones fetched successfully")
    #             redzones = response.json()
    #             msg = String()
    #             msg.data = json.dumps(redzones)
    #             redzone_publisher.publish(msg)
    #         else:
    #             print("Failed to fetch redzones")
        
        
    
        


def main(args=None):
    rclpy.init(args=args)
    listener = JuryIntegration()
    rclpy.spin(listener)
    
    # Shutdown the listener
    listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
