# Turi Image Classifier

**DEPRECATION WARNING**

This code example was intended for use by the legacy Skafos platform and is no longer being maintained. On 05/29/2019, a new version of [Skafos](https://skafos.ai) was released, streamlining model delivery to the edge.

[Sign-up](https://dashboard.skafos.ai/sign-up) for an account, [join](https://join.slack.com/t/metismachine-skafos/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI) our Slack community, and explore some [example models](https://github.com/skafos/colab-example-models) to get started.

---

The following repo contains code for training an image classifier model on Skafos using the [Turi Create framework](https://apple.github.io/turicreate/docs/userguide/image_classifier/). The example model is based on images of cats and dogs, and given a new photo, will classify the photo as a cat or a dog. 

## What is here?

The components of this repo are:
- `image_classifier.ipynb` - a Python notebook that trains and saves an image classifier model to use in your app. Start here.
- `utilities/` - a directory that contains helper functions used by `image_classifier.ipynb`.
- `advanced-usage/` - a directory that contains additional information about this image classification model, how to incorporate your own data, advanced usage, and more. 
- `requirements.txt` - a file describing all required Python dependencies.

## About the model
- The data used to train this example model are 25,000 images, 12,500 Cats and 12,500 Dogs, and can be found [here](https://www.microsoft.com/en-us/download/details.aspx?id=54765). 
- Once trained, you can give the model a photo, and it will identify that photo as a cat or a dog. 
- To retrain this image classification model on new data, we highly recommend doing it on a GPU. As benchmarks, we've found that training this Turi Create image classification model takes about 10 minutes on a GPU and about an hour and a half on Skafos with 6 CPU's and 10G of memory. Training will take considerably more time locally using only CPU. GPU support on Skafos is currently in development and will be coming soon.

## Going beyond the example
- If you wish to incorporate your own data or try another type of image classification model, check out the `advanced_usage/` section. 
- Turi Create's image classifier model uses `model='resnet-50'` by default. Using this model can result in a large `.mlmodel` file. If you are concerned about model size, using a smaller pre-trained model might help conserve memory without sacrificing a significant amount of accuracy. For more about this, read [here](https://apple.github.io/turicreate/docs/userguide/image_classifier/how-it-works.html). 

## Need Help?
Please contact us with questions or feedback! Here are two ways:


-  [**Signup for our Slack Channel**](https://join.slack.com/t/metismachine-skafos/shared_invite/enQtNTAxMzEwOTk2NzA5LThjMmMyY2JkNTkwNDQ1YjgyYjFiY2MyMjRkMzYyM2E4MjUxNTJmYmQyODVhZWM2MjQwMjE5ZGM1Y2YwN2M5ODI)
-  [**Find us on Reddit**](https://reddit.com/r/skafos) 

Also check out Turi Create's [**documentation**](https://apple.github.io/turicreate/docs/userguide/image_classifier/) on image classification basics.
