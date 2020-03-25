from django.shortcuts import render
from covid import Covid
from django.contrib import messages

def listall(request):
    template='listdata.html'
    covid=Covid()
    data=covid.get_data()
    context={
            'data':data,
        }   
    city=request.GET.get("q")
    if city:
        try:
            sdata=covid.get_status_by_country_name(city)
            print(data)
            context={'sdata':sdata,}
        except StopIteration:
            messages.info(request, 'Invalid Country Name...')
                
    return render(request,template,context)

def searchdata(request):
    pass



