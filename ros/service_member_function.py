from experiment_3.srv import PRN                                                          # CHANGE

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(PRN, 'add_Prn', self.add_callback)       # CHANGE
    
    def add_digits(self, num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

    def add_callback(self, request, response):
        prn = request.prn
        
        response.sum = self.add_digits(prn)                                                 # CHANGE
        self.get_logger().info('Incoming request\n PRN: %d ' % (request.prn))  # CHANGE

        return response
        

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
