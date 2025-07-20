# Create your models here.

from django.db import models
import random
import string

# def generate_registration_number():
#     return 'REG' + ''.join(random.choices(string.digits, k=6))

def generate_registration_number():
    last_student = Admission.objects.order_by('-registration_number').first()
    if last_student and last_student.registration_number.isdigit():
        next_number = int(last_student.registration_number) + 1
    else:
        next_number = 500000
    return str(next_number).zfill(6)


def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

class Admission(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    address = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    class_to_admit = models.CharField(max_length=20)


    registration_number = models.CharField(max_length=6, unique=True, editable=False)
    # registration_number = models.CharField(max_length=10, unique=True, editable=False)
    password = models.CharField(max_length=50, editable=False)

    def save(self, *args, **kwargs):
        if not self.registration_number:
            self.registration_number = generate_registration_number()
        if not self.password:
            self.password = generate_password()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
