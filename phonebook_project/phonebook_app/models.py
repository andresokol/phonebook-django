from django.db import models


class Person(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)

    age = models.IntegerField()
    city = models.CharField(max_length=200)

    def __str__(self):
        return (
            f"{self.last_name}, {self.first_name}, "
            f"{self.age} y.o., {self.city}"
        )
