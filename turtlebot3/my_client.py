#!/usr/bin/env python3

from __future__ import print_function
import rospy
import actionlib
import turtlebot3_example.msg
import sys

msg = """
TurtleBot3 için hedef giriniz!
Bu program Turtlebotun girilen hedef konumlari gezerek başlangic noktasina dönmesini saglar.
-----------------------
şuanki konum 0,0,0 kabul edilmistir

Hedefler: X(m),Y(m),W(-180,180) 
"""

class Client():
    def __init__(self):
        rospy.loginfo("Istek bekleniyor")
        self.client()

    def hedefleri_al(self):
        x_list=[]
        y_list=[]
        hedef_nokta_sayisi=int(input("Kac noktayi gezip baslangica dönmemi istersin:"))
        if hedef_nokta_sayisi==0:
            self.shutdown()
        else:
            rospy.loginfo("Yanlis secim")

        for i in range(hedef_nokta_sayisi):
            hedef_x,hedef_y=input(f"| x{i} | y{i} |").split()
            x_list.append(float(hedef_x))            
            y_list.append(float(hedef_y))
        return x_list,y_list ,hedef_nokta_sayisi
    
    def client(self):
        client = actionlib.SimpleActionClient('turtlebot3', turtlebot3_example.msg.Turtlebot3Action)
        
        hedef_xler,hedef_yler,nokta_sayisi=self.hedefleri_al()
        for i in range(nokta_sayisi):
            client.wait_for_server()
            goal = turtlebot3_example.msg.Turtlebot3Goal()
            goal.goal.x=hedef_xler
            goal.goal.y=hedef_yler
            goal.goal.z=nokta_sayisi
            client.send_goal(goal)
            rospy.loginfo("Tamamlandi")
            client.wait_for_result()
            rospy.loginfo(client.get_result())

    def shutdown(self):
        rospy.sleep(1)

if __name__ == '__main__':
    rospy.init_node('turtlebot3_client')
    try:
        while not rospy.is_shutdown():
            print (msg)
            result = Client()
    except:
        print("program close.", file=sys.stderr)
