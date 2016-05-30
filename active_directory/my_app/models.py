from django.db import models
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=100)

    # when we print the class we get a text instead a value in the memory
    def __str__(self):
        return self.user_name


class Emails(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    email1 = models.EmailField(max_length=100, null=False, blank=False)
    email2 = models.EmailField(max_length=100, null=True, blank=True)

    # when we print the class we get a text instead a value in the memory
    def __str__(self):
        return self.email1


class Phones(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    phone1 = models.EmailField(max_length=100, null=False, blank=False)
    phone2 = models.EmailField(max_length=100, null=True, blank=True)

    # when we print the class we get a text instead a value in the memory
    def __str__(self):
        return self.phone1
