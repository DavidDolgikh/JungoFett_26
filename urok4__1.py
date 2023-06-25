# O (N**2)
'''def strcounter(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(f'{sym} - {counter}')'''


# O (N)
'''def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    for sym, count in syms_counter.items():
        print(f'{sym} - {count}')



strcounter('zzzz')'''

# Дз

def palindrom_detector(s):
    if s == s[::-1]:
        print(True)
    else:
        print(False)

palindrom_detector('helloworld')
palindrom_detector('лепсспел')
