'https://projecteuler.net/problem=59'


import itertools

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def search_key(cipher):
    #あり得る鍵を総当りでチェックする
    result = []
    for a, b, c in itertools.product(alphabet, alphabet, alphabet):
        key = (ord(a), ord(b), ord(c))
        decripted = decript(cipher, key)
        if not decripted: continue #制御文字が出てきた場合はパス
        decripted_text = ASCII_to_text(decripted)
        if 'the' in decripted_text.lower(): #平文には'the'が入っているはず
            result.append((key, decripted_text[:50], sum(decripted)))
        
    return result


def decript(cipher, key):
    decripted = []
    for i, n in enumerate(cipher):
        a = n ^ key[i % 3]
        if 0 <= a <= 31 or a == 127: #制御文字が含まれる場合は除外
            return None
        decripted.append(a)
    return decripted

def ASCII_to_text(ls):
    return ''.join((chr(n) for n in ls))

def main():
    with open('src/cipher1.txt', 'r', encoding = 'utf-8') as f:
        cipher = f.read().rstrip().split(',')
        cipher = [int(n) for n in cipher]
    keys = search_key(cipher)
    print('Possible Decrypted Texts')
    for i, key in enumerate(keys):
        print('[{}] {}'.format(i, key[1]))
    print('Choose Key Number:')
        
    i = int(input())
    return keys[i][2]
    
    
if __name__ == '__main__':
    print(main())