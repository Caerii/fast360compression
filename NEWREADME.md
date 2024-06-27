# Fast 360 Video Compression for IoT Camera Sensing

## Introduction
This repository contains the code and documentation for the REU 2021 project on saliency-based compression techniques for 360 video, aimed at optimizing data transmission and storage for IoT camera sensing.

## Authors
- Jun Yi - [Email](mailto:junyiwo28@gmail.com)
- Adam Lenker - [Email](mailto:luigi726333@gmail.com)
- Orren Shachaf - [Email](mailto:orrenshachaf@utexas.edu)
- Alif Jakir - [Email](mailto:jakirab@clarkson.edu)
- Zhisheng Yan - [Email](mailto:zyan@gsu.edu)

Project Repository: [GitHub](https://github.com/Caerii/fast360compression)

## Project Overview
The project utilizes MATLAB to preprocess saliency data and Python to handle the Discrete Cosine Transform (DCT) and further data preprocessing. We aim to establish a linear relationship between macroblock values and saliency scores, which can then be used to predict saliency values dynamically.

### Detailed Workflow
1. **Saliency Data Preprocessing (MATLAB)**:
   - Process 100 video frames, converting each to grayscale and dividing into 16x16 pixel blocks.
   - Compute saliency scores for each block, stored in a 2D array and outputted as a text file.

2. **DCT Data Preprocessing (Python)**:
   - Process DCT data outputted from the x264 encoder.
   - Organize each macroblock into rows of 16 distinct values, representing various components of the image data.

3. **Machine Learning Model Integration**:
   - Both macroblocks and saliency scores are ingested into the model to map a linear relationship.
   - The resulting model function is used to predict saliency values.

## Definitions
- **DCT (Discrete Cosine Transform)**: Transforms an image into a sum of sinusoids.
- **Quantization**: Reduces redundancy post-DCT.
- **Saliency**: Measures human attention on image parts.
- **x264 Codec**: Compresses video files, particularly 360 videos.
- **Machine Learning**: Automates data analysis.
- **Linear Regression**: Models relationships between variables.
- **Preprocessing**: Prepares data for machine learning.
- **Virtual Machine**: Simulates a computer system within another.
- **VirtualBox**: Manages virtual machines.
- **Ubuntu**: Linux distribution used for coding, version 0.24.2.
- **Python & MATLAB**: Used for scripting and data processing.

## Installation and Configuration
### Setup Virtual Environment
- Create a virtual environment using Python and Ubuntu 0.24.2 on VirtualBox.
- Download and customize the x264 encoder from our GitHub.

### Execution Commands
```bash
make # Compile x264 source code
sudo make install # Install the encoder
cp /usr/local/bin/x264 /home/YOUR_DIRECTORY_NAME/encoder/x264/x264/x264
./x264 -o /home/alif/encoder/x264/x264/x264/try.264 NAMEOFVIDEO_WIDTHxHEIGHT.yuv
```

### Extract DCT Information
```bash
./x264 -o [full path] [target file] > [output directory]
```

### Data Preprocessing Scripts
- Adjust resolutions in the preprocessing scripts according to your dataset.
- Scripts organize data for ingestion into the machine learning model.

### Machine Learning Model Execution
- Modify `machinelearning.py` to fit your dataset.
- Split your dataset for training and testing.

## Challenges and Milestones
### Encountered Issues
- Scaling dataset complexities due to encoder multithreading.
- Version-specific dependencies for Python3.
- Debugging C code and managing data for machine learning models.

### Future Milestones
- Expand dataset for enhanced model accuracy.
- Introduce more features for accurate predictions.
- Explore real-time compression based on user saliency.

## Advice for Future Researchers
- Set concrete goals and document your process.
- Maintain constant communication within the team.
- Experiment with methodologies and document findings.

## Additional Resources
- Dataset: [Link to wildlife dataset](#) (Add actual link)
- Images Folder: Includes `poster.png`

