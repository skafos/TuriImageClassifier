import turicreate as tc
import urllib
import tarfile
import coremltools
import save_models as sm
from skafossdk import *

ska  = Skafos()


data_url = "https://s3.amazonaws.com/skafos.example.data/ImageClassifier/PetImages.tar.gz"
data_path = "PetImages.tar.gz"

# pull the tar
ska.log("Retrieving the images from online", labels = ['image_classifier'])
retrieve = urllib.request.urlretrieve(data_url, data_path)

# extract the file
ska.log("Images downloaded, extracting the images", labels = ['image_classifier'])
tar = tarfile.open(data_path)
tar.extractall()
tar.close()

# Load images (Note: you can ignore 'Not a JPEG file' errors)
ska.log("Loading the images locally", labels = ['image_classifier'])
data = tc.image_analysis.load_images('PetImages', with_path=True, ignore_failure = True)

# From the path-name, create a label column
data['label'] = data['path'].apply(lambda path: 'dog' if '/Dog' in path else 'cat')

# Make a train-test split
train_data, test_data = data.random_split(0.8)

# Create the model
ska.log("Building the model", labels = ['image_classifier'])
model = tc.image_classifier.create(train_data, target='label')

# Save the model for later use in Turi Create
coreml_model_name = 'image_classifier.mlmodel'
res = model.export_coreml(coreml_model_name)

model_spec = coremltools.utils.load_spec(coreml_model_name)
model_fp16_spec = coremltools.utils.convert_neural_network_spec_weights_to_fp16(model_spec)
coremltools.utils.save_spec(model_fp16_spec, coreml_model_name)

# compress the model
compressed_model_name, compressed_model = sm.compress_model(coreml_model_name)

# save to Skafos
sm.skafos_save_model(skafos = ska, model_name = compressed_model_name,
								compressed_model = compressed_model,
								permissions = 'public')