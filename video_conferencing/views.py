from django.shortcuts import render\
from django.http import JsonResponse
from django.views import View
from .aes_encryption import *

# Create your views here.

key = "abcd"


def home_page(request, room_id, user_name):
    return render(request, 'video_conferencing/home.html',{'room_id':room_id, 'user_name':user_name})


class APIResponse(View) :

    def get(self, request, room_id, user_name) :
        encrypterObj = AESCipher(key)
        url_path = request.path
        refined_url_path = "meet/" + url_path[5:]   # removing /api/ and prepending meet/
        encrypted_path = encrypterObj.aesencrypt(refined_url_path)
        encrypted_url = "127.0.0.1:8000/" + encrypted_path
        decrypted_url = "127.0.0.1:8000/" + encrypterObj.aesdecrypt(encrypted_path)
        return JsonResponse({"url" : encrypted_url, "decrypted_url" : decrypted_url}, safe=False)
