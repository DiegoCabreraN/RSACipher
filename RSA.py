from RSA_Utils import (
    MaximumCommonDivisor,
    SelectEpsilon,
    FindEpsilonInverse
)


class RSA:
    __alphabet = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
        'A': 27,
        'B': 28,
        'C': 29,
        'D': 30,
        'E': 31,
        'F': 32,
        'G': 33,
        'H': 34,
        'I': 35,
        'J': 36,
        'K': 37,
        'L': 38,
        'M': 39,
        'N': 40,
        'O': 41,
        'P': 42,
        'Q': 43,
        'R': 44,
        'S': 45,
        'T': 46,
        'U': 47,
        'V': 48,
        'W': 49,
        'X': 50,
        'Y': 51,
        'Z': 52,
        '1': 53,
        '2': 54,
        '3': 55,
        '4': 56,
        '5': 57,
        '6': 58,
        '7': 59,
        '8': 60,
        '9': 61,
        '0': 62,
        '*': 63,
        '+': 64,
        '-': 65,
        '!': 66,
        '/': 67,
        '&': 68,
        '~': 69,
        '`': 70,
        '@': 71,
        '#': 72,
        '$': 73,
        '%': 74,
        '^': 75,
        '\n': 76,
    }

    def __init__(self):
        p = 7
        q = 11
        fi = (p-1)*(q-1)
        self.publicKey = (p*q, SelectEpsilon(fi))
        self.privateKey = FindEpsilonInverse(self.publicKey[1], fi)

    def encodeChar(self, char):
        charKeyCode = self.__alphabet[char]
        encryptedCharKeyCode = pow(charKeyCode, self.publicKey[1])
        encryptedCharKeyCode %= self.publicKey[0]
        alphabetChars = list(self.__alphabet.keys())
        encryptedChar = alphabetChars[encryptedCharKeyCode-1]
        return encryptedChar

    def decodeChar(self, char):
        charKeyCode = self.__alphabet[char]
        decryptedCharKeyCode = pow(charKeyCode, self.privateKey)
        decryptedCharKeyCode %= self.publicKey[0]
        alphabetChars = list(self.__alphabet.keys())
        decryptedChar = alphabetChars[decryptedCharKeyCode-1]
        return decryptedChar

    def encodeString(self, string):
        encodedString = ''
        for i in range(len(string)):
            encodedChar = self.encodeChar(string[i])
            encodedString += encodedChar
        return encodedString

    def decodeString(self, string):
        decodedString = ''
        for i in range(len(string)):
            decodedChar = self.decodeChar(string[i])
            decodedString += decodedChar
        return decodedString
