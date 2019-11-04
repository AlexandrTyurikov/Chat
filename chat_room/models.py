from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    creator = models.ForeignKey(User, verbose_name="Комната чата", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="Приглашенные участники", related_name='invited_user')
    creation_date = models.DateTimeField("Дата и время создания", auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField("Дата и время изменения", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Комната чата"
        verbose_name_plural = "Комнаты чатов"


class Chat(models.Model):
    room = models.ForeignKey(Room, verbose_name="Комната чата", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField("Сообщение", max_length=800)
    date = models.DateTimeField("Дата и время отправки", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение чата"
        verbose_name_plural = "Сообщения чатов"
