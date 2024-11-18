from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from pages.getResponse import get_response

@csrf_exempt
def AskBot(request):
  if request.method == 'POST':
    try:
      # Parse JSON data from the request body
      data = json.loads(request.body)
      response = get_response(data.get("prompt",""))
      
      return JsonResponse({'message': 'Data received', 'response': response})
        
    except json.JSONDecodeError:
      return JsonResponse({'error': 'Invalid JSON data'}, status=400)
  else:
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

# Create your views here.
def home(request):
  return render(request, "1.html")