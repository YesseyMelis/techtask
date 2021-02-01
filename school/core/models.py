from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.OneToOneField(Subject, on_delete=models.SET_NULL, null=True, related_name='teachers')

    def __str__(self):
        return self.name


class StudentSubjects(models.Model):
    student = models.ForeignKey("Student", on_delete=models.SET_NULL, null=True, related_name='subscribe_subjects')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name='subscribe_students')


class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ManyToManyField(
        Subject,
        blank=True,
        related_name="students",
        through=StudentSubjects,
        through_fields=["student", "subject"]
    )

    def __str__(self):
        return self.name
