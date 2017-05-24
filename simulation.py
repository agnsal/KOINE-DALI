import ServerPyProlog as SPP
import redis
import time
import datetime

translator=SPP.ServerPyProlog()     #Creation of a ServerPyProlog object

R1 = redis.Redis() # Istanza 1 di Redis
pubsub1 = R1.pubsub() # Canale di ascolto
pubsub1.subscribe('toMAS') # Canale di ricezione dati dei sensori

R2 = redis.Redis() # Istanza 2 di Redis

R2.publish('LINDAchannel', "helloWorld")  # Comunico al MASA i nuovi dati da acquisire