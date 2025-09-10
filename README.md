# 🚍 Sentiment Analysis on MitraDarat App Reviews

## 📌 Overview
This project focuses on sentiment analysis of **MitraDarat**, a mobile application developed by the Indonesian Ministry of Transportation that provides land transportation services, including real-time bus tracking. The goal is to analyze user feedback from Google Play reviews and classify sentiments into **positive**, **neutral**, or **negative** categories.

This is an **individual project** carried out using both **machine learning** and **deep learning** approaches.

---

## 🎯 Objectives
- Identify and understand user sentiment towards the MitraDarat application.  
- Detect trends or recurring issues within user reviews.  
- Provide actionable insights to highlight areas for potential improvement.  

---

## 📊 Dataset
- **Source**: Scraped from Google Play Store using `google-play-scraper` API.  
- **Total Reviews**: 1,902 (from 1,890 unique users).  
- **Languages**: Mostly Indonesian with some English.  
- **Period**: February 2023 – October 2024.  
- **Features**:
  - `content`: review text.  
  - `score`: rating (1–5).  
  - `at`: timestamp of review.  

### Data Preprocessing
- Lowercasing and text cleaning (non-alphabet, numbers, special characters).  
- Stopword removal (Indonesian & English, using **NLTK**).  
- Stemming using **Sastrawi**.  
- Manual normalization of slang words.  
- Null and duplicate values removed.  
- Tokenization with **NLTK**.  

---

## 🛠️ Tech Stack
- **Languages**: Python  
- **Libraries**: Pandas, NLTK, Scikit-learn, TensorFlow, Keras, Sastrawi  
- **Approaches**: Lexicon-based labeling, Machine Learning, Deep Learning  

---

## 🤖 Modeling
Two categories of models were trained:  

### 🔹 Machine Learning
- Random Forest  
- Logistic Regression  
- Decision Tree  

**Results (Test Accuracy):**
- Random Forest: **79.27%**  
- Logistic Regression: **76.42%**  
- Decision Tree: **69.11%**  

### 🔹 Deep Learning (LSTM)
A custom **LSTM** architecture was built with embedding layers, dropout, and batch normalization. Training stopped early at epoch 15 after reaching satisfactory performance.

**Best Result:**
- Accuracy: **84.96%** (Val)  
- Loss: 0.58  

---

## 📈 Visualizations
Some of the key visualizations generated during this project include:
- **Word Cloud**: Distribution of keywords per sentiment label.  
- **Training History**: Line chart of accuracy and loss for training vs validation.  

(📎 *Links/images will be added here*)  

---

## ✅ Conclusion
- User feedback on MitraDarat is mixed, with both positive and negative sentiments.  
- **LSTM outperformed traditional ML models**, achieving the highest accuracy of **84.96%**, thanks to its ability to capture sequential context in text.  
- Classical ML models like Random Forest also performed reasonably well but were less effective in handling language nuances compared to deep learning.  

This analysis demonstrates how sentiment classification can provide valuable insights for improving public service applications.  

---
