
import ctypes
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


class MyQueue(object): 
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x ) :
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1]) # top del stack [-1]
            self.s1.pop()
 
        
        self.s1.append(x)
 
        
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self) -> int:

            # if first stack is empty
        if len(self.s1) == 0:
            print("Q is Empty")
     
        # Return top of self.s1
        x = self.s1[-1]
        self.s1.pop()
        return x
 
    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1
    
    
    def size(self):
        
        #Return size of the stack
        
        return self.l 
         

#best case
q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("best case") 
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())


#worst case complejidad 2n 
print("worst case")
for i in range(9999):
    print(i)
    q.enqueue(i)

print("primer elemento es:")
print(q.dequeue())

#worst case Queue
#recorre una vez toda la cola para insertar el elemento al final  
"""""
class Queue(Queue):
    def enqueue(self, item):
        
        Add new item to the queue
        if self.l == self.n:
            raise ValueError("no more capacity")
        self.queue[self.l] = item
        self.l += 1
"""
#mientras tanto el dequeue en la clase cola tiene copmlejidad n 
""""
class Queue(Queue):
    def dequeue(self):
       
        Remove an element from the queue
      
        c = self.queue[0]
        for i in range(1,self.l):
            self.queue[i-1] = self.queue[i]
        self.queue[self.l - 1] = ctypes.py_object
        self.l -= 1
        return c
"""