# fast360compression
REU 2021 Saliency Based Compression Technique

//Authors are Jun Yi (junyiwo28@gmail.com), Adam Lenker(luigi726333@gmail.com), Orren Shachaf (orrenshachaf@utexas.edu), Alif Jakir (jakirab@clarkson.edu), and Zhisheng Yan (zyan.gsu.edu)
//https://github.com/Caerii/fast360compression
---------------------------------------------------------------
Fast 360 Video Compression for IoT Camera Sensing
---------------------------------------------------------------
Here is our documentation for our research.
---------------------------------------------------------------
We use MATLAB code to pre-process the saliency data. Specifically, we take 100 frames of the videos and we break each frame down individually through the following process. First, we cut up the individual image as a grayscale into cells that each correspond to 16x16 pixel regions in the original image. Then we place the cells into a 2D array, and we take the average value of the 16x16 block and call this an individual saliencyScore. We then add all of these saliencyScores to another 2D array that we then output as a text file, with each of the saliencyScores on one line. We can use this directly as output training values for the machine learning model. We were able to get 36000 saliency scores corresponding to 36000 macroblock values, for 10 frames of video 7.

We use Python code to pre-process the DCT and the saliency data. We take the DCT that is outputted as intermediate values from the x264 encoder and we process them. Each macroblock is placed on its own row as 16 different values. And so for our specific dataset, we had 45 rows and 80 columns. This meant that 3600 (45x80) lines of macroblocks corresponded to one frame of an image. We used 10 frames for our initial dataset, and this meant 36000 lines of macroblocks. We used the first 10 frames of video 7 in particular.

In the machine learning model we read in both of these macroblocks and saliency scores, and we were able to create a linear relationship map between macroblock values and saliency scores. We could then use this model in the form of a function to predict saliency values.

We injected this function into the code.
---------------------------------------------------------------
Definitions:
DCT means discrete cosine transform, this is done to take an image and output it as a sum of sinusoids, which allows you to modify it through numerical transformations.
Quantization is a step after DCT that gets rid of redundant information.
Saliency means attention.
x264 codec is a compression algorithm used to compress videos. We compress 360 videos.
Machine learning is a way to automate the process of analyzing data.
Linear regression is finding a function that provides a line of best fit for your data.
Preprocessing means preparing the data to be used by the machine learning model.
Virtual machine is used in order to host an Ubuntu operating system to run code inside of.
VirtualBox is the software that allows us to run virtual machines.
Ubuntu is an open source Linux distribution. We used version 0.24.2.
Python is used in order to write many of the scripts.
MATLAB is used to preprocess data and write some of the scripts.
---------------------------------------------------------------
The code that we modified in the x264 source code:
encoder.c, x264.c, common.h, macroblock.c, ratecontrol.c
---------------------------------------------------------------
Walkthrough of the code that we created:

First you will need to create a virtual environment in Python with Ubuntu 0.24.2, use VirtualBox to create this.

Second you will need to download the x264 encoder code, you will be modifying this in order to get the outputs you require. Replace the specific files you find in x264 with the ones on our Github, and make sure to ctrl+f and search up "print" and "alif", so that you properly print out information to the correct directories.

Note: you may require several dependencies, make sure to install them.

Third, you will want to run the encoder to make sure that it works properly with your configuration.

Run the following commands to test that this works:

make //use this in ~/encoder/x264/x264/x264 in order to compile the encoder

sudo make install //run this right after make

cp /usr/local/bin/x264 /home/YOUR_DIRECTORY_NAME/encoder/x264/x264/x264 //you want to copy the executable that is generated in the usr bin into your encoder files

// this is how you run the executable file to compress a video, the compressed video will be 
// named try.264 in this instance. Make sure to provide a .yuv file that you want to compress, and name it such that you give the width and height of the pixels of the video.
./x264 -o /home/alif/encoder/x264/x264/x264/try.264 NAMEOFVIDEO_WIDTHxHEIGHT.yuv 

Fourth, in order to extract DCT information from the macroblock prints, you must use the following command:
./x264 -o [full path of x264 file directory and test file here] [name of target file here] > [name of directory for new file to redirect output to]

It might look something like this:
./x264 -o /home/alif/encoder/x264/x264/x264/try.264 akiyo_176x144.yuv > /home/alif/Desktop/dctTest.txt

Fifth, to run the preprocessing, just follow the comments in each of the preprocessor code files. These are simple scripts to structure data in ways to ingest into the machine learning model.

Sixth, machinelearning.py is what you will want to run in order to attempt to train your own data and create your own linear regression model. In order to use it you must make some modifications, you must change the names of the DCT and Saliency files to whatever files that you have as input for the model. You will also have to split the "18000" value to half of the lines of whatever dataset you have. For instance, our dataset has 36,000 lines, so we split it into a training, and a testing dataset, which means two 18,000 line datasets. If your dataset is 500,000 lines total, you want to split it into 250,000 and 250,000. You may also decide to use some kind of for loop to ingest large amounts of data, or keep all of the data in one text file, which requires specific adjustments up to you.

---------------------------------------------------------------
Biggest problems encountered:
Workflow Issues:
Data Issues:
Virtualbox issues:

Future Research:

Blog Posts and why they are useful:

Future Milestones:

Images folder:
poster.png

Advice for future REU researchers:
-Set milestones, set concrete achievable goals, delegate tasks, make sure that everyone knows what is going on, create documentation along the way, COMMENT YOUR CODE
-

The datasets that we used were gotten from:
put the link to the wildlife dataset here


What we need for documentation:
-Map of the workflow. label figures.
-Code, and what each of the codes do, like a walkthrough
-Explanations of what all the parts are useful for.
-biggest problems in the workflow
-what needs to be done to expand the research
-github repository for our code
-readme file
-all of the datasets
-sources cited
-blog posts
