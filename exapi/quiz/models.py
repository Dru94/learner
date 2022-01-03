from django.db import models
from accounts.models import User
# Create your models here.

DIFF_CHOICES = [
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard')
]

LEVEL_CHOICES = [
    ('primary', 'primary'),
    ('secondary', 'secondary')
]


class Quiz(models.Model):
    subject = models.CharField(max_length=225, blank=False)
    topic = models.CharField(max_length=225, blank=True)
    level = models.CharField(
        max_length=9, choices=LEVEL_CHOICES, blank=False, default='')
    level_number = models.PositiveIntegerField(
        null=False, default=1, verbose_name='class')
    quiz_duration = models.PositiveIntegerField(null=False)
    max_score = models.PositiveIntegerField(null=False)
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject + " " + self.topic + " Class: " + self.level + str(self.level_number) + " " + str(self.duration)

    def getQuestions(self):
        return self.quiz.all()


class Question(models.Model):
    question_text = models.CharField(max_length=225, blank=False)
    question_duration = models.PositiveIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Answer(models.Model):
    answer_text = models.CharField(max_length=225, blank=False)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Question: " + self.question.text + " Answer: " + self.answer + " Correct: " + self.correct


class Result(models.Model):
    quiz_exercise = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return "Email: " + self.user.email + " Quiz: " + str(self.quiz_exercise) + " Score: " + str(self.score)
