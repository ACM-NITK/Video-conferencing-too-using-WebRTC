from .aes_encryption import *


class BaseMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)  # Call process_request()
        response = self.get_response(request)
        return response


class decryptUrlMiddleware(BaseMiddleware):

    def process_request(self, request):
        print("Path Info" + request.path_info)

        checkForApiUrl = request.path_info[:5]
        print("checkForApiUrl " + checkForApiUrl)

        if (checkForApiUrl == "/api/"):
            return None

        key = "abcd"
        decrypterObj = AESCipher(key)
        url_path = request.path_info
        refined_url_path = url_path[1:]  # Removing the forward slash
        decrypted_path = decrypterObj.aesdecrypt(refined_url_path)
        refined_decrypted_path = "/" + decrypted_path

        request.path_info = refined_decrypted_path
        print("Decryption Done")
        print("Path Info" + request.path_info)
