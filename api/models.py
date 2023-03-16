from django.db import models


# Create your models here.
# creating company model

class Company(models.Model):
    company_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'),
                                                     ('Non-IT', 'Non-IT')
                                                     )
                            )
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# creating employee model

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(
        ('manager', 'manager'),
        ('Software Developer', 'Software Developer'),
        ('Project Leader', 'Project Leader')
    ))

    def __str__(self):
        return self.name

    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class ExternalUser(models.Model):
    user_Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    address = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
