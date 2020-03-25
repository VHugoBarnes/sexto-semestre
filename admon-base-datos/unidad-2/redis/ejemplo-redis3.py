#!/usr/bin/python
# -*- coding: utf-8 -*-

import redis


hostname="localhost"
port = 6379

client = redis.StrictRedis(host=hostname, port=port, db=0)


a = client.lrange("amigos", 0, -1)

print(a)
