from django.db import models
from django.conf import settings

class Question(models.Model):
    ANSWER_CHOICES = [
        ('answer_1', 'Answer 1'),
        ('answer_2', 'Answer 2'),
        ('answer_3', 'Answer 3'),
        ('answer_4', 'Answer 4'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_question', null=True,blank=True)
    question = models.CharField(max_length=2000)
    answer_1 = models.CharField(max_length=1000)
    answer_2 = models.CharField(max_length=1000)
    answer_3 = models.CharField(max_length=1000)
    answer_4 = models.CharField(max_length=1000)
    correct_answer = models.CharField(max_length=10, choices=ANSWER_CHOICES)

    def __str__(self):
        return self.question

    def get_answer(self):
        answer = self.correct_answer
        if answer == 'answer_1':
            return self.answer_1
        elif answer == 'answer_2':
            return self.answer_2
        elif answer == 'answer_3':
            return self.answer_3
        elif answer == 'answer_4':
            return self.answer_4
        else:
            return None