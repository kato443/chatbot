from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import re
import requests
from bs4 import BeautifulSoup
from .models import UCUQuestion, StudentService

from .models import UCUQuestion, StudentService
from django.db.models import CharField, TextField # Import these if you want to add the keyword field
from django.db.models.functions import Lower

def get_bot_response(user_query):
    # Normalize the user's query
    user_query = user_query.lower()
    query_words = set(user_query.split())

    # Search for keyword matches in your database
    for q_obj in UCUQuestion.objects.all():
        # Get the keywords from the database or generate them on the fly
        saved_keywords = set(q_obj.question.lower().split())

        # Find the number of matching keywords
        common_words = query_words.intersection(saved_keywords)
        
        # If a significant number of keywords match, return the answer
        if len(common_words) >= 2: # You can adjust this threshold
            return q_obj.answer

    # ... (rest of the code, including web scraping and fallback)



    # 3. Handle simple, general conversational queries
    if 'hello' in user_query or 'hi' in user_query:
        return "Hello! I am your UCU Student Assistant. How can I help you today? You can ask me about admissions, academic programs, or student services."
    
    if 'thank you' in user_query or 'thanks' in user_query:
        return "You're welcome! Feel free to ask if you have more questions."
    if 'my results' in user_query or 'my marks' in user_query:
        return 'Thank you for asking contact your lecturer or Academic Registrar'
    if 'How do i register for new semester' in user_query or 'how to apply online' in user_query:
        return "Registration is done both online through the Alpha platform and at the Academic Office. You must complete your registration process within the first two weeks of the semester to receive credit for your courses."
    if 'Where can I get counseling services' in user_query or 'counselling services' in user_query:
        return "The university offers Counselling and Guidance services to help students with academic, personal, and social challenges. Their office is located on campus and you can schedule an appointment."

    if 'How do I access my results?' in user_query or 'access my result' in user_query:
        return "You can access your academic results by logging into your student account on the Alpha platform. Results are released after all fees for the semester have been cleared."
    # 4. Fallback response if no match is found
    return "I'm sorry, I don't have information on that. Please try rephrasing your question or visit the official UCU website for more help."


def chatbot_home(request):
    """
    Renders the main HTML page for the chatbot.
    """
    return render(request, 'student_chatbot/index.html')

@csrf_exempt
def chatbot_api(request):
    """
    Handles the POST requests from the front-end to get a chatbot response.
    It takes the user's message and returns the chatbot's answer as a JSON response.
    The @csrf_exempt decorator is used to bypass Django's CSRF protection for this API endpoint.
    """
    if request.method == 'POST':
        data = request.POST
        user_message = data.get('message', '')
        bot_response = get_bot_response(user_message)
        return JsonResponse({'message': bot_response})
    
    # Return an error message for any request method other than POST
    return JsonResponse({'message': 'This endpoint only accepts POST requests.'})

def home_page(request):
    """
    Renders the home page of the website.
    """
    return render(request, 'student_chatbot/home.html')

def about_page(request):
    """
    Renders the about page of the website.
    """
    return render(request, 'student_chatbot/about.html')    