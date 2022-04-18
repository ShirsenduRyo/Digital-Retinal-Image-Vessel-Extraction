# Digital-Retinal-Image-Vessel-Extraction 
## The Problem
Glaucoma, hypertension, and other ophthalmologic illnesses can easily be detected by examining the vascular structures in the retinal blood vessels, but the images are not clear. Through our proposed algorithm, there is an attempt to solve it

## Algorithm
In the proposed method, 41 different filters (32 Gabor filter variations, Canny Edge, Roberts Edge, Sobel Edge, Scharr Edge, Prewill Edge, Sigma 3 and 7 Gaussian, Sigma 3 and 7 Median and Variance filter was used on all the image. Then, along with the 41 filtered images above, the original and the ground truth image are expanded into one dimension matrix, from which a data frame is formed. Here, the N models, each of their corresponding N image datase, are trained in their respective data frames and applied to the remaining N − 1 images to calculate the corresponding accuracy of each model. Based on the results of these accuracies, the top 3N/4 images were selected, the model was rated the best, and the final model was built using the XGBoost algorithm in the combined data frame of these images.
