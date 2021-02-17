import json
from collections import Counter

filename="askisi11.txt"
with open(filename, encoding="utf8") as file_object:
    contents = file_object.read()
    my_dict=json.loads(contents)

    keys=[]
    #synarthsh pou pros8etei ka8e key sthn lista keys[] oses fores emfanizetai
    def find_keys(d):
        for k,v in d.items():
            keys.append(k)
            

            if type(v) is dict:
                find_keys(v)

            if type(v) is list:
                for ele in v:
                    if type(ele) is dict:
                        find_keys(ele)




    x=find_keys(my_dict)
    
    #dhmioyrgia dictionary poy exei ws key to ka8e stoixeio ths keys[] kai ws value to plh8os emfanishs tou stoixeiou
    dict_count=Counter(keys)

    
    def find_max(d):
        cnt=0
        for k,v in d.items():
            if v>cnt:
                cnt=v
        return cnt

    y=find_max(dict_count)
    print("Το κλειδί/κλειδιά που εμφανίζεται/εμφανίζονται τις περισσότερες φορές ειναι:")
    #ektypwnoume ta kleidia poy emfanizontai fores=max 
    
    for k,v in dict_count.items():
        if v==y:
            print(k)
