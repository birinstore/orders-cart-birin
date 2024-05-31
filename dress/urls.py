from django.urls import path
from . import views

from .views import Dress_List, Dress_detail

urlpatterns = [
    path('', Dress_List.as_view(), name='dress'),
    path('<int:pk>/', Dress_detail.as_view(), name='dress_detail'),

]

# path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create'),
