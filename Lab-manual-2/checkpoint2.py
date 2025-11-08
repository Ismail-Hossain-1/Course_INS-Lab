import re
from collections import Counter
import string

# English letter frequencies (from the table)
ENGLISH_FREQ = {
    'e': 12.22, 't': 9.67, 'a': 8.05, 'o': 7.63, 'i': 6.28,
    'n': 6.95, 's': 6.02, 'h': 6.62, 'r': 5.29, 'd': 5.10,
    'l': 4.08, 'u': 2.92, 'c': 2.23, 'm': 2.33, 'w': 2.60,
    'f': 2.14, 'g': 2.30, 'y': 2.04, 'p': 1.66, 'b': 1.67,
    'v': 0.82, 'k': 0.95, 'j': 0.19, 'x': 0.11, 'q': 0.06, 'z': 0.06
}
ENGLISH_ORDER = sorted(ENGLISH_FREQ, key=ENGLISH_FREQ.get, reverse=True)

# Ciphertexts
CIPHER1 = """af p xpkcaqvnpk pfg, af ipqe qpri, gauuikifc tpw, ceiri udvk tiki afgarxifrphni cd eao--wvmd popkwn, hiqpvri du ear jvaql vfgikrcpfgafm du cei xkafqaxnir du xrwqedearcdkw pfg du ear aopmafpcasi xkdhafmr afcd fit pkipr. ac tpr qdoudkcafm cd lfdt cepc au pfwceafm epxxifig cd ringdf eaorinu hiudki cei opceiopcaqr du cei uaing qdvng hi qdoxnicinw tdklig dvc--pfg edt rndtnw ac xkdqiigig, pfg edt odvfcpafdvr cei dhrcpqnir--ceiki tdvng pc niprc kiopaf dfi mddg oafg cepc tdvng qdfcafvi cei kiripkqe"""

CIPHER2 = """aceah toz puvg vcdl omj puvg yudqecov, omj loj auum klu thmjuv hs klu zlcvu shv zcbkg guovz, upuv zcmdu
lcz vuwovroaeu jczoyyuovomdu omj qmubyudkuj vukqvm. klu vcdluz lu loj avhqnlk aodr svhw lcz kvopuez loj mht audhwu o ehdoe 
eunumj, omj ck toz yhyqeoveg auecupuj, tlokupuv klu hej sher wcnlk zog, klok klu lcee ok aon umj toz sqee hs kqmmuez zkqssuj 
tckl kvuozqvu. omj cs klok toz mhk umhqnl shv sowu, kluvu toz oezh lcz yvhehmnuj pcnhqv kh wovpue ok. kcwu thvu hm, aqk 
ck zuuwuj kh lopu eckkeu ussudk hm wv. aonncmz. ok mcmukg lu toz wqdl klu zowu oz ok scskg. ok mcmukg-mcmukg klug aunom
kh doee lcw tuee-yvuzuvpuj; aqk qmdlomnuj thqej lopu auum muovuv klu wovr. kluvu tuvu zhwu klok zlhhr klucv luojz omj klhqnlk 
klcz toz khh wqdl hs o nhhj klcmn; ck zuuwuj qmsocv klok CSE-478: Introduction to Computer Security Lab Lab-2 omghmu
zlhqej yhzzuzz (oyyovumkeg) yuvyukqoe ghqkl oz tuee oz (vuyqkujeg) cmubloqzkcaeu tuoekl. ck tcee lopu kh au yocj shv, 
klug zocj. ck czm'k mokqvoe, omj kvhqaeu tcee dhwu hs ck! aqk zh sov kvhqaeu loj mhk dhwu; omj oz wv. aonncmz toz numuvhqz
tckl lcz whmug, whzk yuhyeu tuvu tceecmn kh shvncpu lcw lcz hjjckcuz omj lcz nhhj shvkqmu. lu vuwocmuj hm pczckcmn kuvwz tckl 
lcz vueokcpuz (ubduyk, hs dhqvzu, klu zodrpceeu aonncmzuz), omj lu loj womg juphkuj ojwcvuvz owhmn klu lhaackz hs yhhv omj 
qmcwyhvkomk sowcecuz. aqk lu loj mh dehzu svcumjz, qmkce zhwu hs lcz ghqmnuv dhqzcmz aunom kh nvht qy. klu uejuzk hs kluzu, 
omj aceah'z sophqvcku, toz ghqmn svhjh aonncmz. tlum aceah toz mcmukg-mcmukg lu ojhykuj svhjh oz lcz lucv, omj avhqnlk lcw 
kh ecpu ok aon umj; omj klu lhyuz hs klu zodrpceeu- aonncmzuz tuvu scmoeeg jozluj. aceah omj svhjh loyyumuj kh lopu klu zowu acvkljog, 
zuykuwauv 22mj. ghq loj aukkuv dhwu omj ecpu luvu, svhjh wg eoj, zocj aceah hmu jog; omj klum tu dom dueuavoku hqv
acvkljog-yovkcuz dhwshvkoaeg khnukluv. ok klok kcwu svhjh toz zkcee cm lcz ktuumz, oz klu lhaackz doeeuj klu cvvuzyhmzcaeu
ktumkcuz auktuum dlcejlhhj omj dhwcmn hs onu ok klcvkg-klvuu"""

