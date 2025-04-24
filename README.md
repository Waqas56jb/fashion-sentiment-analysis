 
# Fashion Brand Sentiment Analysis 🌟

## 🔍 Project Overview

This project performs **sentiment analysis** on customer reviews for fashion brand products. It uses machine learning models to classify customer sentiment (positive or negative) based on textual review data. The end goal is to help fashion retailers understand customer perceptions and improve product offerings accordingly.

---

## 🎯 Purpose

- Analyze real-world fashion review data.
- Classify customer reviews into **positive** and **negative** sentiments.
- Deploy a **Flask web app** that takes user input and returns the sentiment.
- Serve as a base for further NLP-based fashion analytics projects.

---

## 🧰 Tools & Technologies Used

| Category         | Tools/Technologies |
|------------------|--------------------|
| Programming Language | Python 3.8+ |
| Web Framework    | Flask |
| Machine Learning | Scikit-learn |
| Text Preprocessing | NLTK, Regex |
| Model Selection  | GridSearchCV |
| Serialization    | Joblib |
| UI/UX            | HTML, CSS, JavaScript |
| IDE              | VS Code |
| Dataset Format   | CSV/Excel (User-provided reviews) |

---

## 📦 Project Structure

```
FASHION_SENTIMENT_ANALYSIS/
│
├── artifacts/
│   └── cleaned_fashion_reviews.csv     # Cleaned dataset used for training
│
├── dataset/
│   └── data_amazon.xlsx                # Raw dataset (fashion reviews)
│
├── model/
│   └── train.ipynb                     # Notebook for model training
│
├── templates/
│   └── index.html                      # Frontend HTML UI
│
├── app.py                              # Flask web server
├── LogisticRegression_sentiment_model.pkl  # Trained ML model
├── requirements.txt                    # Project dependencies
├── README.md                           # You're reading it 😄
```

---

## ⚙️ How It Works

1. **Data Cleaning**: The dataset is cleaned to keep only the "Review" (text) and "Cons_rating" columns. Labels are generated from the Cons_rating.
2. **Feature Extraction**: Text data is vectorized using `TfidfVectorizer`.
3. **Model Training**: 5 ML models are trained using `GridSearchCV`:
   - Logistic Regression
   - Naive Bayes
   - SVM
   - Random Forest
   - Gradient Boosting
4. **Best Model Selection**: The best model is chosen and saved as `.pkl`.
5. **Web App Integration**: A simple web interface allows users to input review text and get sentiment prediction in real-time.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fashion-sentiment-analysis.git
   cd fashion-sentiment-analysis
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Run Flask server:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000`

---

## ✅ Features

- Supports customer review input
- Provides binary sentiment output: **Positive / Negative**
- Clean UI with blue-white theme
- Supports real-time prediction via web app

---

## ⚠️ Challenges Faced

- Dealing with noisy and unstructured review text
- Labeling data properly from rating columns
- Choosing the best model with limited data
- Creating a clean yet responsive UI using internal CSS/JS only

---

## 💡 Benefits

- Helps fashion brands make data-driven decisions
- Easily extendable to multiclass sentiment or emotion detection
- Lightweight app suitable for small businesses
- Educational for students learning NLP & ML integration

---

## 📚 Future Improvements

- Add review explanations with LIME or SHAP
- Deploy using Docker / Streamlit Cloud
- Expand to multi-lingual review analysis
- Integrate charts/analytics dashboard

---

## 👨‍💻 Author

**Waqas Naveed*  
Department of Computer Science  
FAST - NUCES, CFD Campus  
Final Year Project – 2025  
```

---