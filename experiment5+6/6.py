from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# 读取第一篇文章
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(
    current_dir,
    "articles",
    "article_1.txt"
)

with open(file_path, "r", encoding="utf-8") as f:
    plaintext = f.read()
   

# AES密钥（16字节）
key = b"1234567890abcdef"

# 创建加密器
cipher = AES.new(key, AES.MODE_ECB)

# 加密
encrypted_bytes = cipher.encrypt(
    pad(plaintext.encode("utf-8"), AES.block_size)
)

# 转Base64方便显示
ciphertext = base64.b64encode(encrypted_bytes).decode()

print("======原文======")
print(plaintext[:200])

print("\n======密文======")
print(ciphertext[:200])

# 解密
decrypt_cipher = AES.new(key, AES.MODE_ECB)

decrypted = unpad(
    decrypt_cipher.decrypt(
        base64.b64decode(ciphertext)
    ),
    AES.block_size
)

print("\n======解密结果======")
print(decrypted.decode("utf-8")[:200])