from django.urls import path
from .views import UserCreate, PostList, QuestionList, CategoryList, UserData, backtest

app_name = 'users'

urlpatterns = [
    path('', PostList.as_view(), name='listcreate'),
    path('create/', UserCreate.as_view(), name="create_user"),
    path('question/<int:id>/', QuestionList.as_view(), name='questionlist'),
    path('profile/', UserData.as_view(), name='userdata'),
    path('category/', CategoryList.as_view(), name='categorylist'),
    path('backtest/', backtest, name="backtest" ),
]
