# fast360compression
REU 2021 Saliency Based Compression Technique

//Authors are Jun Yi (junyiwo28@gmail.com), Adam Lenker(luigi726333@gmail.com), Orren Shachaf (orrenshachaf@utexas.edu), Alif Jakir (jakirab@clarkson.edu), and Zhisheng Yan (zyan.gsu.edu)
//https://github.com/Caerii/fast360compression

Fast 360 Video Compression for IoT Camera Sensing

Here is our documentation for our research.

We use MATLAB code to pre-process the saliency data. Specifically, we take 100 frames of the videos and we break each frame down individually through the following process. First, we cut up the individual image as a grayscale into cells that each correspond to 16x16 pixel regions in the original image. Then we place the cells into a 2D array, and we take the average value of the 16x16 block and call this an individual saliencyScore. We then add all of these saliencyScores to another 2D array that we then output as a text file, with each of the saliencyScores on one line. We can use this directly as output training values for the machine learning model. We were able to get 36000 saliency scores corresponding to 36000 macroblock values, for 10 frames of video 7.

We use Python code to pre-process the DCT and the saliency data. We take the DCT that is outputted as intermediate values from the x264 encoder and we process them. Each macroblock is placed on its own row as 16 different values. And so for our specific dataset, we had 45 rows and 80 columns. This meant that 3600 (45x80) lines of macroblocks corresponded to one frame of an image. We used 10 frames for our initial dataset, and this meant 36000 lines of macroblocks. We used the first 10 frames of video 7 in particular.

In the machine learning model we read in both of these macroblocks and saliency scores, and we were able to create a linear relationship map between macroblock values and saliency scores. We could then use this model in the form of a function to predict saliency values.

We injected this function into the code.

Definitions:
DCT means discrete cosine transform
Saliency means
x264 codec is
Machine learning is
Linear regression is
Preprocessing means
Virtual machine is
VirtualBox is
Ubuntu is
Python is
MATLAB is



The code that we modified in the x264 source code + problems:
encoder.c, x264.c, common.h, macroblock.c, ratecontrol.c

The datasets that we used were gotten from:

Walkthrough of the code that we created:

Biggest problems encountered:
Workflow Issues:
Data Issues:
Virtualbox issues

Future Research:

Blog Posts and why they are useful:

Future Milestones:

Images folder:
poster.png

Advice for future REU researchers:
-Set milestones, set concrete achievable goals, delegate tasks, make sure that everyone knows what is going on, create documentation along the way, COMMENT YOUR CODE
-

Videos:
//put the link to the wildlife dataset here


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
