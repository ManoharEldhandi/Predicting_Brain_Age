from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from predicting_brain_age import settings
from Remote_User import views as remoteuser
from Service_Provider import views as serviceprovider

urlpatterns = [
    path('admin/', admin.site.urls),

    # Remote User Views
    path('', remoteuser.login, name="login"),
    path('Register1/', remoteuser.Register1, name="Register1"),
    path('Predict_BrainAge_Type/', remoteuser.Predict_BrainAge_Type, name="Predict_BrainAge_Type"),
    path('ViewYourProfile/', remoteuser.ViewYourProfile, name="ViewYourProfile"),

    # Service Provider Views
    path('serviceproviderlogin/', serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    path('View_Remote_Users/', serviceprovider.View_Remote_Users, name="View_Remote_Users"),
    path('charts/<str:chart_type>/', serviceprovider.charts, name="charts"),
    path('charts1/<str:chart_type>/', serviceprovider.charts1, name="charts1"),
    path('likeschart/<str:like_chart>/', serviceprovider.likeschart, name="likeschart"),
    path('View_BrainAge_Type_Ratio/', serviceprovider.View_BrainAge_Type_Ratio, name="View_BrainAge_Type_Ratio"),
    path('train_model/', serviceprovider.train_model, name="train_model"),
    path('View_Prediction_Of_Brain_Age_Type/', serviceprovider.View_Prediction_Of_Brain_Age_Type, name="View_Prediction_Of_Brain_Age_Type"),
    path('Download_Predicted_DataSets/', serviceprovider.Download_Predicted_DataSets, name="Download_Predicted_DataSets"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
