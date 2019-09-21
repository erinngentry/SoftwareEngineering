# Margin Problem
# Erinn Gentry

# User enters file name with .txt extension
print('Enter file with .txt extension: ')
user_file = input()

# User enters custom # of inches for left margin
print('Enter left margin size (in inches): ')
left_inches_margin = int(input())

# Display left margin in inches and convert
# left_margin size from inches to pt
print('Left margin size:', left_inches_margin)
left_margin = left_inches_margin * 12

# User enters custom # of inches for right margin
print('Enter right margin size (in inches): ')
right_inches_margin = int(input())

# Display right margin in inches
print('Right margin size:', right_inches_margin)

# Total page width in pt
page_width = 144

# Convert right_margin size from inches to pt
# and subtracting that from total page_width to 
# keep aligned.
right_margin = right_inches_margin * 12

char = 80
# Read-in file line by line
# 'r' reads from file called sample.txt
f = open(user_file, 'r')

# Test Case 1: Check if file exists
if f.readable() == False:
    print('Cannot read file. Please make sure file exists.')
    
print('Creating new file...')

fileIn = f.read()
words = fileIn.split(' ')
sentences = fileIn.split('  ')
while '' in words:
    words.remove('')

count = 0
for x in sentences:
    count += 1


def create_left_margin():
    i = 0
    while i < left_margin:
        h.write(' ')
        i += 1
        
def create_right_margin():
    i = page_width - right_margin
    while i < page_width:
        h.write(' ')
        i += 1

# Print file with margins
# for x in range(0, 30, 1):
#     if x < page_width:
#         create_left_margin()
#         print(f.read(char - left_margin - right_margin), sep = '', end = '')
#         create_right_margin()
#     print('\n', sep = '', end = '')
#     x += 1

# x = 0
# if x < page_width:
#     create_left_margin()
#     print(f.read(char - left_margin - right_margin), sep = '', end = '')
#     create_right_margin()


h = open('output.txt', 'w+')
for x in range(0, count, 1):
	space = char - left_margin - right_margin
	create_left_margin()
	while(len(words[x]) > 0 and len(words[x]) < space and len(words) > 0):
		h.write(words[x] + " ")
		space = space - len(words[x])
		del words[x]
		if len(words) <= 0:
			break
	create_right_margin()
	h.write('\n')
        

