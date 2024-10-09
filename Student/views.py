
from .forms import StudentModelForm
from .models import Student
from django.contrib import messages
from django.views.generic import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.translation import gettext_lazy,gettext as _
from django.utils import translation


# CreateStudent
# @method_decorator(csrf_exempt,name='dispatch')
class UserAddStudent(CreateView):
    template_name='home.html'
    form_class=StudentModelForm
    
    # success_url='/ar/'
    def get_success_url(self):
        current_language = translation.get_language()
        if current_language == 'ar':
            return '/ar/'
        elif current_language == 'en':
            return '/en/'
        else:
            return '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Student.objects.all()
        return context
    def form_valid(self, form):
        messages.add_message(self.request,messages.SUCCESS,'you add new student successfully')
        return super().form_valid(form)
    

#Delete Student

class DeleteStudent(DeleteView):
    model=Student
    template_name='confirm_delete.html'
    pk_url_kwarg='id'
    success_url='/'
    def form_valid(self, form):
        messages.warning(self.request,'you delete the student successfully')
        return super().form_valid(form)

# Update Student

class UpdateStudent(UpdateView):
    model=Student
    form_class=StudentModelForm
    template_name='update.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('add')
    def form_valid(self, form):
        messages.add_message(self.request,messages.SUCCESS,'you Update new student successfully')
        return super().form_valid(form)
    

