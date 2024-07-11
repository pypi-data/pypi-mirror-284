#!/usr/bin/env python3
# -*-coding:UTF-8 -*

import math
import time

from ..gen_obj import real

class Heap:
	"""
	A Heap is a specialized tree-based data structure that satisfies the heap property. For a max heap,
	this property ensures that for any given node I, the value of I is greater than or equal to the values
	of its children. This implementation provides methods to build a heap, maintain the heap property,
	sort the elements using the heap sort algorithm, and visually represent the heap structure.

	Attributes:
	elements (list[float]): The list of floating-point numbers that the heap is built from.
	heap_size (int): The number of elements in the heap that need to be maintained.
	total_elements (int): The total number of elements in the heap, including those not currently in the heap structure.

	Methods:
	build_heap(): Converts the list of elements into a heap.
	heapify(index: int): Ensures the subtree rooted at 'index' satisfies the heap property.
	calculate_height(): Calculates the height of the heap.
	get_left_child(index: int): Gets the index of the left child of the given node.
	get_parent(index: int): Gets the index of the parent of the given node.
	get_right_child(index: int): Gets the index of the right child of the given node.
	sort(): Sorts the elements in the heap using the heap sort algorithm.
	print_elements(): Returns a string representation of the heap elements.
	__str__(spacing: int, arrows: str): Generates a string representation of the heap in a tree-like structure.

	Time Complexity:
	- Building the heap: O(n log n)
	- Heapify operation: O(log n)
	- Calculating heap height: O(1)
	- Finding a child/parent index: O(1)
	- Heap sort: O(n log n)
	- String representation: O(n)

	Space Complexity:
	- All operations: O(1) (in-place with no additional space required except the input list)
	- String representation: O(n)

	Example:
	>>> heap = Heap([3, 2, 1, 7, 8, 4, 10, 16, 12])
	>>> heap.sort()
	>>> print(heap.print_elements())
	[1, 2, 3, 4, 7, 8, 10, 12, 16]
	>>> print(heap)
				  1 
			  ↙       ↘     
		  2               3 
		↙   ↘           ↙   ↘   
	  4       7       8       10
	 ↙ ↘     ↙ ↘     ↙ ↘     ↙ ↘  
	12  16

	"""
	
	def __init__(self, elements: list[real]):
		"""
		Initializes a new Heap object.

		Parameters:
		elements (list[real]): The list of floating-point numbers to be turned into a heap.

		Time Complexity: O(1), as it performs a constant number of operations.
		Space Complexity: O(n), where n is the number of elements in the input list.
		"""
		self.elements = elements
		self.heap_size = len(elements)
		self.total_elements = len(elements)

	def build_heap(self, order: int = 0) -> None:
		"""
		Converts the list of elements into a max heap if order == 0, or a mini heap else.

		Time Complexity: O(n log n), where n is the number of elements in the heap, in the worse case
		Space Complexity: O(1), as it modifies the list in place.
		"""
		self.heap_size = self.total_elements
		for i in range(pow(2, self.calculate_height()) - 2, -1, -1):
			self.heapify(i, order)

	def heapify(self, index: int, order: int = 0) -> None:
		"""
		Ensures the subtree rooted at 'index' satisfies the heap property: a max heap if order == 0, or a min heap else.

		Parameters:
		index (int): The root index of the subtree to heapify.

		Time Complexity: O(log n), where n is the number of elements in the heap.
		Space Complexity: O(log n), due to the recursive call stack.
		"""
		if index >= self.heap_size:
			return

		left_child = self.get_left_child(index)
		right_child = self.get_right_child(index)
		largest = index

		if left_child < self.heap_size and (self.elements[left_child] > self.elements[largest]) + order == 1:
			largest = left_child
		if right_child < self.heap_size and (self.elements[right_child] > self.elements[largest]) + order == 1:
			largest = right_child

		if largest != index:
			self.elements[index], self.elements[largest] = self.elements[largest], self.elements[index]
			self.heapify(largest, order)

	def calculate_height(self) -> int:
		"""
		Calculates the height of the heap.

		Time Complexity: O(1), as it performs a constant number of operations.
		Space Complexity: O(1), as it does not allocate any additional space.

		Returns:
		int: The height of the heap.
		"""
		return int(math.log2(self.total_elements))

	def get_left_child(self, index: int) -> int:
		"""
		Gets the index of the left child of the given node.

		Parameters:
		index (int): The index of the parent node.

		Returns:
		int: The index of the left child.
		"""
		return 2 * index + 1

	def get_parent(self, index: int) -> int:
		"""
		Gets the index of the parent of the given node.

		Parameters:
		index (int): The index of the child node.

		Returns:
		int: The index of the parent.
		"""
		return (index - 1) // 2

	def get_right_child(self, index: int) -> int:
		"""
		Gets the index of the right child of the given node.

		Parameters:
		index (int): The index of the parent node.

		Returns:
		int: The index of the right child.
		"""
		return 2 * index + 2

	def height_i(self, i: int) -> int:
		"""
		Calculates the height of the subtree rooted at the given index.

		Parameters:
		i (int): The index of the subtree root node.

		Returns:
		int: The height of the subtree.
		"""
		# If the index is out of range, the height is 0.
		if i >= self.heap_size:
			return 0

		# The height of a subtree is 1 plus the maximum height of its children.
		left_child = self.get_left_child(i)
		right_child = self.get_right_child(i)
		return 1 + max(self.height_i(left_child), self.height_i(right_child))
	
	def height(self) -> int:
		"""
		Calculates the height of the heap.

		Returns:
		int: The height of the heap.
		"""
		return int(math.log2(self.total_elements))

	def sort(self, order: int = 0) -> None:
		"""
		Sorts the elements in the heap using the heap sort algorithm.
		It sorts in the order of increasing if order == 0, or decreasing if order == 1.

		Time Complexity: O(n log n), where n is the number of elements in the heap.
		Space Complexity: O(1), as it modifies the list in place.
		"""
		self.build_heap(order)

		for i in range(self.total_elements - 1, 0, -1):
			self.elements[0], self.elements[i] = self.elements[i], self.elements[0]
			self.heap_size -= 1
			self.heapify(0, order)

	def print_elements(self) -> None:
		"""
		Prints heap elements.
		"""
		print(self.elements)
		
	def print_smooth(self, space: int = 1, arrows: str = "↙↘", delay: float = 0.2) -> None:
		"""
		Prints a smooth visual representation of the heap tree.

		Parameters:
		space (int): The amount of space between elements in the printed heap.
		arrows (str): The characters used to represent the tree branches.
		delay (float): The delay in seconds between printing steps.

		Returns:
		None
		"""
		# Calculate the maximum width of elements in the heap
		width_max = max([len(str(x)) for x in self.elements])
	
		# Adjust the width based on the evenness of the space
		if space % 2 == 0:
			width = width_max if width_max % 2 == 0 else width_max + 1 
		else:
			width = width_max + 1 if width_max % 2 == 0 else width_max 
		
		# Calculate the height of the heap
		height = self.height()
		
		# Calculate the necessary spacing and sequences for printing
		fact = width + space
		seq = 1
		edge_spaces = [0]
		middle_spaces = [space]
		
		# Calculate edge and middle spaces for each level of the heap
		for i in range(height-1, 0, -1):
			seq *= 2
			edge_spaces.append(int(fact*(seq-1)/2))
			middle_spaces.append(int(fact*seq - width))
		
		seq *= 2
		edge_spaces.append(int(fact*(seq-1)/2))
		middle_spaces.append(0)
		edge_spaces.reverse()
		middle_spaces.reverse()
		tab = self.elements
		
		# Print the root element of the heap
		print(" " * edge_spaces[0] + str(tab[0]).center(width))
		seq1, seq2 = 1, 2
		
		# Print the heap elements in a tree-like structure
		for i in range(1, height+1):
			seq1 = seq2
			seq2 *= 2
			first_index = seq1-1
			last_index = min(seq2-1, self.total_elements)
			edge_space = " " * edge_spaces[i]
			edge_space2 = int((width*3 + middle_spaces[i])/4) * " "
			middle_space = (int((width + middle_spaces[i])/2)-1) * " "
			pattern =  edge_space2 + arrows[0] + middle_space + arrows[1] + edge_space2
   
			print(edge_space + (" " * (middle_spaces[i])).join([pattern for j in range(min(self.total_elements, math.floor(seq1/2)))]))
			time.sleep(delay)
			print(edge_space + (" " * middle_spaces[i]).join([str(tab[j]).center(width) for j in range(first_index, last_index)]))
			time.sleep(delay)

	def __str__(self, spacing: int = 1, arrows: str = "↙↘") -> str:
		"""
		Generates a string representation of the heap in a tree-like structure.

		Parameters:
		spacing (int): The number of spaces between elements in the printed heap.
		arrows (str): The characters used to represent the tree branches.

		Returns:
		str: A string representation of the heap.

		Time Complexity: O(n), where n is the number of elements in the heap.
		Space Complexity: O(n), as it creates a string representation of the heap.

		Note:
		The method calculates the necessary spaces and arranges the elements to visually represent
		the heap's tree structure. The width of elements and spacing are adjusted to create a balanced look.
		"""
		# Find the maximum width of the elements when converted to strings
		max_width = max(len(str(element)) for element in self.elements)

		# Adjust the width for even spacing
		element_width = max_width + 1 if (max_width % 2) != (spacing % 2) else max_width

		# Calculate the height of the heap
		heap_height = self.calculate_height()

		# Initialize variables for spacing calculations
		factor = element_width + spacing
		sequence = 1
		edge_spaces = [0]
		middle_spaces = [spacing]

		# Calculate spaces for edges and middle based on the height of the heap
		for level in range(heap_height - 1, 0, -1):
			sequence *= 2
			edge_spaces.append(int(factor * (sequence - 1) / 2))
			middle_spaces.append(int(factor * sequence - element_width))

		# Final adjustments for the last level
		sequence *= 2
		edge_spaces.append(int(factor * (sequence - 1) / 2))
		middle_spaces.append(0)

		# Reverse the lists to start from the top of the heap
		edge_spaces.reverse()
		middle_spaces.reverse()

		# Start building the string representation from the root
		heap_str = " " * edge_spaces[0] + str(self.elements[0]).center(element_width) + "\n"
		seq_start, seq_end = 1, 2

		# Build the string representation level by level
		for level in range(1, heap_height + 1):
			seq_start = seq_end
			seq_end *= 2
			first_index = seq_start - 1
			last_index = min(seq_end - 1, self.total_elements)
			edge_space = " " * edge_spaces[level]
			edge_space_half = int((element_width * 3 + middle_spaces[level]) / 4) * " "
			middle_space = (int((element_width + middle_spaces[level]) / 2) - 1) * " "
			branch_pattern = edge_space_half + arrows[0] + middle_space + arrows[1] + edge_space_half

			# Add branches and elements for the current level
			heap_str += edge_space + (" " * middle_spaces[level]).join([branch_pattern for _ in range(min(self.total_elements, seq_start // 2))]) + "\n"
			heap_str += edge_space + (" " * middle_spaces[level]).join([str(self.elements[index]).center(element_width) for index in range(first_index, last_index)]) + "\n"

		return heap_str



if __name__ == "__main__":
	import k_general_kit.search_sort.heap as heap
	print(help(heap))

	# Test of print_smooth()
 
	tab = [1, 4, 0, -1, 8, 9]

	tab_heap = heap.Heap(tab)

	print(tab_heap.elements) 

	tab_heap.print_smooth()