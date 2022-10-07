class Node :# class for node 
	def __init__(self,num):
		self.data = num
		self.next = None

class Stack :# class for stack
	def __init__(self):
		self.head = None

	def printlist(self):# print the stack
		node = self.head
		while node:
			print(node.data,id(node.data))
			node = node.next

	def push(self,num):# push to stack(last in)
		new = Node(num)
		if (self.head == None):
			self.head = new
		else: 
			node = self.head
			while(node.next != None):
				node = node.next
			node.next = new

	def pop(self):# pop stack (last out)
		if (self.head == None):
			print("List is empty")
		else:
			node = self.head
			previous_node = Node(None)
			while(node.next != None):
				previous_node = node
				node = node.next
			previous_node.next = None

	def peek(self):# peek the last element
		if (self.head == None):
			print("List is empty")
		else:
			node = self.head
			while(node.next != None):
				node = node.next
			print(node.data)

if __name__=="__main__":
	a = Stack()
	a.push(1)
	a.push(2)
	a.push(3)
	a.push(4)
	a.printlist()
	print("\n")
	# a.pop()
	# a.printlist()
	# print("\n")
	# a.peek()