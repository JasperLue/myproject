from django.shortcuts import render
def index(request):
	List = map(str,range(100))
	return render(request,'index.html',{'List':List})
# Create your views here.
