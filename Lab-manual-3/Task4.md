Got it! Let’s go **step by step** for Task 4 on **padding**, including commands, explanation, and expected observations. I’ll make it fully report-ready.

---

# **CSE-478 Task 4: Padding in Block Ciphers**

---

## **Step 1: Create a Plaintext File**



2. Write Example (20 bytes):

```
This is 20 bytes!!
```


---

## **Step 2: Choose a Cipher and Key/IV**

```bash
openssl rand -hex 16  
openssl rand -hex 16  
```

Example:

* Key: `00112233445566778899aabbccddeeff`
* IV: `0102030405060708090a0b0c0d0e0f10`

---

## **Step 3: Encrypt Using Different Modes**

### **ECB Mode**

```bash
openssl enc -aes-128-ecb -in padding.txt -out ciphertext_ecb.bin -K 00112233445566778899aabbccddeeff
```

* **ECB requires padding** because AES is a block cipher and plaintext length (20 bytes) is not a multiple of 16.
* OpenSSL **automatically uses PKCS#7 padding** by default.

---

### **CBC Mode**

```bash
openssl enc -aes-128-cbc -in padding.txt -out ciphertext_cbc.bin -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10
```

* CBC also **requires padding** for the same reason.
* OpenSSL adds PKCS#7 padding automatically.

---

### **CFB Mode**

```bash
openssl enc -aes-128-cfb -in padding.txt -out ciphertext_cfb.bin -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10
```

* **CFB is a stream cipher mode**: it encrypts smaller units (bytes) individually.
* **Does NOT require padding** because it can handle plaintext of any length.

---

### **OFB Mode**

```bash
openssl enc -aes-128-ofb -in padding.txt -out ciphertext_ofb.bin -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10
```

* OFB is also a stream cipher mode.
* **Does NOT require padding** because it encrypts plaintext byte by byte.

---

## **Step 4: Decrypt to Verify**

### **ECB Mode**

```bash
openssl enc -d -aes-128-ecb -in ciphertext_ecb.bin -out decrypted_ecb.txt -K 00112233445566778899aabbccddeeff
```

### **CBC Mode**

```bash
openssl enc -d -aes-128-cbc -in ciphertext_cbc.bin -out decrypted_cbc.txt -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10
```

### **CFB Mode**

```bash
openssl enc -d -aes-128-cfb -in ciphertext_cfb.bin -out decrypted_cfb.txt -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10
```

### **OFB Mode**

```bash
openssl enc -d -aes-128-ofb -in ciphertext_ofb.bin -out decrypted_ofb.txt -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10
```

* All decrypted files should match the original plaintext.

---

## **Step 5: Observations**

| **Mode** | **Requires Padding?** | **Reason**                                                       |
| -------- | --------------------- | ---------------------------------------------------------------- |
| ECB      | Yes                   | AES is block-based; plaintext not multiple of 16 → padding added |
| CBC      | Yes                   | AES is block-based; padding needed to fill last block            |
| CFB      | No                    | Stream mode; can encrypt partial blocks byte-by-byte             |
| OFB      | No                    | Stream mode; can encrypt partial blocks byte-by-byte             |

---

## **Step 6: Explanation**

1. **Block cipher modes (ECB, CBC):**

   * Encrypt full blocks only. If plaintext length ≠ multiple of block size, padding is added.
   * OpenSSL uses **PKCS#7 padding** automatically.

2. **Stream cipher modes (CFB, OFB):**

   * Operate on **smaller units than the block** (e.g., bytes).
   * Can encrypt any plaintext length without padding.

**Key takeaway:**

* **ECB/CBC → padding required**
* **CFB/OFB → padding not required**

