

def IsVowel(l):
    return l.isalpha() and l.lower() in ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú')

def IsY(l):
    return l.lower() in ('y')

def RemoveAccent(l):
    if l == 'á':
        return 'a'
    if l == 'é':
        return 'e'
    if l == 'í':
        return 'i'
    if l == 'ó':
        return 'o'
    if l == 'ú':
        return 'u'
    if l == 'Á':
        return 'A'
    if l == 'É':
        return 'E'
    if l == 'Í':
        return 'I'
    if l == 'Ó':
        return 'O'
    if l == 'Ú':
        return 'U'
    else:
        return l

def RemoveAccentInWord(word):
    return ToString([RemoveAccent(l) for l in word])

def ToPascalCase(word):
    return ToString(word[0].upper() + word[1:].lower())

def IsConsonant(l):
    return l.isalpha() and not IsVowel(l)

def KeepAlpha(word):
    return ToString([l for l in word if l.isalpha()])

def ToSingular(word, dict):
    word = word.lower()
    if len(word) > 0 and word[-1] == 's':
        singular = ToString(word[:-1])
        if singular in dict:
            return singular
    return word

def ToString(list):
    return ''.join(list)


def IsVeryShort(word):
    return len(word) <= 2

def IsVeryLong(word):
    return len(word) >= 8

def HasTwoVowels(word):
    oneVowel = False
    for l in word:
        if IsVowel(l):
            if oneVowel:
                return True
            oneVowel = True
        elif IsY(l) and oneVowel:
            return True
        else:
            oneVowel = False

def HasTwoConsonants(word):
    oneConsonant = False
    for l in word:
        if IsConsonant(l):
            if oneConsonant:
                return True
            oneConsonant = True
        else:
            oneConsonant = False


def HasRInMiddle(word):
    return len(word) > 1 and HasLetter(word[1:], 'r')

def HasH(word):
    return HasLetter(word, 'h')

def HasC(word):
    return HasLetter(word, 'c')

def HasQ(word):
    return HasLetter(word, 'q')

def HasG(word):
    return HasLetter(word, 'g')

def HasY(word):
    return HasLetter(word, 'y')

def HasLL(word):
    return HasLetter(word, 'll')

def HasLetter(word, letter):
    return letter in word.lower()