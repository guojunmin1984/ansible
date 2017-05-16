from django.shortcuts import render
import os
# Create your views here.
def index(request):
    return render(request,"index.html")




def playbook(request):
    if request.method == "POST":
        ip = request.POST.get("ip")
        ip_list=ip.split()
        temp = "\n".join(ip_list)
        f = open("/export/servers/Ultron/ultron_test/ghosts","w")
        f.write(temp)
        f.close()
        result = playbook_api.pb()
        return render(request,"result.html",{'result': result})


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))