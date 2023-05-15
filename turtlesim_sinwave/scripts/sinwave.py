#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def move():
    rospy.init_node('snake_turtle')
    vel_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

    vel_msg = Twist()
    current_pose=Pose()
    rate = rospy.Rate(10) # 10 Hz

    while not rospy.is_shutdown():
        vel_msg.linear.x=2
        i=1
        while i<5:
            vel_msg.angular.z = 5
            vel_publisher.publish(vel_msg)
            i+=1
            rate.sleep()
        while i>0:
            vel_msg.angular.z= -5
            vel_publisher.publish(vel_msg)
            i-=1
            rate.sleep()
        

def pose_callback(pose):
    rospy.loginfo("Turtle's pose: x=%f, y=%f", pose.x, pose.y)
    

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
