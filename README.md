# 🏥 Predicting Healthcare Outcomes with Cost-Effectiveness Analysis  

**End-to-End Data Science Project | Machine Learning | Healthcare Analytics**

🔗 **Repository:** https://github.com/shahid200620/super-duper-funicular  
🎥 **Demo Video:** Available in `demo_video_link.txt`

---

## 📌 Business Problem

Healthcare providers face two critical challenges:

1. Predicting patient treatment outcomes accurately  
2. Choosing cost-effective treatments without compromising care quality  

Traditional decision-making often relies on uniform treatment strategies, leading to:
- Increased hospitalization costs  
- Inefficient resource allocation  
- Poor outcomes for high-risk patients  

This project addresses these challenges by building a **transparent, data-driven decision support system** that combines **machine learning, interpretability, and cost-effectiveness analysis**.

---

## 🎯 Project Objectives

- Predict patient treatment outcomes with high accuracy  
- Identify key clinical drivers influencing outcomes  
- Quantify financial impact and cost savings  
- Provide an interactive dashboard for non-technical stakeholders  
- Translate analytics into actionable healthcare recommendations  

---

## 🧠 Solution Overview

This project delivers a **production-ready analytics pipeline**:

1. Data Cleaning & Exploratory Analysis  
2. Feature Engineering using clinical domain logic  
3. Predictive Modeling with rigorous validation  
4. Model Interpretability for trust and transparency  
5. Cost-Effectiveness Analysis  
6. Interactive Streamlit Dashboard  
7. Executive-level insights and recommendations  

---

## 📊 Dataset

- **Type:** Synthetic healthcare dataset (300 patients)  
- **Features Include:**
  - Demographics (Age, Height, Weight)
  - Clinical measurements (Blood pressure, Cholesterol, Glucose)
  - Lifestyle factors (Smoking, Exercise)
  - Comorbidity scores
  - Treatment type
  - Outcome (target variable)

Synthetic data was intentionally used to preserve privacy while maintaining realistic clinical patterns.

---

## 🔍 Exploratory Data Analysis (EDA)

EDA focused on:
- Distribution of vital clinical metrics  
- Correlations between risk factors and outcomes  
- Identification of outliers and data inconsistencies  
- Early insights into high-risk patient segments  

📁 Notebook: `notebooks/01_EDA_and_cleaning.ipynb`

---

## 🛠 Feature Engineering

Key engineered features included:

| Feature | Description |
|------|------------|
| BMI | Obesity risk indicator |
| Age Group | Clinical age stratification |
| Smoker × Comorbidity | Lifestyle–disease interaction |
| Risk Score | Composite clinical risk index |

These features significantly improved predictive performance and interpretability.

📁 Notebook: `notebooks/02_feature_engineering_modeling.ipynb`

---

## 🤖 Predictive Modeling

### Models Evaluated
- Logistic Regression (baseline)
- Ensemble Model (final selection)
- Neural Network (comparison)

### Evaluation Strategy
- Stratified train-test split  
- Cross-validation  
- Metrics: Precision, Recall, F1-score  

✅ Final model achieved **F1-score ≥ 0.80**.

---

## 🔎 Model Interpretability

To ensure transparency and clinical trust:

- Permutation Importance was used  
- Top 10 predictive features identified  
- Plain-language explanations created  

📁 Outputs:
- `reports/permutation_importance_top10.png`
- `reports/permutation_importance_full.csv`
- `reports/top10_plain_explanations.txt`

📁 Notebook: `notebooks/03_model_interpretation.ipynb`

---

## 💰 Cost-Effectiveness Analysis

Synthetic cost data was integrated to evaluate:
- Treatment cost differences  
- Expected hospitalization expenses  
- Model-guided vs baseline cost comparison  

Results show measurable cost savings per patient.

📁 Outputs:
- `reports/cost_summary.csv`
- `reports/model_costs_per_patient.csv`
- `reports/cost_distribution.png`

📁 Notebook: `notebooks/04_cost_effectiveness.ipynb`

---

## 📊 Interactive Dashboard

An intuitive **Streamlit dashboard** was developed for real-world usage.

### Dashboard Features:
- Select individual patients  
- View predicted outcome probability  
- See recommended treatment  
- Analyze expected treatment cost  
- Understand feature importance  

▶ Run locally:
```bash
streamlit run dashboard/app.py
