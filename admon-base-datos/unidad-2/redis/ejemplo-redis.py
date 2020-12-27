#!/usr/bin/python
# -*- coding: utf-8 -*-

import redis


hostname="localhost"
port = 6379

client = redis.StrictRedis(host=hostname, port=port, db=0)
foo = client.get('foo')

print(foo)