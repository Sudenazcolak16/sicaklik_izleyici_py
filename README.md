# Sıcaklık İzleyici ROS 2 Paketi

Bu paket, her saniye rastgele 20-40 °C arası sıcaklık üreten bir sensör düğümü ve 30 °C üzerindeki sıcaklıklarda uyarı veren izleyici düğümünü içerir.

## Derleme Adımları
```bash
cd ~/ros2_ws
colcon build --packages-select sicaklik_izleyici_py
source install/setup.bash
