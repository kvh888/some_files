simbol_dict = {}
count = 0

with open('war_and_peace.txt', 'r', encoding='UTF-8') as text:
    for i in text:
        for j in i:
            count += 1
            if j in simbol_dict.keys():
                simbol_dict[j] += 1
            else:
                simbol_dict[j] = 1

sorted_simbol_dict = {i: simbol_dict[i] for i in sorted(simbol_dict) if i.isalpha()}

summ_simb = 0
for key, value in sorted_simbol_dict.items():
    proc_simbol = round((value / count) * 100, 2)
    summ_simb += proc_simbol
    print(f'{key} - {proc_simbol} %')

print(f'Буквенных символов: {summ_simb} %')
print(f'Всего символов (с учетом знаков пунктуации): {count} шт.')
