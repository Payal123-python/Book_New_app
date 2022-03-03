from django.shortcuts import redirect, render
from book.models import Book
from django.http import HttpResponse
import traceback

# Create your views here.

import logging

logger = logging.getLogger("django")

def homepage(request): 
    if request.method == "POST":
        if not request.POST.get("bid"):
            book_name = request.POST["bname"] 
            book_price = request.POST["bprice"]
            book_qty = request.POST["bqty"]
            Book.objects.create(name=book_name, price=book_price, qty=book_qty)
            return redirect("homepage")
        else:
            bid = request.POST.get("bid")
            book_obj = Book.objects.get(id = bid)
            book_obj.name = request.POST["bname"]
            book_obj.price = request.POST["bprice"]
            book_obj.qty = request.POST["bqty"]
            book_obj.save()
            return redirect("homepage")

    elif request.method == "GET":    
        return render(request,template_name="home.html")      
           
def show_all_books(request):     
    logger.info("In Homepage")
    all_books = Book.objects.all()
    logger.info("all_books")
    data = {"books": all_books}
    return render(request, "show_books.html", context=data)   

def edit_data(request,id):       
    book = Book.objects.get(id=id)
    return render(request,template_name="home.html",context={"single_book":book})    

def delete_data(request, id):
    if request.method == "POST":
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as err_msg:
            traceback.print_exc()  
            return HttpResponse(f"Book Does not exist for ID:- {id}")
        else:
            book.delete()
        return redirect("show_all_books")
    else:
        return HttpResponse(f"Request method: {request.method} Not allowed..! Only POST method is allowed")  

def delete_all_data(request):
    if request.method == "GET":
       all_books = Book.objects.all()
       data = {"books": all_books}
       return render(request,"delete_all_books.html",context = data)
    elif request.method == "POST":
        all_books = Book.objects.all().delete()
        data = {"books": all_books}
        return redirect("homepage")  

def soft_delete(request,id):
    if request.method == "GET":
        book = Book.objects.filter(is_active = False)
        book.delete()
        return redirect("show_all_books")
    elif request.method == "POST":
        return HttpResponse("Error")      


from book.forms import StudentForm
 
# Create your views here.
def form_home(request):
    context ={'form':StudentForm()}
    return render(request, "form_home.html", context)











               
# def soft_delete_single(request,id):
#     if request.method == "POST":
#         book_obj = Book.objects.get(id = id)
#         Book_restore.name =  book_obj.name
#         Book_restore.price = book_obj.price
#         Book_restore.qty = book_obj.qty
#         soft_delete_single.objects.create(name=book_name, price=book_price, qty=book_qty)   
#         book_obj.delete()
#         return HttpResponse("soft delete")         
      