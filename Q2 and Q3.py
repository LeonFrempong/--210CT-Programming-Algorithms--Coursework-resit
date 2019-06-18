# q2) double linked list delete node function

class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None
 
class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          #Not actually perfect: how do we prepend to an existing list?
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x

     # the function below in the deleled function that has been implemented.
      
      def delete(self,n, x):
            if n.prev != None: #checks if there is a previous node in the list
                  n.prev.next=n.next# the previous node is then point to the next node in the list
            else:
                  self.head = n.next
                  if n.next != None: # checks if there is a next node
                        n.next.prev = n.prev #the next node can be pointed to the previous node 
                  else:
                        self.tail = n.prev
        #the function below is to find the middle element(s) in the list

      def findMiddleValue(self):
          slow_pointer = self.head 
          fast_pointer = self.head
          if self.head is not None:
              while (fast_pointer is not None and fast_pointer.next is not None):
                  fast_pointer = fast_pointer.next.next
                  slow_pointer = slow_pointer.next
                  print("The middle element is: ", slow_pointer.value) 
      
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ",",".join(values))
       


                                                      


         
if __name__ == '__main__':
      l=List()
      l.insert(None, Node(4))
      l.insert(l.head,Node(6))
      l.insert(l.head,Node(8))
      l.insert(l.head,Node(12))
      l.display()
      l.delete(l.head, Node(4))
      l.display()
      l.findMiddleValue()

      
      


      
