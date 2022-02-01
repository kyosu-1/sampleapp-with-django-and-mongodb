from djongo import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.EmbeddedField(model_container=Author)
