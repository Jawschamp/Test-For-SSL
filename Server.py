from flask import Flask, send_file, request, json, jsonify
#from flask_sslify import SSLify


import ssl
import asyncio
import requests
import logging
import time
import sys



app = Flask(__name__)
#sslify = SSLify(app)
logger = logging.getLogger(__name__)
#c_handler = logging.StreamHandler()
#f_handler = logging.FileHandler('log.log')

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
print(time_string, "UTC")


@app.route('/')
def dog():
	return "h1"


if __name__ == '__main__':
  app.run(debug=True)
