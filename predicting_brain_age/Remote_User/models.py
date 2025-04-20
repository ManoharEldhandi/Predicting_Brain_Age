


from django.db import models
from django.db.models import CASCADE

# =======================
# Client Registration
# =======================
class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=500, default="Hyderabad", blank=True, null=True)
    gender = models.CharField(max_length=300)

    def __str__(self):
        return self.username

# =======================
# Brain Age Prediction Records
# =======================
class brain_age_prediction(models.Model):
    idno = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    age = models.CharField(max_length=300)
    hypertension = models.CharField(max_length=300)
    heart_disease = models.CharField(max_length=300)
    ever_married = models.CharField(max_length=300)
    work_type = models.CharField(max_length=300)
    Residence_type = models.CharField(max_length=300)
    avg_glucose_level = models.CharField(max_length=300)
    bmi = models.CharField(max_length=300)
    smoking_status = models.CharField(max_length=300)
    Prediction = models.CharField(max_length=300)

    def __str__(self):
        return f"ID: {self.idno} - Pred: {self.Prediction}"

# =======================
# Detection Accuracy Chart Data
# =======================
class detection_accuracy(models.Model):
    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.names} - Accuracy: {self.ratio}"

# =======================
# Detection Ratio Chart Data
# =======================
class detection_ratio(models.Model):
    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.names} - Ratio: {self.ratio}"