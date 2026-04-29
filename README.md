# 🧬 Cancer Classification from RNA-Seq Gene Expression 

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Project-green)
![Accuracy](https://img.shields.io/badge/Accuracy-99.88%25-brightgreen)

🔗 **GitHub Repository:** https://github.com/KDeepak0506/gene-expression-cancer-classification

---

## 📌 Overview

This project explores how machine learning can classify different cancer types 
using high-dimensional RNA-Seq gene expression data (~20,000 features per sample).

The focus is on understanding how **feature selection** and **dimensionality reduction**
impact performance in complex biological datasets.

---

## ⚡ Quick Start

```bash
git clone https://github.com/KDeepak0506/gene-expression-cancer-classification.git
cd gene-expression-cancer-classification
pip install -r requirements.txt

# Train model
python -m src.train

# Evaluate model
python -m src.evaluate
```

---

## 🛠 Tech Stack

- Python  
- scikit-learn  
- pandas, numpy  
- matplotlib, seaborn  

---

## 📂 Dataset

📂 **Dataset:** UCI Gene Expression Cancer RNA-Seq Dataset  

The dataset is too large to store in the repository.

🔗 Download here:  
https://archive.ics.uci.edu/dataset/401/gene+expression+cancer+rna+seq  

After downloading, place it in:

```
dataset/raw/
```

---

## 🎯 Objectives

- Classify cancer types based on gene expression  
- Compare performance of multiple ML models  
- Perform feature selection to identify important genes  
- Build a clean, scalable ML pipeline  

---

## 🚀 Features

- ✅ Random Forest & Support Vector Machine (SVM)  
- ✅ Cross-validation for robust evaluation  
- ✅ Feature importance analysis  
- ✅ Feature selection (SelectKBest + VarianceThreshold)  
- ✅ Near-perfect classification performance (~99.8% with SVM)  
- ✅ Modular and production-style project structure  

---

## 🧠 Models Used

### 🌲 Random Forest
- Ensemble learning method  
- Handles high-dimensional data effectively  
- Provides feature importance  

### 📈 Support Vector Machine (SVM)
- Effective in high-dimensional spaces  
- Linear kernel used for classification  
- Requires feature scaling  

---

## 📊 Results

| Model          | Accuracy | Precision | Recall | F1 Score |
|---------------|----------|----------|--------|----------|
| Random Forest | 0.9963   | 0.9964   | 0.9963 | 0.9963   |
| SVM           | 0.9988   | 0.9988   | 0.9988 | 0.9988   |

- Strong performance across all cancer types  
- Minimal misclassification  
- Validated using 5-fold cross-validation  

---

## 📊 Visualizations

### 📌 PCA Visualization (Cluster Formation)

Shows how high-dimensional gene expression data forms clearly separable clusters after dimensionality reduction.

<p align="center">
  <img src="results/Cluster_Formation_of_Classes.png" width="70%">
</p>

---

### 📉 Feature Selection vs Accuracy

Illustrates how model performance remains stable even after drastically reducing the number of genes.

<p align="center">
  <img src="results/feature_vs_accuracy.png" width="70%">
</p>

---

### 📊 Class Distribution

Displays the distribution of different cancer types in the dataset.

<p align="center">
  <img src="results/Class_Distribution.png" width="70%">
</p>

---

### 📊 Random Forest Confusion Matrix

Shows prediction performance across all classes, with most values concentrated along the diagonal.

<p align="center">
  <img src="results/rf_confusion_matrix.png" width="70%">
</p>

---

### 📊 SVM Confusion Matrix

Demonstrates near-perfect classification with extremely low misclassification.

<p align="center">
  <img src="results/svm_confusion_matrix.png" width="70%">
</p>

---

## 🔍 Interpretation

- High accuracy even with fewer genes → strong predictive signal  
- PCA reveals clear cluster separation → highly distinguishable data  
- Feature selection significantly reduces dimensionality  
- Models generalize well across all cancer types  
- Class imbalance has minimal impact  

> 💡 **Key Insight:** A small subset of genes is sufficient to achieve near-perfect classification, indicating strong biological patterns in gene expression data.

---

## 📁 Project Structure

```
project/
│
├── models/
│   ├── rf_model.pkl
│   ├── svm_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── results/
│   ├── rf_results.txt
│   ├── svm_results.txt
│   ├── rf_confusion_matrix.png
│   ├── svm_confusion_matrix.png
│   ├── feature_vs_accuracy.png
│   ├── Class_Distribution.png
│   └── Cluster_Formation_of_Classes.png
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   └── feature_selection.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ▶️ Usage

### Train Models
```bash
python -m src.train
```

### Evaluate Models
```bash
python -m src.evaluate
```

### Feature Selection
```bash
python -m src.feature_selection
```

---

## 📂 Outputs

- 📄 Evaluation reports  
- 📊 Confusion matrices  
- 📉 Feature selection plots  

---

## 🔍 Key Learnings

- Feature selection is critical for high-dimensional data  
- PCA helps uncover hidden structure  
- Simple models can achieve strong performance  
- Cross-validation improves reliability  
- Clean architecture improves scalability  

---

## 🚀 Future Improvements

- Add XGBoost / LightGBM  
- Use SHAP for explainability  
- Perform hyperparameter tuning  
- Deploy as a web API (FastAPI/Flask)  
- Use larger datasets (e.g., TCGA)  

---

## 👨‍💻 Author

**Deepak**

---

## ⭐ Acknowledgements

- UCI Machine Learning Repository  
- scikit-learn documentation  
