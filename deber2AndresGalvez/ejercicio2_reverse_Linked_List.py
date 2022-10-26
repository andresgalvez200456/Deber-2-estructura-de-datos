from email.header import Header
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Node:
    """
    Implementation of a node
    """
    def __init__(self, val=None):
        self.val = val
        self.next_node = None
    
    def set_next_node(self, next_node):
        self.next_node = next_node
        
class Singly_linked_list:
    """
    Implementation of a singly linked list
    """
    def __init__(self, head_node=None):
        self.head_node = head_node


class Singly_linked_list(Singly_linked_list):
    def list_traversed(self):
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node


class Node:
    """
    Implementation of a node
    """
    def __init__(self, val=None):
        self.val = val
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



class Singly_linked_list(Singly_linked_list):
    def insert_head(self, new_node):
        # insert to the head
        # A -> B -> null
        # R -> A -> B -> null 
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        
    def insert_tail(self, new_node):
        # insert to the tail
        # A -> B -> null
        # A -> B -> R -> null 
        node = self.head_node
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


class Singly_linked_list(Singly_linked_list):
    def reverse(self):
        prev = None
        current = self.head_node
        while current:
            next = current.next_node #guardar el nodo siguiente
            current.next_node = prev 
            prev = current
            current = next
        self.head_node = prev      



if __name__ == '__main__':
      
    m1 = Node("A")
    m2 = Node("B")
    m3 = Node("C")     
    m4 = Node("D")  
    m1.set_next_node(m2)
    m2.set_next_node(m3)
    m3.set_next_node(m4)
    list1 = Singly_linked_list(m1)
    list1.list_traversed()
    list1.reverse()
    print("reverse ")
    list1.list_traversed()

    #A -> B -> C -> D  

    #head
    #D -> A -> B -> C

    #HEAD.NEXT
    #D -> C -> A -> B

    #HEAD.NEXT.NEXT
    #D -> C -> B -> A


    #A <- B -> C -> D
    #B NEXT NODE IS A    PREV OF A IS B
    #A <- B <- C -> D

    #A <- B <- C <- D