from collections import Counter

filename='two_cities_ascii.txt'


#function to cut strings into characters
def split_char(wrd):
    return [char for char in word]

#function to execute rounding upwards
def round_up(num):
    if int(num)!=num:
        r=int(num+1)
    else:
        r=int(num)
    return r

with open(filename, encoding="utf8") as file_object:

    contents= file_object.read()

    #remove numbers and punctuation
    char_remove=['0','1','2','3','4','5','6','7','8','9','.',',','!','[',']','(',')','-','{','}',';',':','''"''','<','>','/','?','@','#','$','%','^','&','*','_','~',"""'""",'’','“','‘']
    for charact in char_remove:
        contents=contents.replace(charact,' ')

    words=contents.split()

    all_chars=[]
    for word in words:
        all_chars.append(split_char(word))

    #add in a list the letters with odd ASCII code
    lst_odd=[]
    for item in all_chars:
        for c in item:
            ascii_c=ord(c)
            if ascii_c%2==1:
                lst_odd.append(c)

    length_odd=len(lst_odd)

    #create dictionary that contains as keys the characters and as values their number of appearances
    dict_count=Counter(lst_odd)

    #find the ratio of each letter in text
    for k, v in dict_count.items():
        quotient=(v/length_odd)*100
        var1=round_up(quotient)
        print(k,":", var1*'*')

