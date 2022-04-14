import sys

def Read_list_win():
    openfile = open("winlist.txt", "r") 
    results = []
    for line in openfile:
        results.append(line.strip().split('|')) 

       
    
    openfile.close()

    return results

def Save_list_win(list_to_save):
    length = len(list_to_save)
    i=0
    string = ""
    while i < length:

        string += '|'.join(list_to_save[i])+ "\n"
        i+=1
    return string

def Save_to_file(string):
    plik = open("winlist.txt", "w")
    plik.write(string)

    plik.close()

#zapisuje plik zwycięzców