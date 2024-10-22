from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import spacy
import numpy as np
from sentence_transformers import SentenceTransformer
from keras import models

app = Flask(__name__, static_folder='../Frontend', static_url_path='/')
CORS(app)

# Load the dataset
articles_df = pd.read_csv('/Users/hemavoc/Desktop/Projects/NAS project/ML Model/Dataset/Article Search .csv')
# Load the spaCy model for preprocessing
nlp = spacy.load('en_core_web_sm')

# Load the Sentence Transformer model
sentence_model = SentenceTransformer('/Users/hemavoc/Desktop/Projects/NAS project/ML Model/Models/sentence_bert_model')

# Load your trained model
model =models.load_model('/Users/hemavoc/Desktop/Projects/NAS project/ML Model/Models/NAS_1.keras')


# Function to preprocess the input query
def preprocess_sample_query(query):
    doc = nlp(query.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    query_embedding = sentence_model.encode([' '.join(tokens)])[0] 
    return query_embedding.reshape(1, 1, -1)  # Reshape for LSTM input

# Function to predict category for a given query
def predict_category(query):
    query_vector = preprocess_sample_query(query)
    prediction = model.predict(query_vector)
    predicted_category_index = np.argmax(prediction, axis=1)[0]
    
    # Ensure the predicted index is within the bounds
    if predicted_category_index < len(articles_df['search_query'].unique()):
        predicted_category = articles_df['search_query'].unique()[predicted_category_index]
        return predicted_category
    else:
        return None  # Handle the case where the index is out of bounds

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    
    # Check if the query is empty
    if not query:
        return jsonify({"error": "Empty query provided"}), 400
    
    # Predict category for the query
    predicted_category = predict_category(query)
    
    # Check if a category was predicted
    if predicted_category is None:
        return jsonify({"error": "Category not found"}), 404
    
    # Filter articles that belong to the predicted category
    results = articles_df[articles_df['search_query'] == predicted_category][['article_title', 'article_link']].to_dict(orient='records')
    
    # Check if results are empty
    if not results:
        return jsonify({"message": "No articles found for the predicted category"}), 404
    
    return jsonify(results)

# Route to serve the frontend
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
