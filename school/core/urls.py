from django.urls import path
from school.core import views

urlpatterns = [
    path('subject/<int:subject_id>/', views.get_program),
]