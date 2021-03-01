filename='ask12.txt'

#sunarthsh gia na kovw string se xarakthres
def split_char(wrd):
    return [char for char in word]

with open(filename) as file_object:

    contents= file_object.read()

    #bazw xarakthres se anapodh seira
    contents_reversed=contents[::-1]
    
    #ka8e stoixeio tou contents_reversed to spaw se xarakthres kai tous pros8etw sth char_list
    char_list=[]
    for word in contents_reversed:
        char_list.append(split_char(word))


    strng=''
    #briskw ton katoptriko tou ka8e grammatos
    for item in char_list:
        for c in item:
            k=chr(128-ord(c))
            strng+=k
    print(strng)
