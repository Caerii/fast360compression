# fast360compression
**REU 2021 Saliency Based Compression Technique**

## Introduction
This project develops a saliency-based compression technique for 360 videos, aimed at enhancing IoT camera sensing by optimizing data transmission and storage requirements while maintaining perceptual quality.

## Authors
- Jun Yi - [junyiwo28@gmail.com](mailto:junyiwo28@gmail.com)
- Alif Jakir - [jakirab@clarkson.edu](mailto:jakirab@clarkson.edu) (I coordinated and led the day to day operations of the project.)
- Adam Lenker - [luigi726333@gmail.com](mailto:luigi726333@gmail.com)
- Orren Shachaf - [orrenshachaf@utexas.edu](mailto:orrenshachaf@utexas.edu)
- Zhisheng Yan - [zyan@gsu.edu](mailto:zyan@gsu.edu)

### Project Repository
[GitHub - fast360compression](https://github.com/Caerii/fast360compression)

## Project Documentation

### Saliency Data Preprocessing
Using MATLAB, we process 100 frames from video data by converting each frame into grayscale and then segmenting each into 16x16 pixel blocks. Each block's average grayscale value is computed and used to generate a saliency score, which is then stored in a 2D array. These scores are exported as a line-by-line text file, serving directly as output training values for our machine learning model.

### DCT and Saliency Data Preprocessing
We preprocess the DCT data outputted by the x264 encoder using Python. The macroblocks are extracted and each is laid out in rows of 16 values across 45 rows and 80 columns for each frame. This results in 36000 lines of macroblocks for 10 frames from Video 7, which are then processed to correlate with the saliency scores obtained from the MATLAB preprocessing.

### Machine Learning Model Integration
The linear relationship between macroblock values and saliency scores is established through a machine learning model, allowing us to predict saliency scores efficiently. This model is implemented as a function in our codebase.

## Detailed Definitions
- **DCT (Discrete Cosine Transform):** A method that transforms an image into a sum of sinusoids of varying magnitudes and frequencies, optimizing the image for compression.
- **Quantization:** A compression technique that reduces redundancy by eliminating less important information post-DCT.
- **Saliency:** A measure of how certain parts of an image attract the human eye.
- **x264 Codec:** An open-source video codec used for compressing video streams.
- **Preprocessing:** The process of preparing raw data for further processing.
- **Machine Learning:** A field of computer science that uses statistical techniques to give computer systems the ability to "learn" from data.
- **Linear Regression:** A method for modeling the straight-line relationships between data points.

## Environment and Dependencies
- **Virtual Machine:** We use VirtualBox to host an Ubuntu operating system where all code execution takes place.
- **Python & MATLAB:** The primary languages used for scripting, data processing, and executing the preprocessing tasks.
- **x264 Modifications:** Specific modifications made to `encoder.c`, `x264.c`, `common.h`, `macroblock.c`, and `ratecontrol.c` to adapt the x264 codec for our purposes.

## Complete Walkthrough of Installation and Configuration

### Step 1: Virtual Environment Setup
1. Install VirtualBox and set up a new virtual machine.
2. Install Ubuntu 0.24.2 on the virtual machine and configure it with adequate resources (e.g., CPU, memory).
3. Install all necessary dependencies such as Python, pip, MATLAB, and libraries needed for both Python and MATLAB scripting.

### Step 2: x264 Encoder Customization
1. Clone the x264 encoder source code from our GitHub repository.

```bash
git clone https://github.com/Caerii/fast360compression.git
```

2. Navigate through the cloned files and replace specified sections of the code with custom lines that facilitate data output redirection for further processing. Use the search function in your editor with keywords "print" and "alif" to find relevant sections.
3. Compile the modified encoder using gcc or a similar compiler, ensuring that all paths are correctly set for headers and libraries.

### Command Line Instructions for Setup
```bash
make # Compiles the modified source code of the encoder
sudo make install # Installs the encoder, creating an executable
cp /usr/local/bin/x264 ~/YOUR_DIRECTORY_NAME/encoder/x264/x264/x264 # Copies the executable to your specified directory, as it initially is stored in /usr/local/bin
./x264 -o ~/YOUR_DIRECTORY_NAME/encoder/x264/x264/x264/try.264 NAMEOFVIDEO_WIDTHxHEIGHT.yuv # Runs the encoder, this is how you run the executable file to compress a video, the compressed video will be named try.264. Make sure to provide a .yuv file that you want to compress, and name it such that you give the width and height of the pixels of the video.
```

### Step 3: Extracting DCT Information
1. Use the modified x264 executable to process a .yuv video file. This is used to extract DCT information from the macroblock prints, you must use the following commands.
2. Redirect the output containing DCT data to a designated file for processing:
```bash
./x264 -o [full path of x264 file directory and test file here] [name of target file here] > [name of directory for new file to redirect output to]

# It might look something like this:
./x264 -o /home/alif/encoder/x264/x264/x264/try.264 akiyo_176x144.yuv > /home/alif/Desktop/dctTest.txt

./x264 -o ~/YOUR_DIRECTORY_NAME/encoder/x264/x264/x264/try.264 your_video_176x144.yuv > ~/YOUR_DIRECTORY_NAME/Desktop/dctTest.txt
```

### Step 4: Preprocessing Scripts
1. Modify the resolution parameters in the preprocessing scripts according to your dataset's specifics. To run the preprocessing, just follow the comments in each of the preprocessor code files, change the resolutions associated for your own dataset quality in the code, currently we have 45x80 cell images, but all you must do is divide the resolution by 16 to get how many cells there are. These are simple scripts to structure data in ways to ingest into the machine learning model.
2. Ensure the scripts are set to read and process data from the designated output files correctly.
3. Run these scripts to format the data suitably for ingestion into the machine learning model.

### Step 5: Running the Machine Learning Model
1. Adjust `machinelearning.py` to match your dataset, specifically modifying the paths to the input files and setting the correct number of lines for splitting the dataset into training and testing sets. Running this file is what you will want to run in order to attempt to train your own data and create your own linear regression model. In order to use it you must make some modifications, you must change the names of the DCT and Saliency files to whatever files that you have as input for the model. You will also have to split the "18000" value to half of the lines of whatever dataset you have. For instance, our dataset has 36,000 lines, so we split it into a training, and a testing dataset, which means two 18,000 line datasets. If your dataset is 500,000 lines total, you want to split it into 250,000 and 250,000. You may also decide to use some kind of for loop to ingest large amounts of data, or keep all of the data in one text file, which requires specific adjustments up to you.
2. Execute the script to train the model on your data and evaluate its performance.

### Step 6: Video Conversion for Testing
1. Use ffmpeg to convert .mp4 video files to .yuv format at the desired resolution. In order to get the .yuv you must convert mp4 into .yuv through ffmpeg commands. Download the .mp4 from the dataset linked or from any video in order to prepare .yuv in the correct resolution.
2. Ensure that the converted videos are accessible to the encoder for testing.

## Challenges and Future Directions
### Key Challenges
- Managing large datasets and ensuring that DCT data remains unscrambled despite encoder multithreading.

- Efficiently managing resources on virtual machines, including storage and processing power.

- Dependencies for the code must be the correct versions for Python3.

- The Saliency Models that we tested, many of them malfunctioned when we ran them through the terminal, some of them were missing instructions. Some of the saliency models corrupted the environment and forced a restart from scratch.

- Workflow Issues:
Debugging the C code could at times be difficult because it required finding obscure documentation on the encoder details. Modifying the C code within the x264 codec to tailor it for our specific data processing needs was a challenge.

- Data Issues:
Figuring out how to structure the data in a way where it could be used by the machine learning model properly was a challenge, but we figured out that the data just needs to be in the right shape and then there will be no issues.

- Virtualbox issues:
We used a lot more disk space than we thought we would. At one point there was a black screen that required us to allocate a second core to the virtual box.

### Future Milestones
- Expand the dataset to include hundreds of videos to refine and improve the accuracy of the machine learning model.
- Develop additional predictive features to enhance the model's ability to accurately predict saliency scores.
- Add more ways to automatically check how much the error is from the true saliency scores, with more nuanced saliency models.
- Explore methodologies for real-time streaming compression that utilizes user saliency data to adjust compression parameters on the fly.
- Collect experimental data from test subjects for qualitative testing.

## Advice for Future REU Researchers
- Set clear, achievable goals and maintain rigorous documentation throughout your project.
- Establish a regular communication schedule with your team to address any issues promptly.
- Continuously experiment with different methodologies, always documenting your trials and outcomes to build a robust set of data for analysis.
- Datasets take a lot more time than you think to clean up! They are the most time-consuming and important part of the project.
- Take note of the time that you have to get certain goals done on time and on task.

### Additional Resources
- Dataset: [Link to wildlife dataset](#https://github.com/phananh1010/360VR-wildlife-surveillance?tab=readme-ov-file) (Insert actual link here)
- Images folder: Contains `poster.png`
