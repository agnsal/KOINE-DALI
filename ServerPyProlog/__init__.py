__author__ = 'Agnese'

import re
import json
import os
import time
import stat
import sys

class ServerPyProlog:

    def __init__(self):
        self.StringResult = "" #risultato, stato attuale della conversione
        self.ListResult = list()
        path = sys.path[0]
        self.root = path[:path.rfind('DALI')]
        #print(path)
        #print (self.root)

    def findRoot(self):
        #restituisce il path di root
        return self.root

    def addToStringResult(self,string):
        #aggiunge una stringa al risultato
        string = string + os.linesep
        self.result = self.StringResult + string

    def addToListResult(self,string):
        #aggiunge una stringa al risultato
        self.result = self.ListResult.append(string)

    def getStringResult(self):
        #restituisce la stringa risultato
        return self.StringResult

    def getListResult(self):
        #restituisce la stringa risultato
        return self.ListResult

    def delResult(self): 
        #cancella la stringa contenuta in result
        self.StringResult = ""
        self.ListResult = []

    def notificationTXT(txtName,path): 
        #crea un file testuale vuoto di notifica
        path = path + os.sep + txtName + ".txt"
        handle = False
        while handle is False:
            file = open(path, "w")
        file.close()

    def RESULTtoPL(self, fileName, path, replace):
        # Scrive il risultato su un file Prolog.
        # Se replace è true, cancella un eventuale file precedente con lo stesso nome nel path dato,
        # altrimenti aggiunge result a questo file.
        if path is '':
            destinazione = fileName+'.pl'
        else:
            destinazione = path+os.sep+fileName+".pl"
        handle = False
        if replace is False:
            while (handle is False):
                handle = open(destinazione, 'a')
                time.sleep(0.1)
        else:
            while handle is False:
                handle = open(destinazione, 'w')
                time.sleep(0.1)
        handle.write(os.linesep+self.getStringResult())
        handle.close()

    def RESULTtoTXT(self, fileName, path, replace):
        # Scrive il risultato su un file Prolog.
        # Se replace è true, cancella un eventuale file precedente con lo stesso nome nel path dato,
        # altrimenti aggiunge result a questo file.
        if path is '':
            destinazione = fileName+'.txt'
        else:
            destinazione = path+os.sep+fileName+".txt"
        handle = False
        if replace is False:
            while (handle is False):
                handle = open(destinazione, 'a')
                time.sleep(0.1)
        else:
            while handle is False:
                handle = open(destinazione, 'w')
                time.sleep(0.1)
        handle.write(os.linesep+self.getResult())
        handle.close()

    def cleanName(self,string): 
        # "pulisce" una stringa da trasformare in nome Prolog da caratteri non contemplati 
        string = string.replace(' ', '_')
        string = string.replace('.', '')
        string = string.replace(',', '')
        string = string.replace('=', '')
        string = re.sub("/[^a-zA-Z0-9_-]/", "", string)
        string = string.lower()
        if re.findall('/^[a-z]+$/i', string[0]) is False:
            string = string[1:]
        return string

    def cleanJson(self,string): 
        #"pulisce" il Json da caratteri non contemplati da Prolog
        string = string.replace("{", "")
        string = string.replace("}", "")
        string = string.replace('"', "")
        string = string.replace(' ', "")
        string = string.replace("'", "")
        string = string.lower()
        return string

    def idConverter(self,numericId): 
        # converte i numeri degli id numerici in lettere (il Prolog non gestisce gli id numerici)
        string = str(numericId)
        string = string.replace('0', 'a')
        string = string.replace('1', 'b')
        string = string.replace('2', 'c')
        string = string.replace('3', 'd')
        string = string.replace('4', 'e')
        string = string.replace('5', 'f')
        string = string.replace('6', 'g')
        string = string.replace('7', 'h')
        string = string.replace('8', 'i')
        string = string.replace('9', 'l')
        return string

    def cleanArrayElement(self, element):
        # Pulisce l'elemento di un array
        risultato = str(element).lower()
        return risultato

