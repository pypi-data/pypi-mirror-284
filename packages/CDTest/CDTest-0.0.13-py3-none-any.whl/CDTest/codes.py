def prac1Que1:
	return "# Necessary imports
from itertools import product
from re import findall

# Alphabet array without 'j' as per Playfair Cipher
array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def datalist_normal(key):
    key = key.replace(" ", "").lower()
    list1 = []
    for char in key:
        if char not in list1:
            if char == 'i':
                list1.append('i')
            elif char == 'j':
                if 'i' not in list1:
                    list1.append('i')
            else:
                list1.append(char)
    for char in array:
        if char not in list1:
            list1.append(char)
    return list1

def matrix(list1):
    m = []
    index = 0
    for i in range(5):
        a = []
        for j in range(5):
            a.append(list1[index])
            index += 1
        m.append(a)
    print("Matrix:")
    for row in m:
        print(" ".join(row))
    return m

def plain(text):
    text = text.replace(" ", "").lower()
    text = text.replace("j", "i")
    p = list(text)
    i = 0
    while i < len(p) - 1:
        if p[i] == p[i + 1]:
            p.insert(i + 1, 'x')
        i += 2
    if len(p) % 2 != 0:
        p.append('x')
    return p

def enc(p, m):
    encr = ""
    for i in range(0, len(p), 2):
        a, b = None, None
        c, d = None, None
        for j in range(5):
            for k in range(5):
                if p[i] == m[j][k]:
                    a, b = j, k
                if p[i + 1] == m[j][k]:
                    c, d = j, k
        if a == c and b != d:
            encr += m[a][(b + 1) % 5]
            encr += m[c][(d + 1) % 5]
        elif b == d and a != c:
            encr += m[(a + 1) % 5][b]
            encr += m[(c + 1) % 5][d]
        else:
            encr += m[a][d]
            encr += m[c][b]
    return encr

def dec(p, m):
    decr = ""
    for i in range(0, len(p), 2):
        a, b = None, None
        c, d = None, None
        for j in range(5):
            for k in range(5):
                if p[i] == m[j][k]:
                    a, b = j, k
                if p[i + 1] == m[j][k]:
                    c, d = j, k
        if a == c and b != d:
            decr += m[a][(b - 1) % 5]
            decr += m[c][(d - 1) % 5]
        elif b == d and a != c:
            decr += m[(a - 1) % 5][b]
            decr += m[(c - 1) % 5][d]
        else:
            decr += m[a][d]
            decr += m[c][b]
    return decr

key = input("Enter key: ")
text = input("Enter text: ")

# Creating datalist
list1 = datalist_normal(key)
print("Datalist:", list1)

# Creating matrix
matrix1 = matrix(list1)

# Creating plaintext list and adding dummy letters
plaintext = plain(text)
print("Plaintext:", plaintext)

# Encryption
encrypt = enc(plaintext, matrix1)
print("Encrypted:", encrypt)

# Decryption
decrypt = dec(encrypt, matrix1)
print("Decrypted:", decrypt)

"