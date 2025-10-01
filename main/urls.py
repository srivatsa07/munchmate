from django.urls import path
from .views import chat_view, veggie_vegan_api, home_view, simulate_conversations_view, veggie_vegan_table

urlpatterns = [
    path('', chat_view, name='chat'),
    # path('chat/', chat_view, name='chat'),
    path('api/veggie-vegan/', veggie_vegan_api, name='veggie_vegan_api'),
    path('veggie-vegan/table/', veggie_vegan_table, name='veggie_vegan_table'),
    path("simulate/", simulate_conversations_view, name="simulate_conversations"),
]
