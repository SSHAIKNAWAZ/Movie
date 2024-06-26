
# Movie Recommendation System

## 1. Problem Statement
The goal is to predict the success of a movie before its release by leveraging various features such as plot, cast, crew, budget, and revenues. The key questions to address include:
- Can we identify the factors that contribute to the success or failure of a movie?
- Can we predict which films will be highly rated?

## 2. Overview
This project uses a dataset containing information on several thousand films, including their plot, cast, crew, budget, and revenues. Due to a DMCA takedown request from IMDb, the original dataset was replaced with a similar set of films and data fields from The Movie Database (TMDb). The dataset includes various columns such as genres, keywords, cast, crew, production companies, and vote average.

### Dataset Summary
- **Source**: The Movie Database (TMDb)
- **Key Features**: Plot, cast, crew, budget, revenues, genres, keywords, production companies, original language, and vote average.

## 3. Model Architecture

### Data Preprocessing
1. **Merging Datasets**: Merged the movies and credits datasets on the title.
2. **Feature Selection**: Selected relevant columns such as movie_id, title, overview, genres, keywords, cast, crew, production companies, and vote average.
3. **Handling Missing Values**: Dropped rows with missing values.
4. **Stemming**: Applied stemming to reduce words to their root form.
5. **Text Vectorization**: Used TF-IDF Vectorizer to convert text data into numerical format.
6. **Cosine Similarity**: Calculated cosine similarity to measure the similarity between movie vectors.

### Model
- **Vectorization**: TF-IDF Vectorizer with a custom stemming tokenizer.
- **Similarity Measurement**: Cosine similarity to find the closest matches to a given movie.

### Functions
- **Data Conversion Functions**: Convert JSON fields to lists of relevant values (e.g., genres, cast).
- **Stemming Function**: Custom tokenizer function using PorterStemmer.
- **Recommendation Function**: Recommends movies based on cosine similarity scores.

## 4. Expected Outcome
The expected outcome is a recommendation system that suggests movies similar to a given movie based on the plot, cast, crew, and other features. Users should be able to input a movie title and receive a list of recommended movies that are similar in terms of content and characteristics.

## 5. Model Training and Evaluation

### Training
The model training involved the following steps:
1. **Text Processing**: Applied stemming and TF-IDF vectorization to convert text data into vectors.
2. **Similarity Calculation**: Computed cosine similarity between all movie vectors.

### Evaluation
The evaluation of the model is based on its ability to recommend relevant movies. The recommendations are evaluated qualitatively by checking the relevance and appropriateness of the suggested movies. Quantitative evaluation metrics such as precision, recall, and F1-score can be considered for further enhancement.

### Sample Code
```python
# Example of using the recommendation function
recommend('Iron Man')
```
### Instruction To Run
- First `Flok the Repo`
- Then If you Want to deploy the model you should open the `Pycharm` and open the `streamlit_app.py` in the terminal run the following Command streamlit `run streamlit_app.py`
### Note:
- ` I have Uploaded 2 jupyter notebook`
- 1 Jupyter Notebook  i have used very `less features and used the count vectorizer`
- 2 Jupyter Notebook2  i have done `experiments on features` and used the `tf-idf vectorizer` and this file named ` Movie Recommended Final` worked very well in my view .
- The python .py file is `streamlit_app.py` is for `Final Jupyter Notebook File`
-  The python .py file is `app.py` is for `1st notebook` 
