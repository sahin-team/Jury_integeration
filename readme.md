# Project Title
Jury integration

## Description

The Jury Integration project bridges ROS messages and a jury server, facilitating real-time data exchange. It not only transmits data to the jury server but also receives vital information like red zones, target telemetry, and QR code data, publishing them as ROS messages. This enhances ROS-based system interoperability with external servers.

## Installation
install ros humble from https://docs.ros.org/en/humble/Installation.html

**Clone the Jury Integration Project:**
git clone https://github.com/sahin-team/Jury_integeration.git

**Build the project**
colcon build

**Running the mock Server**
clone and run the mock server from another terminal

git clone https://github.com/sahin-team/mock_server.git
cd mock_server

**Install Dependencies**
pip install -r requirements.txt

**Start the Mock Server**
python3 endpoints.py

**Running the Jury Integration Scripts**
ros2 run controller Jury_integration

ros2 run controller test_telemetry_sender_node
ros2 run controller test_dogfight_sender_node
ros2 run controller test_detection_sender
ros2 run controller test_redzones_subscribe
ros2 run controller test_qr
ros2 run controller test_target_telemetry

## Usage

Subscribe the redzones data from this topic "hss_koordinatlari"
Subscribe the Qr code data from this topic "qr_koordinati"
Subscribe the target telemetry data from this topic "target_telemetry"

