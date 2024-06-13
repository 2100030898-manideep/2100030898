import requests
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from collections import deque
import time
import logging
from .config import AUTH_TOKEN, sliding_windows

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# URLs to fetch different types of numbers from the test server
NUMBER_API_ENDPOINTS = {
    'p': 'http://20.244.56.144/test/primes',
    'f': 'http://20.244.56.144/test/fibo',
    'e': 'http://20.244.56.144/test/even',
    'r': 'http://20.244.56.144/test/rand'
}

@method_decorator(csrf_exempt, name='dispatch')
class NumberAPIView(View):

    def get(self, request, number_type):
        if number_type not in NUMBER_API_ENDPOINTS:
            return JsonResponse({'error': 'Invalid number type'}, status=400)

        start_time = time.time()
        api_url = NUMBER_API_ENDPOINTS[number_type]

        try:
            headers = {
                'Authorization': f'Bearer {AUTH_TOKEN}'
            }
            api_response = requests.get(api_url, headers=headers, timeout=0.5)
            api_response.raise_for_status()  # Raise an exception for HTTP errors
            received_numbers = api_response.json().get('numbers', [])
        except requests.RequestException as error:
            logger.error(f"API request failed: {error}")
            return JsonResponse({'error': 'Failed to fetch numbers from API'}, status=500)

        # Store previous state of the window
        previous_window_state = list(sliding_windows[number_type])
        for number in received_numbers:
            if number not in sliding_windows[number_type]:
                sliding_windows[number_type].append(number)

        current_window_state = list(sliding_windows[number_type])
        average = sum(current_window_state) / len(current_window_state) if current_window_state else 0

        response_data = {
            "numbers": received_numbers,
            "windowPrevState": previous_window_state,
            "windowCurrState": current_window_state,
            "avg": average
        }

        # Ensure the response is sent within 500 milliseconds
        elapsed_time = time.time() - start_time
        if elapsed_time > 0.5:
            return JsonResponse({'error': 'Response time exceeded 500 ms'}, status=500)

        return JsonResponse(response_data)
