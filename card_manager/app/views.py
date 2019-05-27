from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, View, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Card
from .forms import CardSearchForm, CardForm, CardImageAddForm
from .plugins.google_apis import detect_text
import os
import yaml


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CardTemplateView(TemplateView):
    template_name = 'app/index.html'


class CardDetailView(DetailView):
    model = Card


class CardListView(View):

    template_name = 'app/card_list.html'

    def get(self, request, *args, **kwargs):
        object_list = Card.objects.order_by('-created_at')
        form = CardSearchForm(request.GET)
        if form.is_valid():
            company = form.cleaned_data.get('company')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            classification = form.cleaned_data.get('classification')
            if company:
                object_list = object_list.filter(company__contains=company)
            if last_name:
                object_list = object_list.filter(last_name__contains=last_name)
            if first_name:
                object_list = object_list.filter(first_name__contains=first_name)
            if classification:
                object_list = object_list.filter(card_classification__classification=classification)

        return render(request, self.template_name, {'object_list': object_list,
                                                    'form': form})


class CardUpdateView(UpdateView):
    model = Card
    form_class = CardForm
    template_name = 'app/card_update.html'
    success_url = '/card_view'


class CardDeleteView(DeleteView):
    model = Card
    form_class = CardForm
    success_url = reverse_lazy('card_view')


class CardAddView(View):
    create_form = CardForm
    image_form = CardImageAddForm
    template_name = 'app/card_image_add.html'

    def get(self, request, *args, **kwargs):
        image_form = CardImageAddForm(request.GET)

        context = {
            'image_form': image_form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        image_form = CardImageAddForm(request.POST, request.FILES)
        create_form = CardForm(request.POST, request.FILES)

        if 'create-btn' in request.POST:
            print('success')
            if create_form.is_valid():
                print('success')
                create_form.save()

                return render(request, self.template_name, {'image_form': image_form})

        elif 'image-btn' in request.POST:
            if image_form.is_valid():
                google_token = yaml.load(open(os.path.join(BASE_DIR, 'app/config/google.yaml')))
                image_text = detect_text(request.FILES['image'], google_token['token'])
                context = {
                    'create_form': create_form,
                    'image_text': image_text
                }

                return render(request, self.template_name, context)

        return render(request, self.template_name, {'image_form': image_form})


