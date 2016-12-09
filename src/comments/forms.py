from django import forms

from .models import Comment

# class CommentForm(forms.Form):
# 	content = forms.CharField(label="Comment", widget=forms.Textarea({'cols': 22, 'rows': 3 }))

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
	 	fields = [
	 		'content',
	 	]
	 	widgets = {
	 		'content': forms.Textarea(attrs={'cols': 22, 'rows': 3})
	 	}
	