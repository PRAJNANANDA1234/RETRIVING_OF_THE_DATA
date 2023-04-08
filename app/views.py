from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',d)

def display_odisha(request):
    LOOD=Odisha.objects.all()
    LOOD=Odisha.objects.order_by('name')
    LOOD=Odisha.objects.order_by('-name')
    LOOD=Odisha.objects.all()
    LOOD=Odisha.objects.filter(topic_name='puri')
    LOOD=Odisha.objects.exclude(topic_name='BBSR')
    LOOD=Odisha.objects.all()[1:2:]
    LOOD=Odisha.objects.all()
    LOOD=Odisha.objects.filter(name__startswith='J')
    LOOD=Odisha.objects.filter(email__endswith='.com')
    LOOD=Odisha.objects.filter(name__contains='J')
    LOOD=Odisha.objects.filter(name__in=('LINGARAJ','MAABIRAJA'))
    LOOD=Odisha.objects.filter(name__regex='[a-zA-Z]{9}')
    
    
    d={'odisha':LOOD}
    return render(request,'display_odisha.html',d)


def display_temple(request):
    LOT=Temple.objects.all()
    LOT=Temple.objects.filter(date__gt='1890-10-10')
    LOT=Temple.objects.filter(date__gte='1890-10-10')
    LOT=Temple.objects.filter(date__lt='1890-10-10')
    LOT=Temple.objects.filter(date__lte='1890-10-10')
    LOT=Temple.objects.filter(date__year='1480')
    LOT=Temple.objects.filter(date__month='6')
    LOT=Temple.objects.filter(date__day='4')
    LOT=Temple.objects.filter(date__year__gt='1840')
    LOT=Temple.objects.filter(date__month__lt='10')
    d={'temple':LOT}
    return render(request,'display_temple.html',d)