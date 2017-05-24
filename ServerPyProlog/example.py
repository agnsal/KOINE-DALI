__author__ = 'Agnese'

#YOU CAN USE THIS FILE TO TEST "serverPyProlog" LIBRARY WORK.

import ServerPyProlog as SPP

translator=SPP.ServerPyProlog()     #Creation of a ServerPyProlog object

json = '{"nome  ":"felix","cognome":"domesticus"}' #A JSON string (it could be a normal JSON too)
print("Json:")
print(json)
t=translator.JSONtoPmap(json,"gatto")
translator.addToResult(t)
print("Result:")
print(translator.getResult())


id=translator.idConverter(1231)
print("Id:")
print(id)

translator.delResult()

persona={            #A dictionary
    "nome":"agnese",
    "cognome":"salutari"
}
print("Persona:")
print(persona)
t=translator.DICTIONARYtoPmap(persona,id)
translator.addToResult(t)
print("Result:")
print(translator.getResult())

translator.delResult()    #Delete old results collected by serverPyProlog in self.result. Use ADDtoResult(string)
                       #to add a Prolog string to add to result.
print("Result cancellato:")
print("Result="+translator.getResult())


values=["0",2,3]
print("Array of values:")
print(values)
t=translator.VALUEStoPlist(values, "numbers")
translator.addToResult(t) #Convert an array to a Prolog list (in this case, the list is called numbers)
print("Result:")
print(translator.getResult())

#translator.makeAgent('atena')
#translator.cloneAgents('crono',2)

#translator.startMasMary()

translator.RESULTtoPL('prova', '', False)
