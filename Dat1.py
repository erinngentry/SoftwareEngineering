Margin Problem



# User enters file name with .txt extension

print("Enter file with .txt extension: ")

user_file = input()



# User enters custom # of inches for left margin

print("Enter left margin size (in inches): ")

left_inches_margin = int(input())



# Display left margin in inches and convert

# left_margin size from inches to pt

print("Left margin size:", left_inches_margin)

left_margin = left_inches_margin * 12



# User enters custom # of inches for right margin

print("Enter right margin size (in inches): ")

right_inches_margin = int(input())



# Display right margin in inches

print("Right margin size:", right_inches_margin)



# Total page width in pt

page_width = 144



# Convert right_margin size from inches to pt

# and subtracting that from total page_width to 

# keep aligned.

right_margin = right_inches_margin * 12



char = 80

# Read-in file line by line

# "r" reads from file called sample.txt

f = open(user_file, "r")


def create_left_margin():

    i = 0

    while i < left_margin:

        h.write("_")

        i += 1

        

def create_right_margin():

    i = page_width - right_margin

    while i < page_width:

        h.write("_")

        i += 1

space = page_width - left_margin - right_margin



line = f.read(space)

words = line.split(" ")

print(words)

sentences = line.split(".")

print(sentences)



h = open("output.txt", "w+")

for x in range(0, 30, 1):

    if x < page_width:

        create_left_margin()

        h.write(line + "\n")

        create_right_margin()

    x += 1

