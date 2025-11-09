cipher1 = """af p xpkcaqvnpk pfg, af ipqe qpri, gauuikifc tpw, ceiri udvk tiki afgarxifrphni cd eaowvmd popkwn, hiqpvri du ear jvaql vfgikrcpfgafm du cei xkafqaxnir du xrwqedearcdkw pfg du ear aopmafpcasi xkdhafmr afcd fit pkipr. ac tpr qdoudkcafm cd lfdt cepc au pfwceafm
epxxifig cd ringdf eaorinu hiudki cei opceiopcaqr du cei uaing qdvng hi qdoxnicinw tdklig dvcpfg edt rndtnw ac xkdqiigig, pfg edt odvfcpafdvr cei dhrcpqnir--ceiki tdvng pc niprc kiopaf dfi
mddg oafg cepc tdvng qdfcafvi cei kiripkqe"""

def break_substitution_cipher(cipher):
    # Count letter frequencies
    frequency = {}
    for char in cipher.lower():
        if 'a' <= char <= 'z':
            frequency[char] = frequency.get(char, 0) + 1

    # Sort by frequency (descending)
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    common_letters = [entry[0] for entry in sorted_frequency]

    # English letter frequency (most common to least)
    english_frequency = list('eotainshrdlcufwmpygbkqvjxz')

    # Map cipher letters to guessed English letters
    mapping = {common_letters[i]: english_frequency[i] for i in range(len(common_letters))}

    # Decrypt text
    decrypted = ''
    for char in cipher:
        if 'a' <= char <= 'z':
            decrypted += mapping.get(char, char)
        elif 'A' <= char <= 'Z':
            lower = char.lower()
            decrypted += mapping.get(lower, lower).upper()
        else:
            decrypted += char

    return decrypted


decrypted_text = break_substitution_cipher(cipher1)
print("Decryption for Cipher 1:\n")
print(decrypted_text)
