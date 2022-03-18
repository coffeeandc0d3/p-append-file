import os
import time 

# Writes new text into buffer & old text, renames to original filename
def insert(originalfile,string):
	with open(originalfile,'r') as f:
		with open('buffer.txt','w') as f2:
			f2.write(string + "\n")
			f2.write(f.read())
		os.rename('buffer.txt',originalfile)
	
		print("Done!\nFile: " + originalfile + " appended. ")
		time.sleep(1.3)

# User input
def main():
	pastedText = input("Paste text to be appended to file: \n")
	fileToAppend = input("File to be appended: (use ~/ or /home/<username>/ ) \n")

	insert(fileToAppend, pastedText)

if __name__ == "__main__":
	main()

