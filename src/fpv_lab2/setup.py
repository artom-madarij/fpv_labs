from setuptools import find_packages, setup

package_name = 'fpv_lab2'

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
    maintainer='artom',
    maintainer_email='artom@todo.todo',
    description='FPV Lab 2 package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'flight_test = fpv_lab2.main:main',
            'flight_target = fpv_lab2.flight_target_main:main',
        ],
    },
)
