from django import forms
# from .models import FoodSubmission


class ChatForm(forms.Form):
    user_input = forms.CharField(label='Answer', max_length=100)

