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
            'telemetry_sender_node = Jury_integeration.telemetry_sender_node:main',
            'data_listener = Jury_integeration.jury_integeration:main',
            'dogfight_sender_node = Jury_integeration.dogfight_sender_node:main',
            'dedection_sender = Jury_integeration.dedection_sender:main',
        ],
    },
)
