from django.test import TestCase
from polls.models import Question,Choice
import datetime

class QuestionModelTests(TestCase):
    def test_is_empty(self):
        saved_posts = Question.objects.all()
        self.assertEqual(saved_posts.count(), 0)
    
    def test_is_count_one(self):
        question = Question(question_text='test_question',pub_date= datetime.datetime.now())
        question.save()
        saved_posts = Question.objects.all()
        self.assertEqual(saved_posts.count(), 1)

    # def test_saving_and_retrieving_post(self):
    #     question = Question()
    #     question_text = 'test_question_to_retrieve'
    #     question.question_text = question_text
    #     question.save()

    #     saved_posts = Question.objects.all()
    #     actual_post = saved_posts[0]

    #     self.assertEqual(actual_post.question_text, question_text)

class ChoiceModelTests(TestCase):
    def test_is_empty(self):
        saved_posts = Choice.objects.all()
        self.assertEqual(saved_posts.count(), 0)
    
    # def test_is_count_one(self):
    #     choice = Choice(question_id=question_id,choice_text='test_question',votes=0)
    #     choice.save()
    #     saved_posts = Choice.objects.all()
    #     self.assertEqual(saved_posts.count(), 1)

    # def test_saving_and_retrieving_post(self):
    #     choice = Choice()
    #     choice_text = 'test_choice_to_retrieve'
    #     choice.choice_text = choice_text
    #     choice.save()

    #     saved_posts = Choice.objects.all()
    #     actual_post = saved_posts[0]

    #     self.assertEqual(actual_post.choice_textt, choice_text)