# Image Classification Advanced Usage

The purpose of this Advanced Usage Guide is to provide additional tooling, tips, and guidance for building Image Classification Models. 

## Adding New Images

In order for an image classifier to identify a particular type of image, it must have seen other images with the same label. For example, if a model was trained on dogs and cats, and it is shown a plant, it will identify that plant as either a dog or cat. To build an image classification model that identifies plants or other types of objects, you would need to retrain the model, using labeled images of the type you want. 