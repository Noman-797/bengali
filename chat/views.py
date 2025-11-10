import google.generativeai as genai
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# Simple in-memory viewer counter
VIEWER_COUNT = 0

def index(request):
    global VIEWER_COUNT
    VIEWER_COUNT += 1
    return render(request, 'chat/index.html', {'viewer_count': VIEWER_COUNT})

def get_translation_stats(request):
    """API endpoint to get translation statistics"""
    global VIEWER_COUNT
    return JsonResponse({
        'viewer_count': VIEWER_COUNT,
        'status': 'Gemini AI powered translator'
    })





@csrf_exempt
@require_http_methods(["POST"])
def chat(request):
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return JsonResponse({'error': 'Message is required'}, status=400)
        
        # Use hardcoded API key
        try:
            genai.configure(api_key='AIzaSyCHeOd0Ls1C5UZIIyHTCCkSGWf8hu1UEvY')
            model = genai.GenerativeModel('gemini-2.5-flash')
            prompt = f"""ইংরেজি/বাংলিশ টেক্সটটি হুবহু বাংলায় অনুবাদ করো। যা বলবে তাই অনুবাদ করো, নিজের মতো করে বদলাবে না। শুধু সিধা অনুবাদ।

{user_message}"""
            response = model.generate_content(prompt)
            ai_response = response.text.strip()
        except Exception as e:
            return JsonResponse({'error': f'AI translation failed: {str(e)}'}, status=500)
        
        return JsonResponse({'response': ai_response, 'status': 'success'})
        
    except Exception as e:
        return JsonResponse({'error': f'Translation error: {str(e)}'}, status=500)