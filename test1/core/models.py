from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name 

class JournalCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name 

class Journal(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ManyToManyField(JournalCategory)
    publish_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    reviewed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title