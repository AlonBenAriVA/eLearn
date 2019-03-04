from django import forms
from learn.models import VidTopics, ThreadDiscussion

class NewTopicForm(forms.ModelForm):
  comment = forms.CharField(
    widget = forms.Textarea(
      attrs = {'rows':5, 'placeholder':'What is your question?'}
    ),
    max_length = 255,
    help_text = 'max length is 255 characters'
  )
  class Meta:
    model = VidTopics
    fields = ['subject','comment']

class AddComment(forms.ModelForm):
  thread_content = forms.CharField(
     widget = forms.Textarea(
      attrs = {'rows':5, 'placeholder':'What is your question?'}
    ),
    max_length = 255,
    help_text = 'max length is 255 characters'
  )
  class Meta:
    model = ThreadDiscussion
    fields = ['thread_content']
