from django import template
from main.models import *
import ast 
import qrcode , io ,base64
from django.contrib import messages

register = template.Library()

@register.simple_tag
def register_post(name, dob , gender,email, password,number,address,p_email, role ,p1_number,p2_name,p2_address,p2_email,p2_password,p2_number):
   if role == 'teacher':
      Teacher.objects.create(name=name, email=email, password=password) 
   if role == 'student':
      Student.objects.create(name=name, email=email, password=password , gender = gender, phone_number = number , dob = dob , address = address , parent = Parent.objects.get(parent_1_email = p_email) , school = School.objects.get(name = 'St Cyres')) 
   if role == 'parent':
      Parent.objects.create(parent_1_name = name , parent_1_email = email, password1 = password, parent_1_phone = p1_number , parent_1_address = address , parent_2_name = p2_name , parent_2_email = p2_email , password2 = p2_password , parent_2_phone = p2_number, parent_2_address = p2_address)
    
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

@register.simple_tag
def process_cart(cart,student):
   try:
      stud = Student.objects.get(student_id = student)
      crt = Menu.objects.get(menu_id = cart)
      stud.reserves = crt.item_name
      print("std :" + stud.reserves + " std name:" + stud.name)
   except Exception as e:
      print(e)
   