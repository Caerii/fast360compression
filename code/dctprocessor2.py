# upload the files and designate whether they are being read from or written to
read2 = open('DCT_Data', 'r')
write2 = open('dct10', 'w')

# reads all of the lines within the "reading" file
# makes a list with every line of the file as a separate element
lines = read2.readlines()
# for every line in within the list of lines:
for line in lines:
    # checks if there is no "y" in the line
    # if we enter this if-statement, writes the line to the "writing" file
    # the purpose of this is to clean up any misread data from the previous data pre-processing
    if 'y' not in line:
        write2.write(line)
