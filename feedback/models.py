from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return f"{self.student.name} - {self.rating}★"

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.marks}"
