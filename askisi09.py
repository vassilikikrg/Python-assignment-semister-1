from collections import Counter

filename='two_cities_ascii.txt'


#sunarthsh gia na kovw string se xarakthres
def split_char(wrd):
    return [char for char in word]

#sunarthsh gia stroggulopoihsh pros ta panw
def round_up(num):
    if int(num)!=num:
        r=int(num+1)
    else:
        r=int(num)
    return r

with open(filename, encoding="utf8") as file_object:

    contents= file_object.read()

    #afairw ari8mous kai shmeia stikshs
    char_remove=['0','1','2','3','4','5','6','7','8','9','.',',','!','[',']','(',')','-','{','}',';',':','''"''','<','>','/','?','@','#','$','%','^','&','*','_','~',"""'""",'’','“','‘']
    for charact in char_remove:
        contents=contents.replace(charact,' ')

    words=contents.split()

    all_chars=[]
    for word in words:
        all_chars.append(split_char(word))

    #pros8hkh se kainoyrgia lista ka8e gramma me mono kwdiko ascii
    lst_mono=[]
    for item in all_chars:
        for c in item:
            ascii_c=ord(c)
            if ascii_c%2==1:
                lst_mono.append(c)

    num_mono=len(lst_mono)

    #leksiko poy periexei ws kleidia xarakthres kai ws times to plh8os tous
    dict_count=Counter(lst_mono)

    #briskw analogia ka8e grammatos sto keimeno
    for k, v in dict_count.items():
        quotient=(v/num_mono)*100
        var1=round_up(quotient)
        print(k,":", var1*'*')
