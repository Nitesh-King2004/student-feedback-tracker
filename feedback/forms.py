from django import forms
from .models import Feedback, Student, Marks

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['student', 'rating', 'comments']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email']

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'subject', 'marks']
