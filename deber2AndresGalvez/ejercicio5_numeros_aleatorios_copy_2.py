from pickle import FALSE
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from functools import wraps

list_time = []

def timeit1(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time  
        list_time.append(total_time)      
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.10f} seconds')
        return result
    return timeit_wrapper




class Node:
    """
    Implementation of a node
    """
    def __init__(self, val=None):
        self.val = val # el valor usuario se trasnforma en un entero para luego proceder a sumar           
        self.next_node = None
    
    def set_next_node(self, next_node):
        self.next_node = next_node
        
class Singly_linked_list:
    """
    Implementation of a singly linked list
    """
    def __init__(self, head_node=None):
        self.head_node = head_node
        
    def list_traversed(self):
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node
         
        

    #def sum(self):
        #sum = 0
        #node = self.head_node
        #while node:
        #    sum += node.val
        #    node = node.next_node
        #sum_node = Node(sum)
        #insert tail
        #node = self.head_node #indico el primer elemento
        #prev = None
        #while node:
            #prev = node
            #node = node.next_node
        #prev.set_next_node(sum_node)
        

class Singly_linked_list(Singly_linked_list):
    def insert_head(self, new_node):
        # insert to the head
        # A -> B -> null
        # R -> A -> B -> null 
        new_node.set_next_node(self.head_node) # 1450    primera cabeza (0)  luego la cabaeza va a ser (5)   
        self.head_node = new_node
        
    def insert_tail(self, new_node):
        # insert to the tail
        # A -> B -> null
        # A -> B -> R -> null 
        node = self.head_node #indico el primer elemento
        prev = None
        while node:
            prev = node
            node = node.next_node
        prev.set_next_node(new_node)
        
    def insert_middle(self, new_node, value):
        # insert in the middle
        # A -> B -> C -> null
        # A -> B -> R -> C -> null
        node = self.head_node
        while node.val != value:
            node = node.next_node
        if node:
            new_node.set_next_node(node.next_node)
            node.set_next_node(new_node)
        else:
            self.insert_tail(new_node)


if __name__ == '__main__':

    #esta parte sirve para asegurar que el usuario solamente pueda ingresar numeros enteros 
    #porque con los numeros se calcula la suma 
    global numero_Lista
    numero_Lista = 1
    excepcion = 0
    list1 = Singly_linked_list()
    list2 = Singly_linked_list()
    list3 = Singly_linked_list()
    list_sum = Singly_linked_list()

    @timeit1
    def calcular_tiempo():
        global sumatoria
        sumatoria = 0
        for numero_Lista in range(3):
            valor_usuario = random.randint(10**49, 10**50)
            sumatoria += valor_usuario         
            if(numero_Lista == 0):
                while (valor_usuario != 0):   # <----- O(n)      
                    valor = Node(valor_usuario % 10) #145(0) <-- digito 0 guardar en linked list desde la cabeza
                    list1.insert_head(valor) 
                    valor_usuario = valor_usuario//10  #14(5) <--- el siguiente valor es 145 
                print("lista 1")
                list1.list_traversed()    
            if(numero_Lista == 1):
                while (valor_usuario != 0):        
                    valor = Node(valor_usuario % 10) 
                    list2.insert_head(valor)  # <----parte clave para la complejidad, cada vez que inserto un nodo desde la cabeza, es mas efectivo que insertar en la cola, porque no tiene que recorrer ningun nodo extra 
                    valor_usuario = valor_usuario//10  # por lo tanto insert_head se realizara n veces dependiendo del tamanio del numero es decir O(n) 
                print("lista 2")    
                list2.list_traversed()   
            if(numero_Lista == 2):
                while (valor_usuario != 0):        # si se insertaria desde la cola, la complejidad seria n^2  como es desde la cabeza es # <---- O(n)
                    valor = Node(valor_usuario % 10) 
                    list3.insert_head(valor)  
                    valor_usuario = valor_usuario//10  
                print("lista 3") 
                list3.list_traversed()
                while (sumatoria != 0):               
                    valor_sum = Node(sumatoria % 10) 
                    list_sum.insert_head(valor_sum)
                    sumatoria = sumatoria//10   
                print("sumatoria es ")
                list_sum.list_traversed() 
    
    calcular_tiempo()
    print(len(list_time))
    #parte 6 estimacion de la complejidad
    # cada funcion de insert_head tiene copmlejidad dentro del while 0(n)  como son 3 while y otro while para la sumatoria es = 0(4n) 
    #por lo tanto es una complejidad lineal 
    

                  
   


       
    
 
    
       
    