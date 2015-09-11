from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from models import Questions, Choice
from django.template import RequestContext, loader
from django.shortcuts import render
from django.core.urlresolvers import reverse

def index(request):
    """
    """
    print "Views Called...."
    all_questions = Questions.objects.all() # QuerySet Object
#     template = loader.get_template('polls/index.html')
#     context = RequestContext(request,{'questions' : all_questions})
#     questions = ','.join(row.question_text for row in all_questions)
#     return HttpResponse(template.render(context))

    ## using django shortcut method to render the things
    context =  {'questions' : all_questions,
                'request': request }
    return render(request,'polls/index.html', context)

def detail(request, question_id):
    """
    """
    print "details called...."
    question = get_object_or_404(Questions,pk=question_id)
    print "***********************",question.id
    print "***********************",question.question_text
    print dir(question)
#     try:
#         question = Questions.objects.get(pk=question_id)
#     except Questions.DoesNotExist:
#         raise Http404("Could not get the question")
    return render(request, 'polls/details.html',{'question': question})
#     return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    """
    """
    response = "You're looking at the results of question %s."
    question =  get_object_or_404(Questions, pk=question_id)
    return render(request,'polls/results.html',{'question': question})

#     return HttpResponse(response % question_id)


def vote(request, question_id):
    """
    """
    question =  get_object_or_404(Questions,pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
        print "#################3", request.POST['choice']
    except (KeyError, Choice.DoesNotExist):
        # Redisplaying the form
        return render(request,'polls/details.html',{'question':question,'error_message': "You did not select a choice"})
    else:
        choice.votes = choice.votes+1
        choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  
#     return HttpResponse("You're voting on question %s." % question_id)
    