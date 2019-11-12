from django.shortcuts import render, redirect
from app.models import Movie, Showing, Ticket
from datetime import datetime
from app.forms import NewTicketForm

# Create your views here.


def home(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {"movies": movies})


def new_ticket(request, id):
    movie = Movie.objects.get(id=id)
    form = NewTicketForm(request.POST)
    if request.method == "GET":
        return render(request, "new_ticket.html", {"movie": movie, "form": form})
    elif request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            showing_id = form.cleaned_data["showing_id"]
            new_ticket = Ticket.objects.create(
                name=name, purchased_at=datetime.now(), showing_id=showing_id
            )
            new_ticket.save()
            return redirect("ticket_detail", new_ticket.id)
        else:
            return render(request, "new_ticket.html", {"movie": movie, "form": form})


def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, "ticket_detail.html", {"ticket": ticket})
