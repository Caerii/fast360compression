% YourImage = imread('image_00_sphere.jpg');
% YourImage = im2double(YourImage);
% YourImage = rgb2gray(YourImage);

%here we go through all of the blocks and replace them with saliency
%scores
myObj2 = saliencyFunctions;

totalImages = 100; % modify this variable based on how many images you want to process
images = myObj2.imageget(); %this gives us an array with all of the images

% This iterates through

% images and replaces each with a 16x32 block of
% saliency scores
for n = 1:totalImages
    Blocks2 = myObj2.blockify(images{n}); %these blocks will be overwritten
    [x,y] = size(Blocks2);
    %disp(x);
    %disp(y);
    
    counti = 0;
    for i = 1:x
       counti = counti + 1;
       countj = 0;
       for j = 1:y
            countj = countj + 1;

            BlockTemp = Blocks2{i,j}; % a temporary block is created
            BlockScore = myObj2.saliencyScore(BlockTemp); % the score of the block is computed
            BlockScore = round(BlockScore,3);

            Blocks2{counti,countj} = BlockScore; % the score of the block is added to the saliency map blocks
       end
    end
    images{n} = Blocks2;
end

% This iterates through "images" and prints out the contents of everything
% to an external text file

fileID = fopen('SaliencyData.txt','w');
for n = 1:totalImages
    M=images{n};
    writecell(M, "SaliencyData.txt",'WriteMode','append');
    %fprintf(fileID, '\n');
    
end
fclose(fileID);

%take the average value from Blocks{i,j}
%place this value into Blocks2
        
%We need to take the average of each 16x16 saliency block
%Use two for loops to go into every row and column of an image
%Take the average of the 256 pixel values and save that as a saliency score
%We should have 80 columns and 45 rows for each image
%That makes 512 saliency scores for each image
%We need to create a training data set
%We want to pair each macroblock from the DCT with each saliency score
%If there's no macroblock, automatically give a score of zero (0)
%Flatten each macroblock so that it's one row with 16 columns
%The dataset should be a pair (tuple), with each pair having a macroblock
%array and saliency score for each coordinate
%This must be generated algorithmically
%Once we have a dataset, do a linear regression to predict saliency
%Compare the actual saliency score values with the predicted saliency score
%values, then create an error matirx for them
%After the error matrix is done, try to find better input features for
%prediction in order to decrease the error matrix values


