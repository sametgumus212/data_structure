class Node:
    def __init__(self,content):
        self.content=content
        self.next=None

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n1.next=n2
n2.next=n3
n3.next=n4

q=n1
while q!=None:
    print(q.content)
    print(q.next)
    print('=====')
    q=q.next
