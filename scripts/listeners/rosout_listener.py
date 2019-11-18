import message_sender as msgs_sender
from std_msgs.msg import String
from rcl_interfaces.msg import Log
from rclpy.node import Node

import logging, json

logger = logging.getLogger('rousout_listener')

class RosoutListener(Node): 
	def __init__(self):
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

		self.partition = '0'
		self.subscription = self.create_subscription(
			Log,
			'rosout',
			self.listener_callback)

	def listener_callback(self, msg):
		values = {}
		times = {}

		times['sec'] = str(msg.stamp.sec)
		times['nanosec'] = str(msg.stamp.nanosec)

		values['stamp'] = times
		values['level'] = msg.level
		values['name'] = msg.name
		values['msg'] = msg.msg
		values['file'] = msg.file
		values['function'] = msg.function
		values['line'] = msg.line
		msgs_sender.send_message(json.dumps(values), self.conn_str.value, self.eventhub.value, self.partition)
