Perfect! Let’s write the **complete step-by-step solution** for your task, including the commands, a sample hex key, IV, and explanations ready to include in your report. I’ll also highlight the expected observations.

---

# **CSE-478 Task 3: Encryption Mode – Corrupted Cipher Text**

---

## **Step 1: Create a Plaintext File**

```bash
 echo "This is a test file for AES encryption. This is a test file for AES encryption." >> plain1.txt
```

---

## **Step 2: Generate a Key and IV**

AES-128 requires:

* **Key:** 16 bytes → 128 bits → 32 hex characters
* **IV:** 16 bytes → 128 bits → 32 hex characters (for CBC, CFB, OFB)

Generate random key and IV using OpenSSL:

```bash
openssl rand -hex 16   
openssl rand -hex 16  
```

Example  use in command:

* Key: `00112233445566778899aabbccddeeff`
* IV:  `0102030405060708090a0b0c0d0e0f10`

---

## **Step 3: Encrypt the File**

### **ECB Mode**

```bash
openssl enc -aes-128-ecb -in plaintext.txt -out ciphertext_ecb.bin -K 00112233445566778899aabbccddeeff
```

### **CBC Mode**

```bash
openssl enc -aes-128-cbc -in plaintext.txt -out ciphertext_cbc.bin -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10
```

### **CFB Mode**

```bash
openssl enc -aes-128-cfb -in plaintext.txt -out ciphertext_cfb.bin -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10
```

### **OFB Mode**

```bash
openssl enc -aes-128-ofb -in plaintext.txt -out ciphertext_ofb.bin -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10
```

---

## **Step 4: Corrupt a Single Byte**

1. Open the ciphertext in a hex editor:

```bash
hexedit ciphertext_ecb.bin
```

2. Navigating to **byte 30** and flip **one bit**.

   * For example, change `2A` → `2B`.

3. Save as `ciphertext_ecb_corrupted.bin`.

4. Did same for for CBC, CFB, OFB ciphertexts.

---

## **Step 5: Decrypt the Corrupted File**

### **ECB Mode**

```bash
openssl enc -d -aes-128-ecb -in ciphertext_ecb_corrupted.bin -out decrypted_ecb.txt -K 00112233445566778899aabbccddeeff
```

### **CBC Mode**

```bash
openssl enc -d -aes-128-cbc -in ciphertext_cbc_corrupted.bin -out decrypted_cbc.txt -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10
```

### **CFB Mode**

```bash
openssl enc -d -aes-128-cfb -in ciphertext_cfb_corrupted.bin -out decrypted_cfb.txt -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10
```

### **OFB Mode**

```bash
openssl enc -d -aes-128-ofb -in ciphertext_ofb_corrupted.bin -out decrypted_ofb.txt -K 00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10
```

---

## **Step 6: Expected Observations**

| **Mode** | **Corruption Effect**                              | **Recoverable Info**                                  |
| -------- | -------------------------------------------------- | ----------------------------------------------------- |
| **ECB**  | Only the corrupted block is garbled                | Almost entire file recoverable except corrupted block |
| **CBC**  | Current block corrupted + first byte of next block | Most of the file recoverable                          |
| **CFB**  | Current segment + few bytes corrupted              | Rest of file recoverable                              |
| **OFB**  | Only the corrupted byte affected                   | Almost entire file recoverable                        |

---

## **Step 7: Explanation**

* **ECB:** Blocks encrypted independently → corruption contained in one block.
* **CBC:** Block chaining → corruption propagates to next block slightly.
* **CFB:** Self-synchronizing stream → corruption affects current and next few bytes.
* **OFB:** Keystream independent → only corrupted byte affected.

---

## **Step 8: Implications**

1. **Error Propagation:**

   * ECB & OFB → minimal propagation
   * CBC → moderate
   * CFB → limited, depends on segment size

2. **Security vs. Reliability:**

   * ECB is weak against pattern leaks but localizes errors.
   * CBC is widely used but slightly amplifies single-bit errors.
   * OFB is robust for transmission errors.

3. **Choosing Mode:**

   * Use OFB for noisy channels
   * CBC for standard file encryption
   * ECB only for small independent blocks (rarely recommended)

