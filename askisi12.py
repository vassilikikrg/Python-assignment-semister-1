filename='ask12.txt'

#function to cut strings into characters
def split_char(wrd):
    return [char for char in word]

with open(filename) as file_object:

    contents= file_object.read()

    #reverse characters
    contents_reversed=contents[::-1]

    char_list=[]
    for word in contents_reversed:
        char_list.append(split_char(word))


    strng=''
    #find the "mirror" character of each character
    for item in char_list:
        for c in item:
            k=chr(128-ord(c))
            strng+=k
    print(strng)
