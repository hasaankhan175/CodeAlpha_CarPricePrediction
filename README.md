

# 🚗 Car Price Prediction - Machine Learning Project

Streamlit App: [Click ME!](https://codealphacarpriceprediction.streamlit.app/)
## 📌 Project Overview
This project is developed as part of the **CodeAlpha Data Science Internship Task**.  
The goal is to build a machine learning model that can predict the **selling price of used cars** based on various features such as car age, mileage, fuel type, transmission, and ownership history.

The project demonstrates the full ML pipeline including data preprocessing, exploratory data analysis (EDA), feature engineering, model training, hyperparameter tuning, and evaluation.

---

## 🎯 Objective
- Predict the selling price of used cars using regression models  
- Analyze key factors affecting car pricing  
- Compare multiple machine learning algorithms  
- Select the best-performing model based on evaluation metrics  

---

## 📊 Dataset Information

The dataset contains information about used cars with the following features:

| Feature           | Description |
|------------------|-------------|
| Car_Name         | Name/model of the car |
| Year             | Manufacturing year |
| Selling_Price    | Target variable (price in lakhs) |
| Present_Price    | Current showroom price |
| Driven_kms       | Total kilometers driven |
| Fuel_Type        | Petrol / Diesel / CNG |
| Selling_type     | Dealer or Individual |
| Transmission     | Manual or Automatic |
| Owner            | Number of previous owners |

---

## 🛠️ Tech Stack

- Python 🐍
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn
- Machine Learning Models:
  - Linear Regression
  - Ridge Regression
  - Lasso Regression
  - Support Vector Regressor (SVR)
  - K-Nearest Neighbors Regressor

---

## 🔄 Workflow

1. Data Cleaning & Preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Feature Engineering  
   - Car Age creation  
   - Encoding categorical variables  
4. Model Training  
5. Hyperparameter Tuning using GridSearchCV  
6. Model Evaluation  
7. Model Selection  

---

## 🏆 Best Model

- **Model:** SVR (Support Vector Regressor)  
- **Test R² Score:** ~0.94  
- **MAE:** ~0.48  
- **RMSE:** ~0.82  

The SVR model performed best due to its ability to capture **non-linear relationships** in the dataset.

---

## 📈 Key Insights

- Present Price is the strongest predictor of Selling Price  
- Car Age significantly impacts price depreciation  
- Mileage (Driven_kms) negatively affects price  
- Manual cars dominate the dataset  
- Dealers tend to sell higher-priced cars than individuals  

---

## 🚀 How to Run This Project

```bash
# Clone repository
git clone https://github.com/your-username/car-price-prediction.git

# Install dependencies
pip install -r requirements.txt

# Run notebook or script
python app.py
````

---

## 📦 Model Saving

The trained model is saved using Joblib:

```python
import joblib
joblib.dump(model, "car_price_model.pkl")
```

To load the model:

```python
model = joblib.load("car_price_model.pkl")
```

---

## 📌 Future Improvements

* Add Random Forest and XGBoost models
* Deploy model using Flask or FastAPI
* Build a web UI for real-time prediction
* Perform feature importance analysis

---

## 👨‍💻 Author

**Muhammad Hasaan Hasan Khan**

* 🔗 LinkedIn: [Hasaan's LinkedIn](https://www.linkedin.com/in/hasaan-khan-422249289/)
* 💻 GitHub: [Hasaan's GitHub](https://github.com/hasaankhan175)
* 📊 Kaggle: [Hasaan's Kaggle](https://www.kaggle.com/hasaankhan175)
* 🌐 Portfolio: [Hasaan's Portfolio](https://hasaankhan175.github.io/)

---

## 📜 License

This project is for educational purposes under the CodeAlpha Internship program.

---

If you want, I can next help you :contentReference[oaicite:0]{index=0} which will make it look significantly more “industry level” instead of just a notebook project.
```
