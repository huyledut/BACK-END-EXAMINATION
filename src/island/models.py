from django.db import models
from django.contrib.auth.models import User

class Island(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    area = models.FloatField()
    detected_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Island'

    def __str__(self):
        return f"Island {self.id}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    island = models.ForeignKey(Island, on_delete=models.CASCADE)
    comment_text = models.TextField()

    class Meta:
        db_table = 'Comment'

    def __str__(self):
        return f"Comment by {self.user.username} on Island {self.island.id}"

class Media(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPES)
    media_url = models.URLField()

    class Meta:
        db_table = 'Media'

    def __str__(self):
        return f"Media for Comment {self.comment.id}"