from django.db.models import fields
from django.utils import tree
from rest_framework import serializers
from .models import Question, Quiz, Answer, Result


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(required=True)
    # answers = AnswerSerializer(many=True, required=True)

    class Meta:
        model = Question
        fields = "__all__"

    def create(self, validated_data):
        quiz_data = validated_data.pop('quiz')
        quiz = Quiz.objects.create(quiz_data)
        question = Question.objects.create(quiz=quiz, **validated_data)
        print(question)
        return question
