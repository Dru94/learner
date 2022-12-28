from msilib.schema import ServiceInstall
from django.shortcuts import render
from .serializers import QuestionSerializer, QuizSerializer
from rest_framework import viewsets, status, generics
from .models import Question, Quiz, Answer
from rest_framework.views import APIView
from rest_framework.response import Response
import json
# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'quiz'


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'subject'


class TakeQuizView(APIView):
    def get(self, request, id, format=None):
        dct = {}
        qt = []
        qz = Quiz.objects.get(id=id)
        qtn = Question.objects.filter(quiz=qz)
        ans = Answer.objects.all()

        for q in qtn:
            dct[q.question_text] = []

        for a in ans:
            for k in dct.keys():
                if a.question.question_text == k:
                    dct[k].append(a.answer_text)
        
        return Response(data=dct, status=status.HTTP_200_OK)
