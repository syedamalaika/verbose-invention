from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import User, Skill, Test, Result, Certificate
from django.contrib import messages
import uuid

def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        # Simple signup logic for demonstration
        # In a real app, use a proper UserCreationForm
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role', 'student')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = User.objects.create_user(username=username, email=email, password=password, role=role)
            login(request, user)
            return redirect('dashboard')
            
    return render(request, 'signup.html')

@login_required
def dashboard(request):
    results = Result.objects.filter(user=request.user).order_by('-date_taken')
    certificates = Certificate.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {
        'results': results,
        'certificates': certificates
    })

@login_required
def skill_select(request):
    skills = Skill.objects.all()
    return render(request, 'skill_select.html', {'skills': skills})

@login_required
def take_test(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    tests = skill.tests.all()
    return render(request, 'test_page.html', {
        'skill': skill,
        'tests': tests
    })

@login_required
def submit_test(request, skill_id):
    if request.method == 'POST':
        skill = get_object_or_404(Skill, id=skill_id)
        tests = skill.tests.all()
        score = 0
        total = tests.count()
        
        for test in tests:
            user_answer = request.POST.get(f'q_{test.id}')
            if user_answer == test.correct_answer:
                score += 1
        
        percentage = (score / total) * 100 if total > 0 else 0
        
        # Save result
        Result.objects.create(user=request.user, skill=skill, score=int(percentage))
        
        # Generate certificate if score > 70
        if percentage >= 70:
            cert_code = str(uuid.uuid4())[:8].upper()
            Certificate.objects.get_or_create(user=request.user, skill=skill, defaults={'code': cert_code})
            
        return redirect('result_page', skill_id=skill.id)
    return redirect('skill_select')

@login_required
def result_page(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    result = Result.objects.filter(user=request.user, skill=skill).order_by('-date_taken').first()
    if not result:
        return redirect('skill_select')
    certificate = Certificate.objects.filter(user=request.user, skill=skill).first()
    return render(request, 'result_page.html', {
        'skill': skill,
        'result': result,
        'certificate': certificate
    })
