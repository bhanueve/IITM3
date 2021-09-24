def reverse(root):
    """
    takes in a starting node of a linked list, reverses it in place and returns the 
    
    starting node of the reversed list
    """
    if root.isempty():
        return root
    elif root.next == None:
        return root
    temp = root
    length = 1
    while True:
        if temp.next != None:
            length += 1
            temp = temp.next
        else:
            break
    insert_position = root
    for i in range(length):
        last_but_one = root
        for j in range(length - 1):
            if last_but_one.next.next != None:
                last_but_one = last_but_one.next
        last = last_but_one.next
        if i == 0:
            last.next = insert_position
            last_but_one.next = None
            root = last
            home = last
            insert_position = root
        elif i > 0 and i < length - 1:
            last.next = insert_position.next
            last_but_one.next = None
            insert_position.next = last
            insert_position = insert_position.next
        else:
            break
    return home

class node:
    def __init__(self, v = None):
        self.value = v
        self.next = None
        return
    def isempty(self):
        if self.value == None:
            return True
        else:
            return False
    def append(self, v):
        if self.isempty():
            self.value = v
            return
        temp = self
        while temp.next != None:
            temp = temp.next
        temp.next = node(v)
        return
    def showlist(self):
        temp = self
        print(temp.value)
        while temp.next != None:
            temp = temp.next
            print(temp.value)
        

root = node(64)
root.append(7)
root.append(28)
root.append(43)
root.append(3)

a = reverse(root)
    