# Neural Article Search (NAS)
This repository contains the source files and documentation for a deep learning project focused on searching articles based on user queries. The project leverages a dataset containing search queries, articles, and categories, applying NLP techniques and machine learning to predict the most relevant article category for a given query.

# Dataset Information

The dataset used in this project was sourced from Kaggle. It includes search queries, article titles, snippets, and corresponding categories, used to train and test the Neural Article Search (NAS) model.

## Dataset Provider

- **Kaggle**: [Link to Dataset](https://www.kaggle.com/datasets/kishan305/whats-trending-google-india)
  
You can download the dataset directly from Kaggle using the link provided above. Ensure you have access to the dataset before running the project.

---

Please make sure to follow Kaggle’s rules and regulations when using this dataset, and give credit to the original dataset provider when sharing or deploying the project.

## Feature Extraction
### Sentence Embeddings
The project uses the Sentence-BERT model to generate embeddings for both the search queries and article titles. Sentence-BERT converts text into high-dimensional vectors, capturing the semantic meaning of the input text, which is critical for accurate search functionality.

* Reference:
  Sentence-BERT: Sentence Embeddings using BERT
## Dimensionality Reduction
Preprocessing with Lemmatization and Stop Word Removal
To simplify and normalize the text, the project applies lemmatization (reducing words to their base form) and removes stop words (common words that do not contribute to the search meaning, like "the", "and", etc.). This ensures more efficient and meaningful sentence embeddings.
## Machine Learning Model
### Long Short-Term Memory (LSTM)
The project uses an LSTM model for sequence prediction, trained on article queries and their corresponding categories. LSTM is effective for processing sequential data, such as text, due to its ability to capture long-range dependencies.

* The LSTM model is trained on the article search query dataset, learning to predict the most likely category for each query.
* After predicting the category, the system fetches relevant articles associated with that category from the dataset.
## Model Training
### Training Details
* Initial training on 33,000+ rows of data with 1,632 unique categories.
* Evaluation: The model is evaluated based on the ability to predict the category of a given search query.
* Final training: The model is trained using Sentence-BERT embeddings for input query representation.
## Testing
* The model is tested on unseen search queries to evaluate its performance.
* Search queries are evaluated based on their ability to match the correct category and retrieve relevant articles.
  
## Getting Started

### Steps to Run the Project

1. **Create a Virtual Environment:**
   * Use the following command to create a virtual environment:
     ```bash
     python -m venv venv
     ```

2. **Activate the environment:**
   * On Windows:
     ```bash
     venv\Scripts\activate
     ```
   * On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
    ```

4.**Run the Flask application:** 
```bash
   python app.py
 ```

## Key Files and Notebooks
1.NAS_MODEL.ipynb:
* Contains the training code for the LSTM model and preprocessing steps.
  
2.EDA.ipynb:

* This notebook includes all the exploratory data analysis on the dataset, such as query tokenization and category distribution.
  
3.app.py:

* The Flask API server that handles search queries and returns results based on predicted categories.

4.requirements.txt:

* A list of all required Python libraries to run the project.
  
## Final Step
1.Run the Application:
* After running the Flask server, go to your browser and open http://127.0.0.1:5000/.
* Enter a search query in the input box, and the system will predict the relevant category and display matching articles.
  
2.API Endpoint:
* You can also interact with the backend directly by sending GET requests to:
   http://127.0.0.1:5000/search?query=your_search_query
  
This README provides all the necessary details to understand, install, and run the NAS project. Make sure to adjust file paths and directories as per your project setup.


