from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class AESCipher(object):

    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = key + "*"*(24 - len(key))
        print(self.key)

    def aesencrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = "qwertyuioplkjhgf".encode()
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode("utf-8").strip())
        print(len(b64encode(iv + encrypted_text).decode("utf-8")))
        return b64encode(iv + encrypted_text).decode("utf-8")

    def aesdecrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        print(number_of_bytes_to_pad)
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]
