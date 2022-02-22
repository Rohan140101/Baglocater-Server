from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from baglocater.models import Credentials, AddLostAndFound
import json

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def index(request):
    return HttpResponse('Server for baglocater')
    pass

@csrf_exempt
def authenticate(request):
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        username = received_json_data['username']
        password = received_json_data['password']
        try:
            cred = Credentials.objects.get(username=username, password=password)
        except Credentials.DoesNotExist:
            return JsonResponse({'success': 'false'}, status=status.HTTP_404_NOT_FOUND)

    return JsonResponse({"success": "true"})

@csrf_exempt
def addLostAndFound(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        name = received_json_data['name']
        email = received_json_data['email']
        flightNumber = received_json_data['flightNumber']
        phoneNumber = received_json_data['phoneNumber']
        baggageNumber = received_json_data['baggageNumber']
        departureAirport = received_json_data['departureAirport']
        arrivalAirport = received_json_data['arrivalAirport']
        departureDate = received_json_data['departureDate']
        arrivalDate = received_json_data['arrivalDate']
        try:
            print("Inside")
            alaf = AddLostAndFound.objects.create(name=name, email=email, flightNumber=flightNumber, phoneNumber=phoneNumber, baggageNumber=baggageNumber, departureAirport=departureAirport, arrivalAirport=arrivalAirport, departureDate=departureDate, arrivalDate=arrivalDate)
        except:
            return JsonResponse({'success': 'false'})
    return JsonResponse({"success": "true"})

@csrf_exempt
@api_view(['GET', 'POST'])
def decode(request):
    if request.method == 'POST':
        encoded_string = request.data
        encoded_string = encoded_string['data']
        encoded_string = encoded_string.replace('$',',')
        encoded_string = '{' + encoded_string + '}'
        codes = eval(encoded_string)
        encoded_text = codes["encoded_text"]
        codes.pop('encoded_text')
        # print(encoded_text)
        reverse_map = {v: k for k, v in codes.items()}
        def decode(encoded_text):
            current_code = ""
            decoded_text = ""

            for bit in encoded_text:
                current_code += bit
                if(current_code in reverse_map):
                    decoded_text += reverse_map[current_code]
                    current_code = ""

            return decoded_text


        def convert_dict(decoded_text):
            decoded_data = {}
            key = ""
            value = ""
            flag = 0

            for char in decoded_text:
                if(flag == 0):
                    if(char != '='):
                        key += char
                    else:
                        flag = 1
                        continue

                if(flag == 1):
                    if(char != ';'):
                        value += char
                    else:
                        flag = 0
                        decoded_data[key] = value
                        key = ""
                        value = ""

            return decoded_data


        def decompress(encoded_text):
            decoded_text = decode(encoded_text)
            decoded_data = convert_dict(decoded_text)
            return decoded_data

        decoded_string = decompress(encoded_text)
        decoded_string_list = []
        decoded_string_list.append(decoded_string)
        print(decoded_string_list)
        responseData = decoded_string
        # return JsonResponse(decoded_string_list, safe=False)
        return Response(decoded_string)
