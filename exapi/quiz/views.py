from django.shortcuts import render
from .serializers import QuestionSerializer, QuizSerializer
from rest_framework import viewsets, status, generics
from .models import Question, Quiz

# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'url'


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'url'
