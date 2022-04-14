import time
import random
import sys
from datetime import date
from Read_List_WInners import Read_list_win
from winning_cond import winning_condition
from Read_List_Cc import Read_list_Cc
from find_letter import Find_Letter
from find_letter import Find_Hit
from drawing import HANGMANPICS
#import bibliotek oraz funkcji z pozostałych plików

list_countries = Read_list_Cc()
leng_country = len(list_countries)-1
list_win = Read_list_win()
today = date.today()
words_hit =  []
start = time.time()
life = 5
guessing_attempts = 0
drawing_number = 0
dashes = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#zerowanie zmiennych

print("Welcome to Hangman. Save the world from SKYNET!")   
print("Your life = " + str(life))

word_index = random.randrange(0,leng_country) #losowanie słowa
word = list_countries[word_index][1]
word = word[1:] #odejmujemy pierwszy znak (pause)
#print(word)

word_length = len(word)
dashes = "_" * word_length
dashes = list(dashes)
print(dashes) #zamienia liczbę liter na podkreślenia
words_tried = [] #lista błędnych słów

word_out_spaces_list = word.split()
word_out_spaces_string = "".join(word_out_spaces_list)
word_length = len(word_out_spaces_string)



is_exit = True

while is_exit: #inicjuje program póki gracz ma życia
    print("These are the answers that you tried: ", words_tried)
    if life < 3: #dodaje podpowiedź
        print("It's the capital of:", end=" ")
        print(list_countries[word_index][0])
    let_or_word = "" #zmienna odpowiedzialna za wybór słowa lub litery

    #allowed_choices = ["l", "w"]

    while let_or_word.lower() != "w" and let_or_word.lower() != "l":
        
        let_or_word = input("Do you want  to input a letter or a word? Please insert l for letter and w for word.")
        #domaga sie odpowiedzi póki nie dostaniemy w lub l
        
        if let_or_word.lower() == "w": #wprowadzanie słowa
            guessing_attempts += 1
            answer = "3" #zmienna chroniaca przed wpisaniem cyfry zamiast slowa
            while answer.isdigit() == True:
                answer = input("Please enter a word" + " ")

            if answer.lower() == word.lower(): #jesli trafilismy poprawny winik -> zakonczenie gry
                print("You are the winner!")
                end = time.time()
                guessing_time = end - start
                guessing_time = round(guessing_time,2)
                print("You guessed the capital after " + str(guessing_attempts) + " attempts.")
                print("It took you " + str(guessing_time))
                name = input("Please input your name? ")
                new_winner = [name, str(today), str(guessing_time), str(guessing_attempts), word] #zapisujemy zwyciesce do listy
                winning_condition(list_win, guessing_attempts, new_winner) #pozwala na zalisanie wygr. do pliku
                
                
                again_game= "" #pozwala zaczac grę od nowa
                while again_game.lower() != "y" and again_game.lower() != "n":
                    again_game = input("Do you want to play again? Y/N ")
                    if again_game.lower() == "y": #jesli chcemy kontynuowac program wraca do początkowych wartości
                        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                        list_win = Read_list_win()
                        today = date.today()
                        start = time.time()
                        life = 5
                        guessing_attempts = 0
                        dashes = []
                        words_hit =  []
                        drawing_number = 0
                        #zaczyna gre od nowa - zerowanie wartości
                        print("Welcome to Hangman. Save the world from SKYNET!") 
                        print("Your life = " + str(life))
                        word_index = random.randrange(0,leng_country)
                        word = list_countries[word_index][1]
                        word = word[1:]
                        word_length = len(word)
                        dashes = "_" * word_length
                        dashes = list(dashes)
                        print(dashes)
                        print(word_length)
                        words_tried = []
                        word_out_spaces_list = word.split()
                        word_out_spaces_string = "".join(word_out_spaces_list)
                        word_length = len(word_out_spaces_string)

                    elif again_game.lower()== "n":
                        #sys.exit() #wyjscie z programu
                        print("Thank you. Goodbye!")
                        is_exit = False
                    else:
                        print("Wrong input. Please try again.") #ochrona przed zla odpowiedzia
            elif answer.lower() != word: #wybór złego słowa
                life -= 2
                print("Wrong answer. Try again")
                print("Your life = " + str(life))
                if life > 0:
                    print(HANGMANPICS[drawing_number]) #drukowanie wisielca
                else:
                    print(HANGMANPICS[4])
                drawing_number = drawing_number + 1
                
                words_tried.append(answer) #dodaje złą odpowiedź do listy złych odpowiedzi
        elif let_or_word.lower() == ("l"): #wybór litery
            guessing_attempts += 1
            answer="3"
            while answer.isdigit() == True or len(answer) >= 2:
                answer = input("Please enter a letter" + " ") #zabespiecza przed wpisaniem cyfry
            answer = answer.upper()
            word_hit = []
            appearance = Find_Letter(answer, word, dashes)
            hit = Find_Hit(answer, alphabet) 
            if hit > 0: #sprawdza czy próbowaliśmy wprowadzić dany znak
                
                print("You have already tried this letter.")
            else: #jeśli nie - zmniejsza liczbę znaków do znalezienia
                word_length = word_length  - appearance
            print(dashes)
            if appearance == 0 and hit == 0: #użytkowanik wprowadził złą odpowiedź 
                print("Wrong answer. Please try again.")
                life -= 1
                print("Your life = " + str(life))
                words_tried.append(answer)
                if life > 0:
                    print(HANGMANPICS[drawing_number]) #drukowanie wisielca
                else:
                    print(HANGMANPICS[4])
                
                drawing_number = drawing_number + 1
            if word_length == 0: #użytkownik znalazł wszystkie litery
                print("You are the winner")
                end = time.time()
                guessing_time = end - start
                guessing_time = round(guessing_time,2)
                print("You guessed the capital after " + str(guessing_attempts) + " attempts.")
                print("It took you " + str(guessing_time))
                name = input("Please input your name? ")
                new_winner = [name, str(today), str(guessing_time), str(guessing_attempts), word]
                winning_condition(list_win, guessing_attempts, new_winner) #lista zwycięzców (zapis)
                
                again_game= "" #ponowne włączenie programu
                while again_game.lower() != "y" and again_game.lower() != "n":
                    again_game = input("Do you want to play again? Y/N ")
                    if again_game.lower() == "y":
                        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                        list_win = Read_list_win()
                        today = date.today()
                        start = time.time()
                        life = 5
                        guessing_attempts = 0
                        dashes = []
                        words_hit =  []
                        drawing_number = 0

                        print("Welcome to Hangman. Save the world from SKYNET!") 
                        print("Your life = " + str(life))
                        word_index = random.randrange(0,leng_country)
                        word = list_countries[word_index][1]
                        word = word[1:]
                        word_length = len(word)
                        dashes = "_" * word_length
                        dashes = list(dashes)
                        print(dashes)
                        print(word_length)
                        words_tried = []
                        word_out_spaces_list = word.split()
                        word_out_spaces_string = "".join(word_out_spaces_list)
                        word_length = len(word_out_spaces_string)
                    elif again_game.lower()== "n":
                        #sys.exit()
                        print("Thank you. Goodbye!")
                        is_exit = False
                    else:
                        print("Wrong input. Please try again.")   


 
    if life <= 0: #koniec gry kiedy skończą się życia
        print("You've lost!")
        again_game = ""
        while again_game.lower() != "y" and again_game.lower() != "n":
            again_game = input("Do you want to play again? Y/N ")
            if again_game.lower() == "y":
                list_win = Read_list_win()
                today = date.today()
                start = time.time()
                life = 5
                guessing_attempts = 0
                dashes = []
                words_hit =  []
                drawing_number = 0

                print("Welcome to Hangman. Save the world from SKYNET!") 
                print("Your life = " + str(life))
                word_index = random.randrange(0,leng_country)
                word = list_countries[word_index][1]
                word = word[1:]
                word_length = len(word)
                dashes = "_" * word_length
                dashes = list(dashes)
                print(dashes)
                print(word_length)
                words_tried = []
            elif again_game.lower()== "n":
                #sys.exit()
                print("Thank you. Goodbye!")
                is_exit = False
            else:
                print("Wrong input. Please try again.")



  