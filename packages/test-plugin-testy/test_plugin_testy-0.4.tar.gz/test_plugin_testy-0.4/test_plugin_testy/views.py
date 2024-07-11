from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import UploadFileForm

class UploadFileFormView(View):
    form_class = UploadFileForm
    template_name = 'upload_form.html'  # Указание пути к шаблону

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # Save the file or handle it as needed
            return redirect(reverse('plugin_example:upload-success'))
        return render(request, self.template_name, {'form': form})


class UploadSuccessView(View):
    template_name = 'upload_success.html'  # Указание пути к шаблону

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
