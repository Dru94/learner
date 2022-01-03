from django.urls import path
from . import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'question', views.QuestionViewSet, basename="question")
router.register(r'quiz', views.QuizViewSet, basename="quiz")

urlpatterns = router.urls
