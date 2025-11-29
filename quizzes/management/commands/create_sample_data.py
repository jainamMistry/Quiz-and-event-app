"""
Management command to create sample quizzes and events for testing
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from quizzes.models import Quiz, Question, Answer
from events.models import Event


class Command(BaseCommand):
    help = 'Creates sample quizzes and events for testing'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating sample data...'))
        
        # Create Sample Quiz 1: General Knowledge
        quiz1, created = Quiz.objects.get_or_create(
            title="General Knowledge Quiz",
            defaults={
                'description': 'Test your general knowledge with this fun quiz covering various topics including science, history, and geography.'
            }
        )
        
        if created:
            # Question 1
            q1 = Question.objects.create(
                quiz=quiz1,
                text="What is the capital of France?",
                question_type="multiple_choice"
            )
            Answer.objects.create(question=q1, text="London", is_correct=False)
            Answer.objects.create(question=q1, text="Berlin", is_correct=False)
            Answer.objects.create(question=q1, text="Paris", is_correct=True)
            Answer.objects.create(question=q1, text="Madrid", is_correct=False)
            
            # Question 2
            q2 = Question.objects.create(
                quiz=quiz1,
                text="What is the largest planet in our solar system?",
                question_type="multiple_choice"
            )
            Answer.objects.create(question=q2, text="Earth", is_correct=False)
            Answer.objects.create(question=q2, text="Jupiter", is_correct=True)
            Answer.objects.create(question=q2, text="Saturn", is_correct=False)
            Answer.objects.create(question=q2, text="Neptune", is_correct=False)
            
            # Question 3
            q3 = Question.objects.create(
                quiz=quiz1,
                text="Who wrote 'Romeo and Juliet'?",
                question_type="multiple_choice"
            )
            Answer.objects.create(question=q3, text="Charles Dickens", is_correct=False)
            Answer.objects.create(question=q3, text="William Shakespeare", is_correct=True)
            Answer.objects.create(question=q3, text="Jane Austen", is_correct=False)
            Answer.objects.create(question=q3, text="Mark Twain", is_correct=False)
            
            self.stdout.write(self.style.SUCCESS(f'✓ Created quiz: {quiz1.title}'))
        
        # Create Sample Quiz 2: Python Programming
        quiz2, created = Quiz.objects.get_or_create(
            title="Python Programming Basics",
            defaults={
                'description': 'Test your knowledge of Python programming fundamentals including syntax, data structures, and basic concepts.'
            }
        )
        
        if created:
            # Question 1
            q1 = Question.objects.create(
                quiz=quiz2,
                text="Which of the following is used to define a function in Python?",
                question_type="multiple_choice"
            )
            Answer.objects.create(question=q1, text="function", is_correct=False)
            Answer.objects.create(question=q1, text="def", is_correct=True)
            Answer.objects.create(question=q1, text="define", is_correct=False)
            Answer.objects.create(question=q1, text="func", is_correct=False)
            
            # Question 2
            q2 = Question.objects.create(
                quiz=quiz2,
                text="What does 'len()' function do in Python?",
                question_type="multiple_choice"
            )
            Answer.objects.create(question=q2, text="Converts to lowercase", is_correct=False)
            Answer.objects.create(question=q2, text="Returns the length of an object", is_correct=True)
            Answer.objects.create(question=q2, text="Sorts a list", is_correct=False)
            Answer.objects.create(question=q2, text="Returns the maximum value", is_correct=False)
            
            # Question 3
            q3 = Question.objects.create(
                quiz=quiz2,
                text="Which data type is mutable in Python?",
                question_type="multiple_choice"
            )
            Answer.objects.create(question=q3, text="tuple", is_correct=False)
            Answer.objects.create(question=q3, text="list", is_correct=True)
            Answer.objects.create(question=q3, text="string", is_correct=False)
            Answer.objects.create(question=q3, text="int", is_correct=False)
            
            self.stdout.write(self.style.SUCCESS(f'✓ Created quiz: {quiz2.title}'))
        
        # Create Sample Quiz 3: Web Development
        quiz3, created = Quiz.objects.get_or_create(
            title="Web Development Fundamentals",
            defaults={
                'description': 'Test your understanding of web development basics including HTML, CSS, and JavaScript concepts.'
            }
        )
        
        if created:
            # Question 1
            q1 = Question.objects.create(
                quiz=quiz3,
                text="What does HTML stand for?",
                question_type="multiple_choice"
            )
            Answer.objects.create(question=q1, text="HyperText Markup Language", is_correct=True)
            Answer.objects.create(question=q1, text="High Tech Modern Language", is_correct=False)
            Answer.objects.create(question=q1, text="Home Tool Markup Language", is_correct=False)
            Answer.objects.create(question=q1, text="Hyperlink and Text Markup Language", is_correct=False)
            
            # Question 2
            q2 = Question.objects.create(
                quiz=quiz3,
                text="Which CSS property is used to change the text color?",
                question_type="multiple_choice"
            )
            Answer.objects.create(question=q2, text="text-color", is_correct=False)
            Answer.objects.create(question=q2, text="color", is_correct=True)
            Answer.objects.create(question=q2, text="font-color", is_correct=False)
            Answer.objects.create(question=q2, text="text-style", is_correct=False)
            
            self.stdout.write(self.style.SUCCESS(f'✓ Created quiz: {quiz3.title}'))
        
        # Create Sample Events
        today = timezone.now().date()
        
        event1, created = Event.objects.get_or_create(
            title="Tech Conference 2025",
            defaults={
                'description': 'Join us for an exciting tech conference featuring talks on the latest trends in web development, AI, and cloud computing. Network with industry professionals and learn from experts.',
                'date': today + timedelta(days=15),
                'location': 'Convention Center, New York'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'✓ Created event: {event1.title}'))
        
        event2, created = Event.objects.get_or_create(
            title="Python Workshop for Beginners",
            defaults={
                'description': 'A hands-on workshop designed for beginners to learn Python programming. No prior experience required. We will cover basics, data structures, and create a small project.',
                'date': today + timedelta(days=30),
                'location': 'Community College, San Francisco'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'✓ Created event: {event2.title}'))
        
        event3, created = Event.objects.get_or_create(
            title="Web Development Hackathon",
            defaults={
                'description': 'A 24-hour hackathon where teams compete to build innovative web applications. Prizes for the top 3 teams. Food and drinks provided. Register your team now!',
                'date': today + timedelta(days=45),
                'location': 'Tech Hub, Seattle'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'✓ Created event: {event3.title}'))
        
        event4, created = Event.objects.get_or_create(
            title="Django Framework Meetup",
            defaults={
                'description': 'Monthly meetup for Django developers. This month we will discuss Django 5.0 features, best practices, and share our experiences. Bring your questions!',
                'date': today + timedelta(days=20),
                'location': 'Coffee Shop, Austin'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'✓ Created event: {event4.title}'))
        
        self.stdout.write(self.style.SUCCESS('\n✓ Sample data created successfully!'))
        self.stdout.write(self.style.SUCCESS('You can now view quizzes and events on the website.'))

