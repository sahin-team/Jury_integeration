import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

def main(args=None):
    rclpy.init(args=args)
    node = Node('humble_node')
    
    # Create JSON publisher
    json_publisher = node.create_publisher(String, 'json_telemetry', 10)

    # Create DogFight JSON publisher
    dogfight_json_publisher = node.create_publisher(String, 'dogfight_telemetry', 10)

        
        # Create timer callback function
    def timer_callback():
        # Create the desired dictionary with telemetry data
        telemetry_data = {
            "source": "mavlink",
            "subject": "telemetry",
            "format": "object",
            "data": {
                "iha_enlem": 41.508775,
                "iha_boylam": 36.118335,
                "iha_irtifa": 38,
                "iha_dikilme": 7,
                "iha_yonelme": 210,
                "iha_yatis": -30,
                "iha_hiz": 28,
                "iha_batarya": 50,
                "iha_otonom": 1,
                "gps_saati": {
                    "saat": 11,
                    "dakika": 38,
                    "saniye": 37,
                    "milisaniye": 654,
                },
            },
        }

        dogfight_telemetry_data = {
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

        
        # Convert the dictionary to a JSON string
        dogfight_telemetry_json = json.dumps(dogfight_telemetry_data)
        telemetry_json = json.dumps(telemetry_data)

        dogfight_json_msg = String()
        dogfight_json_msg.data = dogfight_telemetry_json
        
        # Create a String message
        json_msg = String()
        json_msg.data = telemetry_json
        
        # Publish the JSON message
        json_publisher.publish(json_msg)
        dogfight_json_publisher.publish(dogfight_json_msg)

    # Create timer
    timer_period = 3.0  # 3 second
    timer = node.create_timer(timer_period, timer_callback)
    dogfight_timer = node.create_timer(timer_period, timer_callback)

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
