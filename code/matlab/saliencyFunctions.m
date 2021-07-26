classdef saliencyFunctions
    methods
        function [Blocks] = blockify(obj,image)
        % This function takes an image, and turns it into 16x16 blocks
        % Please input a grayscale double image for the input
        % The a specific block output can be accessed through Blocks{row#,column#}
            [m,n] = size(image);
            Blocks = cell(m/16,n/16);
            counti = 0;
            for i = 1:16:m-15
                counti = counti + 1;
                countj = 0;
                for j = 1:16:n-15
                    countj = countj + 1;
                    Blocks{counti,countj} = image(i:i+15,j:j+15);
                end
            end
        end
        function [AverageOfBlock] = saliencyScore(obj, block)
        % Gives you the average of a 2D array, AKA the saliency score
            AverageOfBlock = mean2(block); %gives you the average of a block
        end
        function [images] = imageget(obj)
        % This function does not take in anything, but it produces
        % "images", which is a 1x100 cell, that contains all of the
        % saliency maps that we will be using
            imagefiles = dir('*.jpg');
            nfiles = length(imagefiles);    % Number of files found
            for ii=1:nfiles % This traverses the "imagefiles", which are all of the images in the directory
               currentfilename = imagefiles(ii).name; % this adds the name of the image file
               currentimage = imread(currentfilename); % this actually reads in the image from the filename
               currentimage = im2double(currentimage); % changes the image to a double
               currentimage = rgb2gray(currentimage); % changes the image to a gray image
               currentimage = imresize(currentimage, [720 1280]); % scales the image so that it matches our DCT data
               images{ii} = currentimage; % this stores the saliency map data 
            end
        end
    end
end



function [averageSaliencyScore] = average_saliency(image)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
outputArg1 = inputArg1;
outputArg2 = inputArg2;
end

