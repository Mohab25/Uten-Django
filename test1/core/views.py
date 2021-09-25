from django.shortcuts import render
from django.db.models import Q
from .models import *


def validate(param):
    """
    as there is a repetition with the validation proccess, takes the form of 
    if title_contains!='' and title_contains is not None:
    ..
    elif id_exact!='' and id_exact is not None: 
    .. 
    hence this method is to shortcut that repetition 
    """
    return param!='' and param is not None

def BootstrapForm(request):
    categories = JournalCategory.objects.all()
    title_contains = request.GET.get('title contains')
    id_exact = request.GET.get('id exact')
    author_or_category = request.GET.get('author or category')
    min_count = request.GET.get('min count')
    max_count = request.GET.get('max count')
    publish_date_min = request.GET.get('publish date min')
    publish_date_max = request.GET.get('publish date max')
    cats_query = request.GET.get('Categories')
    review = request.GET.get('reviewed')
    queryset = ''

    if validate(title_contains):
        queryset = Journal.objects.filter(title__icontains=title_contains)
        Ob = Journal.objects.get(id=7)  # this means that id begins with 5.
        print(Ob.title)
    elif validate(id_exact):
        queryset = Journal.objects.filter(id__exact=id_exact)
        
    elif validate(author_or_category):
        queryset = Journal.objects.filter(Q(author__name__icontains=author_or_category)|Q(category__name__icontains=author_or_category)).distinct() 

    if validate(min_count):
        queryset = Journal.objects.filter(views__gte=min_count)
    
    if validate(max_count):
        queryset = Journal.objects.filter(views__lt=max_count)

    if validate(publish_date_min):
        queryset = Journal.objects.filter(publish_date__gte=publish_date_min)
    if validate(publish_date_max):
        queryset = Journal.objects.filter(publish_date__lt=publish_date_max)
    
    if validate(cats_query):
        queryset = Journal.objects.filter(category__name__iexact=cats_query)

    if review=='on':
        queryset = Journal.objects.filter(reviewed=True)
    elif review =='off':
        queryset.GET.get(reviewed=False)
    
    context = {'qs1':queryset,'cats':categories}
    return render(request,'boot_form.html',context)