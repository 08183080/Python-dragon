
import rclpy # 导入ROS 2的Python客户端库。
import math
import numpy as np
import skfuzzy as fuzz


#from skfuzzy import control as ctrl
from rclpy.node import Node # 创建 节点类
from sensor_msgs.msg import LaserScan # 导入ROS中的激光雷达消息类型。
from geometry_msgs.msg import Twist # 导入ROS中的Twist消息类型，用于控制机器人的线性和角度速度。
from nav_msgs.msg import Odometry # 导入ROS中的Odometry消息类型，用于获取机器人的位置和姿态信息。
from tf2_ros import TransformRegistration # 导入ROS中的tf2_ros库，用于处理坐标系转换。
from rclpy.qos import QoSProfile, ReliabilityPolicy
from skfuzzy import control as ctrl

class fuzzy:
	#distance  = [0.0,0.25,0.5,0.75,1.0]
	close = [0.0, 0.25, 0.5]
	med = [0.25, 0.5, 0.75]
	far=  [0.5, 0.75, 1]

	distance = {'close' : close, 'med': med, 'far': far} 
	F=input_Front_Distance
	B=input_Back_Distance
	
	def caculate(F):
		for key,value in distance:
			for j in range (0,3):
				if F > value[j]:
					return key,value[j],value[j+1]

class FuzzyController:
    def __init__(self):
        self.front_distance = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'front_distance')
        self.back_distance = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'back_distance')
        self.angular_velocity = ctrl.Consequent(np.arange(-1, 1.1, 0.1), 'angular_velocity')
        self.linear_velocity = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'linear_velocity')

        # Define fuzzy membership functions
        self.front_distance['close'] = fuzz.trimf(self.front_distance.universe, [0, 0, 0.5])
        self.front_distance['med'] = fuzz.trimf(self.front_distance.universe, [0, 0.5, 1])
        self.front_distance['far'] = fuzz.trimf(self.front_distance.universe, [0.5, 1, 1])

        self.back_distance['close'] = fuzz.trimf(self.back_distance.universe, [0, 0, 0.5])
        self.back_distance['med'] = fuzz.trimf(self.back_distance.universe, [0, 0.5, 1])
        self.back_distance['far'] = fuzz.trimf(self.back_distance.universe, [0.5, 1, 1])

        self.angular_velocity['left'] = fuzz.trimf(self.angular_velocity.universe, [-1, -1, -0.5])
        self.angular_velocity['straight'] = fuzz.trimf(self.angular_velocity.universe, [-0.5, 0, 0.5])
        self.angular_velocity['right'] = fuzz.trimf(self.angular_velocity.universe, [0.5, 1, 1])

        self.linear_velocity['slow'] = fuzz.trimf(self.linear_velocity.universe, [0, 0, 0.5])
        self.linear_velocity['medium'] = fuzz.trimf(self.linear_velocity.universe, [0, 0.5, 1])
        self.linear_velocity['fast'] = fuzz.trimf(self.linear_velocity.universe, [0.5, 1, 1])

        # Define fuzzy rules
        rule1 = ctrl.Rule(self.front_distance['close'] & self.back_distance['close'], 
                          (self.angular_velocity['left'], self.linear_velocity['slow']))
        rule2 = ctrl.Rule(self.front_distance['med'] & self.back_distance['close'], 
                          (self.angular_velocity['left'], self.linear_velocity['medium']))
        rule3 = ctrl.Rule(self.front_distance['far'] & self.back_distance['close'], 
                          (self.angular_velocity['left'], self.linear_velocity['fast']))
        rule4 = ctrl.Rule(self.front_distance['close'] & self.back_distance['med'], 
                          (self.angular_velocity['straight'], self.linear_velocity['slow']))
        rule5 = ctrl.Rule(self.front_distance['med'] & self.back_distance['med'], 
                          (self.angular_velocity['straight'], self.linear_velocity['medium']))
        rule6 = ctrl.Rule(self.front_distance['far'] & self.back_distance['med'], 
                          (self.angular_velocity['straight'], self.linear_velocity['fast']))
        rule7 = ctrl.Rule(self.front_distance['close'] & self.back_distance['far'], 
                          (self.angular_velocity['right'], self.linear_velocity['slow']))
        rule8 = ctrl.Rule(self.front_distance['med'] & self.back_distance['far'], 
                          (self.angular_velocity['right'], self.linear_velocity['medium']))
        rule9 = ctrl.Rule(self.front_distance['far'] & self.back_distance['far'], 
                          (self.angular_velocity['right'], self.linear_velocity['fast']))

        # Create fuzzy control system
        self.fuzzy_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
        self.fuzzy_sim = ctrl.ControlSystemSimulation(self.fuzzy_ctrl)

    def calculate(self, front_distance, back_distance):
        """
        利用前方输入和后方输入（Front Distance , Back Distance）,同样输出角速度和线速度，实现避障功能。
        """
        self.fuzzy_sim.input['front_distance'] = front_distance
        self.fuzzy_sim.input['back_distance'] = back_distance
        self.fuzzy_sim.compute()

        angular_velocity = self.fuzzy_sim.output['angular_velocity']
        linear_velocity = self.fuzzy_sim.output['linear_velocity']
        return angular_velocity, linear_velocity

