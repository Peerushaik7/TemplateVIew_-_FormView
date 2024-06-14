
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse
from app.form import *

# Create your views here.
class DataInsertByTv(TemplateView):
    template_name='DataInsertByTv.html'
    
    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        # ECDO['name']='peeru'
        # ECDO['age']=23
        # return ECDO
        
        ECDO['ECDO']=CollegeForm()
        return ECDO
    
    def post(self,request):
        CFDO=CollegeForm(request.POST)
        if CFDO.is_valid():
            CFDO.save()
            return HttpResponse('DataInsertByTv is Done')
        else:
            return HttpResponse('DataInsertByTv not done')
        
class InsertDataByFv(FormView):
    template_name='InsertDataByFv.html'
    form_class=CollegeForm
    
    def form_valid(self,form):
        form.save()
        return HttpResponse('Formview is Done Successfully')        
        