###############################################################################################################################

    def JSONtoPmapString(self,json,mapName):
        # Converte una stringa Json in una stringa lista Prolog
        json = str(json)
        list = self.cleanJson(json)
        mapName = self.cleanName(mapName)
        risultato = ""
        array = list.strip().split(',') #strip() rimuove gli spazi; split() splitta la stringa in un array
        l = len(array)
        for i in range(0,l):
            map = array[i].split(':')
            r = mapName+"("+map[0].lower()+","+map[1]+")." + os.linesep
            risultato = risultato + r
        return risultato

    def JSONtoPmapList(self,json,mapName):
        # Converte una stringa Json in una stringa lista Prolog
        json = str(json)
        list = self.cleanJson(json)
        mapName = self.cleanName(mapName)
        risultato = []
        array = list.strip().split(',') #strip() rimuove gli spazi; split() splitta la stringa in un array
        l = len(array)
        for i in range(0,l):
            map = array[i].split(':')
            r = mapName+"("+map[0].lower()+","+map[1]+")."
            risultato.append(r)
        return risultato

    def JSONtoAtom(self,json,atomName):
        # Converte una stringa Json in una stringa lista Prolog
        json = str(json)
        list = self.cleanJson(json)
        atomName = self.cleanName(atomName)
        risultato = []
        array = list.strip().split(',') #strip() rimuove gli spazi; split() splitta la stringa in un array
        l = len(array)
        r = atomName + "("
        for i in range(0,l):
            map = array[i].split(':')
            r = atomName+"("+map[0].lower()+","+map[1]+")."
            risultato.append(r)
        return risultato

    def cleanDictionary(self,dict): 
        # "pulisce" i dictionary per elaborarli in Prolog
        dict = json.dumps(dict)
        return dict

    def DICTIONARYtoPmap(self,dict,mapName): 
        # trasforma un dictionary in una mappa Prolog
        mapName = self.cleanName(mapName)
        dict = self.cleanDictionary(dict)
        dict = self.cleanJson(dict)
        risultato = self.JSONtoPmap(dict,mapName)
        return risultato

    def DICTIONARYtoPpredicate(self,dict,predicateName): 
        #trasforma un dictionary in un insieme di predicati Prolog
        predicateName = self.cleanName(predicateName)
        dict = str(dict)
        dict = self.cleanJson(dict)
        array = dict.split(',')
        a = ""
        risultato = ""
        l = len(array)
        for i in range(0,l):
            subarray = str(array[i]).split(':')
            pred = predicateName+"("+subarray[0]+","+subarray[1]+").\r\n"
            risultato = risultato+pred
        return risultato

    def VALUEStoPlist(self,valuesArray,listName): 
        # trasforma un'array di valori in una lista Prolog
        v = str(valuesArray[0])
        l = len(valuesArray)
        for i in range(1,l-1):
            v = v+","+str(valuesArray[i])
        if listName!=' ':
            name = self.cleanName(listName)
            risultato = name + "=["+v+"]." + os.linesep
        else:
            risultato = "[" + v + "]." + os.linesep
        return risultato

    def ARRAYtoParrayTerm(self, arrayArg, functor=''):
        # crea un termine Prolog che ha per nome (ovvero come funtore), la stringa functor e come argomento l'array arrayArg
        if (functor!=' ' and functor!='' and functor!=None) :
            name = self.cleanName(functor)
            risultato = name + '(['
            for a in arrayArg:
                a = self.cleanArrayElement(a)
                risultato = risultato + a + ','
        else:
            risultato = '(['
            for a in arrayArg:
                a = self.cleanArrayElement(a)
                risultato = risultato + a + ','
        risultato = risultato[:-1]
        risultato = risultato + ']).'
        return risultato

    def TIMEtoPlist(self, tempo, tName):
        # Trasforma una variabile contenente tempo (es. 10:30:22) in una lista Prolog
        if (tName!=' ' and tName!='' and tName!=None) :
            name = self.cleanName(tName)
            risultato = name + '=[' + str(tempo).replace(':', ',').replace('.',',').replace('/',',') +']'
        else:
            risultato = '[' + str(tempo).replace(':', ', ').replace('.',',') +']'
        return risultato

    def DATEtoPlist(self, date, dateName):
        # Trasforma una variabile contenente tempo (es. 10:30:22) in una lista Prolog
        if (dateName!=' ' and dateName!='' and dateName!=None) :
            name = self.cleanName(dateName)
            risultato = name + '=[' + str(time).replace(':', ',').replace('.',',').replace('/',',') +']'
        else:
            risultato = '[' + str(date).replace(':', ', ').replace('.',',').replace('/',',') +']'
        return risultato

    def MESSAGEtoPlist(self, msg, msgName=''):
        # Trasforma una variabile contenente tempo (es. 10:30:22) in una lista Prolog
        if (msgName!=' ' and msgName!='' and msgName!=None) :
            name = self.cleanName(msgName)
            risultato = name + '=[' + str(time).replace(':', ',').replace('.',',').replace('/',',') +']'
        else:
            risultato = '[' + str(msg).replace(':', ', ').replace('.',',').replace('/',',') +']'
        return risultato




    ##########################################################################################


    def makeAgent(self,agentType):
        # crea un agente a partire da un tipo di agente.
        # Es di agentType: 'atena'
        agentFolder = self.root + os.sep + 'DALI' + os.sep + 'ServerDALImas' + os.sep + 'mas' + os.sep + 'instances'
        others = os.listdir(agentFolder)
        print(others)
        brothers=list()
        for o in others:
            if o.find(agentType)!=-1:
                o.split('.txt')
                brothers.append(o)
                #print(brothers)
        l=len(brothers)
        newBornName = agentType + str(l) + '.txt'
        print(newBornName)
        newAgent = self.root + os.sep + 'DALI' + os.sep + 'ServerDALImas' + os.sep + 'mas' + os.sep + 'instances' + os.sep + newBornName
        out_file = open(newAgent, "w")
        out_file.write("agentType" + agentType.title())
        out_file.close()

    def cloneAgents(self,agentType,n):
        # crea n degli agenti cloni a partire da un tipo di agente.
        # Es di agentType: 'atena'
        agentFolder = self.root + os.sep + 'DALI' + os.sep + 'ServerDALImas' + os.sep + 'mas' + os.sep + 'instances'
        others = os.listdir(agentFolder)
        print(others)
        brothers = list()
        for o in others:
            if o.find(agentType) != -1:
                o.split('.txt')
                brothers.append(o)
                #print(brothers)
        l = len(brothers)
        i=0
        while i<n:
            newBornName = agentType + str(l+i) + '.txt'
            print(newBornName)
            newAgent = self.root + os.sep + 'DALI' + os.sep + 'ServerDALImas' + os.sep + 'mas' + os.sep + 'instances' + os.sep + newBornName
            out_file = open(newAgent, "w")
            out_file.write("agentType" + agentType.title())
            out_file.close()
            i=i+1

    def startMasMary(self):
        os.system('bash ' + self.root + 'DALI' + os.sep + 'ServerDALImas' + os.sep + 'startmasMary.sh ' + self.root + 'DALI')








