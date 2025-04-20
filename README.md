🧠 Predicting Brain Age using Machine Learning

This project leverages Machine Learning to predict whether a person's brain health aligns with a longer or shorter age expectancy based on clinical and lifestyle features. Built with Django for the web interface and scikit-learn for predictive modeling, this solution aims to assist early identification of neurological aging risks using healthcare data.

---

📦 Requirements

- Python 3.10+
- Django 4.0+
- pip3
- mysql
- httpd
- brew

🔧 Required Packages
Install all required packages via pip:
pip3 install django djangorestframework pandas numpy scikit-learn matplotlib seaborn xgboost imbalanced-learn joblib mysqlclient mariadb --break-system-packages

If program runs on sklearn:
Export the env variable just for this install : export SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True
Then install with override: pip3 install sklearn --break-system-packages


▶️ How to Run the Project
1.Clone the Repository
   git clone https://github.com/YourUsername/Predicting_Brain_Age.git
   cd Predicting_Brain_Age

2.Starting Apache and MySQL 
  brew services start mysql
  brew services start httpd

3.Creating Database: predicting_brain_age
  Login to MySQL as root: mysql -u root -p
  password : sqlpassword
    
  Now run these SQL commands:
  CREATE DATABASE predicting_brain_age;
  USE predicting_brain_age;

4.Run database migrations
  python manage.py makemigrations
  python manage.py migrate

5.Start the development server
  python manage.py runserver

6.Open in Browser
  Navigate to http://127.0.0.1:8000/ in your browser.

🧪 How to Use
	1.	Register/Login as a remote user.
	2.	Navigate to Predict Brain Age.
	3.	Fill out the form with details like:
	•	Age
	•	Gender
	•	BMI
	•	Blood Glucose
	•	Heart Disease, etc.
	4.	Submit to view the predicted brain age category.
	5.	The prediction result (“Short Age” or “Long Age”) will be shown and logged.

🌟 Features
	•	✅ User registration and authentication
	•	✅ Dynamic form-based prediction interface
	•	✅ Real-time ML model integration using ensemble classifiers
	•	✅ Preprocessed healthcare dataset
	•	✅ Naive Bayes, SVM, Decision Tree, KNN, and Logistic Regression models
	•	✅ Voting-based ensemble prediction
	•	✅ Stores user predictions in the database
	•	✅ Clean and responsive UI using HTML templates


---

Let me know your GitHub username and if you want help generating a nice `requirements.txt` file too.💻✨
      
  
