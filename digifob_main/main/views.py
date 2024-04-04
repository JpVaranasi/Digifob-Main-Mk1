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
import datetime
import matplotlib.pyplot as plt
import io 
import base64
from collections import Counter , defaultdict

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
        if request.POST.get('role') == 'student':
            name = request.POST.get('s_name')
            email = request.POST.get('s_email')
            password = request.POST.get('s_password')
            role = request.POST.get('role')
            dob = request.POST.get('s_dob')
            gender = request.POST.get('s_gender')
            number = request.POST.get('s_number')
            address = request.POST.get('s_address')
            p_email = request.POST.get('p_email')

            register_post(name = name, dob = dob , gender = gender,email = email, password = password ,number = number,address = address,p_email = p_email, role = role)
            return redirect(reverse('index')) # Redirect to a success page after successful registration
        if request.POST.get('role') == 'teacher':
            name = request.POST.get('t_name')
            email = request.POST.get('t_email')
            password = request.POST.get('t_password')
            role = request.POST.get('role')
            number = request.POST.get('t_number')
            register_post(name,email, password,number, role)
            return redirect(reverse('index'))
        if request.POST.get('role') == 'parent':
            name = request.POST.get('p1name')
            email = request.POST.get('p1email')
            password = request.POST.get('p1password')
            role = request.POST.get('role')
            p1_number = request.POST.get('p1number')
            address = request.POST.get('p1address')
            p2_name = request.POST.get('p2name')
            p2_email = request.POST.get('p2email')
            p2_password = request.POST.get('p2password')
            role = request.POST.get('role')
            p2_number = request.POST.get('p2number')
            p2_address = request.POST.get('p2address')
            register_post(name = name ,email = email, password = password ,p1_number = p1_number,address = address,role = role,p2_name = p2_name,p2_address = p2_address,p2_email = p2_email,p2_password = p2_password,p2_number = p2_number)
            return redirect(reverse('index'))
     
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
                    request.session['teacher_id'] = user.teacher_id
                    return redirect(reverse('teachers'))
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
                    request.session['parent_id'] = user.parent_id
                    return redirect(reverse('parents'))
                else:
                    messages.error(request, f"Wrong password {user.password1},{password}")
            except ObjectDoesNotExist:
                try:
                    user = Parent.objects.get(parent_2_email=email)
                    if user.password2 == password:
                        messages.success(request, "Login successful")
                        request.session['parent_id'] = user.parent_id
                        return redirect(reverse('parents'))
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
   return render(request,"C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\qTopUp\\qTopUp.html")


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
    
def payNow(request):
    student = get_object_or_404(Student, pk=request.session.get('student_id'))
    return render(request, 'C:\\Users\\jayap\\Documents\\GitHub\\Digifob-Main-Mk1\\digifob_main\\main\\templates\\main\\pages\\payNow\\payNow.html', {'student': student})

def qTopUp(request):
    student = get_object_or_404(Student, pk=request.session.get('student_id'))
    return render(request, 'C:\\Users\\jayap\\Documents\\GitHub\\Digifob-Main-Mk1\\digifob_main\\main\\templates\\main\\pages\\qTopup\\qTopUp.html', {'student': student})
    
def parents(request):
    parents = get_object_or_404(Parent, pk=request.session.get('parent_id'))
    return render(request, 'C:\\Users\\jayap\\Documents\\GitHub\\Digifob-Main-Mk1\\digifob_main\\main\\templates\\main\\parents\\parents.html', {'parent': parents})
    
def teachers(request):
    teachers = get_object_or_404(Teacher, pk=request.session.get('teacher_id'))
    return render(request, 'C:\\Users\\jayap\\Documents\\GitHub\\Digifob-Main-Mk1\\digifob_main\\main\\templates\\main\\schools\\schools.html', {'teacher': teachers})
