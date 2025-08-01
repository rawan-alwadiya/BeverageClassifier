# BeverageClassifier: Smart Predictions from Chemistry to Category

BeverageClassifier is a machine learning project that predicts wine types based on their chemical composition. It demonstrates how dimensionality reduction and classification models can be applied to real-world problems — with relevance to the beverage and food industries.

---

## Demo

[![Watch Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

---

## Project Overview

BeverageClassifier uses a robust ML pipeline to categorize wines into three classes based on 13 chemical features. The workflow includes:

- Exploratory Data Analysis (EDA)
- Dimensionality Reduction using PCA
- Modeling with 7 classification algorithms
- Deployment through a Streamlit web app

After benchmarking, **Logistic Regression** was chosen for deployment due to its performance and interpretability.

### Performance Metrics (Logistic Regression)
- **Accuracy**: 97.2%  
- **Precision**: 97.8%  
- **Recall**: 96.7%  
- **F1 Score**: 97.1%

---

## Project Workflow

- **Exploration & Visualization**: Histograms, pairplots, scatter plots, etc.  
- **Preprocessing**: Feature scaling using `StandardScaler`  
- **Dimensionality Reduction**: PCA reduced 13 features to 9 principal components (94% variance retained)  
- **Modeling Algorithms**:  
  - Logistic Regression  
  - Support Vector Machine (RBF)  
  - Random Forest  
  - Gradient Boosting  
  - HistGradientBoosting  
  - XGBoost  
  - CatBoost  
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1 Score  
- **Deployment**: Deployed using Streamlit for live predictions

---

## Dataset

- **Source**: [UCI Wine Dataset](https://archive.ics.uci.edu/dataset/109/wine)  
- **Samples**: 178  
- **Features**: 13 chemical components  
- **Target Classes**: 3 wine cultivars

Each sample represents a chemical analysis of wines grown in the same region in Italy.

---

## Real-World Impact

This project highlights how chemical analysis and classical ML methods can work together to:

- Automate quality control  
- Support product labeling  
- Power personalized recommendation systems in food and beverage analytics

---

## 📎 Project Links

- 🔗 **GitHub**: [BeverageClassifier Repository](https://github.com/rawan-alwadiya/BeverageClassifier)  
- 🔗 **Kaggle Notebook**: [BeverageClassifier on Kaggle](https://www.kaggle.com/code/rawanalwadeya/beverageclassifier-wine-prediction)  
- 🔗 **Live Streamlit App**: [Try it Now](https://beverageclassifier-4yxpvngnibm8fp2n6xbnzr.streamlit.app/)

---

## 🛠 Tech Stack

**Languages & Tools**:
- Python, Pandas, NumPy, scikit-learn
- XGBoost, CatBoost
- Matplotlib, Seaborn
- Streamlit (Deployment)
