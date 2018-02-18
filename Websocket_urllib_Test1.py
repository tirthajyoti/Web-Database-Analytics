import urllib.request, urllib.parse, urllib.error

print("Opening the file connection...")
# Following example reads Project Gutenberg EBook of Adventures of Huckleberry Finn
fhand = urllib.request.urlopen('http://www.gutenberg.org/files/76/76-0.txt')

txt_dump = ''
line_count=0
word_count=0
for line in fhand:
	txt_dump+=line.decode()
	line_count+=1
	word_count+=len(line.decode().split(' '))

# Determine the first newline character
firstblank = txt_dump.find('\n')
# Print the first line of the text data (just before the newline char position)
print(txt_dump[:firstblank])
# Prints basic informationn about the text data
print("\nPrinting some info on the text dump\n"+"-"*60)
print("Total characters:",len(txt_dump))
print("Total words:",word_count)
print(f"Total lines: {line_count}")