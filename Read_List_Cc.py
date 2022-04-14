def Read_list_Cc():
    openfile = open("countries-and-capitals.txt", "r") 
    results = []
 
    for line in openfile:
        results.append(line.strip().split('|')) 
        
    openfile.close()

    return results
    #zapisuje plik do listy
    

