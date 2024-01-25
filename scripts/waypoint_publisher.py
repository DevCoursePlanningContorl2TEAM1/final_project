#!/usr/bin/env python3

import rospy
import time
import tf.transformations

from std_msgs.msg import Empty
from geometry_msgs.msg import PoseWithCovarianceStamped

# wp_id : (x, y, yaw)
<<<<<<< HEAD
wp_list = {1 : (4.0, 0.0, 0.7),
           2 : (5.23, -4.51, -0.78),
           3 : (-5.97, -4.28, -3.14),
           4 : (-11.56, -0.1, 0.7),
           5 : (-7.79, -0.24, -3.14)}

def talker():
    pub_wp = rospy.Publisher('my_t3_waypoints', PoseWithCovarianceStamped, queue_size=1)
=======
wp_list = {1 : (4.5, -0.5, 0.7),
           2 : (5.5, -4.5, -0.78),
           3 : (-6.5, -4.2, -2.14),
           4 : (-12.0, 0.0, 0.7),
           5 : (-9.0, 0.0, -1.57)}

def talker():
    pub_wp = rospy.Publisher('my_waypoints', PoseWithCovarianceStamped, queue_size=1)
>>>>>>> 095a39a (Created waypoint_publisher.py file.)
    pub_path_ready = rospy.Publisher('path_ready', Empty, queue_size=1)

    rospy.init_node('waypoint_publisher', anonymous=True)
    rate = rospy.Rate(10) # hz

    my_wp = PoseWithCovarianceStamped()
    my_wp.header.stamp = rospy.Time.now()
    my_wp.header.frame_id = 'map'

    for i in range(len(wp_list)):
        rospy.loginfo("Waypoint" + str(i+1))

        init_x, init_y, init_yaw = wp_list[i+1]
        init_roll = 0.0
        init_pitch = 0.0

        quaternion = tf.transformations.quaternion_from_euler(init_roll, init_pitch, init_yaw)

        my_wp.pose.pose.position.x = init_x
        my_wp.pose.pose.position.y = init_y
        my_wp.pose.pose.orientation.x = quaternion[0]
        my_wp.pose.pose.orientation.y = quaternion[1]
        my_wp.pose.pose.orientation.z = quaternion[2]
        my_wp.pose.pose.orientation.w = quaternion[3]

        while not rospy.is_shutdown():
            connections = pub_wp.get_num_connections()
            if connections > 0:
                pub_wp.publish(my_wp)
                break
<<<<<<< HEAD
            rospy.loginfo("Wait for 'my_t3_waypoints' topic")
=======
            rospy.loginfo("Wait for 'my_waypoints' topic")
>>>>>>> 095a39a (Created waypoint_publisher.py file.)
            rate.sleep()

        rospy.loginfo("Published waypoint number " + str(i+1))
        time.sleep(2)

    start_command = Empty()

    while not rospy.is_shutdown():
        connections = pub_path_ready.get_num_connections()
        if connections > 0:
            pub_path_ready.publish(start_command)
            rospy.loginfo("Sent waypoint list execution command")
            break
        rospy.loginfo("Waiting for 'path_ready' topic")
        rate.sleep()

if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass