from django.db import models

# Create your models here.

DIFF_CHOICES = [
	('easy','easy'),
	('medium','medium'),
	('hard','hard')
]

class Quiz(models.Model):
	subject = models.CharField(max_length=225, blank=False)
	topic = models.CharField(max_length=225, blank=False)
	level = models.PositiveIntegerField(null=False)
	duration = models.PositiveIntegerField(null=False)
	score = models.PositiveIntegerField(null=False)
	difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.subject + " " + self.topic + " " + str(self.level) + " " + str(self.duration)

	def getQuestions(self):
		return self.quiz.all()

class Question(models.Model):
		text = models.CharField(max_length=225, blank=False)
		quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="quiz")
		duration = models.PositiveIntegerField(null=False)
		created_at = models.DateTimeField(auto_now_add=True)
		updated_at = models.DateTimeField(auto_now=True)

		def __str__(self):
			return self.text

		def getAnswers(self):
			return self.question.all()


class Answer(models.Model):
	answer = models.CharField(max_length=225, blank=False)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
	correct = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "Question: " + self.question.text + " Answer: " + self.answer + " Correct: " + str(self.correct)
