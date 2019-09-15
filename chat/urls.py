from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import QuestionCreate, QuestionList, QuestionDetail, QuestionUpdate, ResponseCreate, ResponseList


urlpatterns = [
    path('create/', login_required(QuestionCreate.as_view()), name='question-create'),
    path('list/', login_required(QuestionList.as_view()), name='question-list'),
    path('<int:pk>/', login_required(QuestionDetail.as_view()), name='question-detail'),
    path('<int:pk>/edit', login_required(QuestionUpdate.as_view()), name='question-edit'),
    path('<int:pk>/respond', login_required(ResponseCreate.as_view()), name='response-edit'),
    path('<int:pk>/responses', login_required(ResponseList.as_view()), name='response-list')
]