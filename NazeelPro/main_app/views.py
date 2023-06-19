from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from service_app.models import SubService , MainService
import json
import openai
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def home(request:HttpRequest):
    """Rendering the home page template"""
    services = MainService.objects.all()[:3]
    return render(request,'main_app/home.html',{"services":services})

def history(request:HttpRequest):
    return render(request,'main_app/history.html')

def services(request:HttpRequest):
    return render(request,'main_app/services.html')

def about(request:HttpRequest):
    return render(request,'main_app/about.html')

def order(request:HttpRequest,main_services_id):
    sub_services_all = SubService.objects.all()
    main_services = MainService.objects.get( id = main_services_id )
    sub_service = SubService.objects.filter(main_service=main_services)
    total_price = 0

    if request.method == 'POST':
        selected_items = request.POST.getlist('selected_items')

        for item_id in selected_items:
            sub_service = SubService.objects.get(id=item_id)
            quantity = int(request.POST.get(f'quantity_{item_id}', 1))

            total_price += sub_service.price * quantity

    context = {
        'sub_service': sub_service,
        'total_price': total_price,
        'sub_service_all':sub_services_all,
        'main_service':main_services,
    }

    return render(request, 'main_app/order.html', context)


def maps(request:HttpRequest):
    return render(request,'main_app/maps.html')



def chatbot(request):
            if request.method == 'POST':
                data = json.loads(request.body)
                clean_data = list(data.values())

                # Remove leading and trailing whitespace from each value
                clean_data = [value.strip() for value in clean_data]

                # Access the clean text or join the values together
                clean_text = ' '.join(clean_data)
                user_input = request.POST.get('message')
                print(clean_text)
                # Define the chatbot's responses for different questions
                responses = {
                    'hi': 'Hello! How can I assist you today?',
                    'hello': 'Hello! How can I assist you today?',
                    'check in time': 'The check-in time is at 3:00 PM.',
                    'check out time': 'The check-out time is at 11:00 AM.',
                    'breakfast': 'Yes, we offer complimentary breakfast for all guests.',
                    'parking': 'Yes, we have free parking available for our guests.',
                    'wifi': 'Yes, we provide free Wi-Fi access in all rooms and public areas.',
                    'room service': 'Yes, we offer 24-hour room service.',
                    'pool': 'Yes, we have an outdoor pool for guests to enjoy.',
                    'gym': 'Yes, we have a fully equipped gym available for guests to use.',
                    'thank you': 'You\'re welcome! If you have any more questions, feel free to ask.',
                    'bye': 'Goodbye! Have a great day!'
                    }

                responses_more={
                    'restaurant': 'Yes, we have an on-site restaurant that serves breakfast, lunch, and dinner.',
                    'room types': 'We offer a variety of room types including standard rooms, suites, and deluxe rooms.',
                    'amenities': 'Our hotel amenities include a spa, concierge service, business center, and laundry facilities.',
                    'pet-friendly': 'Yes, we are a pet-friendly hotel. Additional charges may apply.',
                    'cancellation policy': 'Our cancellation policy allows free cancellation up to 24 hours before check-in.',
                    'local attractions': 'Some popular local attractions near our hotel include museums, parks, and shopping centers.',
                    'nearest airport': 'The nearest airport is XYZ Airport, located approximately 10 miles away from our hotel.',
                    'special offers': 'We have special offers and packages available. Please visit our website for more details.',
                }

                # Check if the user's message matches any of the predefined questions
                if clean_text in responses :
                    return JsonResponse({'response': responses[clean_text]})
                elif clean_text in responses_more:
                    return JsonResponse({'response': responses_more[clean_text]})

                # If the user's message doesn't match any predefined questions, provide a default response
                return JsonResponse({'response': 'I\'m sorry, I couldn\'t understand your question. Please try again.'})

            return render(request, 'main_app/chatbot.html')


