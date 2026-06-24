def rc4_crypt(data: bytes, key: bytes) -> bytes:
    """
Ham ma hoa va giai ma
    """
    S = list(range(256)) # Tạo mảng S từ 0 đến 255
    j = 0
    key_length = len(key)
    
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        # Hoán vị S[i] và S[j]
        S[i], S[j] = S[j], S[i]


    out = bytearray()
    i = 0
    j = 0
    
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        

        S[i], S[j] = S[j], S[i]
        

        K = S[(S[i] + S[j]) % 256]
        
  
        out.append(byte ^ K)
        
    return bytes(out)


if __name__ == "__main__":
    import binascii


    secret_key = b"KhoaBimat123"
    plaintext = "Ma hoa RC4".encode('utf-8')
    
    print(f"Van ban goc: {plaintext.decode('utf-8')}")
    print(f"Khoa: {secret_key.decode('utf-8')}\n")

    ciphertext = rc4_crypt(plaintext, secret_key)
    
    hex_ciphertext = binascii.hexlify(ciphertext).decode('utf-8')
    print("--- KQ ma hoa ---")
    print(f"Ban ma (Hex): {hex_ciphertext}\n")

    decrypted_bytes = rc4_crypt(ciphertext, secret_key)
    decrypted_text = decrypted_bytes.decode('utf-8')
    
    print("--- KQ giai ma ---")
    print(f"Van ban phuc hoi: {decrypted_text}")