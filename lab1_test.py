
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.tail=None
        return
    


class CDLL:
    def __init__(self):
        self.head = None
        self.size = 0
        return 
    

    def add_first(self, new_data):
        new_data = Node(new_data)
        if self.head is None:
            self.head = new_data
            new_data.next=self.head
            new_data.tail=self.head
        else:
            last_node=self.head.tail
            last_node.next=new_data
            new_data.tail=last_node
            new_data.next=self.head
            self.head.tail=new_data
            self.head=new_data
        self.size+=1
        return
    
    def add_last(self, new_data):
        new_data = Node(new_data)
        if self.head is None:
            self.head = new_data
            new_data.next=self.head
            new_data.tail=self.head
        else:
            last_node=self.head.tail
            last_node.next=new_data
            new_data.tail=last_node
            new_data.next=self.head
            self.head.tail=new_data
        self.size+=1
        
        return

    def delete_first(self):
        if self.head is None:
            return
        if self.head.next==self.head:
            self.head=None
            self.size-=1
            return
        self.head=self.head.next
        self.head.tail=self.head.tail.tail
        self.size-=1 
        return
    
        

        
    def delete_last(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head=None
            self.size-=1
            return
        last_node=self.head.tail
        last_node.tail.next=self.head
        self.head.tail=last_node.tail
        self.size-=1
        return
    

        

    def update_at_position(self, value, position):
        if position>=self.size:
            return "INVALID POSITION"
        temp = self.head
        for i in range(position):
            temp = temp.next
        temp.data=value    
        return  

    def delete_at_position(self, position):
        if position>=self.size:
            return "INVALID POSITION"
        if position==0:
            self.delete_first()
            return
        temp = self.head
        for i in range(position):
            temp = temp.next
        temp.tail.next=temp.next
        temp.next.tail=temp.tail
        self.size-=1
        return 

    def insert_at_position(self, value, position):
        if position>self.size:
            return "INVALID POSITION"
        if position==0:
            self.add_first(value)
            return
        else:
            new_node=Node(value)
            temp = self.head
            for i in range(position-1):
                temp = temp.next
            new_node.next=temp.next
            new_node.tail=temp
            temp.next=new_node
            new_node.next.tail=new_node
            self.size+=1
        return
        


    def rotate(self, steps=1):
        if self.head is None:
            return
        if steps>0:
            for i in range(steps):
                self.head=self.head.next
        else:
            for i in range(-steps):
                self.head=self.head.tail
        return
    
        
    
    def __str__(self):
        temp = self.head
        out = '' 
        while temp:
            out += str(temp.data) + ' ' 
            temp = temp.next
            if temp == self.head:
                break
        return out 
    

test_list = CDLL()

# Add elements to the list
test_list.add_last(1)
test_list.add_last(2)
test_list.add_last(3)
test_list.add_last(4)
test_list.add_last(5)
test_list.add_first(0)
test_list.add_first(-1)

# Print the initial list
print("Initial list:")
print(test_list)

# Rotate the list forward by 2 steps
test_list.rotate(2)
print("List after rotating forward by 2 steps:")
print(test_list)

# Rotate the list backward by 1 step
test_list.rotate(-1)
print("List after rotating backward by 1 step:")
print(test_list)

# Add an element to a list on a given index
test_list.insert_at_position(100,3)
print("List after adding 100 at index 3:")
print(test_list)

# Delete the first element of the list
test_list.delete_first()
print("List after deleting the first element:")
print(test_list)

# Delete the last element of the list
test_list.delete_last()
print("List after deleting the last element:")
print(test_list)

#ZADATAK 2 ROUND ROBIN SCHEDULING

process_names = ['A', 'B', 'C', 'D', 'E']
process_times = [363, 120, 200, 232, 75]
time_slice = 100
n = len(process_times)
# Create a circular doubly linked list
process_list = CDLL()
for i in range(n):
    process_list.add_last([process_names[i], process_times[i]])


# Print the initial list
print("Initial list:")
print(process_list)
# Perform round robin scheduling
print("Round robin scheduling:")
while process_list.size > 0:
    process = process_list.head.data
    process[1] -= time_slice
    if process[1] <= 0:
        print("Process", process[0], "completed.")  
        process_list.delete_first()
    else:
        print("Process", process [0], "remaining time:", process[1], "ms.")
        process_list.rotate()

print("All processes completed.")