from django.urls import path
from . import views

app_name = 'experience'

urlpatterns = [
    path('', views.all_experience, name='all_experience'),
    path('<int:experience_id>/', views.experience_detail, name='experience_detail'),
]
