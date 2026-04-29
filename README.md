# 🧬 Cancer Classification from RNA-Seq Gene Expression 

## 📌 Overview

This project focuses on classifying different types of cancer using gene expression (RNA-Seq) data.
Machine learning models are trained on high-dimensional biological data to identify patterns that distinguish cancer types.

---
## 📂 Dataset

📂 Dataset: UCI Gene Expression Cancer RNA-Seq Dataset

The dataset used in this project is too large to be stored in the repository.

You can download it from:
https://archive.ics.uci.edu/dataset/401/gene+expression+cancer+rna+seq

After downloading, place it in:

dataset/raw/

## 🎯 Objectives

* Classify cancer types based on gene expression
* Compare performance of multiple ML models
* Perform feature selection to identify important genes
* Build a clean, scalable ML pipeline

---

## 🚀 Features

* ✅ Random Forest & Support Vector Machine (SVM)
* ✅ Cross-validation for robust evaluation
* ✅ Feature importance analysis
* ✅ Feature selection (SelectKBest + VarianceThreshold)
* ✅ Near-perfect classification performance (~99.8% with SVM)
* ✅ Industry-style project structure

---

## 🧠 Models Used

### 🌲 Random Forest

* Ensemble learning method
* Handles high-dimensional data effectively
* Provides feature importance

### 📈 Support Vector Machine (SVM)

* Effective in high-dimensional spaces
* Linear kernel used for classification
* Requires feature scaling

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

Visualization of high-dimensional gene expression data after dimensionality reduction using PCA.

Clear clusters indicate strong separability between cancer types.

<p align="center">
  <img src="results/Cluster_Formation_of_Classes.png" width="600">
</p>

---

### 📉 Feature Selection vs Accuracy

This plot shows how model performance changes with the number of selected genes.

<p align="center">
  <img src="results/feature_vs_accuracy.png" width="600">
</p>

---

### 📊 Class Distribution

Distribution of different cancer types in the dataset.

<p align="center">
  <img src="results/Class_Distribution.png" width="600">
</p>

---

### 📊 Confusion Matrix

Shows model performance across all cancer classes.

Most predictions lie on the diagonal, indicating near-perfect classification with minimal misclassification.

<p align="center">
  <img src="results/rf_confusion_matrix.png" width="600">
</p>

---

## 🔍 Interpretation

* High accuracy is achieved even with fewer genes → strong predictive signal in the data  
* PCA reveals clear cluster separation → underlying structure is highly distinguishable  
* Feature selection significantly reduces dimensionality without performance loss  
* Models generalize well across all cancer types  
* Slight class imbalance has minimal impact on performance  

---

## 📁 Project Structure

```
project/
│
├── models/                     # Saved trained models
│   ├── rf_model.pkl           # Random Forest model
│   ├── svm_model.pkl          # Support Vector Machine model
│   └── scaler.pkl             # Feature scaler (for SVM)
│
├── notebooks/                 # Jupyter notebooks for experimentation
│   └── exploratory_analysis.ipynb
│
├── results/                   # Outputs (plots, metrics, reports)
│   ├── rf_results.txt
│   ├── svm_results.txt
│   ├── rf_confusion_matrix.png
│   ├── svm_confusion_matrix.png
│   ├── feature_vs_accuracy.png
│   ├── Class_Distribution.png
│   └── Cluster_Formation_of_Classes.png
│
├── src/                       # Source code (modular ML pipeline)
│   ├── __init__.py
│   ├── data_loader.py         # Load and preprocess dataset
│   ├── model.py               # Model definitions (RF, SVM)
│   ├── train.py               # Training pipeline
│   ├── evaluate.py            # Model evaluation + metrics
│   └── feature_selection.py   # Feature selection experiments
│
├── .gitignore                 # Ignored files (env, dataset, etc.)
├── README.md                  # Project documentation
└── requirements.txt           # Dependencies

```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 🔹 Train Models

```bash
python -m src.train
```

### 🔹 Evaluate Models

```bash
python -m src.evaluate
```

### 🔹 Feature Selection Analysis

```bash
python -m src.feature_selection
```

---

## 📂 Outputs

All outputs are saved in the `results/` folder:

* 📄 Model evaluation reports (`.txt`)
* 📊 Confusion matrices
* 📉 Feature selection plots

---

## 🔍 Key Learnings

* High-dimensional biological data requires feature selection
* Even simple models perform well on structured datasets
* Cross-validation ensures reliable performance evaluation
* Clean project structure improves scalability and maintainability

---

## 🚀 Future Improvements

* Add XGBoost / LightGBM
* Use SHAP for model explainability
* Perform advanced hyperparameter tuning
* Deploy as a web API (Flask/FastAPI)
* Use TCGA dataset for more complexity

---

## 👨‍💻 Author

**Deepak**

---

## ⭐ Acknowledgements

* UCI Machine Learning Repository
* scikit-learn documentation
