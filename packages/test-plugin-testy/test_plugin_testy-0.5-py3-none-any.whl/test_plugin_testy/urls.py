from django.urls import path
from . import views

app_name = 'test_plugin_testy'

urlpatterns = [
    path('', views.UploadFileFormView.as_view(), name='upload-file-form'),
    path('success/', views.UploadSuccessView.as_view(), name='upload-success'),
]
