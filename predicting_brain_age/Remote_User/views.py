from django.db.models import Count, Q
from django.shortcuts import render, redirect, get_object_or_404
from Remote_User.models import ClientRegister_Model, brain_age_prediction
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from django.conf import settings

def login(request):
    if request.method == "POST" and 'submit1' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = ClientRegister_Model.objects.get(username=username, password=password)
            request.session["userid"] = user.id
            return redirect('ViewYourProfile')
        except ClientRegister_Model.DoesNotExist:
            pass
    return render(request, 'RUser/login.html')

def Register1(request):
    if request.method == "POST":
        ClientRegister_Model.objects.create(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            phoneno=request.POST.get('phoneno'),
            country=request.POST.get('country'),
            state=request.POST.get('state'),
            city=request.POST.get('city'),
            address=request.POST.get('address'),
            gender=request.POST.get('gender')
        )
        return render(request, 'RUser/Register1.html', {'object': "Registered Successfully"})
    return render(request, 'RUser/Register1.html')

def ViewYourProfile(request):
    userid = request.session.get('userid')
    user = get_object_or_404(ClientRegister_Model, id=userid)
    return render(request, 'RUser/ViewYourProfile.html', {'object': user})

def Predict_BrainAge_Type(request):
    if request.method == "POST":
        idnumber = request.POST.get('idno')
        gender = request.POST.get('gender')
        age = int(request.POST.get('age'))
        hypertension = int(request.POST.get('hypertension'))
        heart_disease = int(request.POST.get('heart_disease'))
        ever_married = request.POST.get('ever_married')
        work_type = request.POST.get('work_type')
        Residence_type = request.POST.get('Residence_type')
        avg_glucose_level = float(request.POST.get('avg_glucose_level'))
        bmi = float(request.POST.get('bmi'))
        smoking_status = request.POST.get('smoking_status')

        dataset_path = os.path.join(settings.BASE_DIR, 'Healthcare_Datasets.csv')
        df = pd.read_csv(dataset_path)

        # Encode categorical values
        df['ever_married'] = df['ever_married'].map({'Yes': 1, 'No': 0})
        df['gender'] = df['gender'].map({'Male': 0, 'Female': 1, 'Other': 2})
        df['work_type'] = df['work_type'].astype('category').cat.codes
        df['Residence_type'] = df['Residence_type'].map({'Urban': 1, 'Rural': 0})
        df['smoking_status'] = df['smoking_status'].astype('category').cat.codes

        df['results'] = df['neurological_diseases'].map({'Yes': 1, 'No': 0})

        # Handle NaN values — this fixes your crash
        df.fillna(df.median(numeric_only=True), inplace=True)

        features = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
                    'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status']
        X = df[features]
        y = df['results']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        models = []
        gnb = GaussianNB()
        gnb.fit(X_train, y_train)
        models.append(('NaiveBayes', gnb))

        svc = svm.SVC(kernel='linear', probability=True)
        svc.fit(X_train, y_train)
        models.append(('SVM', svc))

        lr = LogisticRegression(max_iter=200)
        lr.fit(X_train, y_train)
        models.append(('LogisticRegression', lr))

        dtc = DecisionTreeClassifier()
        dtc.fit(X_train, y_train)
        models.append(('DecisionTree', dtc))

        knn = KNeighborsClassifier()
        knn.fit(X_train, y_train)
        models.append(('KNN', knn))

        ensemble_model = VotingClassifier(estimators=models, voting='hard')
        ensemble_model.fit(X_train, y_train)

        input_dict = {
            'gender': 0 if gender == 'Male' else 1 if gender == 'Female' else 2,
            'age': age,
            'hypertension': hypertension,
            'heart_disease': heart_disease,
            'ever_married': 1 if ever_married == 'Yes' else 0,
            'work_type': pd.Series([work_type]).astype('category').cat.codes[0],
            'Residence_type': 1 if Residence_type == 'Urban' else 0,
            'avg_glucose_level': avg_glucose_level,
            'bmi': bmi,
            'smoking_status': pd.Series([smoking_status]).astype('category').cat.codes[0],
        }

        input_df = pd.DataFrame([input_dict])
        prediction = ensemble_model.predict(input_df)[0]
        result = 'Short Age' if prediction == 1 else 'Long Age'

        brain_age_prediction.objects.create(
            idno=idnumber,
            gender=gender,
            age=age,
            hypertension=hypertension,
            heart_disease=heart_disease,
            ever_married=ever_married,
            work_type=work_type,
            Residence_type=Residence_type,
            avg_glucose_level=avg_glucose_level,
            bmi=bmi,
            smoking_status=smoking_status,
            Prediction=result
        )

        return render(request, 'RUser/Predict_BrainAge_Type.html', {'objs': result})

    return render(request, 'RUser/Predict_BrainAge_Type.html')
