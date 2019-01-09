# Turi Image Classifier

_This public repository is designed for use in the Skafos ML delivery platform, which is available at metismachine.com. Use of this repo outside of the Skafos platform is not supported by Metis Machine._

The following repo contains code for training an image classifier model on Skafos using the Turi Create framework. We have based this example model on [Turi Create's image classifier example](https://apple.github.io/turicreate/docs/userguide/image_classifier/). This example model is based on images of cats and dogs, and given a new photo, will predict whether that photo is of a cat or a dog. 

## What is here?

The main components of this repo are:
- `image_classifier.py` - a Skafos job that trains 
- `image_classifier.ipynb` - a Python notebook a cat/dog image classifier model and saves a core ml model to the Skafos framework

Additionallly, there exist:

- `metis.config.yml` - a file telling Skafos how to execute the jobs in this project
- `requirements.txt` - a file telling Skafos the project's dependencies
- `utilities/` - a directory that contains helper functions used by `image_classifier.ipynb`
- `userguide/` - a directory that contains additional information about this Image Classification model, how to incorporate your own data, advanced usage, and more. 

## Further notes:
- The data used to train this example model are 25000 images, 12500 Cats and 12500 Dogs, and can be found [here](https://www.microsoft.com/en-us/download/details.aspx?id=54765). 
- To retrain this image classification model on new data, we highly recommend doing it on a GPU. As benchmarks, we've found that training this Turi Create image classification model takes about 10 minutes on a GPU and about an hour and a half on Skafos with 6 CPU's and 10G of memory. Training will take considerably more time locally using only CPU. GPU support on Skafos is currently in development and will be coming soon.

## Going beyond the example model:
- By default, Skafos uses the default image classifier model trained to detect cats and dogs. For your usecase, you will likely want to retrain the model on different data. `utilities/images_in_turicreate.ipynb` provides an example if how to read in new data and use it to train a new image classification model. 
- Turi Create's image classifier model uses `model='resnet-50'` by default. Using this model can result in a large `.mlmodel` file. If you are concerned about model size, using a smaller pre-trained model might help conserve memory without sacrificing a significant amount of accuracy. For more about this, read [here](https://apple.github.io/turicreate/docs/userguide/image_classifier/how-it-works.html). 