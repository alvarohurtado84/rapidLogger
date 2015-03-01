from django.db import models


class Entry(models.Model):
    """Define the basic behaviors for bullets."""

    title = models.CharField()

    irrelevant = models.BooleanField(default=False)

    created_at = models.DateTimeField()
    accomplish_at = models.DateTimeField()


class Task(Entry):
    """Define a Task bullet."""

    done = models.BooleanField(default=False)
    done_at = models.DateTimeField()

    migrated_from = models.OneToOneField('Task',
                                         related_name='migrated_to')


class Event():
    """Define an Event bullet."""

    pass


class Note():
    """Define a Note bullet."""

    pass
