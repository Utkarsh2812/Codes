import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from prn_interfaces.action import Prn


class PrimeActionServer(Node):

    def __init__(self):
        super().__init__('prime_numbers_action_server')
        self._action_server = ActionServer(
            self,
            Prn,
            'prime',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        feedback_msg = Prn.Feedback()
        feedback_msg.partial_sequence = [2]

        num = 3  # Start checking from 3
        while len(feedback_msg.partial_sequence) < goal_handle.request.order:
            if self.is_prime(num):
                feedback_msg.partial_sequence.append(num)
                self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
                goal_handle.publish_feedback(feedback_msg)
            num += 1
            time.sleep(1)

        goal_handle.succeed()

        result = Prn.Result()
        result.sequence = feedback_msg.partial_sequence
        return result

    def is_prime(self, num):
        """
        Checks if a number is prime.
        """
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True



def main(args=None):
    rclpy.init(args=args)

    prime_action_server = PrimeActionServer()

    rclpy.spin(prime_action_server)


if __name__ == '__main__':
    main()