from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.shortcuts import get_object_or_404, reverse, render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib import messages

from dress.models import Dress
from products.models import Product
from shoes.models import Shoes
# from models import Contact

# from .models import Post
# from .forms import CommentForm
# from django.shortcuts import render, get_object_or_404


# Create your views here.
class AboutPage(TemplateView):
    template_name = 'pages/about.html'


class SupportPage(TemplateView):
    template_name = 'pages/support.html'


class HomePage(TemplateView):
    template_name = 'home.html'


class Contact(TemplateView):
    template_name = 'pages/contact.html'

#
# def post_detail(request, slug):
#     template_name = 'post_detail.html'
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None  # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.get = get
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#     return render(request, template_name, {'post': post,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})
