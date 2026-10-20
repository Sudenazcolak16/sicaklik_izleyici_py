import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class IzleyiciNode(Node):
    def __init__(self):
        super().__init__('izleyici_node')
        
        # Bonus: Eşik değerini parametre olarak tanımlama (varsayılan: 30.0)
        self.declare_parameter('esik_degeri', 30.0)
        
        # /sicaklik konusuna abone olma
        self.subscription = self.create_subscription(
            Float32,
            '/sicaklik',
            self.temperature_callback,
            10
        )
        self.get_logger().info('Sıcaklık izleyici düğümü başlatıldı.')

    def temperature_callback(self, msg):
        # Tanımlanan eşik değerini parametreden çekme
        esik = self.get_parameter('esik_degeri').get_parameter_value().double_value
        
        # Değeri ekrana yazdırma ve eşik kontrolü
        if msg.data > esik:
            self.get_logger().warn(f'UYARI: Sıcaklık {esik:.1f} °C üzerine çıktı! Güncel değer: {msg.data:.2f} °C')
        else:
            self.get_logger().info(f'Okunan sıcaklık: {msg.data:.2f} °C')

def main(args=None):
    rclpy.init(args=args)
    node = IzleyiciNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
