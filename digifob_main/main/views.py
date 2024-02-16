from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from .models import Student,Teacher,Menu,Balance,School,YearForm
from django.shortcuts import render
from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from .templatetags.tags import register_post
from django.contrib import messages
from django.http import HttpResponseNotAllowed, HttpResponse
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from .models import *
import qrcode
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from django.urls import reverse_lazy
import ast
@csrf_exempt
def process_qr_code(request):
    if request.method == 'POST':
        decoded_text = request.POST.get('decoded_text')
        student = Student.objects.get(id = int(decoded_text))
        student =  [student.name,student.email]
        return JsonResponse({'status': 'success', 'message': json.dumps(student) })
    else:
        return JsonResponse({'status': 'error'})
     

@require_http_methods(['POST'])
def register_1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        register_post(name, email, password, role)
        return redirect(reverse('index')) # Redirect to a success page after successful registration

    return redirect(reverse('register'))


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        
        if role == 'teacher':
            try:
                user = Teacher.objects.get(email=email)
                if user.password == password:
                    messages.success(request, "Login successful")
                    return redirect(reverse('teachers', kwargs={'user_id': user.teacher_id}))
                else:
                    messages.error(request, "Wrong password")
            except ObjectDoesNotExist:
                messages.error(request, "Email does not exist")
        
        elif role == 'student':
            try:
                user = Student.objects.get(email=email)
                if user.password == password:
                    messages.success(request, "Login successful")
                    request.session['student_id'] = user.student_id
                    return redirect(reverse('student_detail'))
                else:
                    messages.error(request, "Wrong password")
            except ObjectDoesNotExist:
                messages.error(request, "Email does not exist")
        elif role == 'parent':
            try:
                user = Parent.objects.get(parent_1_email=email)
                if user.password1 == password:
                    messages.success(request, "Login successful")
                    return redirect(reverse('parents', kwargs={'user_id': user.parent_id}))
                else:
                    messages.error(request, f"Wrong password {user.password1},{password}")
            except ObjectDoesNotExist:
                try:
                    user = Parent.objects.get(parent_2_email=email)
                    if user.password2 == password:
                        messages.success(request, "Login successful")
                        return redirect(reverse('parents', kwargs={'user_id': user.id}))
                    else:
                        messages.error(request, f"Wrong password {user.password2},{password}")
                except ObjectDoesNotExist:
                    messages.error(request, "Email does not exist")

    return redirect(reverse('index'))


def update_amount(request):
   if request.method == 'POST':
       amount = Decimal(request.POST.get('money'))
       obj = Balance.objects.get(student=1)
       obj.balance += amount
       obj.save()
   return render(request, "C:\\Users\\jayap\\Documents\\GitHub\\Digifob-Mark-0\\digifob_mk_0\\main\\templates\\main\\pages\\qTopUp\\qTopUp.html")


@csrf_exempt
def process_qr_code(request):
    if request.method == 'POST':
        decoded_text = request.POST.get('decoded_text')
        student = Student.objects.get(id = int(decoded_text))
        student =  [student.name,student.email]
        return JsonResponse({'status': 'success', 'message': json.dumps(student) })
    else:
        return JsonResponse({'status': 'error'})
     
def student_detail(request):

    student = get_object_or_404(Student, pk=request.session.get('student_id'))
    return render(request, 'C:\\Users\\jayap\\Documents\\GitHub\\Digifob-Main-Mk1\\digifob_main\\main\\templates\\main\\students\\students.html', {'student': student})

def balance(request):
    student_id = request.session.get('student_id')
    if student_id is not None:
        try:
            balance_obj = Balance.objects.get(student_id=student_id)
            balance = balance_obj.balance
            history = balance_obj.transaction_history
            price = []
            for j in ast.literal_eval(history):
                price.append(format(j[2],".2f"))     
            dates = []
            for j in ast.literal_eval(history):
                    dates.append(j[0])
            items = []
            for j in ast.literal_eval(history):
                items.append(j[1])     
            return render(request, 'C:\\Users\\jayap\\Documents\\GitHub\\Digifob-Main-Mk1\\digifob_main\\main\\templates\\main\\pages\\balance\\balance.html', {'balance': balance,'history' : history,'dates':dates,'items':items,'price':price})
        except Balance.DoesNotExist:
            messages.error(request, "No balance found for the student.")
            return redirect(reverse('index'))
    else:
        messages.error(request, "You must be logged in to view your balance.")
        return redirect(reverse('index'))