# Model Saving and Loading Instructions

Due to GitHub's file size limit (25MB), the trained LSTM model and Sentence-BERT model are not included in this repository. Below are instructions on how to save and load both models in your local environment for use in the Neural Article Search (NAS) project.

## 1. LSTM Model

### Saving the Trained LSTM Model

After training of LSTM model, you can save it using the following code in VS code python :

```python
from keras.models import load_model

# Save the trained LSTM model
model.save('NAS_model.h5')
```
This will save your model as an .h5 file, which can be loaded later for predictions.

## 2. Sentence-BERT Model

Saving the Sentence-BERT Model
After loading or fine-tuning your Sentence-BERT model, you can save it to a directory using the following code:

```python
from sentence_transformers import SentenceTransformer

# Load or fine-tune your Sentence-BERT model
sentence_model = SentenceTransformer('path_to_model_or_pretrained_model')

# Save the Sentence-BERT model to a directory
sentence_model.save('path_to_save_directory/sentence_bert_model')

```
This will save all model files into the specified directory.

## Final Integration Steps
1.Save both the trained LSTM model and the Sentence-BERT model as shown above.
2.Load these models in your application as needed or use in the own predicting.
3.Make sure that all file paths are correct when using these models in your project.

These instructions allow you to recreate and use both models in your local environment for running the Neural Article Search (NAS) project.
