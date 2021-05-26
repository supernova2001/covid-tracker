from django.shortcuts import render
# Create your views here.
import requests
import json
import csv
import requests
from .models import Oxygen
from .models import Pharmacy
url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
testing_centers="https://covid-19india-api.herokuapp.com/v2.0/helpline_numbers"
headers = {
    'x-rapidapi-key': "a2754a286fmsh4e95bc3d869543dp1940dfjsnd36ee6367523",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers).json()
def showView(request):
    display=response['state_wise']
    states=response['state_wise'].keys()
    L=[]
    list_of_districts=[]
    answer=''
    districts=''
    selectedstate=''
    India=response['total_values']
    for item in states:
        L.append(display[item])
    if(request.method=='POST'):
        selectedstate=request.POST['selectedstate']
        answer=display[selectedstate]
        districts=answer['district']
        for district in districts:
            list_of_districts.append(district)
        for name in list_of_districts:
            print(districts[name]['active'])
        lastupdated=answer['lastupdatedtime'].split(" ")
    context={'India': India,'statename':selectedstate,'output': states,'display':L,'states':display,'answer':answer,'final': list_of_districts,'naam': districts}
    return render(request,'index.html',context)

def OxygenView(request):
    details=Oxygen.objects.all()
    detailsofoxygen={'details':details}
    return render(request,'oxygen.html',detailsofoxygen)

def SubmitOxygen(request):
    if(request.method=='POST'):
        leadname = request.POST["leadname"]
        agencyname=request.POST["agencyname"]
        agencyaddress=request.POST["agencyaddress"]
        agencyphone=request.POST["agencynumber"]
        verified = request.POST["vertification"]
        ins=Oxygen(leadname=leadname,agencyname=agencyname,agencyaddress=agencyaddress,agencyphone=agencyphone,verified=verified)
        ins.save()
        print("The Data has been uploaded")
    return render(request,'oxygenform.html')

def Pharmacies(request):
    pharmacylist=Pharmacy.objects.all()
    context={'pharmacylist': pharmacylist}
    return render(request,'pharmacies.html',context)





        
