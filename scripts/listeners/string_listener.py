import message_sender as msgs_sender
from std_msgs.msg import String
from rclpy.node import Node
from rclpy.parameter import Parameter

class TopicNode(Node):
	def __init__(self, topic):
		super().__init__('node_logger')

		self.conn_str = self.declare_parameter("conn_str")
		self.eventhub = self.declare_parameter("eventhub_name")

		self.conn_str = self.get_parameter("conn_str")
		self.eventhub = self.get_parameter("eventhub_name")

		if (self.conn_str.type_ == Parameter.Type.NOT_SET):
			self.get_logger().error('Please insert connection string to eventhub')
			exit(-1)

		if (self.eventhub.type_ == Parameter.Type.NOT_SET):
			self.get_logger().error('Please insert the eventhub name')
			exit(-1)
		


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
		msgs_sender.send_message(msg.data, self.conn_str.value, self.eventhub.value,self.partition)
