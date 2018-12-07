# Turi Image Classifier

_This public repository is designed for use in the Skafos ML delivery platform, which is available at metismachine.com._

The following repo contains code for training an image classifier model on Skafos using the Turi Create framework. As much as possible, the code in this repo mimicks Turi Create's image classifier example which can be found [here](https://apple.github.io/turicreate/docs/userguide/image_classifier/). 

## What is here?

The two main components to this repo are:
- `image_classifier.py` - a Skafos job that trains an image classifier model and saves a core ml model
- `image_classifier.ipynb` - a python notebook with the same code as the above `image_classifier.py` job.

Additionallly, there exist:
- `metis.config.yml` - a file telling Skafos how the jobs in this project
- `requirements.txt` - a file telling Skafos the project's dependencies
- `save_models.py` - a helper module to save the core ml model to Skafos

## Further notes:
- The data for this example are 25000 images, which breaks down to 12500 Cats and 12500 Dogs, and can be found [here](https://www.microsoft.com/en-us/download/details.aspx?id=54765). 
- For this project, we highly recommend running it on a GPU. We encourage you to do this once you've changed the data to reflect your use case. As benchmarks, we've found this takes about 3 minutes on a GPU and about an hour on Skafos with 6 CPU's and 10G of memory. This can take considerably more time locally using only CPU. 
