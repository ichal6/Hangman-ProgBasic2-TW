from Read_List_WInners import Save_to_file
from Read_List_WInners import Save_list_win

def Sort_list(list_win):
    iter = 0
    size_list = len(list_win)

    while iter < size_list:
        next_winner=0
        while next_winner <= size_list-2:
            if int(list_win[next_winner][3]) > int(list_win[next_winner+1][3]):
                temp = list_win[next_winner+1]
                list_win[next_winner+1] = list_win[next_winner]
                list_win[next_winner] = temp
            next_winner+=1
        iter+=1
    
#sortuje wg uzyskanych punktów (guessing_tries)

def winning_condition(list_win, my_score, new_winner):
    length_list_win = len(list_win)-1
    if int(list_win[length_list_win][3]) > my_score:
        if length_list_win == 9:
            list_win.pop(length_list_win)
        list_win.append(new_winner)
        Sort_list(list_win)
        Save_to_file(Save_list_win(list_win))
        
        
#sprawdza czy wynik miesci sie na liscie i dodaje do listy zwycięsców 
    
    print(*list_win, sep="\n")
def read_file_to_string():
    open_file = open("winlist.txt", "r")
    for el in open_file:
        print(el, end="")

#read_file_to_string()