# upload the files and designate whether they are being read from or written to
read1 = open('dct1.txt', 'r')
write1 = open('dct1', 'w')

# read the first line
line = read1.readline()
# while there is another line in the "reading" file
while line:
    # checks if there is "y" in the line
    # based on the structure of the data, if there is "y" in the line
    # then either of the following are true:
    # there is a non-zero macroblock following OR
    # there are no numbers following, and the macroblock should be recorded as all zeroes
    if 'y' in line:
        # reads the next line
        line = read1.readline()
        # checks if there is "y" in the line
        # if there is, then there should be an all-zero macroblock recorded
        if 'y' in line:
            # writes 16 zeroes
            for i in range(16):
                write1.write('0 ')
            write1.write('\n')
        # if there is NOT "y" in the line, there will be a non-zero macroblock following
        else:
            # skips a line (based on the structure of the data)
            read1.readline()
            # reads through the next 4 lines and writes the values in a single line
            # each line contains 4 numbers, making the 16-number macroblock
            for i in range(4):
                line = read1.readline()
                macroblockValues = line.strip().split(' ')
                for j in range(4):
                    write1.write(macroblockValues[j] + ' ')
            write1.write('\n')
    # if there was not "y" in the line, then skips it
    # this happens only with lines only containing "\n" or markers for new frames
    else:
        line = read1.readline()

# closes both of the files
read1.close()
write1.close()
