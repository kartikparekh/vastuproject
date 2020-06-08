from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404
from django.db.models import Q 
# Create your views here.
from django.shortcuts import render, redirect, reverse
from .models import Property_Information,PropertyImage
from marketing.models import Subscription
from django.core.mail import send_mail
from vastu import settings
from django import http
from django.template import loader
def search(request):
    query_set = Property_Information.objects.all()
    
    loc = request.GET.get('location')
    # furnish = request.GET.get('furnish')
    ptype = request.GET.get('ptype')
    types = request.GET.get('type')
    bhk = request.GET.get('bhk')

    #TODO: SSearch form to be done
    
    if loc and types and ptype and bhk:
        query_set = query_set.filter(
            Q(location__icontains=loc) &
            Q(property_type__exact=ptype) &
            # Q(furnishing__exact=furnish) &
            Q(status__exact=types) &
            Q(BHK__exact=bhk) 
        )
    
    
    context = {
        'queryset':query_set,
    }
    return render(request,'search_results.html',context)

def index(request):
    latest = Property_Information.objects.order_by('-timestamp')[0:3]
    property_list = Property_Information.objects.all()
    paginator = Paginator(property_list,3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    if request.method == "POST":
        email = request.POST["email"]
        new_subscription = Subscription()
        new_subscription.email = email
        new_subscription.save()

    context = {
        'latest': latest,
        "queryset":paginated_queryset,
        "page_request_var":page_request_var,
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html',{})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = loader.get_template('email_content.txt')
        context = {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message,
        }
        content = template.render(context)

        send_mail(
            subject,
            content,
            email,
            ['receiver_email@gmail.com'],
            fail_silently=False
        )
        print(email)

        return redirect(reverse('contact'))
    return render(request, 'contact.html',{})

def properties(request):
    property_list = Property_Information.objects.all()
    paginator = Paginator(property_list,6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        "queryset":paginated_queryset,
        "page_request_var":page_request_var,
    }
    return render(request, 'property-grid.html',context)

def property_detail(request,id):
    propertY = get_object_or_404(Property_Information, id=id)
    photos = PropertyImage.objects.filter(propertY=propertY)
    context = {
        'propertY':propertY,
        'photos':photos,
    }
    return render(request, 'property-single.html',context)
