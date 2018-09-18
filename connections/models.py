from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Connection(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conn_senders')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conn_receivers')
    timestamp = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.sender.username + '-' + self.receiver.username