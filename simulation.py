

'''
Copyright 2017-2018 Agnese Salutari.
Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on 
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License
'''

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