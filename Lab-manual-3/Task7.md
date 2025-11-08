
---

## **Step 1: Creating a Plaintext File**


```
This is a sample text file to study the avalanche effect of hash functions.
```
**original_file.txt** 

---

## **Step 2: Generate Original Hash (H1)**

Use OpenSSL to generate the hash of the original file. We will try **MD5** and **SHA-256**.

### **2.1 MD5 Hash**

```bash
openssl dgst -md5 original_file.txt
```

### **2.2 SHA-256 Hash**

```bash
openssl dgst -sha256 original_file.txt
```

*Save the outputs as H1_MD5 and H1_SHA256.*

---

## **Step 3: Modify the File**

1. Open the file in a hex editor, such as `ghex`:

```bash
ghex original_file.txt
```

2. Flip a single bit in any byte of the file (e.g., the 10th byte).
3. Save the modified file as `modified_file.txt`.

---

## **Step 4: Generate Hash of Modified File (H2)**

Use the same hash algorithms to generate hashes of the modified file.

### **4.1 MD5 Hash**

```bash
openssl dgst -md5 modified_file.txt
```

### **4.2 SHA-256 Hash**

```bash
openssl dgst -sha256 modified_file.txt
```

*Save the outputs as H2_MD5 and H2_SHA256.*

---

## **Step 5: Observations**

| **Hash Algorithm** | **H1 (Original)** | **H2 (Modified)** | **Observation**                                                                                                        |
| ------------------ | ----------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------- |
| MD5                | H1_MD5            | H2_MD5            | Even flipping a single bit in the input results in a completely different hash. Demonstrates the **avalanche effect**. |
| SHA-256            | H1_SHA256         | H2_SHA256         | Same observation. A tiny change produces a drastically different output.                                               |

**Key Observations:**

1. Hash functions are **highly sensitive to input changes**.
2. Flipping just **one bit** changes almost all bits of the hash.
3. This property ensures **integrity detection**: small modifications in the input are easily detectable.

---

## **Step 6: (Bonus) Count Matching Bits Between H1 and H2**

You can write a short Python script to compare H1 and H2 bit by bit:

```python
def count_same_bits(h1, h2):
    # Convert hex strings to integers
    i1 = int(h1, 16)
    i2 = int(h2, 16)
    xor = i1 ^ i2
    total_bits = len(h1)*4
    diff_bits = bin(xor).count('1')
    same_bits = total_bits - diff_bits
    return same_bits

# Example usage
H1 = "e2c569be17396eca2a2e3c11578123ed"
H2 = "5f4dcc3b5aa765d61d8327deb882cf99"

print("Same bits:", count_same_bits(H1, H2))
```

---

## **Step 7: Commands Used**

```bash
# Original file hashes
openssl dgst -md5 original_file.txt
openssl dgst -sha256 original_file.txt

# Modified file hashes
openssl dgst -md5 modified_file.txt
openssl dgst -sha256 modified_file.txt
```

---

## **Step 8: Files to Attach**

* `original_file.txt`
* `modified_file.txt`
* H1 and H2 hash outputs for MD5 and SHA-256

---

