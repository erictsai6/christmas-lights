import json
import datetime
import pytz
from random import randint
import logging
import time

class RedisQueue():

    def __init__(self, client_id, queue_name, redis_client):
        self.client_id = client_id
        self.queue_name = queue_name
        self.redis = redis_client
    
    def queue(self, data):
        msg = json.dumps({ "client_id" : self.client_id, "data" : data, "attempts" : 0})
        self.redis.lpush(self.queue_name, msg)

    def poll(self):
        value = self.redis.rpop(self.queue_name)
        msg = json.loads(value) if value is not None else None 
        return msg

    def get_list(self):
        return self.redis.lrange(self.queue_name, 0, -1)

    def length(self):
        return self.redis.llen(self.queue_name) 

    def delete(self):
        self.redis.delete(self.queue_name)