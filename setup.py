from setuptools import find_packages, setup

package_name = 'controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test_telemetry_sender_node = Jury_integration.test_telemetry_sender_node:main',
            'Jury_integration = Jury_integration.jury_integration:main',
            'test_dogfight_sender_node = Jury_integration.test_dogfight_sender_node:main',
            'test_detection_sender = Jury_integration.test_detection_sender:main',
            'test_redzones_subscribe = Jury_integration.test_redzones_subscribe:main',
            'test_qr = Jury_integration.test_qr:main',
            'test_target_telemetry = Jury_integration.test_target_telemetry:main',
        ],
    },
)
