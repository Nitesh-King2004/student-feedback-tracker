from django.shortcuts import render, redirect
from .forms import FeedbackForm, StudentForm, MarksForm
from .models import Feedback, Marks

def home(request):
    return render(request, 'feedback/home.html')

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/submit_feedback.html', {'form': form})

def add_marks(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MarksForm()
    return render(request, 'feedback/add_marks.html', {'form': form})

def view_performance(request):
    marks = Marks.objects.all()
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback/view_performance.html', {'marks': marks, 'feedbacks': feedbacks})
