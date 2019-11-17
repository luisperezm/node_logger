import message_sender as msgs_sender
from std_msgs.msg import String
from rclpy.node import Node

class TopicNode(Node):	
	 def __init__(self, topic):
	   super().__init__('node_logger')
	   #conn_str = self.declare_parameter("conn_str")
	   conn_str = self.get_parameter("conn_str")
	   print("\nParameter: ",conn_str.value)
	   self.partition = '1'
	   self.subscription = self.create_subscription(
				String,
				topic,
				self.listener_callback)
	   self.topic = topic


	 def listener_callback(self, msg):
	   self.msg = msg
	   print('sending message')
	   msgs_sender.send_message(msg.data,self.partition)
