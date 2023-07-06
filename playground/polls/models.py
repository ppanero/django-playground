import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


"""
Testing how to make queries

$ python manage.py shell

>>> from polls.models import Choice, Question

# in-memory creation + commit
>>> q1 = Question(question_text="Is this okay?", pub_date="2023-07-06")
>>> q1.save()

# <Model>.objects is the manager, accessible only from the class (not instance)
# create + commit in one line
>>> q2 = Question.objects.create(
        question_text="Is this okay, too?", pub_date="2023-07-06"
    )

# all parameters must be kwargs
>>> c1 = Choice.objects.create(question=q1, choice_text="yes")
>>> c2 = Choice.objects.create(question=q1, choice_text="no")

# all brings everything in memory, for big tables use `.all().iterator()`
>>> Choice.objects.all()
<QuerySet [<Choice: yes>, <Choice: no>]>

# each chained filter returns a query set
>>> qs1 = Choice.objects.filter(votes=0)
>>> qs2 = qs1.filter(choice_text="no")
>>> id(qs1)
4490105616
>>> id(qs2)
4489496752

# query sets are lazy they do not run a query until they are evaluated
>>> qs2
<QuerySet [<Choice: no>]>

# unless specified there is a incremental integer as pk
>>> Choice.objects.filter(pk=1)
<QuerySet [<Choice: yes>]>

# operators as part of the attribute/column name
>>> Choice.objects.filter(votes__gte=0)
<QuerySet [<Choice: yes>, <Choice: no>]>
>>> Choice.objects.filter(votes__gte=1)
<QuerySet []>

# cached is only populated when evaluating all the query set not part
# e.g. qs[1] would not cache it
>>> cached = Choice.objects.filter(votes=0)
>>> [i for i in cached]
<QuerySet [<Choice: yes>, <Choice: no>]>

# DANGER! cache is not invalidated
>>> c3 = Choice.objects.create(question=q1, choice_text="maybe")
>>> [i for i in cached]
<QuerySet [<Choice: yes>, <Choice: no>]>
"""
