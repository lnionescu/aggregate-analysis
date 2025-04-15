'''
code published by the cellpose developers that trains a model
i rewrote it from .ipynb to .py, with the main purpose of understanding the syntax and modules they use directly from their own code
'''

# import necessary modules
from cellpose import train, models, io, metrics
import numpy as np
import matplotlib.pyplot as plt

use_GPU = True
initial_model = 'cyto3'

# set up logger to track training progress across epochs
logger = io.logger_setup()

# create a cellpose model
model = models.CellposeModel(gpu=use_GPU, model_type=initial_model)

# specify which color channels to use for segmentation
# channels[0]: grayscale/primary channel
# channels[1]: optional nuclear/secondary channel (use if nuclei are separately stained)
chan = 0
chan2 = 0
channels = [chan, chan2]

train_dir = "training-data"
test_dir = "training-data"

# load training and testing data
# train_dir: training images and masks
# test_dir: test images and masks
# mask_filter='_seg.npy': identifies which files are masks
output = io.load_train_test_data(train_dir, test_dir, mask_filter='_masks.png')

# unpack loaded data into separate variables
train_data, train_labels, test_data, test_labels = output[:4]

# train segmentation model
# model.net: NN to train
# save_path: where to save the model
# n_epochs: number of training interations
# learning_rate: controls how quickly the model updates weights
# weight_decay: regularization parameter to prevent overfitting
# SGD=True: uses stochastic gradient descent optimizer
# nimg_per_epoch=8: number of images to process before updating weights TODO
# model_name
new_model_path, train_losses, test_losses = train.train_seg(model.net, train_data=train_data, train_labels=train_labels, test_data=test_data, channels=channels, save_path=train_dir, n_epochs=n_epochs, learning_rate=learning_rate, weight_decay=weight_decay, SGD=True, nimg_per_epoch=8, model_name=model_name)

# get the cell diameter estimated from the training data; the model will scale appropriately for differnet image magnifications
diam_labels = model.net.diam_labels.item()

# directories for training and testing data
train_dir = "human_in_the_loop/train"
test_dir = "human_in_the_loop/test"
base = "/content"  # base directory for saving files TODO

# initial pre-trained model and name for new model
initial_model = "cyto"
model_name = "CP_tissuenet"   # name for new model

# training parameters
n_epochs = 100

# define which color channels to use
Channel_to_use_for_training = "Green"
Second_training_channel = "Red"

# set advanced training parameters
Use_Default_Advanced_Parameters = True

# if using default parameters, set standard values TODO
if Use_Default_Advanced_Parameters:
    print("Default advanced parameters enabled")
    learning_rate = 0.1
    weight_decay = 0.0001

# reload test data for evaluation (since it may have been transformed during training) TODO
output = io.load_train_test_data(test_dir, mask_filter='_seg.npy')
test_data, test_labels = output[:2]

# run the trained model on test images to generate predicted masks
# diameter: estimated cell diameter for scaling
masks = model.eval(test_data, channels=[chan, chan2], diameter=diam_labels)[0]

# evaluate model performance using average precision at IoU threshold of 0.5
ap = metrics.average_precision(test_labels, masks)[0]
print('')
print(f'>>> average precision at iou threshold 0.5 = {ap[:,0].mean():.3f}')

# create a figure to visualize results
plt.figure(figsize=(12,8), dpi=150)   # TODO

# loop through test images to display them with predictions and ground truth
for k, im in enumerate(test_data):
    img = im.copy()

    # plot original image
    plt.subplot(3, len(train_files), k+1)
    img = np.vstack((img, np.zeros_like(img)[:1]))
    img = img.transpose(1,2,0)
    plt.imshow(img)
    plt.axis('off')
    if k==0:
        plt.title('image')

    # plot precited mask
    plt.subplots(3, len(train_files), len(train_files) + k+1)  # TODO
    plt.imshow(masks[k])
    plt.axis('off')
    if k==0:
        plt.title('predicted labels')

    # plot ground truth mask
    plt.subplots(3, len(train_files), 2*len(train_files) + k+1)
    plt.imshow(test_labels[k])
    plt.axis('off')
    if k==0:
        plt.title('true labels')

plt.tight_layout()
plt.show()









































