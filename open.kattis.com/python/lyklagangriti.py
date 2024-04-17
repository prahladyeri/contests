class Node:
    def __init__(self, data):
        self.data = data  # Assigns the given data to the node
        self.next = None  # Initialize the next attribute to null

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None
        
    def insertAt(self, idx, data):
        if not self.head: # empty head, append at start
            self.head = Node(data)
            return
        temp, i = self.head, 0
        endNode = None
        while i < idx:
            if temp.next == None: endNode = temp
            temp = temp.next
            i += 1
        if temp == None:
            n = Node(data)
            endNode.next = n
        else:
            n = Node(temp.data)
            n.next = temp.next
            temp.data = data
            temp.next= n
            
    def removeAt(self, idx):
        p, n, i = None, self.head, 0
        while i < idx:
            p = n
            n = n.next
            i += 1
        if idx == 0 and n:
            if not n.next:
                self.head = None
            else:
                self.head = n.next
        elif p:
            p.next = n.next
            n = None # delete
        else: # zero node
            self.head = n
            
    def printAll(self):
        temp = self.head
        while temp:
            print(temp.data, end='')
            temp = temp.next
        print("")
        
        
    def __repr__(self):
        temp = self.head # Start from the head of the list
        ss = ''
        while temp:
            ss += temp.data + "=>"
            temp = temp.next # Move to the next node
        return ss

out = LinkedList() #deque() #[] #["" for x in range(len(line))]
#sout = ""
idx, n = 0, 0
for c in input():
    if c == 'L':
        idx -= 1
    elif c == 'R':
        idx += 1
    elif c == 'B' and idx > 0:
        idx -= 1
        #out.pop(idx)
        #del out[idx]
        out.removeAt(idx)
        n -= 1
    else:
        #out.insert(idx, c)
        out.insertAt(idx, c)
        n += 1
        idx += 1

#print(''.join(out))
out.printAll()