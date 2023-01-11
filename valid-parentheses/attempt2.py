# NEW ATTEMPT
class Solution:
	def isValid(self,s):
		Map = {
			")":"(",
			"]":"[",
			"}":"{"
		}
		stack = []
		
		for c in s:
			if c not in Map: # if not closing parentheses, add to stack to be matcher later
				stack.append(c)
				continue
			#O.W. closing parenthesis
			if not stack or Map[c] != stack[-1]:
			# if stack is empty then no way to match this closing parentheses
			# if the opening parenthesis don't match for this closing, then not valid match
				return False
			# Valid match
			stack.pop() # parenthesis have been matched correctly, pop opening from list
		return not stack
		# EXAMPLE RUN:
		"""
		VALID TEST:
			Given s="{[()]()()[[]]}"
			stack = "{"
			stack = "{["
			stack = "{[("
			stack = "{["
			stack = "{"
			stack = "{("
			stack= "{"
			stack="{("
			stack = "{"
			stack = "{["
			stack = "{[["
			stack = "{["
			stack = "{"
			stack = ""
			return True

		VALID TEST:
			Given s="{[({)]()()[[]]}"
			stack = "{"
			stack = "{["
			stack = "{[("
			stack = "{[({"
			return False #since ) doesn't match {
		"""