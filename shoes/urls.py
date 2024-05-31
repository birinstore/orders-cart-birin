from django.urls import path
from . import views

from .views import Shoes_List, Shoes_detail

urlpatterns = [
    path('', Shoes_List.as_view(), name='shoes'),
    path('<int:pk>/', Shoes_detail.as_view(), name='shoe_detail'),

]

# path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create'),
