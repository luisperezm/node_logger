from azure.eventhub import EventHubClient, Sender, EventData
import os
import sys

from rclpy.node import Node



def send_message(message, conn_str, eventhub ,partition=1):
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
