from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import os

# Configuration
INPUT_FILE = "original.bmp"
KEY = get_random_bytes(16)  # AES-128 key (16 bytes)
IV = get_random_bytes(16)  # For CBC mode
HEADER_SIZE = 54  # BMP header size
CORRUPT_BYTE_INDEX = 29  # 30th byte (0-based index)
CORRUPT_BIT_POSITION = 0  # Flip the 0th bit (LSB); change 0–7 to flip other bits

def encrypt_file_ecb(input_path, output_path, key):
    with open(input_path, 'rb') as f:
        data = f.read()
    
    # Preserve header
    header = data[:HEADER_SIZE]
    plaintext = data[HEADER_SIZE:]
    
    # Pad to multiple of 16 bytes
    padded_plaintext = pad(plaintext, AES.block_size)
    
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(padded_plaintext)
    
    # Reattach header
    encrypted_data = header + ciphertext
    
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)
    
    print(f"[+] ECB encrypted: {output_path}")
    return encrypted_data

def encrypt_file_cbc(input_path, output_path, key, iv):
    with open(input_path, 'rb') as f:
        data = f.read()
    
    header = data[:HEADER_SIZE]
    plaintext = data[HEADER_SIZE:]
    padded_plaintext = pad(plaintext, AES.block_size)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_plaintext)
    
    encrypted_data = header + ciphertext
    
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)
    
    print(f"[+] CBC encrypted: {output_path}")
    return encrypted_data

def corrupt_bit(data, byte_index, bit_position):
    """Flip a specific bit in the byte at byte_index"""
    byte = data[byte_index]
    corrupted_byte = byte ^ (1 << bit_position)  # XOR to flip bit
    new_data = bytearray(data)
    new_data[byte_index] = corrupted_byte
    return bytes(new_data)

def save_corrupted_file(data, output_path):
    with open(output_path, 'wb') as f:
        f.write(data)
    print(f"[+] Corrupted file saved: {output_path}")


if not os.path.exists(INPUT_FILE):
    print(f"[-] Error: {INPUT_FILE} not found!")
    exit(1)

print(f"[*] Using key: {KEY.hex()}")
print(f"[*] Using IV : {IV.hex()}")

# Task 2: Encrypt in ECB and CBC
ecb_encrypted = encrypt_file_ecb(INPUT_FILE, "encrypted_ecb.bmp", KEY)
cbc_encrypted = encrypt_file_cbc(INPUT_FILE, "encrypted_cbc.bmp", KEY, IV)

# Task 3: Corrupt 30th byte (index 29), flip 1 bit
print(f"\n[*] Corrupting 30th byte (index {CORRUPT_BYTE_INDEX}), bit {CORRUPT_BIT_POSITION}...")

ecb_corrupted = corrupt_bit(ecb_encrypted, CORRUPT_BYTE_INDEX, CORRUPT_BIT_POSITION)
cbc_corrupted = corrupt_bit(cbc_encrypted, CORRUPT_BYTE_INDEX, CORRUPT_BIT_POSITION)

save_corrupted_file(ecb_corrupted, "encrypted_ecb_corrupted.bmp")
save_corrupted_file(cbc_corrupted, "encrypted_cbc_corrupted.bmp")

# Optional: Save key and IV for reference (not to be submitted unless allowed)
with open("encryption_info.txt", "w") as f:
    f.write(f"Key (hex): {KEY.hex()}\n")
    f.write(f"IV  (hex): {IV.hex()}\n")
    f.write(f"Corrupted byte index: {CORRUPT_BYTE_INDEX} (30th byte)\n")
    f.write(f"Corrupted bit position: {CORRUPT_BIT_POSITION}\n")

print("\n[+] All files generated:")
print("    - encrypted_ecb.bmp")
print("    - encrypted_cbc.bmp")
print("    - encrypted_ecb_corrupted.bmp")
print("    - encrypted_cbc_corrupted.bmp")
print("    - encryption_info.txt")