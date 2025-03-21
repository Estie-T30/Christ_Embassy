from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


# Create your views here.
def list_students(request):
    all_students = Student.objects.all()
    # return render(request, 'Students/all_students.html', {'all_students': all_students})
    return render(request, 'Students/new_template.html', {'all_students': all_students})

def retrieve_student(request, id_from_the_web):
    Students = Student.objects.get(id=id_from_the_web)
    return render(request, 'Students/one_student.html', {'Students': Students})

# def create_student(request):
#     return render(request, 'Students/create_student.html',)

# def create_student(request):
#     form = StudentForm()
#     return render(request, 'Students/create_student.html', {'form': form})

def create_student(request):
    if request.method == "GET":
        form = StudentForm()
    else:
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() #save the form to the database
        return redirect("Students/")
    return render(request, "students/create_student.html", {'form': form})




