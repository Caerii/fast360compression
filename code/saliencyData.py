# upload the files and designate whether they are being read from or written to
read3 = open('SaliencyData.txt', 'r')
write3 = open('saliencyData', 'w')

# read the first line
line = read3.readline()
# while there is another line in the "reading" file
while line:
    # splits the saliency scores based on the inclusion of a comma between them
    saliencyScores = line.strip().split(',')
    # there are 80 saliency scores per line
    for i in range(80):
        # writes the saliency score onto its own individual line within a different file
        # we are doing this based on the way we are analyzing data in our machine learning model
        write3.write('' + saliencyScores[i] + '\n')
    # read the next line
    line = read3.readline()
