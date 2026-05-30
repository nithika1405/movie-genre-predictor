# AI Movie Genre Predictor

An intelligent Machine Learning web application that predicts the genre of a movie based on its plot summary using Natural Language Processing (NLP) techniques and Machine Learning algorithms.

Built with Python, Scikit-Learn, Streamlit, and TF-IDF Vectorization.

---

## Project Overview

Movie genres can often be identified through the storyline and plot description. This project uses NLP and Machine Learning to analyze movie plot summaries and predict the most likely genre.

The application provides an interactive web interface where users can enter a movie plot and instantly receive a genre prediction.

---

## Features

-- Predict movie genres from plot summaries

-- Natural Language Processing using TF-IDF

-- Machine Learning-based classification

-- Interactive Streamlit web interface

-- Attractive and responsive UI

-- Real-time genre prediction

-- Data visualization using Plotly

-- Easy to deploy and use

---

## Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Scikit-Learn | Machine Learning |
| Pandas | Data Processing |
| TF-IDF | Text Feature Extraction |
| Logistic Regression | Genre Classification |
| Streamlit | Web Application |
| Plotly | Data Visualization |
| Joblib | Model Serialization |

---

## Dataset Structure

dataset/

├── train_data.txt

├── test_data.txt

├── test_data_solution.txt

└── description.txt

The dataset contains:

- Movie ID
- Movie Title
- Genre
- Plot Summary

---

## Machine Learning Workflow

### 1. Data Collection

Load movie information from the training dataset.

### 2. Text Preprocessing

- Remove unnecessary characters
- Convert text into machine-readable format

### 3. Feature Extraction

TF-IDF (Term Frequency-Inverse Document Frequency) is used to convert movie plots into numerical vectors.

### 4. Model Training

The classifier learns relationships between plot descriptions and genres.

Algorithm Used:

- Logistic Regression

### 5. Prediction

The trained model predicts the genre for new movie plots entered by users.

---

## System Architecture

User Input Movie Plot

↓

TF-IDF Vectorization

↓

Trained Logistic Regression Model

↓

Genre Prediction

↓

Display Result

---

## Project Structure

MovieGenrePredictor/

├── dataset/

│ ├── train_data.txt

│ ├── test_data.txt

│ └── test_data_solution.txt

│

├── model/

│ ├── genre_model.pkl

│ └── tfidf.pkl

│

├── app.py

├── train.py

├── style.css

├── requirements.txt

└── README.md

---

## Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/nithika1405/movie-genre-predictor.git
cd movie-genre-predictor
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Train the Model

Run:

```bash
python train.py
```

Output:

```text
Model saved successfully
```

Generated files:

```text
model/genre_model.pkl
model/tfidf.pkl
```

---

## Run the Application

```bash
streamlit run app.py
```

Open browser:

```text
http://localhost:8501
```

---

## Application Screens

### Home Screen

- Movie plot input area
- Genre prediction button
- Interactive visualizations

### Prediction Screen

- Displays predicted genre
- Instant response

---

## Future Enhancements

- Support for multiple machine learning models
- Genre probability scores
- Deep Learning (LSTM/BERT)
- Movie recommendation system
- User authentication
- Cloud deployment

---

## Learning Outcomes

Through this project, the following concepts were explored:

- Natural Language Processing
- Text Classification
- TF-IDF Vectorization
- Logistic Regression
- Model Training and Evaluation
- Streamlit Dashboard Development
- Machine Learning Deployment

---

## Author

S J Nithika

Artificial Intelligence & Machine Learning Student

---

## License

This project is developed for educational and academic purposes.

---

## Acknowledgements

- Scikit-Learn Documentation
- Streamlit Documentation
- Plotly Documentation
- Open Movie Genre Dataset Contributors

---

### If you found this project useful, don't forget to ⭐ the repository!