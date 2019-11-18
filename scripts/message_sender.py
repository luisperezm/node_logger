from azure.eventhub import EventHubClient, Sender, EventData
import os
import sys

from rclpy.node import Node

CONNECTION_STR = os.environ["EVENT_HUB_CONN_STR"]
EVENT_HUB = os.environ['EVENT_HUB_NAME']

#cadena = Node.declare_parameter("conn_str")
#cadena = Node.get_parameter("conn_str")
#print(cadena)

def send_message(message, partition=1, conn_str, eventhub):
	client = EventHubClient.from_connection_string(conn_str, eventhub)
	sender = client.add_sender(partition=partition)
	print(cadena)
	client.run()
	try:
		sender.send(EventData(message))
	except:
		import traceback
		traceback.print_exc(file=sys.stdout)
	finally:
		client.stop()
