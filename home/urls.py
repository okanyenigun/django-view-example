from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, RedirectView
import home.views as hv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', hv.AboutView.as_view(),name='about'),
    path('redirect/', hv.PreRedirectView.as_view(), name='redirect'),
    path('', hv.HomeView.as_view(), name='home'),
    path('<int:pk>/',hv.PlayerDetailView.as_view(), name='detail'),

    path('lists/', hv.PlayerListView.as_view(), name="player-list"),
    path('lists/<str:nationality>', hv.NationView.as_view(), name="nation"),

    # path('add/', hv.AddView.as_view(), name='add'),
    path('add/', hv.CreatePlayerView.as_view(), name='add'),
    path('<int:pk>/edit',hv.EditPlayerView.as_view(), name='edit'),
    # path("redirect/",RedirectView.as_view(url='https://www.google.com/?client=safari'), name='redirect-to-google')

]
