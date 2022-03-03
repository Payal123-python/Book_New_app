
from django import forms
from book.models import Book
 
# creating a form
class StudentForm(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())


# print(StudentForm())    

class StudentForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"