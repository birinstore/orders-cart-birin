from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404, reverse, render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib import messages

from .models import Dress


# from .forms import CommentForm


class Dress_List(generic.ListView):
    model = Dress
    queryset = Dress.objects.filter(active=True)
    template_name = 'dress/dress.html'
    context_object_name = 'dress'

    # def get_queryset(self):
    #


class Dress_detail(generic.DetailView):
    model = Dress
    template_name = 'dress/details_dress.html'
    context_object_name = 'dress_detail'
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comment_form'] = CommentForm()
    #     return context

#
# class CommentCreateView(generic.CreateView):
#     model = Comment
#     form_class = CommentForm
#
#     # def get_success_url(self):
#     #     return reverse('product_list')
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.author = self.request.user
#
#         product_id = int(self.kwargs['product_id'])
#         product = get_object_or_404(Product, id=product_id)
#         obj.product = product
#
#         messages.success(self.request, _('Comment successfully created'))
#
#         return super().form_valid(form)

# Create your views here.
