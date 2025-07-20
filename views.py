# Create your views here.

# from django.shortcuts import render
from .forms import AdmissionForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admission

def admission_view(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'admission_success.html')
    else:
        form = AdmissionForm()
    return render(request, 'admission.html', {'form': form})





def index(request):
    return render(request, "index.html")

def student_login(request):
    if request.method == "POST":
        reg_num = request.POST.get("registration_number")
        password = request.POST.get("password")
        
        try:
            student = Admission.objects.get(registration_number=reg_num)
            if student.password == password:
                request.session["student_id"] = student.id
                return redirect("student_page")
            else:
                messages.error(request, "Incorrect password")
        except Admission.DoesNotExist:
            messages.error(request, "Invalid registration number")

    return redirect("index")

def student_page(request):
    student_id = request.session.get("student_id")
    if not student_id:
        return redirect("index")
    
    student = Admission.objects.get(id=student_id)
    return render(request, "student.html", {"student": student})

def forget_password(request):
    if request.method == "POST":
        reg_num = request.POST.get("registration_number")
        new_password = request.POST.get("new_password")
        
        try:
            student = Admission.objects.get(registration_number=reg_num)
            student.password = new_password
            student.save()
            messages.success(request, "Password reset successfully!")
            return redirect("index")
        except Admission.DoesNotExist:
            messages.error(request, "Invalid registration number")
    
    return render(request, "forget_password.html")
