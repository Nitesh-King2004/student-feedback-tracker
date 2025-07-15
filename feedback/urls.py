from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('add-marks/', views.add_marks, name='add_marks'),
    path('view-performance/', views.view_performance, name='view_performance'),
]
