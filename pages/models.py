# from django.db import models
#
#
# class Post(models.Model):
#     title = models.CharField(max_length=20)
#     name = models.CharField(max_length=20)
#     phone_number = models.CharField(max_length=11)
#
#
# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=False)
#
#     class Meta:
#         ordering = ['created_on']
#
#     def __str__(self):
#         return 'Comment {} by {}'.format(self.body, self.name)
# #
# #
# # class ContactUs(models.Model):
# #     name = models.CharField(max_length=15)
# #     phone_number = models.CharField(max_length=11)
# #     title = models.CharField(max_length=10)
# #     textarea = models.TextField(max_length=100)
