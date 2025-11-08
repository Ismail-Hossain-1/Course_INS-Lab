
### **Lab 3: Symmetric Encryption & Hashing**


---

### **Objective**

The objective of this lab is to perform symmetric encryption and hashing using the OpenSSL tool and a hex editor (GHex). The lab includes tasks to explore various encryption algorithms, modes, padding schemes, and message digest generation. We will also analyze the properties of encryption modes and one-way hash functions.

---

### **Tools Used**

* **OpenSSL**: For symmetric encryption (AES) and hashing (MD5, SHA1, SHA256).
* **GHex**: A hex editor used to manipulate binary files.
* **Ubuntu**: Linux distribution for performing all tasks.

---

### **Tasks Overview**

---

### **Task 1: AES Encryption Using Different Modes (2 Marks)**

#### **Objective**:

To explore AES encryption in different modes (e.g., CBC, CFB, ECB) and observe the effects of these modes on encryption and decryption.

#### **Commands Used:**

1. **Encryption using AES-128-CBC**

   ```bash
   openssl enc -aes-128-cbc -e -in plain.txt -out encrypted_cbc.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
   ```

2. **Encryption using AES-128-CFB**

   ```bash
   openssl enc -aes-128-cfb -e -in plain.txt -out encrypted_cfb.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
   ```

3. **Encryption using AES-128-ECB**

   ```bash
   openssl enc -aes-128-ecb -e -in plain.txt -out encrypted_ecb.bin -K 00112233445566778889aabbccddeeff
   ```

#### **Explanation**:

* In this task, I experimented with three encryption modes: **CBC (Cipher Block Chaining)**, **CFB (Cipher Feedback)**, and **ECB (Electronic Code Book)**.
* The files `plain.txt` (input file) were encrypted using different modes, and the resulting encrypted files were stored as `cipher.bin`, `cipher_cfb.bin`, and `cipher_ecb.bin`.
* **Decryption** was tested by running:

  ```bash
  openssl enc -d -aes-128-cbc -in cipher.bin -out decrypted.txt -K 00112233445566778889aabbccddeeff -iv 0102030405060708
  ```

  This confirmed that encryption and decryption worked as expected.

  Decrypt the Files

#### Now, to verify that the encryption and decryption work, you should decrypt the files.

Decrypt AES-128-ECB File:
```
openssl enc -aes-128-ecb -d -in encrypted_ecb.bin -out decrypted_ecb.txt -K 00112233445566778889aabbccddeeff
```

Decrypt AES-128-CBC File:
```
openssl enc -aes-128-cbc -d -in encrypted_cbc.bin -out decrypted_cbc.txt -K 00112233445566778889aabbccddeeff -iv 0102030405060708
```

Decrypt AES-128-CFB File:
```
openssl enc -aes-128-cfb -d -in encrypted_cfb.bin -out decrypted_cfb.txt -K 00112233445566778889aabbccddeeff -iv 
```

#### **Files Attached**:

* `plain.txt` (Original text file)


### **Task 2: ECB vs CBC (3 Marks)**

#### **Objective**:

To compare AES encryption in **ECB** and **CBC** modes by encrypting a `.bmp` image and analyzing the effects.

#### **Commands Used:**

1. **Encryption with ECB mode**

   ```bash
   openssl enc -aes-128-ecb -in original.bmp -out encrypted_ecb.bmp -K 00112233445566778889aabbccddeeff
   ```

2. **Encryption with CBC mode**

   ```bash
   openssl enc -aes-128-cbc -in original.bmp -out encrypted_cbc.bmp -K 00112233445566778889aabbccddeeff -iv 0102030405060708
   ```

#### **Explanation**:

* I used AES encryption in ECB and CBC modes to encrypt an image (`original.bmp`).
* After encrypting, I used **GHex** to replace the header of the encrypted `.bmp` files with the header of the original `.bmp` file to allow the encrypted files to be viewed as valid image files.
* **Visual Observations**:

  * When opening the encrypted files as images, the **ECB** encrypted image displayed recognizable patterns due to its block-wise independent encryption. This made the image's structure partially visible even after encryption.
  * The **CBC** encrypted image appeared as random noise, which is the expected result due to the chaining mechanism that makes each block dependent on the previous one.

