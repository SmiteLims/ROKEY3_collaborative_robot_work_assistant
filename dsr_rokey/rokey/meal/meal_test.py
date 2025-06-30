# run_menu_service.py
import rclpy
from rclpy.node import Node
from od_msg.srv import SrvDepthPosition

class RunMenuService(Node):
    def __init__(self):
        super().__init__('run_menu_service_test')
        self.srv = self.create_service(SrvDepthPosition, 'run_menu', self.handle_run_menu)
        self.get_logger().info('🍽️ [run_menu] 서비스 대기 중...')

    def handle_run_menu(self, request, response):
        self.get_logger().info(f"✅ [meal] 요청 수신: {request.result}")
        text = request.result
        object, target = text.strip().split("/")
        

        coffee = False
        cereal = False
        if '커피' in text:
            coffee = True
        else:
            coffee = False
        if '시리얼' in text:
            cereal = True
        else:
            cereal = False
        # 상황에 맞는 맛 pub
        if coffee == True and cereal == False:
            target.strip().split(' ')[0]
        elif coffee == True and cereal == True:
            target.strip().split(' ')[0]
            target.strip().split(' ')[1]
        elif coffee == False and cereal == True:
            target.strip().split(' ')[0]
        else:
            pass
        
        # 동작 완료 srv 수신
        
        # durl
        response.success = True
        response.feedback = "메뉴 동작 완료"
        return response

def main():
    rclpy.init()
    node = RunMenuService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
