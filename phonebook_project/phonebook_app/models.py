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

    class Meta:
        ordering = ["-last_name", "-first_name"]
        verbose_name = "Человек из засписной книжки"
        verbose_name_plural = "Люди"


class Account(models.Model):
    account_slug = models.SlugField(unique=True)
    amount = models.IntegerField(default=0)
    person_name = models.CharField(max_length=200)

    def __str__(self):
        return (
            f"{self.person_name} ({self.account_slug}): "
            f"{self.amount} денег"
        )
