import string
from collections import Counter

# Frequency table (from the problem, rounded to 2 decimals)
ENGLISH_FREQ = {
    'e': 12.22, 't': 9.67, 'a': 8.05, 'o': 7.63, 'i': 6.28,
    'n': 6.95, 's': 6.02, 'h': 6.62, 'r': 5.29, 'd': 5.10,
    'l': 4.08, 'u': 2.92, 'c': 2.23, 'm': 2.33, 'w': 2.60,
    'f': 2.14, 'g': 2.30, 'y': 2.04, 'p': 1.66, 'b': 1.67,
    'v': 0.82, 'k': 0.95, 'x': 0.11, 'j': 0.19, 'q': 0.06, 'z': 0.06
}

def frequency_count(text):
    """Return percentage frequency of each letter (ignore non-letters)."""
    text = ''.join(c.lower() for c in text if c.isalpha())
    total = len(text)
    if total == 0:
        return {}
    cnt = Counter(text)
    return {c: (cnt[c] * 100.0 / total) for c in cnt}

def build_mapping(cipher_freq, plain_order):
    """Map most frequent cipher letters to most frequent plain letters."""
    cipher_letters = sorted(cipher_freq, key=cipher_freq.get, reverse=True)
    mapping = {}
    for c_letter, p_letter in zip(cipher_letters, plain_order):
        mapping[c_letter] = p_letter
    return mapping

def apply_mapping(text, mapping):
    """Decrypt using the mapping, keep non-letters unchanged."""
    result = []
    for c in text:
        if c.isalpha():
            result.append(mapping.get(c.lower(), c).upper() if c.isupper() else mapping.get(c.lower(), c))
        else:
            result.append(c)
    return ''.join(result)

def solve_cipher(ciphertext):
    freq = frequency_count(ciphertext)
    plain_order = [c for c in 'etaoinsrhdlucmfywgpbvkxjqz']  # top to bottom
    mapping = build_mapping(freq, plain_order)
    decrypted = apply_mapping(ciphertext, mapping)
    return decrypted, mapping, freq

# ------------------- Cipher-1 -------------------
cipher1 = """af p xpkcaqvnpk pfg, af ipqe qpri, gauuikifc tpw, ceiri udvk tiki afgarxifrphni cd eao--wvmd popkwn, hiqpvri du ear jvaql vfgikrcpfgafm du cei xkafqaxnir du xrwqedearcdkw pfg du ear aopmafpcasi xkdhafmr afcd fit pkipr. ac tpr qdoudkcafm cd lfdt cepc au pfwceafm epxxifig cd ringdf eaorinu hiudki cei opceiopcaqr du cei uaing qdvng hi qdoxnicinw tdklig dvc--pfg edt rndtnw ac xkdqiigig, pfg edt odvfcpafdvr cei dhrcpqnir--ceiki tdvng pc niprc kiopaf dfi mddg oafg cepc tdvng qdfcafvi cei kiripkqe"""

dec1, map1, freq1 = solve_cipher(cipher1)

print("=== Cipher-1 Decrypted ===")
print(dec1)
print("\nMapping:")
print(map1)
print()

# ------------------- Cipher-2 -------------------
cipher2 = """aceah toz puvg vcdl omj puvg yudqecov, omj loj auum klu thmjuv hs klu zlcvu shv zcbkg guovz, upuv zcmdu lcz vuwovroaeu jczoyyuovomdu omj qmubyudkuj vukqvm. klu vcdluz lu loj avhqnlk aodr svhw lcz kvopuez loj mht audhwu o ehdoe eunumj, omj ck toz yhyqeoveg auecupuj, tlokupuv klu hej sher wcnlk zog, klok klu lcee ok aon umj toz sqee hs kqmmuez zkqssuj tckl kvuozqvu. omj cs klok toz mhk umhqnl shv sowu, kluvu toz oezh lcz yvhehmnuj pcnhqv kh wovpue ok. kcwu thvu hm, aqk ck zuuwuj kh lopu eckkeu ussudk hm wv. aonncmz. ok mcmukg lu toz wqdl klu zowu oz ok scskg. ok mcmukg-mcu klug aunom kh doee lcw tuee-yvuzuvpuj; aqk qmdlomnuj thqej lopu auum muovuv klu wovr. kluvu tuvu zhwu klok zlhhr klucv luojz omj klhqnlk klcz toz khh wqdl hs o nhhj klcmn; ck zuuwuj qmsocv klok CSE-478: Introduction to Computer Security Lab Lab-2 omghmu zlhqej yhzzuzz (oyyovumkeg) yuvyukqoe ghqkl oz tuee oz (vuyqkujeg) cmubloqzkcaeu tuoekl. ck tcee lopu kh au yocj shv, klug zocj. ck czm'k mokqvoe, omj kvhqaeu tcee dhwu hs ck! aqk zh sov kvhqaeu loj mhk dhwu; omj oz wv. aonncmz toz numuvhqz tckl lcz whmug, whzk yuhyeu tuvu tceecmn kh shvncpu lcw lcz hjjckcuz omj lcz nhhj shvkqmu. lu vuwocmuj hm pczckcmn kuvwz tckl lcz vueokcpuz (ubduyk, hs dhqvzu, klu zodrpceeu aonncmzuz), omj lu loj womg juphkuj ojwcvuvz owhmn klu lhaackz hs yhhv omj qmcwyhvkomk sowcecuz. aqk lu loj mh dehzu svcumjz, qmkce zhwu hs lcz ghqmnuv dhqzcmz aunom kh nvht qy. klu uejuzk hs kluzu, omj aceah'z sophqvcku, toz ghqmn svhjh aonncmz. tlum aceah toz mcmukg-mcu lu ojhykuj svhjh oz lcz lucv, omj avhqnlk lcw kh ecpu ok aon umj; omj klu lhyuz hs klu zodrpceeu- aonncmzuz tuvu scmoeeg jozluj. aceah omj svhjh loyyumuj kh lopu klu zowu acvkljog, zuykuwauv 22mj. ghq loj aukkuv dhwu omj ecpu luvu, svhjh wg eoj, zocj aceah hmu jog; omj klum tu dom dueuavoku hqv acvkljog-yovkcuz dhwshvkoaeg khnukluv. ok klok kcwu svhjh toz zkcee cm lcz ktuumz, oz klu lhaackz doeeuj klu cvvuzyhmzcaeu ktumkcuz auktuum dlcejlhhj omj dhwcmn hs onu ok klcvkg-klvuu"""

dec2, map2, freq2 = solve_cipher(cipher2)

print("=== Cipher-2 Decrypted ===")
print(dec2)
print("\nMapping:")
print(map2)