'''
Given a mapping of digits to letters (as in a phone number),
 and a digit string, return all possible letters the number 
 could represent. You can assume each valid number in the 
 mapping is a single digit.

For example if 
{“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} 
then “23” should return 
[“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"]
'''
import math
class numberMapping:
		def __init__(self, num, letters):
			self.num = num
			self.letters = letters

def findLetters(num,mapping):
	for i in range(0,len(mapping)):
		if mapping[i].num == num:
			return mapping[i].letters
		
def displayConfigurations(number,mapping):
	preList = []
	finalList = []
	string = ""
	totalLength = 1

	for i in number:
		preList.append(findLetters(i,mapping))

	for i in range(0,len(preList)):
		totalLength *= len(preList[i])

	interval = totalLength / len(preList[0])
	for i in range(0,totalLength):
		j = math.floor(i / interval)
		finalList.append(preList[0][j])
	
	for i in range(1,len(preList)):
		interval = interval / len(preList[i])
		for k in range(0,totalLength):
			j = math.floor(k / interval)
			while j >= len(preList[i]):
				j = j - len(preList[i])
			finalList[k] += preList[i][j]
	print (finalList)


def main():
	mapping = []
	mapping.append(numberMapping("2",["a","b","c"]))
	mapping.append(numberMapping("3",["d","e","f"]))
	mapping.append(numberMapping("4",["g","h","i"]))
	mapping.append(numberMapping("5",["j","k","l"]))
	mapping.append(numberMapping("6",["m","n","o"]))
	mapping.append(numberMapping("7",["p","q","r","s"]))
	mapping.append(numberMapping("8",["t","u","v"]))
	mapping.append(numberMapping("9",["w","x","y","z"]))
	# print("mapping:")
	# for i in range(0,8):
	# 	print(f"{mapping[i].num} - {mapping[i].letters}")
	num = "23"
	displayConfigurations(num,mapping)

if __name__ == "__main__":
	main()
