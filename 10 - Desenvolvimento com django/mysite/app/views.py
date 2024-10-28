from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from app.models import Question, Choice
from django.db.models import F
from django.urls import reverse

# Create your views here.
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {
    "latest_question_list": latest_question_list,
  }
  return render(request, "app/index.html", context)
  
def detail(request, question_id):
 try:
   question = Question.objects.get(pk=question_id)
   choice = Choice.objects.get(question_id=question_id)
 except Question.DoesNotExist as e:
   print(e)
   raise Http404("Question does not exist")
 return render(request, "app/detail.html", {"question": question, "choice": choice.choice_text})
   

def results(request, question_id):
  question = get_object_or_404(Question, id=question_id)
  return render(request, "app/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "app/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("app:results", args=[question.id]))
