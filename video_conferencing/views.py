from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .aes_encryption import *

import random
import string

# Create your views here.

key = "abcd"

attendees = {}

def home_page(request, room_id, user_name, randomKey):
    if user_name in attendees and randomKey == attendees[user_name]:
        return HttpResponse("Cannot Access The Meet Link")
    else:
        attendees.update({user_name : randomKey})

    return render(request, 'video_conferencing/home.html', {'room_id':room_id, 'user_name':user_name})


class MeetingUrl(View) :

    def get(self, request, room_id, user_name) :
        encrypterObj = AESCipher(key)

        url_path = request.path
        refined_url_path = "meet/" + url_path[5:]   # removing /api/ and prepending meet/

        randomKey = ''.join(random.choice(string.ascii_letters) for i in range(5))
        refined_url_path = refined_url_path + randomKey
        encrypted_path = encrypterObj.aesencrypt(refined_url_path)
        encrypted_url = "127.0.0.1:8000/" + encrypted_path
        decrypted_url = "127.0.0.1:8000/" + encrypterObj.aesdecrypt(encrypted_path)

        return JsonResponse({"url" : encrypted_url, "decrypted_url" : decrypted_url}, safe=False)
