import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class JuryIntegration(Node):
    
    BASE_URL = os.getenv('BASE_URL')
    
    
    def __init__(self):
        super().__init__('data_listener')
        self.detection_data = None
        self.last_message_time = None
        self.last_msg_second = None
        self.last_msg_minute = None
        self.telemetry_subscription = self.create_subscription(
            String,
            'json_telemetry',
            self.telemetry_listener_callback,
            10)
        
        self.target_telemetry_publisher = self.create_publisher(String, 'target_telemetry', 10)
        
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
        
        
        self.publish_hss_koordinatlari()
        
        self.publish_qr_koordinati()
        
        
        
    
    def telemetry_listener_callback(self, msg):
        # Extract JSON string from the message
        json_str = msg.data
        
        # Parse the JSON string into a dictionary
        telemetry_data = json.loads(json_str)
        
        # Log the received data
        
        
        ENDPOINT = '/api/telemetri_gonder'
        
        self.now_time = self._clock.now()
        
        seconds = self.now_time.nanoseconds / 1e9
        time_delta = timedelta(seconds=seconds)
        datetime_obj = datetime(1970, 1, 1) + time_delta

        now_minute = datetime_obj.minute
        now_second = datetime_obj.second
        
        if self.detection_data is not None and self.last_msg_second in (now_second,now_second-1) and self.last_msg_minute == now_minute:
            
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
        else:
            payload = telemetry_data["data"]
            
            
        self.get_logger().info(f'Received JSON data: {payload}')
        # self.get_logger().info(f'last msg second: {self.last_msg_second}, Second: {now_second}')
        # self.get_logger().info(f'last msg minute: {self.last_msg_minute}, Minute: {now_minute}')
        
        response = requests.post(f'{JuryIntegration.BASE_URL}{ENDPOINT}', data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        # print(response.json())
        
        # Publish the response in JSON format
        response_msg = String()
        response_msg.data = json.dumps(response.json())
        self.target_telemetry_publisher.publish(response_msg)
        
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
        
        # self.get_logger().info(f'Received detection data: {self.detection_data}')
        
        self.last_message_time = self._clock.now()
        
        seconds = self.last_message_time.nanoseconds / 1e9
        time_delta = timedelta(seconds=seconds)
        datetime_obj = datetime(1970, 1, 1) + time_delta

        self.last_msg_minute = datetime_obj.minute
        self.last_msg_second = datetime_obj.second

        # self.get_logger().info(f'Minute: {minute}, Second: {self.second}')
        
    
    
    def publish_hss_koordinatlari(self):
            redzone_publisher = self.create_publisher(String, 'hss_koordinatlari', 10)
            
            response = requests.get(f'{self.BASE_URL}/api/hss_koordinatlari')
            if response.status_code == 200:
                print("hss_koordinatlari fetched successfully") 
                hss_koordinatlari = response.json()
                msg = String()
                msg.data = json.dumps(hss_koordinatlari)
                redzone_publisher.publish(msg)
            else:
                print("Failed to fetch hss_koordinatlari")
    
    def publish_qr_koordinati(self):
        qr_publisher = self.create_publisher(String, 'qr_koordinati', 10)
        
        response = requests.get(f'{self.BASE_URL}/api/qr_koordinati')
        if response.status_code == 200:
            print("QR codes fetched successfully")
            print(response.json())
            qr_koordinati = response.json()
            msg = String()
            msg.data = json.dumps(qr_koordinati)
            qr_publisher.publish(msg)
        else:
            print("Failed to fetch QR codes")
        
        
    
        


def main(args=None):
    rclpy.init(args=args)
    listener = JuryIntegration()
    rclpy.spin(listener)
    
    # Shutdown the listener
    listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
