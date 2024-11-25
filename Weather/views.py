from django.shortcuts import render,HttpResponse,redirect
import requests


# Create your views here.

def weather_info(request):
    if request.method == "POST":
        api_key = "60e71ef363261de7d092343233068828"
        city = request.POST.get('cityname')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Data is successfully retrieved
            content = {
                'city': city,
                'temperature': f"{data['main']['temp']} K",
                'weather': data['weather'][0]['description'],
                'style': "display: block;",  # Show weather details
            }
            return render(request, 'index.html', content)
        else:
            # Handle error from API
            content = {
                'error': data.get('message', 'An error occurred'),
                'style': "display: none;",  # Hide weather details
            }
            return render(request, 'index.html', content)

    # Default context for GET requests
    content = {
        'style': "display: none;",  # Hide weather details
    }
    return render(request, 'index.html', content)