from django.shortcuts import render, redirect
from home.forms import PlayerForm
from home.models import Player


# def home(request):
#     form = PlayerForm()
#     players = Player.objects.all()
#     if request.method == "POST":
#         form = PlayerForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, './templates/home.html', {'form':form, 'players':players})

from django.views import View

class HomeView(View):

    def get(self, request):
        form = PlayerForm()
        players = Player.objects.all()
        return render(request, './templates/home.html', {'form':form, 'Players':players})
    
    def post(self, request):
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')


from django.views.generic.base import TemplateView, RedirectView

class AboutView(TemplateView):

    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Something Else"
        return context

class PreRedirectView(RedirectView):

    pattern_name = 'home:about'

    def get_redirect_url(self, *args, **kwargs):
        print("Customize here")
        return super().get_redirect_url(*args, **kwargs)

from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

class PlayerDetailView(DetailView):

    template_name='detail.html'
    #queryset = Player.objects.all()

    def get_object(self):
        idx = self.kwargs.get("pk")
        return get_object_or_404(Player, id=idx)


from django.views.generic.list import ListView

class PlayerListView(ListView):

    model = Player 
    template_name = "lists.html"  
    context_object_name = "Players"
    paginate_by = 1

    def get_queryset(self):
        queryset = Player.objects.filter(first_name="Lionel")
        return queryset

class NationView(ListView):
    model = Player 
    template_name = "lists.html"  
    context_object_name = "Players"
    paginate_by = 1

    def get_queryset(self):
        queryset = Player.objects.filter(nationality=self.kwargs.get("nationality"))
        return queryset

from django.views.generic.edit import FormView

class AddView(FormView):
    template_name = "add_player.html"
    form_class = PlayerForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


from django.views.generic.edit import CreateView

class CreatePlayerView(CreateView):
    model = Player
    template_name = "add_player.html"
    form_class = PlayerForm
    success_url = '/'

from django.views.generic.edit import UpdateView

class EditPlayerView(UpdateView):
    model = Player
    template_name = "add_player.html"
    form_class = PlayerForm
    success_url = '/'
