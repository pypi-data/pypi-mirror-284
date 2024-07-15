# coding: utf-8
""" 消息队列
@comment 基于pika实现的rabbitmq消息队列模块
"""

import pika

class MessageQueueOption:
  
  def __init__(self, host, port=5672, virtual_host='/', username:str=None, password:str=None):
    self.host = host
    self.port = port
    self.virtual_host = virtual_host
    self.username = username
    self.password = password


class MessageQueue:
  
  def __init__(self, queueName: str, options:MessageQueueOption):
    self.options = options
    auth_credentials = pika.PlainCredentials(self.options.username, self.options.password)
    self.connection = pika.BlockingConnection(
      pika.ConnectionParameters(
        self.options.host, 
        self.options.port, 
        virtual_host=self.options.virtual_host, 
        credentials=auth_credentials))
    
    self.channel = self.connection.channel()
    self.channel.queue_declare(queue=queueName)
    
  def change_queue(self, queueName) :
    self.channel.queue_declare(queue=queueName)
    
  def pub_string(self, routeKey:str, body: str):
    self.channel.basic_publish(exchange='', routing_key=routeKey, body=body)
    
    
  def consume(self, queueName, onMessaged):
    self.channel.basic_consume(queue=queueName,
                      auto_ack=True,
                      on_message_callback=onMessaged)
    
  def start_loop(self):
    self.channel.start_consuming()
    
    
  def stop_loop(self):
    self.channel.stop_consuming()