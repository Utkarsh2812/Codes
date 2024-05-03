import rclpy
from rclpy.node import Node

from experiment_3.msg import Birthday                       # CHANGE

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Birthday, 'bhai_ka_bday', 10)  # CHANGE
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Birthday()                                                # CHANGE
        msg.year = 2003
        msg.month = 12
        msg.day = 28                                           # CHANGE
        self.publisher_.publish(msg)
        self.get_logger().info('y:"%d"' % msg.year)
        self.get_logger().info('m"%d"' % msg.month)  
        self.get_logger().info('d"%d"' % msg.day)         # CHANGE

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)


    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()