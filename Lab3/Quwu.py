class Node :# class for node
	def __init__(self,num):
		self.data = num
		self.next = None

class Queue :# class for queue
	def __init__(self):
		self.head = None

	def printlist(self):# print function
		node = self.head
		while node:
			print(node.data,id(node.data))
			node = node.next

	def push(self,num):# push(last in)
		new = Node(num)
		if (self.head == None):
			self.head = new
		else: 
			node = self.head
			while(node.next != None):
				node = node.next
			node.next = new	

	def pop(self):# pop(first out)
		if(self.head == None):
			print("List is empty")
		else:
			node = self.head
			node = node.next
			self.head = node

	def peek(self):# peek the last element
		if (self.head == None):
			print("List is empty")
		else:
			node = self.head
			while(node.next != None):
				node = node.next
			print(node.data)

if __name__=="__main__":
	# a = Queue()
	# temp=0;
	# while temp == 0:
	# 	var=input("Enter 1 to push \nEnter 2 to pop \nEnter 3 to to peek\nEnter 4 to print\nEntere 5 to exit ")
	# 	if var==1:
	# 		data = input("Enter the data to be pushed")
	# 		a.push(data)
	# 	elif var == 2:
	# 		a.pop()
	# 	elif var == 3:
	# 		a.peek()
	# 	elif var == 4:
	# 		a.printlist()
	# 	else:
	# 		break
	a = Queue()
	a.push(1)
	a.push(2)
	a.push(3)
	a.push(4)
	a.printlist()
	# print("\n")
	# a.pop()
	# a.printlist()
	# print("\n")
	# a.peek()

			

