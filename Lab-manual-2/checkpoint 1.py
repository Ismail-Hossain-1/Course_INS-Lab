cipher = "odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo"

def decrypt_caesar(text, shift):
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':  #
            new_char = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            result += new_char
        else:
            result += ch
    return result

# Try all 26 possible shifts
for k in range(26):
    print(f"Shift {k:2d}: {decrypt_caesar(cipher, k)}")

# for k=10 the output strign is most meaningfull
print(f"\nShift {10}: {decrypt_caesar(cipher, 10)}")
print("Ans: ethereum is the best smart contract platform out there")