#                                                                     Object-detection-captioning

# Abstract
Our aim is to perform image-to-sentence generation, also known as ‘Image Captioning’, which will bridge the gap between vision and natural language. If our results comes out to be accurate, we can then utilize NLP technologies to understand the world in images. The current dataset that we are working on is: Flickr8K. To achieve our goal, we are going to study and apply existing pre-trained CNN Models i.e. VGG16, ResNet50 & Inception V3. Further, we’ll be attaching our RNN using LSTM language model to it. In the end, We’ll be evaluating our results & comparing each one of them. 

# Main Focus 
Convolution Neural Network used as a feature extractor.
![This](https://github.com/amandeep25/Object-detection-captioning/blob/main/CNN.jpg)

# Dataset used 
Flickr8k data set used 
Brief introduction: 
Flickr8k_Dataset: Contains a total of 8092 images in JPEG format with different shapes and sizes. Of which 6000 are used for training, 1000 for test and 1000 for development.
Flickr8k_text : Contains text files describing train_set ,test_set. Flickr8k.token.txt contains 5 captions for each image i.e. total 40460 captions.

Download from here: https://www.kaggle.com/ming666/flicker8k-dataset

# EDA 
![This](https://github.com/amandeep25/Object-detection-captioning/blob/main/eda.jpg)


# VGG 16 Model 
VGG 16 is a convolutional neural network model proposed by K. Simonyan and A. Zisserman from the University of Oxford in the paper “Very Deep Convolutional Networks for Large-Scale Image Recognition”. The model achieves 92.7% top-5 test accuracy in ImageNet, which is a dataset of over 14 million images belonging to 1000 classes.
 
![This](https://github.com/amandeep25/Object-detection-captioning/blob/main/result.jpg)

# The final predictions:
![This](https://github.com/amandeep25/Object-detection-captioning/blob/main/result_image.jpg)



