from geometry_msgs.msg import TwistStamped

from .flight_state import FlightState
from .flight_test_node import FlightTestNode
from .handlers import HANDLERS
from .handlers.going_to_target import GoingToTargetHandler
from .handlers.target_hovering import TargetHoveringHandler


class FlightTargetNode(FlightTestNode):
    TARGET_DELTA_X = 3.5
    TARGET_DELTA_Y = -0.4
    TARGET_TOLERANCE = 0.3
    KP = 0.5
    MAX_SPEED = 1.0

    def __init__(self):
        super().__init__()

        self.initial_x = None
        self.initial_y = None
        self.target_x = None
        self.target_y = None

        self.cmd_vel_publisher = self.create_publisher(
            TwistStamped,
            "/ap/v1/cmd_vel",
            10,
        )

        self._handlers = dict(HANDLERS)
        self._handlers[FlightState.HOVERING] = TargetHoveringHandler()
        self._handlers[FlightState.GOING_TO_TARGET] = GoingToTargetHandler()

        self.get_logger().info("Flight target node started")
        self.get_logger().info(
            f"Target delta: dx={self.TARGET_DELTA_X}, dy={self.TARGET_DELTA_Y}"
        )
