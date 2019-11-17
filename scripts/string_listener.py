import message_sender as msgs_sender
from std_msgs.msg import String
from rclpy.node import Node

class TopicNode(Node):   
    def __init__(self, topic):
	conn_str = Node.declare_parameter("conn_str")
	conn_str = Node.get_parameter("conn_str")
	print(conn_str)
        super().__init__('node_logger')
        self.partition = 1
        self.subscription = self.create_subscription(
            String,
            topic,
            self.listener_callback)
        self.topic = topic


    def listener_callback(self, msg):
        self.msg = msg
        msgs_sender.send_message(msg.data,self.partition)
