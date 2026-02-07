from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('employer', 'Employer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='tests')
    question = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1)  # A, B, C, or D

    def __str__(self):
        return f"Test for {self.skill.name}: {self.question[:50]}..."

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.skill.name}: {self.score}%"

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True)
    date_issued = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Cert for {self.user.username} - {self.skill.name}"
