def checkBrackets(str):
	brackets = []
	pairs = {"(": ")", "[": "]", "{": "}"}
	for symbol in str:
		if symbol == "(" or symbol == "[" or symbol == "{":
			brackets.append(symbol)
		elif symbol == ")" or symbol == "]" or symbol == "}":
			if len(brackets) > 0 and symbol == pairs[brackets[-1]]:
				brackets.pop()
			else:
				return False
	return len(brackets) == 0

str = "if (someValue > 7) { mas[6] = 7; }"

if checkBrackets(str) == True:
	print ("Check Passed.")
else:
	print ("Check Failed.") 
