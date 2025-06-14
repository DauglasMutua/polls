from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# The reverse() function is used to reverse-resolve URLs in Django.
from django.views import generic
# The generic module provides a set of generic views that can be used to create common web application patterns.
from .models import Choice, Question
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    # The get_queryset() method is used to define the data that will be displayed in the view.
    # By default, it returns all objects of the model specified in the view's model attribute.
    def get_queryset(self):
    #"""Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    # The DetailView is a generic view that displays a single object.
    # It is used to display the details of a specific object, such as a question in this case.
    model = Question
    template_name = "polls/detail.html"

    # The get_queryset() method is used to define the data that will be displayed in the view.
    # By default, it returns all objects of the model specified in the view's model attribute.
    def get_queryset(self):
        #"""Excludes any questions that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        #request.POST is a dictionary-like object that lets you access submitted data by key name. 
        # In this case,request.POST['choice'] returns the ID of the selected choice, as a string. 
        # request.POST values are always strings
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form
        return  render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing 
        # with POST data. This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
