from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
	
		class Meta:
			model = Feedback
			fields = ('user_name','neighbourhoods','phone_number','rating','comment')


