# 🧠 Sonar Rock vs Mine Classifier

This project uses machine learning to classify sonar signals as either **rocks** or **mines**, based on frequency-based features. It demonstrates a complete **end-to-end ML pipeline** — from data cleaning and exploration to model tuning, evaluation, and web app deployment.

---

## 📌 Project Overview

- 🎯 **Goal:** Predict whether a sonar return indicates a **rock** or a **mine**.
- 📊 Dataset: 208 samples, 60 frequency-based features, labeled as `M` (mine) or `R` (rock).
- 🧪 Models used: Logistic Regression, Random Forest (with hyperparameter tuning).
- 🌐 Deployed using **Streamlit** for a simple and interactive web interface.

---

## 🚀 Demo

👉 _Coming Soon: [Streamlit App](https://mlprojectsgit-p2cazmzdyupyrdbx2brfgz.streamlit.app/)_

---

## 📂 Folder Structure

```
ML_projects/
├── app.py                         # Streamlit web app
├── Complete_Sonar_Classifier_Project.ipynb  # Full ML notebook
├── requirements.txt              # Required packages
├── sonar_rf_model.pkl            # Final trained model
├── scaler.pkl                    # Saved standard scaler
├── Datasets/
│   └── Sonar data                # Original dataset
```

---

## 🛠️ Technologies Used

- Python
- NumPy, Pandas
- Seaborn, Matplotlib (EDA & visualizations)
- Scikit-learn (modeling, tuning, evaluation)
- Joblib (model saving)
- Streamlit (deployment)

---

## 📊 ML Pipeline Covered

- ✅ Importing and exploring data  
- ✅ Label encoding and standardization  
- ✅ Handling class imbalance  
- ✅ Logistic Regression and Random Forest modeling  
- ✅ Hyperparameter tuning with `GridSearchCV`  
- ✅ Evaluation with Confusion Matrix, Classification Report, ROC  
- ✅ Feature Importance (tree-based models)  
- ✅ Web deployment with Streamlit

---

## 🧠 Key Learnings

- Build and deploy a real-world binary classifier.
- Practice the complete machine learning workflow.
- Learn to interpret model performance using metrics and plots.

---

## 📥 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/John-Akech/ML_projects.git
cd ML_projects

# (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

---

## 🤝 Contributing

Contributions are welcome! Fork the repository, make your changes, and open a pull request.

---

## 👤 Author

**John Akech**  
Student | ML & AI Enthusiast | Capstone: FloodSense  
🔗 [GitHub](https://github.com/John-Akech)
