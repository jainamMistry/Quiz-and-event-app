from django.contrib import admin
from .models import Quiz, Question, Answer, UserSubmission, UserAnswer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2
    fields = ('text', 'is_correct')

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    fields = ('text', 'question_type')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'question_count')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')
    inlines = [QuestionInline]
    
    def question_count(self, obj):
        return obj.questions.count()
    question_count.short_description = 'Questions'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'question_type', 'created_at')
    list_filter = ('quiz', 'question_type', 'created_at')
    search_fields = ('text',)
    inlines = [AnswerInline]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    list_filter = ('is_correct', 'question__quiz')
    search_fields = ('text',)

@admin.register(UserSubmission)
class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'quiz', 'score', 'submitted_at')
    list_filter = ('quiz', 'submitted_at')
    search_fields = ('user_name',)
    readonly_fields = ('submitted_at',)

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('submission', 'question', 'answer', 'is_correct')
    list_filter = ('is_correct', 'submission__quiz')
    search_fields = ('submission__user_name', 'question__text')
