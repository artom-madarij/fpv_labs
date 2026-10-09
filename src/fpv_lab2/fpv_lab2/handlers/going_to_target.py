import math
from typing import TYPE_CHECKING

from geometry_msgs.msg import TwistStamped

from ..flight_state import FlightState
from .handler import FlightStateHandler

if TYPE_CHECKING:
    from ..flight_target_node import FlightTargetNode


class GoingToTargetHandler(FlightStateHandler):
    def handle(self, node: "FlightTargetNode") -> None:
        if node.initial_x is None and node.odometry is not None:
            node.initial_x = node.odometry.pose.pose.position.x
            node.initial_y = node.odometry.pose.pose.position.y
            node.target_x = node.initial_x - node.TARGET_DELTA_X
            node.target_y = node.initial_y - node.TARGET_DELTA_Y
            node.get_logger().info(
                f"Start position: x0={node.initial_x:.2f}, y0={node.initial_y:.2f}"
            )
            node.get_logger().info(
                f"Target: x={node.target_x:.2f}, y={node.target_y:.2f}"
            )

        if node.odometry is None:
            return

        x = node.odometry.pose.pose.position.x
        y = node.odometry.pose.pose.position.y
        diff_x = node.target_x - x
        diff_y = node.target_y - y
        distance = math.hypot(diff_x, diff_y)

        node.get_logger().info(f"Distance to target: {distance:.2f} m")

        message = TwistStamped()
        message.header.stamp = node.get_clock().now().to_msg()
        message.header.frame_id = "map"

        if distance < node.TARGET_TOLERANCE:
            message.twist.linear.x = 0.0
            message.twist.linear.y = 0.0
            node.cmd_vel_publisher.publish(message)
            node.get_logger().info(
                f"Target reached, position error: {distance:.2f} m"
            )
            node.state = FlightState.LANDING
            return

        speed = node.KP * distance
        if speed > node.MAX_SPEED:
            speed = node.MAX_SPEED

        message.twist.linear.x = (diff_x / distance) * speed
        message.twist.linear.y = (diff_y / distance) * speed
        node.cmd_vel_publisher.publish(message)
