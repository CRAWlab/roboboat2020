#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist 
# Initialize the node
rospy.init_node('sysID_vel_commands', anonymous=True)
# Create a publisher to publish cmd_vel tell it to move
cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=0)
# 10 Hz update rate - update to match your setup
rate = rospy.Rate(10)
# Define the move command's Twist as a Twist message
move_cmd = Twist()
seq=0
try:
    while not rospy.is_shutdown():        
            # assign the translational velocity commands
            move_cmd.linear.x = 0
            move_cmd.linear.y = .5
            # assign the angular velocity command
            move_cmd.angular.z = 0
            #stop moving after 60seconds
            if seq>600:
                move_cmd.linear.x = 0
                move_cmd.linear.y = 0
                move_cmd.angular.z = 0
            # Then publish it
            cmd_vel.publish(move_cmd)
            rate.sleep()
            cmd_vel.publish(move_cmd)
            seq+=1
except (KeyboardInterrupt, SystemExit):
    cmd_vel.publish(Twist()) # publish all zeros to stop