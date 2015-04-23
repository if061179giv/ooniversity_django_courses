# -*- coding: utf_8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from students.models import Students


class MessageMixin(object):
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MessageMixin, self).delete(request, *args, **kwargs)


def contact(request):
    return render(request, 'contact.html')


class StudentsListView(ListView):
    model = Students

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Students.objects.filter(course=course_id)
        else:
            students = Students.objects.all()
        return students


class StudentsDetailView(DetailView):
    model = Students


class StudentsCreateView(SuccessMessageMixin, CreateView):
    model = Students
    success_url = reverse_lazy('student_list')
    success_message = u"Студент %(first_name)s %(surname)s был успешно создан"


class StudentsUpdateView(SuccessMessageMixin, UpdateView):
    model = Students
    success_url = reverse_lazy('student_list')
    template_name_suffix = '_update_form'
    success_message = u"Информация о студенте %(first_name)s %(surname)s была успешно обновлена"


class StudentsDeleteView(MessageMixin, DeleteView):
    model = Students
    success_url = reverse_lazy('student_list')
    success_message = u"Студент был успешно удален"