import sys

abcd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

file = str(sys.argv[1])
file = open(file,'r')
lines = file.readlines()
kod = lines[0]
kod = kod[:(len(kod)-1)]
podsl = lines[1]
file.close()

def odsifr(kod,podsl):
    p = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for k in range(0,52):
        for j in range(len(kod)):
            ind = abcd.index(kod[j])
            if (abcd[(ind+k)%52] == podsl[j]):
                p[k].append(1)
    k = p.index((max(p)))
    return k

def result(k):
    result = ''
    for i in range(len(kod)):
        ind = abcd.index(kod[i])
        result = result + ((abcd[(ind+k)%52]))
    return result


def errors_check():
    def chybny_vstup():
        for i in range(len(kod)):
            try:
                abcd.index(kod[i])
            except IndexError:
                pass
            except ValueError:
                return False
        for j in range(len(podsl)):
            try:
                abcd.index(podsl[j])
            except ValueError: 
                return False
            except IndexError:
                pass
        return True

    def delka_vstupu():
        if (len(kod) > len(podsl)) or (len(kod) < len(podsl)):
            return False
        return True

    if chybny_vstup() == False:
        print('Error: Chybny vstup!')
        exit()
    if chybny_vstup() == False and delka_vstupu() == False:
        print('Error: Chybny vstup!')
        exit()
    if delka_vstupu() == False:
        print('Error: Chybna delka vstupu!')
        exit()

def tisk(vystup):
    file = open('output.txt','w')
    if errors_check:
        file.write(vystup)
        file.close()

errors_check()
tisk(result(odsifr(kod,podsl)))