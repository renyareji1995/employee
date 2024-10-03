from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import EmployeeForm
from myapp.models import Employee

#view for creating an employee 
#methods:GET,POST
#url=>localhost:8000/employee/add/

class EmployeeCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=EmployeeForm()

        return render(request,'employee_add.html',{'form':form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            # Employee.objects.create(
            #     name=data.get('name'),
            #     designation=data.get('designation'),
            #     department=data.get('department'),
            #     salary=data.get('salary'),
            #     contact=data.get('contact'),
            #     address=data.get('address')
            # )


            #OR

            Employee.objects.create(**data)  #dictionary unpacking it is used only when the column nane in models is exactly same as in form class

            return redirect('employee-list')
        
        else:

            return render(request,'employee_add.html',{'form':form_instance})
        


class EmployeeListView(View):

    def get(self,request,*args,**kwargs):

        form_instance=Employee(request.POST)

        data=Employee.objects.all()

        return render(request,'employee_list.html',{'employees':data})



#employee detail view

class EmployeeDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id)

        return render(request,'employee_detail.html',{'employee':qs})

 #employee deletew view   
class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Employee.objects.get(id=id).delete()

        return redirect('employee-list')
    

class EmployeeUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        emp_obj=Employee.objects.get(id=id)

        emp_dictionary={
            "name":emp_obj.name,
            "designation":emp_obj.designation,
            "department":emp_obj.department,
            "salary":emp_obj.salary,
            "contact":emp_obj.contact,
            "address":emp_obj.address
        }

        form_instance=EmployeeForm(initial=emp_dictionary)

        return render(request,"employee_edit.html",{'form':form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            id=kwargs.get("pk")

            Employee.objects.filter(id=id).update(**data)

            return redirect('employee-list')
        
        else:

            return render(request,"employee_edit.html",{'form':form_instance})



  



