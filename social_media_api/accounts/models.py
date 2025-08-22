from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

def __str__(self):
    return self.username

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # ManyToManyField with an explicit through model
    following = models.ManyToManyField(
        'self',
        through='UserFollowing',
        symmetrical=False,
        related_name='followers',
        through_fields=('user_from', 'user_to'),
        blank=True
    )

    def follow(self, user):
        if self != user:
            UserFollowing.objects.get_or_create(user_from=self, user_to=user)

    def unfollow(self, user):
        UserFollowing.objects.filter(user_from=self, user_to=user).delete()

    def is_following(self, user):
        return UserFollowing.objects.filter(user_from=self, user_to=user).exists()


class UserFollowing(models.Model):
    user_from = models.ForeignKey(CustomUser, related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey(CustomUser, related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_from', 'user_to')

    def __str__(self):
        return f"{self.user_from.username} follows {self.user_to.username}"
