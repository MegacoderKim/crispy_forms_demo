from django.shortcuts import render
from .forms import FeedbackForm

# Create your views here.
def index(request):
	template = 'feedback/feedback.html'
	context = {'msg':"This is packed in view"}
	return render(request,template,context)

def feedback(request):

	if request.method == 'POST':
		form = FeedbackForm(request.POST)

	else:
		feedform = FeedbackForm()
		context = {'form':feedform,}
		template ='feedback/feedform.html'
		return render(request,template,context)