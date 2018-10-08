from django.db import models


class Tweet(models.Model):

    tweet_text = models.CharField(max_length=140)
    tweet_date = models.DateTimeField('tweet date')

    '''
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    '''
