from django import forms

class EmployeeForm(forms.Form):

    name=forms.CharField()

    designation=forms.CharField()

    department=forms.CharField()

    salary=forms.IntegerField()

    contact=forms.CharField()

    address=forms.CharField()

    
    def clean(self):

        cleaned_data=super().clean()

        salary=cleaned_data.get("salary")

        if int(salary)<15000 or int(salary)>100000:

            error_message="salary should above 15000 and less than 1000000"

            self.add_error("salary",error_message)


        
