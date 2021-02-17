filename='two_cities_ascii.txt'

with open(filename) as file_object:

    contents= file_object.read()

    #afairw ari8mous kai shmeia stikshs
    char_remove=['0','1','2','3','4','5','6','7','8','9','.',',','!','[',']','(',')','-','{','}',';',':','''"''','<','>','/','?','@','#','$','%','^','&','*','_','~',"""'""",'’','“','‘']
    for charact in char_remove:
        contents=contents.replace(charact,' ')

    words=contents.split()

    #dymioyrgw dict opoy key=leksh kai value=mhkos lekshs
    d={}
    for word in words:
        word1=word.lstrip()
        d[word1]=len(word1)

    flag=0
    #zeygarwnw lekseis bash mhkous xarakthrwn(=20) kai afou tis zeygarwsw 8etw to mhkos toys iso me 100 wste na mhn xrhsimopoih8oyn se allo zeygari
    for i in range (1,11):
        lst=[]
        for k_1,v_1 in d.items():
            if int(v_1)==i:
                for k_2,v_2 in d.items():
                    if k_1!=k_2 and int(v_1)+int(v_2)==20:
                        print(k_1.lower(),k_2.lower(),",")
                        d[k_1]=100
                        d[k_2]=100
                        flag=1
                        break
    if flag==0:
        print('Δεν βρέθηκε ζευγάρι λέξεων')