mynode_ = None
pub_ = None
regions_ = {
    'right': 0,
    'fright': 0,
    'front1': 0,
    'front2': 0,
    'fleft': 0,
    'left': 0,
}
twstmsg_ = None
ep=0
ei=0
# main function attached to timer callback




def PID(kp,ki,kd,target_distance, right_distance):
    global ep,ei
    e =target_distance - right_distance
    ei += e
    ed = e-ep
    angular_velocity = kp*e+ ki*ei + kd*ed
    ep =e
    print(angular_velocity)
    return angular_velocity

def timer_callback():
    global pub_, twstmsg_
    if ( twstmsg_ != None ):
        pub_.publish(twstmsg_)

def clbk_laser(msg):
    global regions_, twstmsg_
    
    regions_ = {
        #LIDAR readings are anti-clockwise
        'front1':  find_nearest (msg.ranges[0:5]),
        'front2':  find_nearest (msg.ranges[355:360]),
        'right':  find_nearest(msg.ranges[265:275]),
        'fright': find_nearest (msg.ranges[310:320]),
        'fleft':  find_nearest (msg.ranges[40:50]),
        'left':   find_nearest (msg.ranges[85:95])
        
    } 
      
    twstmsg_ = Twist() 
    twstmsg_= movement()

# Find nearest point
def find_nearest(list):
    f_list = filter(lambda item: item > 0.0, list)  # exclude zeros
    return min(min(f_list, default=10), 10)

#Basic movement method


def movement():
    #print("here")
    global regions_, mynode_
    regions = regions_
    
    
    #print("Min distance in front region: ", regions_['front1'],regions_['front2'])
    
    #create an object of twist class, used to express the linear and angular velocity of the turtlebot 
    msg = Twist()
    
    msg.linear.x = 0.05
    '''right_distance =  regions_['right']
    print("right distance:", right_distance)
    msg.angular.z = PID(0.1,0.0,0.0,0.3,right_distance)'''
    return msg     

#used to stop the rosbot
def stop():
    global pub_
    msg = Twist()
    msg.angular.z = 0.0
    msg.linear.x = 0.0
    pub_.publish(msg)


def main():
    global pub_, mynode_

    rclpy.init()
    mynode_ = rclpy.create_node('reading_laser')

    # define qos profile (the subscriber default 'reliability' is not compatible with robot publisher 'best effort')
    qos = QoSProfile(
        depth=10,
        reliability=ReliabilityPolicy.BEST_EFFORT,
    )

    # publisher for twist velocity messages (default qos depth 10)
    pub_ = mynode_.create_publisher(Twist, '/cmd_vel', 10)

    # subscribe to laser topic (with our qos)
    sub = mynode_.create_subscription(LaserScan, '/scan', clbk_laser, qos)

    # Configure timer
    timer_period = 0.2  # seconds 
    timer = mynode_.create_timer(timer_period, timer_callback)

    # Run and handle keyboard interrupt (ctrl-c)
    try:
        rclpy.spin(mynode_)
    except KeyboardInterrupt:
        stop()  # stop the robot
    except:
        stop()  # stop the robot
    finally:
        # Clean up
        mynode_.destroy_timer(timer)
        mynode_.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()