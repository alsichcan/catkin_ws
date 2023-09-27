#!/usr/bin/env python3

import rospy
from basics.msg import Complex
from random import random

rospy.init_node('message_publisher')

pub = rospy.Publisher('complex', Complex, queue_size=10)

rate = rospy.Rate(2)

count = 0
while not rospy.is_shutdown():
    msg = Complex()
    msg.real = random()
    msg.imaginary = random()
    pub.publish(msg)
    rate.sleep()