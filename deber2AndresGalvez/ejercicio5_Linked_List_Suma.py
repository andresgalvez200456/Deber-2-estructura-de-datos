from pickle import FALSE
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

global sumatoria
sumatoria = 0


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

    
    for numero_Lista in range(3):
        valor_usuario = input("ingresar un valor : ")
        try:
            valor_usuario = int(valor_usuario)
            sumatoria += valor_usuario
        except:
            while (excepcion == 0): #se ejecutara solamente hasta que el usuario ingrese un valor entero
                valor_usuario = input("(ERROR) ingresar un valor entero: ") 
                try:
                    valor_usuario = int(valor_usuario)
                    if(isinstance(valor_usuario,int) == True):
                        excepcion = 1
                except:
                    excepcion = 0
            excepcion = 0 #para qeu vuelva a entrar en el while anterior la SEGUNDA VEZ
             
            
        if(numero_Lista == 0):
            while (valor_usuario != 0):        
                valor = Node(valor_usuario % 10) #145(0) <-- digito 0 guardar en linked list desde la cabeza
                list1.insert_head(valor)
                valor_usuario = valor_usuario//10  #14(5) <--- el siguiente valor es 145 
            list1.list_traversed()    
        if(numero_Lista == 1):
            while (valor_usuario != 0):        
                valor = Node(valor_usuario % 10) #145(0) <-- digito 0 guardar en linked list desde la cabeza
                list2.insert_head(valor)
                valor_usuario = valor_usuario//10  #14(5) <--- el siguiente valor es 145 
            list2.list_traversed()   
        if(numero_Lista == 2):
            while (valor_usuario != 0):        
                valor = Node(valor_usuario % 10) #145(0) <-- digito 0 guardar en linked list desde la cabeza
                list3.insert_head(valor)
                valor_usuario = valor_usuario//10  #14(5) <--- el siguiente valor es 145 
            list3.list_traversed()
            while (sumatoria != 0):               
                valor_sum = Node(sumatoria % 10) #145(0) <-- digito 0 guardar en linked list desde la cabeza
                list_sum.insert_head(valor_sum)
                sumatoria = sumatoria//10  #14(5) <--- el siguiente valor es 145 
            print("sumatoria es ")
            list_sum.list_traversed() 

    
    

                  
   


       
    
 
    
       
    