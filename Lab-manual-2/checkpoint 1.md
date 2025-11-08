Here’s a **shorter, concise version** of your report while keeping all the key points:

---

# Report: Breaking the Caesar Cipher

**Ciphertext:**

```
odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo
```

---

## 1. Understanding the cipher

The ciphertext uses the **Caesar cipher**, where each letter is shifted by a fixed key `k` (0–25). Decryption requires shifting letters **backward** by `k`.

Since there are only 26 possible keys, a brute-force approach is straightforward.

---

## 2. Approach

1. Loop through all possible keys `k = 0..25`.
2. For each key, shift every letter in the ciphertext backward by `k`.
3. Print all 26 candidate plaintexts.
4. Identify the one that is **meaningful English**.

This guarantees finding the correct plaintext because Caesar cipher has a tiny keyspace.

---

## 3. Implementation (Python code)

```python
cipher = "odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo"

def decrypt_caesar(text, shift):
    return ''.join(
        chr((ord(c) - ord('a') - shift) % 26 + ord('a')) if 'a' <= c <= 'z' else c
        for c in text
    )

for k in range(26):
    print(f"Shift {k:2d}: {decrypt_caesar(cipher, k)}")
```

---

## 4. Result

After trying all 26 shifts, the **meaningful English text** appears at:

**Key `k = 10`:**

```
ethereum is the best smart contract platform out there
```

This is the decrypted plaintext.

---

## 5. Summary

* Tried **all possible keys** (0–25) and inspected outputs.
* Selected the only **readable English candidate**, confirming key = 10.
* Brute-force is efficient here because the Caesar cipher has a **small keyspace**.

