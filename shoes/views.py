from django.views import generic
from django.shortcuts import get_object_or_404, reverse, render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.contrib import messages
from .forms import SearchForm
from .models import Shoes


# from .forms import CommentForm


class Shoes_List(generic.ListView):
    model = Shoes
    queryset = Shoes.objects.filter(active=True)
    template_name = 'shoes/shoes.html'
    context_object_name = 'shoes'

    # def get_queryset(self):
    #


class Shoes_detail(generic.DetailView):
    model = Shoes
    template_name = 'shoes/details.html'
    context_object_name = 'shoe'
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

def search_view(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        results = Shoes.objects.filter(title=search_query)

    return render(request, 'shoes/shoes.html', {'form': form, 'results': results})
