from django.views.generic import CreateView, ListView, UpdateView
from django.http import HttpResponseRedirect

from .services import get_response_history
from .models import Question, QuestionHistory, Response
from .forms import QuestionForm, ResponseForm

class QuestionCreate(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question/question-form.html'
    success_url = '/question/list'

    # Create a question history entry to match newly created question
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by=self.request.user
        self.object.save()
        QuestionHistory.objects.create(question_text=self.object.text, question=self.object)
        return HttpResponseRedirect(self.get_success_url())

class QuestionList(ListView):
    model = Question
    queryset = Question.objects.all()
    context_object_name = 'question_list'
    template_name = 'question/question-list.html'

class QuestionDetail(ListView):
    model = Question
    context_object_name = 'question'
    template_name = 'question/question-detail.html'

    # Get change history of question
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        history = QuestionHistory.objects.filter(question_id=self.kwargs['pk']).order_by('created_on')
        data['original'] = history.first()
        data['original_pk'] = self.kwargs['pk']
        data['q_history'] = history.order_by('-created_on')

        return data

class QuestionUpdate(UpdateView):
    model = Question
    form_class = QuestionForm
    context_object_name = 'question'
    template_name = 'question/question-form.html'
    success_url = '/question/list'

    # Create new question history on every question update
    def form_valid(self, form):
        question = form.save()
        QuestionHistory.objects.create(question_text=question.text, question=question)
        return HttpResponseRedirect(self.get_success_url())

class ResponseCreate(CreateView):
    model = Response
    form_class = ResponseForm
    template_name = 'response/response-form.html'
    success_url = '/question/list'

    def form_valid(self, form):
        response = form.save(commit=False)
        response.user = self.request.user
        most_recent_question = QuestionHistory.objects.filter(question_id=self.kwargs['pk']).order_by('created_on').last()
        response.question_history = most_recent_question
        return super(ResponseCreate, self).form_valid(form)

class ResponseList(ListView):
    model = Response
    queryset = Response.objects.all()
    context_object_name = 'response_list'
    template_name = 'response/response-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        question_id = self.kwargs['pk']

        # Get responses with corresponding questions texts
        rows = get_response_history(question_id)
        data['responses'] = rows
        return data