def manageP(request):
    parents = get_object_or_404(Parent, pk=request.session.get('parent_id'))
    students = (Student.objects.filter(parent = Parent.objects.get( parent_id = request.session.get('parent_id'))))
    students = list(students)
    return render(request, 'C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\manage(P)\\manageP.html', {'parent': parents, 'student':students})
   
def reserve(request):
    student = get_object_or_404(Student, pk=request.session.get('student_id'))
    return render(request, 'C:\\Users\\jayap\\Documents\\GitHub\\Digifob-Main-Mk1\\digifob_main\\main\\templates\\main\\pages\\reserve\\reserve.html', {'student': student})

    
@csrf_exempt
def delete_student(request, student_id):
    if request.method == 'DELETE':
        try:
            student = Student.objects.get(student_id=student_id)
            student.delete()
            return JsonResponse({'status': 'success', 'message': 'Student deleted successfully'})
        except Student.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Student not found'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
@csrf_exempt
def delete_menu_item(request, menu_id):
    if request.method == 'DELETE':
        try:
            item = Menu.objects.get(menu_id = menu_id)
            item.delete()
            return JsonResponse({'status': 'success', 'message': 'Student deleted successfully'})
        except Student.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Student not found'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
      
def manageS(request):
    teacher = get_object_or_404(Teacher, pk=request.session.get('teacher_id'))
    students = []
    for student in Student.objects.all():
        if Student.objects.filter(school = teacher.school):
            students.append(student)
    return render(request,'C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\manage(S)\\manageS.html', {'student':students})

def sDetails(request):
    teacher = get_object_or_404(Teacher, pk=request.session.get('teacher_id'))
    if YearForm.objects.get(head_teacher = teacher):
        print(YearForm.objects.get(head_teacher = teacher).students)
        return render(request,"C:\\Users\\jayap\\Documents\\GitHub\\DIGIFOB-MAIN-MK1\\digifob_main\\main\\templates\\main\\pages\\sDetails\\sDetails.html",{"form":YearForm.objects.filter(head_teacher = teacher)})
def sDetailsEditor(request,student_id):
    return render(request , 'C:\\Users\\jayap\\Documents\\GitHub\\Digifob-Main-Mk1\\digifob_main\\main\\templates\\main\\pages\\sDetails\\sDetailsEditor.html',{'student_id':student_id})

@require_http_methods(['POST'])
def editDetails(request):
    if request.method == "POST":
            id = request.POST.get('id')
            name = request.POST.get('s_name')
            email = request.POST.get('s_email')
            number = request.POST.get('s_number')
            address = request.POST.get('s_address')
            student = Student.objects.get(student_id = id)
            try:
                student.name = name
                student.email = email
                student.phone_number = number
                student.address = address
            except Exception:
                pass
# forms
#


@csrf_exempt
def process_qr_code(request):
    if request.method == 'POST':
        decoded_text = request.POST.get('decoded_text')
        student = Student.objects.get(student_id = int(decoded_text))
        return JsonResponse({'status': 'success', 'message': "Now serving: " + student.name })
    else:
        return JsonResponse({'status': 'error'})
     
@csrf_exempt
def submit_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cart_items = data.get('cart_items', [])
        student_id = data.get('student_id', None)

        if not student_id:
            return JsonResponse({'success': False, 'message': 'Student ID is missing.'})

        try:
            student = Student.objects.get(student_id=student_id)
            balance = Balance.objects.get(student=student)
            total_amount = sum(item['price'] for item in cart_items)

            if balance.balance < total_amount:
                return JsonResponse({'success': False, 'message': 'Insufficient balance.'})

            try:
                transaction_history = json.loads(balance.transaction_history)
            except json.JSONDecodeError:
                transaction_history = []
            new_transaction = [datetime.datetime.now().strftime('%d/%m/%y'), [item['name'] for item in cart_items], total_amount]
            transaction_history.append(new_transaction)
            balance.balance -= total_amount
            balance.transaction_history = json.dumps(transaction_history)
            balance.save()

            # Here you can add logic to save the order details, if needed

            return JsonResponse({'success': True, 'message': 'Order submitted successfully.'})
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Student not found.'})
        except Balance.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Balance not found for the student.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})

     
