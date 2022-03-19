import os
import time 

# Writes new & old text into buffer, renames buffer to original filename
def insert(originalfile,string):
	with open(originalfile,'r') as f:
		with open('buffer.txt','w') as f2:
			f2.write(string + "\n\n")
			f2.write(f.read())
		os.rename('buffer.txt',originalfile)
	
		print("Done!\nFile: " + originalfile + " appended. ")
		time.sleep(1.0)

# User input
def main():
	pastedText = input("Paste text to be appended to file: \n")
	fileToAppend = input("File to be appended: (for $home type: /home/<username>/<file> ) \n")

	insert(fileToAppend, pastedText)

if __name__ == "__main__":
	main()

