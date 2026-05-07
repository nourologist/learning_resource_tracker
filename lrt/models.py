from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    '''A broad topic a user wants to learn about, e.g. "software development"'''

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Tag(models.Model):
    '''A sub-topic a user wants to learn about, e.g. "python"'''

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # class Meta:
        # ordering = ['last_used']

    def __str__(self):
        return self.text

# This should be editable by user but should have a few choices pre-populated
class ResourceType(models.Model):
    '''Format of the learning resource, e.g. "book", "video", or "tool"'''

    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


# Does this need to be its own class to be clickable, or should it be part of the Entry model?
# Should these choices be editable by the user?
class Status(models.Model):
    '''Tracks the status of a learning resource'''

    STATUS_CHOICES = (
        ('UNS', 'Unstarted'),
        ('INP', 'In Progress'),
        ('FIN', 'Finished'),
    )

    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='UNS')


class Entry(models.Model):
    '''A specific learning resource, individually added, e.g. a link to a website'''

    # Mandatory Fields:
    text = models.TextField(help_text='Name or link')
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # Should I choose a different on_delete?
    date_added = models.DateTimeField(auto_now_add=True)

    # Optional Fields:
    tags = models.ManyToManyField(Tag, blank = True, null = True)
    resource_type = models.ForeignKey(ResourceType, on_delete = models.PROTECT, blank = True, null = True)
    author = models.CharField(help_text = 'Author', max_length = 50, blank = True)
    preferred_format = models.CharField(help_text = 'Preferred format, e.g. paperback, audiobook, etc.', max_length = 50, blank = True)
    recommender = models.CharField(help_text = 'Person, institution, website, or tweet that recommended the learning resource to you', max_length = 100, blank = True)
    #screenshot = [attachment]
    location = models.CharField(help_text = 'File path, URL, bookshop name, or library', max_length = 250, blank = True)
    status = models.ForeignKey(Status, default = 'UNS', on_delete = models.CASCADE) # do I need to specify the default here too, or just in the class? #[toggle from one of the established choices, default='UN']
    notes = models.TextField(help_text = 'e.g. why the recommender recommended it, you added it, what it covers, details such as price, or even what you are learning from this resource!', blank = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return str(self.text[:100]) # I changed this from what the book said

