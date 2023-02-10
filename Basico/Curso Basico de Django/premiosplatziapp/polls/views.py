from django.shortcuts import render,get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Question,Choice
from django.urls import reverse
from django.views import generic 
# Create your views here.

# def index(request):
#     lastest_question_list=Question.objects.all()    
#     return render(request, "polls/index.html",{'lastest_question_list':lastest_question_list})

# def detail(request, id):
#     question=get_object_or_404(Question, pk=id)    
#     return render(request, "polls/detail.html", {'question':question})


# def results(request, id):
#     question = get_object_or_404(Question, pk=id)
#     return render(request, 'polls/results.html', {'question': question})
    
    
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
            """Return the last five published questions."""
            return Question.objects.order_by('-pub_date')[:5]
        
        
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
        

def vote(request, id):
    question=get_object_or_404(Question, pk=id)
    # print(f"pregunta: {question }")
    # print(f"pregunta id:{id }")
    # print(f'request.POST["choice"] {request.POST["choice"]}')
    try:
       
        selected_choice= question.choice_set.get(pk=request.POST["choice"])
        
    except (KeyError, Choice.DoesNotExist):
        return render(
            request, 
            "polls/detail.html",
            {"question": question,
             "error_message":"No elegiste una respuesta"})
    else:
        # print(f'selected_choice {selected_choice}')
        # print()
        print(selected_choice)
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(id,)))
    
