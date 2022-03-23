import os
import time 
import prompt_toolkit

# Writes new & old text into buffer, renames buffer to original filename
def insert(originalfile,strings):
	with open(originalfile,'r') as f:
		with open('buffer.txt','w') as f2:
			for line in strings:
				f2.write(line + "\n\n")
				f2.write(f.read())
		os.rename('buffer.txt',originalfile)
	
		print("Done!\nFile: " + originalfile + " appended. ")
		time.sleep(1.0)

# User input
def main():

	print('Enter or paste text to append: ')
	
	x =  input() 
	rawInput = []

	count = 0
	while True:
		
	#   Allows pasting multi-line text	
		while x != '':  
			rawInput.append(x) 
			x = input()
		print(rawInput)
	
		count += 1
		print (count)
		
		if (count >= 2):
			print("Sorry couldn't find that filepath. ")
		
		fileToAppend = input("File to be appended: (for $home type: /home/<username>/<file> ) \n")
		
		if(os.path.isfile(fileToAppend) == True):
			count += 1
			print(count)
			break

	insert(fileToAppend, rawInput)

if __name__ == "__main__":
	main()
