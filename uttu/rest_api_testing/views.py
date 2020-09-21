from django.shortcuts import render
import requests

# Create your views here.

def rest_api_testing(request):
    #response = requests.get('http://freegeoip.net/json/')
    client_ip = request.META['REMOTE_ADDR']

    response = requests.get('http://ip-api.com/json/{}'.format(client_ip))
    geodata = response.json()
    template_name='rest_api_testing/home.html'
    return render(request, template_name, {
        'ip': geodata['query'],
        #'country': geodata['country']

        #https://ip-api.com/docs/api:json chech the field from here

    })
