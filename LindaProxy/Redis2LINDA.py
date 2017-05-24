'''
Example of Linda Proxy in Python

 Licensed with Apache Public License
 by AAAI Research Group
 Department of Information Engineering and Computer Science and Mathematics
 University of L'Aquila, ITALY
 http://www.disim.univaq.it

'''

import LindaProxy.lindaproxy as lp
import redis

def makeAtomic(s):
    out = s.replace('(', 'A')
    out = out.replace(')', 'B')
    out = out.replace('[', 'C')
    out = out.replace(']', 'D')
    out = out.replace('.', 'E')
    out = out.replace(',', 'F')
    out = out.replace('/', 'G')
    out = out.replace('\\', 'H')
    out = out.replace("'", 'I')
    out = out.replace(' ', 'O')
    return out

# Canale di comunicazione da Redis a LINDA e da LINDA al MAS.
# Da usare come main rispetto a lindaproxy

#Il proxy è usato solo per inviare messaggi al MAS DALI
L = lp.LindaProxy(host='127.0.0.1')
L.connect()

#Il sistema inoltra gli eventi redis al MAS
R = redis.Redis()
pubsub = R.pubsub()
pubsub.subscribe('LINDAchannel')
for item in pubsub.listen():
    if item['type']=='message':
        msg=item['data'].decode('utf-8')
        atomic = makeAtomic(msg)
        print('evento redis', msg, atomic)
        L.send_message('masa', "redis(" + atomic + ")")