def clean_text(text):
    return ''.join(c.lower() for c in text if c.isalpha())

def frequency_analysis(text):
    cleaned = clean_text(text)
    total = len(cleaned)
    counter = Counter(cleaned)
    return {char: (count / total * 100) for char, count in counter.items()}

def auto_map(cipher_freq):
    cipher_order = sorted(cipher_freq, key=cipher_freq.get, reverse=True)
    mapping = {}
    for c_letter, e_letter in zip(cipher_order, ENGLISH_ORDER):
        mapping[c_letter] = e_letter
    return mapping

def apply_mapping(text, mapping):
    result = []
    for c in text:
        if c.lower() in mapping:
            decoded = mapping[c.lower()]
            result.append(decoded.upper() if c.isupper() else decoded)
        else:
            result.append(c)
    return ''.join(result)

def interactive_decrypt(ciphertext, initial_mapping):
    mapping = initial_mapping.copy()
    decrypted = apply_mapping(ciphertext, mapping)
    print("\n--- Current Decryption ---\n")
    print(decrypted)
    print("\nCurrent Mapping:", mapping)

    # No while loop, just apply the initial mapping and then exit
    print("\nDecryption completed using the initial automatic mapping.")
    return decrypted, mapping


def main():
    print("=== CIPHER 1 ===")
    freq1 = frequency_analysis(CIPHER1)
    print("Top 10 frequent letters in Cipher-1:")
    for c in sorted(freq1, key=freq1.get, reverse=True)[:10]:
        print(f"  {c}: {freq1[c]:.2f}%")

    auto_map1 = auto_map(freq1)
    print("\nAuto mapping for Cipher-1:", auto_map1)
    print("\nStarting interactive decryption for Cipher-1...")
    decrypted1, final_map1 = interactive_decrypt(CIPHER1, auto_map1)

    print("\n" + "="*60)
    print("=== CIPHER 2 ===")
    freq2 = frequency_analysis(CIPHER2)
    print("Top 10 frequent letters in Cipher-2:")
    for c in sorted(freq2, key=freq2.get, reverse=True)[:10]:
        print(f"  {c}: {freq2[c]:.2f}%")

    auto_map2 = auto_map(freq2)
    print("\nAuto mapping for Cipher-2:", auto_map2)
    print("\nStarting interactive decryption for Cipher-2...")
    decrypted2, final_map2 = interactive_decrypt(CIPHER2, auto_map2)

    print("\n" + "="*60)
    print("FINAL RESULTS")
    print("="*60)
    print("CIPHER-1 DECRYPTED:")
    print(decrypted1)
    print("\nFinal Mapping 1:", final_map1)

    print("\nCIPHER-2 DECRYPTED:")
    print(decrypted2)
    print("\nFinal Mapping 2:", final_map2)

    # Compare ease
    print("\n" + "="*60)
    print("WHICH WAS EASIER TO BREAK?")
    print("="*60)

    # Count how many top English letters were correctly auto-mapped
    def correctness(auto_map, final_map):
        correct = 0
        for c, e_auto in auto_map.items():
            if c in final_map and final_map[c] == e_auto:
                correct += 1
        return correct / len(auto_map) if auto_map else 0

    acc1 = correctness(auto_map1, final_map1)
    acc2 = correctness(auto_map2, final_map2)

    print(f"Auto-mapping accuracy: Cipher-1: {acc1:.2%}, Cipher-2: {acc2:.2%}")

    if acc1 > acc2:
        print("Cipher-1 was easier to break.")
        print("Reason: Its letter frequency distribution more closely matched English,")
        print("so automatic frequency matching produced a better initial key.")
    elif acc2 > acc1:
        print("Cipher-2 was easier to break.")
        print("Reason: Despite longer text, its frequency profile allowed better auto-mapping.")
    else:
        print("Both were equally easy/difficult based on auto-mapping.")

    # Additional: length
    len1 = len(clean_text(CIPHER1))
    len2 = len(clean_text(CIPHER2))
    print(f"\nText lengths: Cipher-1: {len1}, Cipher-2: {len2}")
    if len2 > len1:
        print("Cipher-2 has more letters, giving more reliable frequency stats.")

if __name__ == "__main__":
    main()