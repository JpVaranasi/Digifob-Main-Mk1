from django.db import models
from django.core.validators import EmailValidator , RegexValidator
from django.contrib.auth.models import User
# Create your models here.

def validate_email(value):
    allowed_domain = "stcyres.org"
    if not value.endswith('@' + allowed_domain):
        raise models.ValidationError("Email must end with @{}".format(allowed_domain))

class Parent(models.Model):
    parent_id = models.AutoField(primary_key=True)
    parent_1_name = models.CharField(max_length = 50 , null = False, blank = False)
    parent_1_email = models.EmailField(validators = [EmailValidator] , null = False, blank = False)
    password1 = models.CharField(max_length = 50, blank = False , null = False)
    parent_1_phone = models.CharField(max_length = 10, blank = False , null = False)
    parent_1_address = models.CharField(max_length = 100 , null = False, blank = False)
    parent_2_name = models.CharField(max_length = 50 , null = False, blank = False)
    parent_2_email = models.EmailField(validators = [EmailValidator] , null = False, blank = False)
    password2 = models.CharField(max_length = 50, blank = False, null = False)
    parent_2_phone = models.CharField(
        max_length = 13,
        blank = False,
        null = False,
        validators = [
            RegexValidator(
                regex= r'^\+44\d{10}$',
                message="Phone numbers must start with +44 and have 10 digits."
                )
            ]
        )
    parent_2_address = models.CharField(max_length = 100 , null = False, blank = False)   
    def __str__(self):
        return self.parent_1_name
class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 30 , null = False, blank = False)
    address = models.CharField(max_length = 100 , null = False, blank = False)
    def __str__(self):
        return self.name
  
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key= True)
    name = models.CharField(max_length = 50 , null = False, blank = False)
    email = models.EmailField(validators = [EmailValidator()] , null = False, blank = False)
    password = models.CharField(max_length = 50, blank = False, null = False)
    phone_number = models.CharField(
        max_length = 13,
        blank = False,
        null = False,
        validators = [
            RegexValidator(
                regex= r'^\+44\d{10}$',
                message="Phone numbers must start with +44 and have 10 digits."
            )
        ]
        )
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50 , null = False, blank = False)
    dob = models.DateField(null = False, blank = False)
    gender_choices = [('M','Male'),("F","Female"),("O","Other")]
    gender = models.CharField(max_length = 1 , choices = gender_choices , null = False, blank = False)
    email = models.EmailField(validators = [EmailValidator(),validate_email] , null = False, blank = False)
    password = models.CharField(max_length = 50, blank = False, null = False)
    phone_number = models.CharField(
        max_length = 13,
        blank = False,
        null = False,
        validators = [
            RegexValidator(
                regex= r'^\+44\d{10}$',
                message="Phone numbers must start with +44 and have 10 digits."
            )
        ]
        )
    address = models.CharField(max_length = 100 , null = False, blank = False)
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE, related_name = "students")
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class YearForm(models.Model):   
    name = models.CharField(max_length = 10 , blank = False, null = False)
    head_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    def __str__(self):
        return self.name
class Balance(models.Model):
    balance = models.DecimalField(max_digits = 5 , decimal_places = 2)
    transaction_history = models.TextField()
    student = models.OneToOneField(Student, on_delete = models.CASCADE, primary_key = True)
    def __str__(self):
        return self.student.name + "'s balance"

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length = 30, blank = False, null = False)
    price = models.DecimalField(max_digits = 5 , decimal_places = 2 , null = False, blank = False)
    ingredients = models.TextField(null = False, blank = False)
    dietary_information = models.TextField(null = False, blank = False)
    def __str__(self):
        return self.item_name

