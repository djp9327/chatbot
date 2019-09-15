from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Question, Response

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Question'))

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('response_text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Response'))
