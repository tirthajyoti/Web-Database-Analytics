import urllib.request, urllib.parse, urllib.error

print("Opening the file connection...")
# Following example reads Project Gutenberg EBook of Pride and Prejudice
fhand = urllib.request.urlopen('http://www.gutenberg.org/files/1342/1342-0.txt')

txt_dump = ''
line_count=0
word_count=0
# Iterate over the lines in the file handler object and dump the data into the text string. Also increment line and word counts
for line in fhand:
	# Use decode method to convert the UTF-8 to Unicode string
	txt_dump+=line.decode()
	line_count+=1
	# Count the length of words in the line and add to the running count
	word_count+=len(line.decode().split(' '))

# Determine the first newline character
firstblank = txt_dump.find('\n')
# Print the first line of the text data (just before the newline char position)
print('\n'+txt_dump[:firstblank])
# Prints basic informationn about the text data
print("\nPrinting some info on the text dump\n"+"-"*60)
print("Total characters:",len(txt_dump))
print("Total words:",word_count)
print(f"Total lines: {line_count}")


# Function for counting top N words
def print_top_N_words(text, top_N=10):
	"""
	This function accepts a text data (in the form of string) and extracts the top N words from it.
	N is supplied to the function. If not, default 10 is taken.
	"""
	# Initialize a dictionary
	counts = dict()
	txt_dump=text
	top_N=top_N
	words = txt_dump.split()
	for word in words:
		counts[word.lower()]=counts.get(word.lower(),0)+1

	common_words = set(line.strip() for line in open('stopwords.txt'))
	tmplst = []
	for key,val in counts.items():
		if key not in common_words:
			# Store the value first and then key (later used for sorting)
			newtup = (val,key)
			tmplst.append(newtup)

	# Sort the list by 'value' i.e. word count
	tmplst=sorted(tmplst,reverse=True)

	print(f"Top {top_N} words in this file are shown below\n"+"-"*55)
	for val,key in tmplst[:top_N]:
		print(f"{key}:{val}")

# Common words' list

common_words = ['i','in','the','a','an','to','is','are','on','yes','no',
				'not','he','she','you','I','my','me','at','of','so','but',
				'it','as','if','for','oh','him','her','them','and','all',
				'this','that','those','these','his','her','was','had','get',
				'have','has','with','up','down','out','when','where','how',
				'then','now','we','they','got','there','by','or','by','would',
				'will','shall','what','be','do','done','did']


# Now prints the most frequenct N words. Accepts input from user on the terminal.
print("\n")
top_N = int(input("How many most freqently used owrds do you want to display: "))
print_top_N_words(txt_dump,top_N)

print("\nNow closing the file connection...")
fhand.close()

