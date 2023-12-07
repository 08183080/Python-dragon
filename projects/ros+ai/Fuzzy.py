
import rclpy
import math
import numpy as np
#import skfuzzy as fuzz


#from skfuzzy import control as ctrl
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf2_ros import TransformRegistration
from rclpy.qos import QoSProfile, ReliabilityPolicy

class fuzzy:
	#distance  = [0.0,0.25,0.5,0.75,1.0]
	close = [0.0, 0.25, 0.5]
	med = [0.25, 0.5, 0.75]
	far=  [0.5, 0.75, 1]

	distance = {'close' : close, 'med': med, 'far': far} 
	F=input_Front_Distance
	B=input_Back_Distance
	
	def caculate(F);
		for key,value in distance:
			for j in range (0,3):
				if F > value[j]:
					return key,value[j],value[j+1]

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
'''
def fuzz (front1,front2,fright,right,fleft,left):
	def fuzz_and(a,b):
		return min(a,b)
	def fuzz_or(a,b):
		return max(a,b)
    rule1=fuzz_and(front1,right)
    rule2=fuzz_and(front2,right)
    rule3=fuzz_or(fuzz_or(front1,fleft),fuzz_and(front2,fright))
    rule4=fuzz_or(fuzz_and(front1,fright),left)
    angular_velocity = rule1*0.5+rule2*0.5+rule3*-0.5+rule4*-0.5
    return angular_velocity
'''





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
    
    
    '''
    #If an obstacle is found to be within 0.25 of the LiDAR sensors front region the linear velocity is set to 0 (turtlebot stops)
    if (regions_['front1'])< 0.25:
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        return msg
    #if there is no obstacle in front of the robot, it continues to move forward
    elif (regions_['front2'])< 0.25:
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        return msg
    else:
        msg.linear.x = 0.1
        msg.angular.z = 0.0
        return msg
        '''

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
