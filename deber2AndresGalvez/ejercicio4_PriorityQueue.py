import time
import pandas as pd
import numpy as np
import matplotlib
import ctypes




class builder():
    def __init__(self, data, priority):
        self.l = 0
        self.data = data #DATO INSERTADO
        self.priority = priority # POSICION DE PRIORIDAD 

class PriorityQueue:
    def __init__(self):
        self.queue = list()       
    def insert(self,node): # ingresar a la cola
        """
        Add new item to the queue
        """
        ##########################################################################################  busca el elemento con mayor prioridad 
        if(self.size() == 0):
            self.queue.append(node)  # SI NO TENGO NADA EN MI COLA, INSERTO EN EL PRIMERO
        else:
            for i in range(0, self.size()):
                if(node.priority >= self.queue[i].priority):
                    if(i == (self.size()-1)):
                        self.queue.insert(i+1, node) #################################### SU COMPLEJIDAD ES O(n)
                    else:
                        continue
                else:
                    self.queue.insert(i, node)

        ############################################################################################################
    def dequeue(self): #sacar de la cola y retornar el elemento con mayor prioridad
        """
        Remove an element from the queue
        """
        return self.queue.pop(0) # primero se ordena segun su prioridad y luego se elimina el elemento que este priemro porque ese seria el de mayor prioridad

    
    def show(self):
        for i in self.queue:
            print("{} - {}".format(i.data, i.priority))

    
    def size(self):
        return len(self.queue)

if __name__ == '__main__':
    b1 = builder("C", "4")
    b2 = builder("v", "1")
    b3 = builder("g", "3")
    b4 = builder("h", "8")

    pq = PriorityQueue()
    pq.insert(b1)
    pq.insert(b2)
    pq.insert(b3)
    pq.insert(b4)


    pq.show()

    print("dequeue first element")
    pq.dequeue() # borrar el elemento que este primero, como ya esta ordenado la prioridad 

    pq.show()

