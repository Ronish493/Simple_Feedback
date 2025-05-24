from django.shortcuts import render, HttpResponseRedirect
from SpeakUp.models import Feedback
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def feedback_list(request):
    feedbacks= Feedback.objects.all()
    return render(
        request,
        "feedback_list.html",
        {"feedbacks": feedbacks},
    )

def feedback_submit(request):
    if request.method=="GET":
        return render(request, "feedback_submit.html")

    else:
        name_recived= request.POST["name"]
        email_recived= request.POST["email"]
        feedback_recived=request.POST["feedback"]
        Feedback.objects.create(name=name_recived, email=email_recived, message=feedback_recived)
        return HttpResponseRedirect("/")
    
