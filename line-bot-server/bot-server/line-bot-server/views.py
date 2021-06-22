import json
import requests
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, StickerMessage
 
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser       = WebhookParser(settings.LINE_CHANNEL_SECRET)


def get_gym_capacity():
    url = 'https://ntusportscenter.ntu.edu.tw/counter.txt'
    r   = requests.get(url)
    if r.status_code == requests.codes.ok:
        r = json.loads(r.text)
        capacity = r['CounterData'][0]['innerCount'].split(';')[0]
        print(capacity)
        return f'體育館人數：{capacity}'
    else:
        return 'error occurs when fetch the data'


"""
Normally when you make a request via a form you want the form being submitted to your view to originate from your website and not come from some other domain. 
To ensure that this happens, you can put a csrf token in your form for your view to recognize. 
If you add @csrf_exempt to the top of your view, then you are basically telling the view that it doesn't need the token. 
This is a security exemption that you should take seriously.
"""
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
    
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent) or isinstance(event, StickerMessage):
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=get_gym_capacity())
                )
        return HttpResponse()
    else:
        return HttpResponse()
