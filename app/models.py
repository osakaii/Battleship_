from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.id}'


class Game(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user2')
    game_code = models.IntegerField()

    def __str__(self):
        return f'{self.game_code}'


class ShipsArea(models.Model):

    game_code = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    sh_sum = models.PositiveIntegerField(default=5)
    shot_sum = models.PositiveIntegerField(default=0)

    x1 = models.BooleanField(default=False)
    x2 = models.BooleanField(default=False)
    x3 = models.BooleanField(default=False)
    x4 = models.BooleanField(default=False)
    x5 = models.BooleanField(default=False)
    x6 = models.BooleanField(default=False)
    x7 = models.BooleanField(default=False)
    x8 = models.BooleanField(default=False)
    x9 = models.BooleanField(default=False)
    x10 = models.BooleanField(default=False)
    x11 = models.BooleanField(default=False)
    x12 = models.BooleanField(default=False)
    x13 = models.BooleanField(default=False)
    x14 = models.BooleanField(default=False)
    x15 = models.BooleanField(default=False)
    x16 = models.BooleanField(default=False)
    x17 = models.BooleanField(default=False)
    x18 = models.BooleanField(default=False)
    x19 = models.BooleanField(default=False)
    x20 = models.BooleanField(default=False)
    x21 = models.BooleanField(default=False)
    x22 = models.BooleanField(default=False)
    x23 = models.BooleanField(default=False)
    x24 = models.BooleanField(default=False)
    x25 = models.BooleanField(default=False)
    s_x1 = models.BooleanField(default=False)
    s_x2 = models.BooleanField(default=False)
    s_x3 = models.BooleanField(default=False)
    s_x4 = models.BooleanField(default=False)
    s_x5 = models.BooleanField(default=False)
    s_x6 = models.BooleanField(default=False)
    s_x7 = models.BooleanField(default=False)
    s_x8 = models.BooleanField(default=False)
    s_x9 = models.BooleanField(default=False)
    s_x10 = models.BooleanField(default=False)
    s_x11 = models.BooleanField(default=False)
    s_x12 = models.BooleanField(default=False)
    s_x13 = models.BooleanField(default=False)
    s_x14 = models.BooleanField(default=False)
    s_x15 = models.BooleanField(default=False)
    s_x16 = models.BooleanField(default=False)
    s_x17 = models.BooleanField(default=False)
    s_x18 = models.BooleanField(default=False)
    s_x19 = models.BooleanField(default=False)
    s_x20 = models.BooleanField(default=False)
    s_x21 = models.BooleanField(default=False)
    s_x22 = models.BooleanField(default=False)
    s_x23 = models.BooleanField(default=False)
    s_x24 = models.BooleanField(default=False)
    s_x25 = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('game_code', 'user')

    def __str__(self):
        return f'{self.game_code}'
