#!/usr/bin/python

import requests
import time
import json
import sys

class RabbitMQStats():
	"""This is the class docstring"""
	host = None
	port = None
	base_url = None
	username = None
	password = None

	timestamp = 0

	def __init__(self, host, port, url, user, pwd):
		# Get epoch. can be formatted later
		self.timestamp = int(time.time())
		self.host = host
		self.port = port
		self.base_url = url
		self.username = user
		self.password = pwd

	def get_queues(self):
		body = self._request('/queues')
		return body

	def _request(self, path):
		try:
			r = requests.get('http://{0}:{1}{2}{3}'.format(self.host, self.port, self.base_url, path), auth = (self.username, self.password))
		except Excpetion as e:
			print('_request: {0}'.format(e))
			return {}
		return r.json()
