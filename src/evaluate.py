import os
import joblib
import matplotlib.pyplot as plt
import matplotx as mpx
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import cross_validate, cross_val_predict

from src.data_loader import Load_Data

# Create results folder
os.makedirs("results", exist_ok=True)

# Load data
df = Load_Data()
X = df.drop(['Class', 'SampleID'], axis=1)
y = df['Class']

# Get class names
class_names = sorted(y.unique())

# Load models
rf_model = joblib.load("models/rf_model.pkl")
svm_model = joblib.load("models/svm_model.pkl")
scaler = joblib.load("models/scaler.pkl")

scoring = ['accuracy', 'precision_weighted', 'recall_weighted', 'f1_weighted']

# ================= RF =================
rf_scores = cross_validate(rf_model, X, y, cv=5, scoring=scoring)
rf_pred = cross_val_predict(rf_model, X, y, cv=5)

rf_cm = confusion_matrix(y, rf_pred)

# 🔥 RF Plot with Dracula style
with plt.style.context(mpx.styles.dracula):
    plt.figure(figsize=(7, 5), dpi=300)
    disp = ConfusionMatrixDisplay(confusion_matrix=rf_cm, display_labels=class_names)
    disp.plot(cmap="viridis", values_format='d')  # clean colors + integers
    plt.title("Random Forest - Confusion Matrix")
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.tight_layout()
    plt.savefig("results/rf_confusion_matrix.png", bbox_inches='tight')
    plt.close()

rf_text = f"""
===== RANDOM FOREST =====
Accuracy: {rf_scores['test_accuracy'].mean()}
Precision: {rf_scores['test_precision_weighted'].mean()}
Recall: {rf_scores['test_recall_weighted'].mean()}
F1: {rf_scores['test_f1_weighted'].mean()}

{classification_report(y, rf_pred)}
Confusion Matrix:
{rf_cm}
"""

print(rf_text)

with open("results/rf_results.txt", "w") as f:
    f.write(rf_text)


# ================= SVM =================
X_scaled = scaler.transform(X)

svm_scores = cross_validate(svm_model, X_scaled, y, cv=5, scoring=scoring)
svm_pred = cross_val_predict(svm_model, X_scaled, y, cv=5)

svm_cm = confusion_matrix(y, svm_pred)

# 🔥 SVM Plot with Dracula style
with plt.style.context(mpx.styles.dracula):
    plt.figure(figsize=(7, 5), dpi=300)
    disp = ConfusionMatrixDisplay(confusion_matrix=svm_cm, display_labels=class_names)
    disp.plot(cmap="viridis", values_format='d')
    plt.title("SVM - Confusion Matrix")
    plt.xlabel("Predicted Label")
    plt.ylabel("True Label")
    plt.tight_layout()
    plt.savefig("results/svm_confusion_matrix.png", bbox_inches='tight')
    plt.close()

svm_text = f"""
===== SVM =====
Accuracy: {svm_scores['test_accuracy'].mean()}
Precision: {svm_scores['test_precision_weighted'].mean()}
Recall: {svm_scores['test_recall_weighted'].mean()}
F1: {svm_scores['test_f1_weighted'].mean()}

{classification_report(y, svm_pred)}
Confusion Matrix:
{svm_cm}
"""

print(svm_text)

with open("results/svm_results.txt", "w") as f:
    f.write(svm_text)