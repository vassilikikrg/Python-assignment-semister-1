filename='ask12.txt'

#sunarthsh gia na kovw string se xarakthres
def split_char(wrd):
    return [char for char in word]

#synarthsh gia na metatrepw lista se string
def list_to_string(lst):
    #dhmiourgw keno string
    strng = ""
    for ele in lst:
        strng += ele
    #epistrefw string
    return strng

with open(filename) as file_object:

    contents= file_object.read()

    #afairw ari8mous kai shmeia stikshs
    char_remove=['0','1','2','3','4','5','6','7','8','9','.',',','!',
    '[',']','(',')','-','{','}',';',':','''"''','<','>','/','?','@','#','$','%','^','&','*','_','~',"""'"""]
    for charact in char_remove:
        contents=contents.replace(charact,' ')
    #print(contents)
    #bazw xarakthres se anapodh seira
    contents_reversed=contents[::-1]

    #xwrizw keimeno se lekseis
    words=contents_reversed.split()

    #ka8e stoixeio ths listas words to spaw se xarakthres kai tous pros8etw sth char_list
    char_list=[]
    for word in words:
        char_list.append(split_char(word))
    

    #briskw ton katoptriko tou ka8e grammatos
    lst1=[]
    for item in char_list:
        for c in item:
            k=chr(128-ord(c))
            lst1.append(k)
        lst1.append(" ")

    k=list_to_string(lst1)
    print(k.rstrip())
