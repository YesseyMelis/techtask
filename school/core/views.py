from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from school.core.models import Subject


def get_program(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    teacher = subject.teachers
    if not teacher:
        return HttpResponse('Teacher not found', status=404)
    students = subject.students.all().values_list('name', flat=True)
    return JsonResponse({
        "subject": str(subject),
        "teacher": str(teacher),
        "students": list(students)
    }, status=200)
