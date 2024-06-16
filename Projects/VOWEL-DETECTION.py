def isVowel(ch):
    str = "aeiouAEIOU"
    return (str.find(ch) != -1)

def Name(n):
    count = []
    for i in n:
        if(isVowel(i) is True):
            count.append(i)
    return count

if __name__ == '__main__':
    name = input('Enter the name : ')
    print('No of vowel is :',len(Name(name)))