from django.contrib import admin
from .models import User, Skill, Test, Result, Certificate

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role', 'is_staff')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('skill', 'question', 'correct_answer')
    list_filter = ('skill',)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill', 'score', 'date_taken')
    list_filter = ('skill', 'date_taken')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill', 'code', 'date_issued')
