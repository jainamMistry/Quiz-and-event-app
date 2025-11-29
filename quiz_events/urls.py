"""
URL configuration for quiz_events project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from quiz_events import views as project_views
from quizzes import views as quiz_views
from events import views as event_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', project_views.home, name='home'),
    path('quizzes/', quiz_views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', quiz_views.start_quiz, name='start_quiz'),
    path('quiz/<int:quiz_id>/submit/', quiz_views.submit_quiz, name='submit_quiz'),
    path('result/<int:submission_id>/', quiz_views.quiz_result, name='quiz_result'),
    path('events/', event_views.event_list, name='event_list'),
]

