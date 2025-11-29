from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Answer, UserSubmission, UserAnswer

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/quiz_list.html', {'quizzes': quizzes})

def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quizzes/quiz_attempt.html', {'quiz': quiz})

def submit_quiz(request, quiz_id):
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, id=quiz_id)
        user_name = request.POST.get('user_name')
        
        if not user_name or not user_name.strip():
            # Handle empty user name
            return render(request, 'quizzes/quiz_attempt.html', {
                'quiz': quiz,
                'error': 'Please enter your name.'
            })
        
        score = 0
        total_questions = quiz.questions.count()
        submission = UserSubmission.objects.create(quiz=quiz, user_name=user_name.strip(), score=score)

        # Process all questions
        for question in quiz.questions.all():
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                try:
                    answer = Answer.objects.get(id=selected_answer_id, question=question)
                    is_correct = answer.is_correct
                    UserAnswer.objects.create(
                        submission=submission,
                        question=question,
                        answer=answer,
                        is_correct=is_correct
                    )
                    if is_correct:
                        score += 1
                except Answer.DoesNotExist:
                    # Invalid answer selected
                    pass

        submission.score = score
        submission.save()
        return redirect('quiz_result', submission_id=submission.id)
    
    # If not POST, redirect to quiz
    return redirect('start_quiz', quiz_id=quiz_id)

def quiz_result(request, submission_id):
    submission = get_object_or_404(UserSubmission, id=submission_id)
    # Get all questions for the quiz
    all_questions = submission.quiz.questions.all()
    # Create a dictionary of user answers for easy lookup
    user_answers_dict = {ua.question.id: ua for ua in submission.answers.all()}
    
    # Create a list of question results with answer information
    question_results = []
    for question in all_questions:
        user_answer = user_answers_dict.get(question.id)
        question_results.append({
            'question': question,
            'user_answer': user_answer,
            'was_answered': user_answer is not None,
            'is_correct': user_answer.is_correct if user_answer else False,
        })
    
    context = {
        'submission': submission,
        'question_results': question_results,
        'total_questions': all_questions.count(),
    }
    return render(request, 'quizzes/quiz_result.html', context)
