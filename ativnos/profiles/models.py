from django.conf import settings
from django.db import models

from ativnos.tags.models import Cause, Skill


class UserTagAbstractBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    description = models.TextField(max_length=300, blank=True)

    class Meta:
        abstract = True
        unique_together = (('user', 'tag'),)

    def __str__(self):
        return "{user}: {tag}".format(user=self.user, tag=self.tag)


class UserCause(UserTagAbstractBase):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='causes', related_query_name='cause')
    tag = models.ForeignKey(Cause, on_delete=models.CASCADE)


class UserSkill(UserTagAbstractBase):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='skills', related_query_name='skill')
    tag = models.ForeignKey(Skill, on_delete=models.CASCADE)
