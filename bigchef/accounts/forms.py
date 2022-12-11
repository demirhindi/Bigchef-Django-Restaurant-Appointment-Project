from django import forms
from accounts.models import Comment

class CommentForm(forms.ModelForm):
	bodytext = forms.CharField(widget=forms.Textarea(), required=True)

	class Meta:
		model = Comment
		fields = ('bodytext',)