#### **Files Attached**:

* `original.bmp` (Original image)
* `encrypted_cbc.bmp` (Encrypted image using ECB)
* `encrypted_ecb.bmp` (Encrypted image using CBC)

**CBC**

![Alt text](./encrypted_cbc.bmp)
**CBC**

![Alt text](./encrypted_ecb.bmp)

---

### **Task 3: Corrupted Ciphertext (3 Marks)**

#### **Objective**:

To observe the effects of ciphertext corruption on decrypted data and compare how different encryption modes handle such errors.

#### **Commands Used:**

1. **Encryption using AES-128**

   ```bash
   openssl enc -aes-128-cbc -in file.txt -out encrypted.txt -K 00112233445566778889aabbccddeeff -iv 0102030405060708
   ```

2. **Corruption of Ciphertext**:
   I used **GHex** to modify a single bit of the 30th byte in the encrypted file (`encrypted.txt`).

3. **Decryption after Corruption**

   ```bash
   openssl enc -d -aes-128-cbc -in corrupted_encrypted.txt -out decrypted.txt -K 00112233445566778889aabbccddeeff -iv 0102030405060708
   ```

#### **Explanation**:

* I observed the effects of corrupting one bit of the ciphertext and then attempting to decrypt it.
* In **ECB mode**, the corruption led to a predictable distortion of the corresponding plaintext block, but the rest of the text was decrypted correctly.
* In **CBC mode**, the corruption caused a ripple effect, where the corresponding plaintext block and the following block were corrupted.

#### **Files Attached**:

* `file.txt` (Original text file)
* `encrypted.txt` (Encrypted file before corruption)
* `corrupted_encrypted.txt` (Corrupted encrypted file)

---

### **Task 4: Padding (3 Marks)**

#### **Objective**:

To explore which encryption modes require padding and which do not.

#### **Commands Used:**

1. **Encryption in ECB mode**

   ```bash
   openssl enc -aes-128-ecb -in file.txt -out cipher_ecb.bin -K 00112233445566778889aabbccddeeff
   ```

2. **Encryption in CBC mode**

   ```bash
   openssl enc -aes-128-cbc -in file.txt -out cipher_cbc.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
   ```

3. **Encryption in CFB mode**

   ```bash
   openssl enc -aes-128-cfb -in file.txt -out cipher_cfb.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
   ```

4. **Encryption in OFB mode**

   ```bash
   openssl enc -aes-128-ofb -in file.txt -out cipher_ofb.bin -K 00112233445566778889aabbccddeeff -iv 0102030405060708
   ```

#### **Explanation**:

* **ECB mode** did **not** require padding since the text file's size was already a multiple of the block size.
* **CBC, CFB, and OFB modes** automatically added padding where necessary to handle files that weren't a perfect multiple of the block size.

#### **Files Attached**:

* `cipher_ecb.bin` (Encrypted file in ECB mode)
* `cipher_cbc.bin` (Encrypted file in CBC mode)
* `cipher_cfb.bin` (Encrypted file in CFB mode)
* `cipher_ofb.bin` (Encrypted file in OFB mode)

---

### **Task 5: Generating Message Digest (3 Marks)**

#### **Objective**:

To generate hash values using different one-way hash algorithms (MD5, SHA-1, SHA-256).

#### **Commands Used:**

1. **MD5 Hash**

   ```bash
   openssl dgst -md5 file.txt
   ```

2. **SHA-1 Hash**

   ```bash
   openssl dgst -sha1 file.txt
   ```

3. **SHA-256 Hash**

   ```bash
   openssl dgst -sha256 file.txt
   ```

#### **Explanation**:

* The text file `file.txt` was hashed using MD5, SHA-1, and SHA-256 algorithms.
* As expected, each algorithm produced a different length hash (MD5 = 128 bits, SHA-1 = 160 bits, SHA-256 = 256 bits).

#### **Files Attached**:

* `file.txt` (Text file used for hashing)
* Hashes generated for MD5, SHA-1, and SHA-256.

---
