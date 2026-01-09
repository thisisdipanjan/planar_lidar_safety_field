#include "planar_safety_field/planar_lidar_safety.hpp"

int main(int argc, char * argv[]){
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<LidarSafety>());
    rclcpp::shutdown();
    return 0;
}