#   mode 1  |  mode 2  |  mode 3  |   mode 4 |  mode 5  |
#     *    |    *    |    *    |    *    |    *    |
#    ***   |   * *   |   *.*   |   * *   |   *.*   |
#   *****  |  * * *  |  *.*.*  |  *   *  |  *...*  |
#  ******* | * * * * | *.*.*.* | *     * | *.....* |
#   *****  |  * * *  |  *.*.*  |  *   *  |  *...*  |
#    ***   |   * *   |   *.*   |   * *   |   *.*   |
#     *    |    *    |    *    |    *    |    *    | 
#

def printRomb(size, mode):
	if mode < 1 or mode > 5:
		mode = 1
	middle = int(size / 2)
	for i in range(0, size):
		line = ""
		b = True
		for j in range(0, size):
			length = i + 1 if i < middle else size - i
			if mode < 4:
				if j > middle - length and j < middle + length:
					if mode == 1:
						line += "*"
					else:
						if b == True:
							line += "*"
							b = False
						else:
							if mode == 2:
								line += " "
							else:
								line += "."
							b = True
				else:
					line += " "
			else:
				if j == middle - length + 1 or j == middle + length - 1:
					line += "*"
				else:
					if mode == 4:
						line += " "
					elif mode == 5:
						if j > middle - length and j < middle + length:
							line += "."
						else:
							line += " "
		print (line)

# main

size = int(input("size = "))
mode = int(input("mode = "))
printRomb(size, mode)
