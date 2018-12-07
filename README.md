# Turi Image Classifier

_This public repository is designed for use in the Skafos ML delivery platform, which is available at metismachine.com. Use of this repo outside of the Skafos platform is not supported by Metis Machine._

The following repo contains code for training an image classifier model on Skafos using the Turi Create framework. As much as possible, the code in this repo mimicks Turi Create's image classifier example which can be found [here](https://apple.github.io/turicreate/docs/userguide/image_classifier/). 

## What is here?

The two main components to this repo are:
- `image_classifier.py` - a Skafos job that trains an image classifier model and saves a core ml model
- `image_classifier.ipynb` - a python notebook with the same code as the above `image_classifier.py` job.

Additionallly, there exist:
- `metis.config.yml` - a file telling Skafos how to execute the jobs in this project
- `requirements.txt` - a file telling Skafos the project's dependencies
- `save_models.py` - a helper module to save the core ml model to Skafos

## Further notes:
- The data for this example are 25000 images, which breaks down to 12500 Cats and 12500 Dogs, and can be found [here](https://www.microsoft.com/en-us/download/details.aspx?id=54765). 
- For retraining this image classification model on new data, we highly recommend doing it on a GPU. As benchmarks, we've found that training this Turi Create image classification model takes about 10 minutes on a GPU and about an hour and a half on Skafos with 6 CPU's and 10G of memory. Training will take considerably more time locally using only CPU. GPU support on Skafos is currently in development and will be coming soon.
