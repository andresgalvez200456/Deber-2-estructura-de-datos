

import ctypes
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
        self.size = 0
        
    def list_traversed(self):
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node

class Singly_linked_list(Singly_linked_list):
    def push(self, new_node): #push # en un stack vacio siempre se inserta en la primera posicion por eficiencia 
        # insert to the head
        # A -> B -> null
        # R -> A -> B -> null    
        #O(1) mejor que insertar al final
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        self.size += 1

class Singly_linked_list(Singly_linked_list): # se elimina la cabeza en elemento del Stack 
    def pop(self):

            temporal = self.head_node
            self.head_node.set_next_node(None)  #A -> X (B) PUNTERO (A) APUNTA A NULL
            self.head_node =  temporal          # A = B     A(X)   LA CABEZA A SE TRANSFORMA EN B
            self.size -= 1
            return temporal              # B -> C -> D     LA NUEVA CABEZA B APUNTA HACIA C Y LA CADENA CONTINUA
                    
class Singly_linked_list(Singly_linked_list):
    def top(self):
        """
        Show the top element of the stack
        """
        return self.head_node

class Singly_linked_list(Singly_linked_list):
    def full(self):
        """
        Show the top element of the stack
        """
        if(self.size != 5):
            return False
        else:
            return True

class Singly_linked_list(Singly_linked_list):
    def empty(self):
        """
        Show the top element of the stack
        """
        if(self.size != 0):
            return False
        else:
            return True

class Singly_linked_list(Singly_linked_list):
    def size(self):
        """
        Show the top element of the stack
        """
        return self.size


class Stack(object):
    """
    Implementation of the stack data structure
    """

    def __init__(self, n):
        self.l = 0
        self.n = n
        self.stack = self._create_stack(self.n)        
    
    def _create_stack(self, n):
        """
        Creates a new stack of capacity n
        """
        return (n * ctypes.py_object)()


class Stack(Stack):
    def push(self, item):
        """
        Add new item to the stack
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        self.stack[self.l] = item
        self.l += 1

class Stack(Stack):
    def pop(self):
        """
        Remove an element from the stack
        """
        # self.l = 0
        # 0 is equivalent to False
        # any number != 0 is True
        if not self.l:
            raise('stack is empty')
        c = self.stack[self.l-1]
        self.stack[self.l] = ctypes.py_object
        self.l -= 1
        return c

class Stack(Stack):
    def top(self):
        """
        Show the top element of the stack
        """
        return self.stack[self.l-1]

class Stack(Stack):
    def full(self):
        """
        Is the stack full?
        """
        return self.l == self.n
        # if self.l == self.n:
        #    return True
        # return False

    def empty(self):
        """
        Is the stack empty?
        """
        return self.l == 0
        #if self.l == 0:
        #    return True
        #return False

    def size(self):
        """
        Return size of the stack
        """
        return self.l                

