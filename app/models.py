from django.db import models


class UserInfo(models.Model):
    TYPE_CHOICES = [
        ('student',  'Student'),
        ('employee', 'Employee'),
    ]
    class UserInfo(models.Model):
        COURSE_CHOICES = [

    ]

    name    = models.CharField(max_length=100)
    email   = models.EmailField()
    phone   = models.CharField(max_length=15)
    type    = models.CharField(max_length=10, choices=TYPE_CHOICES)
    message = models.TextField()
    course  = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name       = models.CharField(max_length=80)
    email      = models.EmailField()
    phone      = models.CharField(max_length=15)
    message    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table  = "contact"
        ordering  = ["-created_at"]

    def __str__(self):
        return f"{self.name} – {self.email}"
