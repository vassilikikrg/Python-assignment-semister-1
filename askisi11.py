import json
from collections import Counter

filename="askisi11.txt"

def find_max(d):
    cnt=0
    for k,v in d.items():
        if v>cnt:
            cnt=v
    return cnt

#function that finds all the keys of the dict and appends them in a list
def find_keys(d,lst):
    for k,v in d.items():
        lst.append(k)

        if type(v) is dict:
            find_keys(v,lst)

        if type(v) is list:
            for ele in v:
                if type(ele) is dict:
                    find_keys(ele,lst)



with open(filename, encoding="utf8") as file_object:
    contents = file_object.read()
    my_dict=json.loads(contents)






    keys=[]
    x=find_keys(my_dict,keys)

    #create dictionary that contains as keys the characters and as values their number of appearances
    dict_count=Counter(keys)


    y=find_max(dict_count)

    print("Το κλειδί/κλειδιά που εμφανίζεται/εμφανίζονται τις περισσότερες φορές ειναι:")
    #print the keys that appear most times
    for k,v in dict_count.items():
        if v==y:
            print(k)
