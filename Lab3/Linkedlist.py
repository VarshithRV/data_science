class Node :
	def __init__(self,num):
		self.data = num
		self.next = None

class linked_list :
	def __init__(self):
		self.head = None
	def printlist(self):
		node = self.head
		while node:
			print(node.data)

			node = node.next
	def push(self,num):
		new = Node(num)
		if (self.head == None):
			self.head = new
		else: 
			node = self.head
			while(node.next != None):
				node = node.next
			node.next = new	

	def popforstack(self):
		if (self.head == None):
			print("List is empty")
		else:
			node = self.head
			previous_node = Node(None)
			while(node.next != None):
				previous_node = node
				node = node.next
			previous_node.next = None

	def popforqueue(self):
		if(self.head == None):
			print("List is empty")
		else:
			node = self.head
			node = node.next
			self.head = node

if __name__ == "__main__":
	a = linked_list()
	a.head = Node(2)
	second = Node(3)
	third = Node(4)
	a.head.next = second
	second.next = third
	a.printlist()
	print("\n")
	a.push(5)
	a.printlist()
	print("\n")
	a.popforstack()
	a.printlist()
	print("\n")
	a.popforqueue()
	a.printlist()
