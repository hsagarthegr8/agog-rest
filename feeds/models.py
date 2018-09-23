from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.posted_by.username +' - '+ self.content


class Response(models.Model):
    responded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    responded_on = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    replied_on = models.ForeignKey('Response', on_delete=models.CASCADE, related_name='replied', null=True, blank=True)
    is_reply = models.BooleanField(default=False)
    response = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.response


class Reactions(models.Model):
    CHOICES = (('A', 'Angry'),
               ('H', 'Haha'),
               ('L', 'Love'),
               ('S', 'Sad'),
               ('W', 'Wow'))
    reacted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=1, choices=CHOICES)
    reacted_on_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    reacted_on_response = models.ForeignKey(Response, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        try:
            return self.get_reaction_display() +' - Post - '+ self.reacted_on_post.content
        except:
            return self.get_reaction_display() +' - Response - '+ self.reacted_on_response.response

    class Meta:
        verbose_name_plural = 'Reactions'