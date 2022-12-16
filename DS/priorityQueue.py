import sys

# Structure for the elements in the
# priority queue
class item :
	value = 0
	priority = 0
class GFG :

	# Store the element of a priority queue
	pr = [None] * (100000)
	
	# Pointer to the last index
	size = -1
	
	# Function to insert a new element
	# into priority queue
	@staticmethod
	def enqueue( value, priority) :
	
		# Increase the size
		GFG.size += 1
		
		# Insert the element
		GFG.pr[GFG.size] = item()
		GFG.pr[GFG.size].value = value
		GFG.pr[GFG.size].priority = priority
		
	# Function to check the top element
	@staticmethod
	def peek() :
		highestPriority = -sys.maxsize
		ind = -1
		
		# Check for the element with
		# highest priority
		i = 0
		while (i <= GFG.size) :
		
			# If priority is same choose
			# the element with the
			# highest value
			if (highestPriority == GFG.pr[i].priority and ind > -1 and GFG.pr[ind].value < GFG.pr[i].value) :
				highestPriority = GFG.pr[i].priority
				ind = i
			elif(highestPriority < GFG.pr[i].priority) :
				highestPriority = GFG.pr[i].priority
				ind = i
			i += 1
			
		# Return position of the element
		return ind
	
	# Function to remove the element with
	# the highest priority
	@staticmethod
	def dequeue() :
	
		# Find the position of the element
		# with highest priority
		ind = GFG.peek()
		
		# Shift the element one index before
		# from the position of the element
		# with highest priority is found
		i = ind
		while (i < GFG.size) :
			GFG.pr[i] = GFG.pr[i + 1]
			i += 1
			
		# Decrease the size of the
		# priority queue by one
		GFG.size -= 1