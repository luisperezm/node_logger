#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
import sys
import logging

import message_sender as msgs_sender
from rosout_listener import RosoutListener
from string_listener import TopicNode


logger = logging.getLogger("node_logger")

def main(args=None):
    rclpy.init(args=args)

    #Executor to control all topic nodes 
    executor = MultiThreadedExecutor()

    nodeList = []

    #std_msgs/String topics -- 
    topics = ['rosout', 'actions', 'status']

    rosout_node = RosoutListener()
    executor.add_node(rosout_node)
    logger.info(f'creating node for rosout messages')
    nodeList.append(rosout_node)

    for topic in topics:
        #Node creation for all topics
        subscriber = TopicNode(topic)
        executor.add_node(subscriber)
        nodeList.append(subscriber)
        print(f'creating node for string topic /{topic} messages')
        
    try:
         executor.spin()
         
    finally:
         executor.shutdown()
         for subscriber in nodeList:
            subscriber.destroy_node()
   
    rclpy.shutdown()


if __name__ == '__main__':
    main()
