from django import template
from main.models import *
import ast 
import qrcode , io ,base64
from django.contrib import messages

register = template.Library()

@register.simple_tag
def register_post(name, email, password, role):
    if role == 'teacher':
        Teacher.objects.create(name=name, email=email, password=password) 
    if role == 'student':
        Student.objects.create(name=name, email=email, password=password) 
@register.simple_tag
def view_data(student_id):
    try:
        student = Student.objects.get(student_id = student_id)  # Access the student profile linked to the authenticated user
        qr = qrcode.make(str(student_id))
        buffer = io.BytesIO()
        qr.save(buffer, format='PNG')
        image_data = buffer.getvalue()
        image_data_base64 = base64.b64encode(image_data).decode()
        return image_data_base64
    except Exception as e:
        return e


@register.simple_tag
def fetch_data(decoded_text):
    try:
        student = Student.objects.get(id = int(decoded_text))
        return student
    except Exception as e:
        return decoded_text
@register.simple_tag
def get_menu():
   x = []
   for i in Menu.objects.all():
      x.append(i)
   return x

@register.simple_tag
def get_balance():
   x = []
   for i in Balance.objects.all():
      x.append(i)
   return x

@register.simple_tag
def get_date():
   x = []
   for i in Balance.objects.all():
      for j in ast.literal_eval(i.transaction_history):
         x.append(j[0])     
   return x

@register.simple_tag
def get_price():
   x = []
   for i in Balance.objects.all():
         for j in ast.literal_eval(i.transaction_history):
            x.append(format(j[2],".2f"))     
   return x

@register.simple_tag
def get_history_items():
   x = []
   for i in Balance.objects.all():
         for j in ast.literal_eval(i.transaction_history):
            x.append(j[1])     
   return x

@register.simple_tag
def get_sDetails():
   x = []
   for i in Student.objects.all():
      x.append(i)
   return x

