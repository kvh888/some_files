'''
Полный алфавит из всех печатных символов
кирилица включая буквы ё и Ё, латынь,
символы !, ?, :, $, % и т.д.
'''
cyrillic = [chr(ord("А") + i) for i in range(64)]
latin = [chr(simb) for simb in range(33, 123)]
alphabet = [*cyrillic, *latin]
alphabet.insert(38, chr(ord('ё')))
alphabet.insert(6, chr(ord('Ё')))

word = 'это питон'
'''Сдвиг'''
shift = 2

'''Сммещаем на shift символов'''
crypt_word = [alphabet[(alphabet.index(let) + shift) % len(alphabet)]
              if let in alphabet else ' ' for let in word]

print(''.join(crypt_word))
