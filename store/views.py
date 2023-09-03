
from django.shortcuts import render,redirect
from store.forms import BookShopeForm
from store.models import BookShopeModel
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.




def item_list(request):
    if request.method =='GET':
        query=request.GET.get('query')
        if query:
            post=BookShopeModel.objects.filter(book_name__icontains=query)
            #print(post)
            return render(request, 'search_result.html',{'post':post})
        else:
            #print("No Information to Show")
            #return request(request, {})
            return redirect('no_search')


def show_book(request):
    book = BookShopeModel.objects.all()
    paginator =Paginator(book,10)
    page = request.GET.get('page')
    
    paged_product = paginator.get_page(page)
    # for i in paged_product:
    #     # print(i)
    context = {'page_items': paged_product, 'data':book, 'page': paginator }
    return render(request, 'show_book.html', context)


def add_book(request):
    if request.method == 'POST':
        book = BookShopeForm(request.POST)
        if book.is_valid():
            print(book.cleaned_data)
            book.save()
            return redirect('show_book')
    else:
         book = BookShopeForm()
    return render(request, 'store.html',{'form':book})


def edit_book(request, id):
     book = BookShopeModel.objects.get(pk=id)
     form = BookShopeForm(instance=book)
     if request.method == 'POST':
        form = BookShopeForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show_book')
     return render(request, 'store.html',{'form':form})


def delete_book(request, id):
    book = BookShopeModel.objects.get(pk=id).delete()
    return redirect('show_book')


def no_search_value(request):
    return render(request, 'no_search.html')