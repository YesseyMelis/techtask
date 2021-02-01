from django.contrib import admin
from .models import *


admin_models = [
    Subject,
    Teacher,
    Student,
    StudentSubjects,
]


admin.site.register(admin_models)
