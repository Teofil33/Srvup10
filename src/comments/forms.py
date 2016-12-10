from django import forms

from .models import Comment

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

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

	def __init__(self, data=None, files=None, **kwargs):
		super(CommentForm, self).__init__(data, files, kwargs)
		self.helper = FormHelper()
		self.helper.form_show_labels = False
		#self.helper.add_input(Submit('submit', "Comment", css_class='btn btn-primary btn-block',))	
	