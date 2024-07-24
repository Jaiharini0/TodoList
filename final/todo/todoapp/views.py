from django.http import HttpResponse
from django.shortcuts import render,redirect
from todoapp.models import Task

# Create your views here.

def index(request):
    return render(request,"index.html")

def list(request):
    return render(request,"list.html")

def delete(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('list')

def update(request,id):
    if request.method=='POST':

        Taskname=request.POST.get('Taskname', '')
        Description=request.POST.get('Description', '')
        completed=request.POST.get('completed','')
        task=Task.objects.get(id=id)
        task.Taskname=Taskname
        task.Description=Description
        task.completed=completed
        task.save()
        return redirect('/')
    
    else:
        items=Task.objects.get(id=id)
        return render(request,"completed.html",{'items':items})
    




def lists(request):
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
# def lists(request):
#      return HttpResponse("""<html>
#      <script>
#             function closeForm(){
              
#               document.getElementById("Myform").style.display="none";
#                 document.getElementById("Cards").style.display="block";

             
#             }
            
#            </script>
#      </html> """
#      )         

    # return redirect('planner_today')

def planner_today(request):
    return render(request,"planner_today.html")

def planner_tomorrow(request):
    return render(request,"planner_tomorrow.html")

def completed(request):
    return render(request,"completed.html")


def list(request):

   task = Task.objects.all()

   return render(request,'list.html',{'task':task})

def planner_today(request):

   task = Task.objects.all()

   return render(request,"planner_today.html",{'task':task})

def planner_today(request):
    
    if request.method == 'POST':

        Taskname=request.POST.get('Taskname', '')
        Description=request.POST.get('Description', '')

       
        new_task=Task(Taskname=Taskname,Description=Description)
        new_task.save()
            
        
    return render(request,"planner_today.html",{})

