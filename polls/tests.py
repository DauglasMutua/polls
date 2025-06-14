import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
# The TestCase class is a subclass of unittest.TestCase that provides a set of methods and assertions for testing Django applications.
from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is older than 1 day.
        """
        time = timezone.now( - datetime.timedelta(days=1, seconds=1))
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_datetime=time)
        self.assertIs(recent_question.was_published_recently(), True)

# The following code is used to create a question with a specific publication date.
# This is useful for testing purposes, as it allows you to create questions with different publication dates.
def create_question(question_text,days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions
    published in the past, positive for questions that have yet to be
    published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

# The following code is used to test the index view of the polls application.
# The index view is the main page of the polls application, where users can see a list of available polls.
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

# The following code is used to test the case where there is a single past question.
    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

# The following code is used to test the case where there is a single future question.
    # The test_future_question() method tests the case where a question is published in the future.
    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

# The following code is used to test the case where there is both a past and a future question.
    # The test_future_question_and_past_question() method tests the case where both past and future questions exist.
    def test_future_question_and_past_question(self):
        """
        If both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

# The following code is used to test the case where there are multiple past questions.
    def test_two_past_questions(self):
        """ 
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )

# The following code is used to test the detail view of a question.
# The detail view displays the details of a specific question.
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,) )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404
        )

# The test_future_question() method tests the case where a question is published in the future.
    # The test_past_question() method tests the case where a question is published in the past.
    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,) )
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)