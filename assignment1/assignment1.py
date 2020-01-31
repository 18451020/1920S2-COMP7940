from __future__ import unicode_literals

import redis


# fill in the following.
HOST = "redis-15494.c16.us-east-1-3.ec2.cloud.redislabs.com"
PWD = "oxy7Xdopdk8m15GqnwHhi2XXKY6baxjo"
PORT = "15494" 

redis1 = redis.Redis(host = HOST, password = PWD, port = PORT)

while True:
    msg = input("Please enter your query (type 'quit' or 'exit' to end):").strip()
    if msg == 'quit' or msg == 'exit':
        break
    if msg == '':
        continue
    print("You have entered " + msg, end=' ') 

   
    # Add your code here



    print('for X times')
