from django import forms


class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search')

# from django import forms
# from .models import Comment
#
#
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['body', 'stars', ]
#
#
# class CommentsForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['body', 'stars', ]
