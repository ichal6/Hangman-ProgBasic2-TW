def Find_Letter(letter, word, dashes):
    length_word = len(word)
    iteration = 0

    appearance = 0

    while iteration < length_word:
        if letter == word[iteration].upper():
            dashes[iteration] = letter
            appearance +=1
        iteration +=1
    return appearance
#znajduje litere w tekscie, zwraca ilosc jej wystepowan i podmienia dashe na litery
def Find_Hit(letter, word):
    
    length_word = len(word)
    iteration = 0

    appearance = 1

    while iteration < length_word:
        if letter == word[iteration].upper():
            word[iteration] = " "
            appearance = 0
        
        iteration +=1
    return appearance
#szuka na liscie alfabet wystapienia litery (ochrona przed powrótnym wprowadzeniem litery), 
# funkcja zwraca wartość jeśli znalazła liteę