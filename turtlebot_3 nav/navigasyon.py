#!/usr/bin/env python3

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib import SimpleActionClient
from geometry_msgs.msg import PoseStamped

def move_base_demo():
    rospy.init_node('move_base_demo', anonymous=True)

    action_client = SimpleActionClient('move_base', MoveBaseAction)
    action_client.wait_for_server()

    # Rota listesini oluşturun
    route = []

    # Kullanıcıdan hedef konumları alın ve rotaya ekleyin
    while True:
        goal_x = input("Hedef konumun x koordinatını girin (çıkmak için q): ")
        if goal_x == "q":
            break
        goal_y = input("Hedef konumun y koordinatını girin: ")

        # Hedef konumu rotaya ekleyin
        goal = PoseStamped()
        goal.header.frame_id = "map"  # Hedef konumun referans çerçevesi
        goal.pose.position.x = float(goal_x)
        goal.pose.position.y = float(goal_y)
        goal.pose.position.z = 0.0
        goal.pose.orientation.x = 0.0
        goal.pose.orientation.y = 0.0
        goal.pose.orientation.z = 0.0
        goal.pose.orientation.w = 1.0

        route.append(goal)

    rospy.sleep(1)  # Yayıncının başlatılması için bir süre bekleme

    # Rotayı yayınlayın ve sonuçlarını bekle
    for goal in route + list(reversed(route)):
        move_base_goal = MoveBaseGoal()
        move_base_goal.target_pose = goal
        action_client.send_goal(move_base_goal)
        action_client.wait_for_result(rospy.Duration(10.0))

    rospy.spin()

if __name__ == '__main__':
    try:
        move_base_demo()
    except rospy.ROSInterruptException:
        pass
