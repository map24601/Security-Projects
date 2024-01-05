key = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt(message, shift):
    result = ""
    if shift > 26: shift = shift%26
    for i in message:
        #place = key.index(i)
        #newLetter = key[place+shift]
        #result = result + newLetter
        newIndex = (shift+key.index(i))
        if newIndex > 26: newIndex = newIndex - 26
        result = result + key[newIndex]
    return result

def decrypt(message, shift):
    result = ""
    if shift > 26: shift = shift%26
    for i in message: 
        newIndex = (key.index(i) - shift)
        if newIndex < 0: newIndex = newIndex + 26
        result = result + key[newIndex]
    return result

print(encrypt("cab", 33))
print(decrypt(encrypt("cab", 33),33))