@csrf_exempt
def reserve_order(request):
    if request.method == 'POST':
        print('hello')
        data = json.loads(request.body)
        cart_items = data.get('cart_items', [])
        student_id = data.get('student_id', None)
        date = data.get('time')
        print(date)
        if not student_id:
            return JsonResponse({'success': False, 'message': 'Student ID is missing.'})

        try:
            student = Student.objects.get(student_id=student_id)
            balance = Balance.objects.get(student=student)
            total_amount = sum(item['price'] for item in cart_items)

            if balance.balance < total_amount:
                return JsonResponse({'success': False, 'message': 'Insufficient balance.'})

            try:
                transaction_history = json.loads(balance.transaction_history)
            except json.JSONDecodeError:
                transaction_history = []
            new_transaction = [datetime.datetime.now().strftime('%d/%m/%y'), [item['name'] for item in cart_items], total_amount]
            transaction_history.append(new_transaction)
            balance.balance -= total_amount
            balance.transaction_history = json.dumps(transaction_history)
            balance.save()
            try:
                reserve = json.loads(student.reserves)
            except json.JSONDecodeError:
                reserve = []
            new_reserves = [date, [item['name'] for item in cart_items], total_amount]
            reserve.append(new_reserves)
            student.reserves = json.dumps(reserve)
            student.save()
            # Here you can add logic to save the order details, if needed

            return JsonResponse({'success': True, 'message': 'Order submitted successfully.'})
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Student not found.'})
        except Balance.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Balance not found for the student.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def plot_graph2():
    dataset = []
    balance = Balance.objects.all()
    for i in balance:
        for j in ast.literal_eval(i.transaction_history):
            dataset.append(j)
    food_items = [food for sublist in [data[1] for data in dataset] for food in sublist]
    food_item_counts = Counter(food_items)
    # Plot the bar chart
    plt.bar(food_item_counts.keys(), food_item_counts.values())
    plt.xlabel('Item')
    plt.ylabel('Frequency')
    plt.title('Frequency of Items')
    plt.xticks(rotation=45)
    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()  # Close the plot to prevent it from being displayed
    return image_base64

def plot_graph():
    dataset = []
    balance = Balance.objects.all()
    for i in balance:
        for j in ast.literal_eval(i.transaction_history):
            dataset.append(j)

    # Extract dates and purchase amounts
    dates = [datetime.datetime.strptime(data[0], "%d/%m/%y").strftime("%b") for data in dataset]
    purchase_amounts = [data[2] for data in dataset]

    # Calculate the average purchase amount per month
    monthly_averages = defaultdict(list)
    for date, amount in zip(dates, purchase_amounts):
        monthly_averages[date].append(amount)
    average_purchase_amounts = {month: sum(amounts) / len(amounts) for month, amounts in monthly_averages.items()}

    # Plot the scatter plot of purchase amounts
    plt.scatter(dates, purchase_amounts, label='Purchase Amount')

    # Plot the average line
    plt.plot(list(average_purchase_amounts.keys()), list(average_purchase_amounts.values()), color='r', linestyle='--', label='Average Purchase Amount')

    plt.xlabel('Month')
    plt.ylabel('Purchase Amount')
    plt.title('Total Purchase Amount by Month')
    plt.xticks(rotation=45) # Rotate the x-axis labels for better readability
    plt.legend()
    plt.tight_layout()

    # Convert the plot to a base64-encoded string
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close() # Close the plot to prevent it from being displayed

    return image_base64
def stats(request):
    image_base64 = plot_graph()
    image_base642 = plot_graph2()

    return render(request, 'main/pages/stats/stats.html', {'image_base64': image_base64 , 'image_base642' : image_base642})

