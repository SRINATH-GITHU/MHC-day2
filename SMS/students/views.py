from django.shortcuts import render,get_object_or_404,redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request,"student_list.html",{'students':students})


def student_add(request):
    if request.method == 'POST':
        # Extract data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        grade = request.POST.get('grade')
        address = request.POST.get('address')
        
         # Create a new student
        Student.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        date_of_birth=date_of_birth,
        grade=grade,
        address=address
        )
        # Redirect to the student list after saving
        return redirect('student-list')
 # If GET request, render the form
    return render(request, 'student_form.html')


def student_edit(request, pk):
 # Fetch the student by primary key (ID)
   student = get_object_or_404(Student, pk=pk)
   if request.method == 'POST':
       student.first_name = request.POST.get('first_name')
       student.last_name = request.POST.get('last_name')
       student.email = request.POST.get('email')
       student.date_of_birth = request.POST.get('date_of_birth')
       student.grade = request.POST.get('grade')
       student.address = request.POST.get('address')
       student.save() # Save changes to the database
       return redirect('student-list')
   return render(request, 'student_form.html', {'student': student})


def student_delete(request, pk):
 # Fetch the student by primary key (ID)
   student = get_object_or_404(Student, pk=pk)
   if request.method == 'POST':
       student.delete() # Delete the student record
       return redirect('student-list')
   return render(request, 'student_confirm_delete.html', {'student': student})