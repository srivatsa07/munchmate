from openai import OpenAI
from django.conf import settings
from main.models import FoodSubmission

def simulate_conversations():
    openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)
    question =( 
        "Imagine you are a international food enthusiast, List your top 3 favourite foods as a comma-separated line. "
        "Do NOT pick common items Be as creative and diverse as possible with max_length=255 characters for complete output."
        "Then on the next line, classify the list as vegan, vegetarian, or other. "
        "Please reply in this format:\n "   
        "foods: food1, food2, food3\n"
        "type: vegan/vegetarian/other"
    )
    for i in range(100):
        messages = [{"role": "user", "content": question}]
        response = openai_client.chat.completions.create(
            model="gpt-4o", messages=messages, temperature=1.3, frequency_penalty=1, presence_penalty=1
        )
        answer = response.choices[0].message.content.strip()
        foods, type_ = None, None

        # Parse the response
        for line in answer.splitlines():
            if line.lower().startswith("foods:"):
                foods = line.partition(":")[2].strip()
            if line.lower().startswith("type:"):
                type_ = line.partition(":")[2].strip().lower()
        foods = foods or ""
        type_ = type_ or "other"

        FoodSubmission.objects.create(foods=foods, type=type_)
