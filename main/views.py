from django.shortcuts import render, redirect
from .forms import ChatForm
from .services import ask_favorite_foods
from .models import FoodSubmission 
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib import messages
from .utils import simulate_conversations

def home_view(request):
    return HttpResponse('Welcome! Try /chat/ or /api/veggie-vegan/')


def chat_view(request):
    response = None
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            FoodSubmission.objects.create(foods=user_input)
            response = ask_favorite_foods(user_input)
    else:
        form = ChatForm()
    return render(request, "main/chat.html", {"form": form, "response": response})

def veggie_vegan_api(request):
    queryset = FoodSubmission.objects.filter(type__in=["vegan", "vegetarian"])
    results = []
    for submission in queryset:
        results.append({
            "foods": submission.foods,
            "type": submission.type,
            "submitted_at": submission.submitted_at,
        })
    return JsonResponse({"users": results})



def veggie_vegan_table(request):
    entries = FoodSubmission.objects.filter(type__in=["vegan", "vegetarian"]).order_by("-submitted_at")
    return render(request, "main/veggie_vegan_table.html", {"entries": entries})



def simulate_conversations_view(request):
    if request.method == "POST":
        simulate_conversations()
        messages.success(request, "100 conversations saved!")
        return redirect("/")

