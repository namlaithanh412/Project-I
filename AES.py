import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class AESCipherGCM:
    def __init__(self, key=None):
        self.key = key if key else get_random_bytes(32)

    def encrypt(self, plaintext: str) -> dict:
        """
       Ma hoa van ban thanh ban ma.
        """
        data_to_encrypt = plaintext.encode('utf-8')
        
        cipher = AES.new(self.key, AES.MODE_GCM)
        
        ciphertext, tag = cipher.encrypt_and_digest(data_to_encrypt)
        
        return {
            'nonce': base64.b64encode(cipher.nonce).decode('utf-8'),
            'ciphertext': base64.b64encode(ciphertext).decode('utf-8'),
            'tag': base64.b64encode(tag).decode('utf-8')
        }

    def decrypt(self, encrypted_dict: dict) -> str:
        """
        Giai du lieu
        """
        try:
            nonce = base64.b64decode(encrypted_dict['nonce'])
            ciphertext = base64.b64decode(encrypted_dict['ciphertext'])
            tag = base64.b64decode(encrypted_dict['tag'])
            
            cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce)
            
            decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
            
            return decrypted_data.decode('utf-8')
            
        except ValueError as e:
            return f"Loi giai ma: {e}"
        except KeyError:
            return "Loi do thieu thanh phan (nonce, ciphertext, or tag)."


if __name__ == "__main__":

    aes_system = AESCipherGCM()
    
    print(f"Khoa bi mat (Base64): {base64.b64encode(aes_system.key).decode('utf-8')}\n")

    message = "Mat khau la: jjffors67"
    print(f"Van ban goc: {message}")

    encrypted_data = aes_system.encrypt(message)
    print("\n--- KQ ma hoa ---")
    print(f"Nonce (IV):   {encrypted_data['nonce']}")
    print(f"Ciphertext:   {encrypted_data['ciphertext']}")
    print(f"Tag (MAC):    {encrypted_data['tag']}")

    decrypted_message = aes_system.decrypt(encrypted_data)
    print(f"\n--- KQ giai ma ---")
    print(f"Van ban phuc hoi: {decrypted_message}")