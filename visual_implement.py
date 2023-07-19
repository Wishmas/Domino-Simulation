from tkinter import *
from game_logic import *
from tkinter import font as tkFont


def show_hand_top_left(l,coord,col):
    a,b,c,d = coord
    for i in range(7):
        cv.create_rectangle(a, b, c, d, fill=col, outline='black',activedash=(5, 4))
        cv.create_text(a+20, b+20, text=f'{l[i][0]}',justify=CENTER, font="Verdana 12")
        cv.create_rectangle(a, b+40, c, d+40, fill=col, outline='black',activedash=(5, 4))
        cv.create_text(a+20, b+60, text=f'{l[i][1]}',justify=CENTER, font="Verdana 12")
        a = a + 40
        c = c + 40

def show_hand_top_right(l,coord,col):
    a,b,c,d = coord
    for i in range(7):
        cv.create_rectangle(a, b, c, d, fill=col, outline='black',activedash=(5, 4))
        cv.create_text(a-20, b+20, text=f'{l[i][0]}',justify=CENTER, font="Verdana 12")
        cv.create_rectangle(a, b+40, c, d+40, fill=col, outline='black',activedash=(5, 4))
        cv.create_text(a-20, b+60, text=f'{l[i][1]}',justify=CENTER, font="Verdana 12")
        a = a - 40
        c = c - 40

def show_hand_bot_left(l,coord,col):
    a,b,c,d = coord
    for i in range(7):
        cv.create_rectangle(a, b, c, d, fill=col, outline='black',activedash=(5, 4))
        cv.create_text(a+20, b-20, text=f'{l[i][0]}',justify=CENTER, font="Verdana 12")
        cv.create_rectangle(a, b-40, c, d-40, fill=col, outline='black',activedash=(5, 4))
        cv.create_text(a+20, b-60, text=f'{l[i][1]}',justify=CENTER, font="Verdana 12")
        a = a + 40
        c = c + 40
        
def show_hand_bot_right(l,coord,col):
    a,b,c,d = coord
    for i in range(7):
        cv.create_rectangle(a, b, c, d, fill=col, outline='black',activedash=(5, 4))
        cv.create_text(a-20, b-20, text=f'{l[i][0]}',justify=CENTER, font="Verdana 12")
        cv.create_rectangle(a, b-40, c, d-40, fill=col, outline='black',activedash=(5, 4))
        cv.create_text(a-20, b-60, text=f'{l[i][1]}',justify=CENTER, font="Verdana 12")
        a = a - 40
        c = c - 40
             
        
def show_end_top_left(l,coord):
    a,b,c,d = coord
    if len(l) == 0:
        cv.create_rectangle(a, b+120, c+160, d+120, fill='#99ff66', outline='black',activedash=(5, 4))
        cv.create_text(a+90, b+140, text=f'Победитель',justify=CENTER, font="Verdana 16")
    for i in range(len(l)):
        cv.create_rectangle(a, b+120, c, d+120, fill='#99ff66', outline='black',activedash=(5, 4))
        cv.create_text(a+20, b+140, text=f'{l[i][0]}',justify=CENTER, font="Verdana 12")
        cv.create_rectangle(a, b+160, c, d+160, fill='#99ff66', outline='black',activedash=(5, 4))
        cv.create_text(a+20, b+180, text=f'{l[i][1]}',justify=CENTER, font="Verdana 12")
        a = a + 40
        c = c + 40


def show_end_top_right(l,coord):
    a,b,c,d = coord
    if len(l) == 0:
        cv.create_rectangle(a, b+120, c-160, d+120, fill='#99ff66', outline='black',activedash=(5, 4))
        cv.create_text(a-100, b+140, text=f'Победитель',justify=CENTER, font="Verdana 16")
    for i in range(len(l)):
        cv.create_rectangle(a, b+120, c, d+120, fill='#99ff66', outline='black',activedash=(5, 4))
        cv.create_text(a-20, b+140, text=f'{l[i][0]}',justify=CENTER, font="Verdana 12")
        cv.create_rectangle(a, b+160, c, d+160, fill='#99ff66', outline='black',activedash=(5, 4))
        cv.create_text(a-20, b+180, text=f'{l[i][1]}',justify=CENTER, font="Verdana 12")
        a = a - 40
        c = c - 40

def show_end_bot_left(l,coord):
    a,b,c,d = coord
    if len(l) == 0:
        cv.create_rectangle(a, b-120, c+160, d-120, fill='#99ff66', outline='black',activedash=(5, 4))
        cv.create_text(a+90, b-140, text=f'Победитель',justify=CENTER, font="Verdana 16")
    for i in range(len(l)):
        cv.create_rectangle(a, b-120, c, d-120, fill='#99ff66', outline='black',activedash=(5, 4))
        cv.create_text(a+20, b-140, text=f'{l[i][0]}',justify=CENTER, font="Verdana 12")
        cv.create_rectangle(a, b-160, c, d-160, fill='#99ff66', outline='black',activedash=(5, 4))
        cv.create_text(a+20, b-180, text=f'{l[i][1]}',justify=CENTER, font="Verdana 12")
        a = a + 40
        c = c + 40
        
def show_end_bot_right(l,coord):
    a,b,c,d = coord
    if len(l) == 0:
        cv.create_rectangle(a, b-120, c-160, d-120, fill='#99ff66', outline='black',activedash=(5, 4))
        cv.create_text(a-100, b-140, text=f'Победитель',justify=CENTER, font="Verdana 16")
    for i in range(len(l)):
        cv.create_rectangle(a, b-120, c, d-120, fill='#99ff66', outline='black',activedash=(5, 4))
        cv.create_text(a-20, b-140, text=f'{l[i][0]}',justify=CENTER, font="Verdana 12")
        cv.create_rectangle(a, b-160, c, d-160, fill='#99ff66', outline='black',activedash=(5, 4))
        cv.create_text(a-20, b-180, text=f'{l[i][1]}',justify=CENTER, font="Verdana 12")
        a = a - 40
        c = c - 40        
          
def color_check(board,hand_box,i):
    for h in range(len(hand_box)):
            if (board[i][0],board[i][1]) in hand_box[h] or (board[i][1],board[i][0]) in hand_box[h]:
                return h

        
def show_board(board,h,w,hand_box):
    
    a,b,c,d = 40, h/2-80, 80, h/2-40
    go = True

    for i in range(len(board)):

        col = color_check(board=board,hand_box=hand_box,i=i)
        
        if w - c >= 40 and go:
            cv.create_rectangle(a, b, c, d, fill=colors[col], outline='black',activedash=(5, 4))
            cv.create_text(a+20, b+20, text=f'{board[i][0]}',justify=CENTER, font="Verdana 12")
            cv.create_rectangle(a+40, b, c+40, d, fill=colors[col], outline='black',activedash=(5, 4))
            cv.create_text(a+60, b+20, text=f'{board[i][1]}',justify=CENTER, font="Verdana 12")
            a = a + 80
            c = c + 80
                
        elif go:
            a = a - 40
            b = b + 40
            c = c - 40
            d = d + 40
            cv.create_rectangle(a, b, c, d, fill=colors[col], outline='black',activedash=(5, 4))
            cv.create_text(a+20, b+20, text=f'{board[i][0]}',justify=CENTER, font="Verdana 12")
            cv.create_rectangle(a, b+40, c, d+40, fill=colors[col], outline='black',activedash=(5, 4))
            cv.create_text(a+20, b+60, text=f'{board[i][1]}',justify=CENTER, font="Verdana 12")
            a = a - 40 
            b = b + 40
            c = c - 40
            d = d + 40
            go = False
        
        else:
            cv.create_rectangle(a, b, c, d, fill=colors[col], outline='black',activedash=(5, 4))
            cv.create_text(a+20, b+20, text=f'{board[i][0]}',justify=CENTER, font="Verdana 12")
            cv.create_rectangle(a-40, b, c-40, d, fill=colors[col], outline='black',activedash=(5, 4))
            cv.create_text(a-20, b+20, text=f'{board[i][1]}',justify=CENTER, font="Verdana 12")
            a = a - 80
            c = c - 80
    

def show_roll(coord_box,h,w,colors):
    global brd,hand_box,final_box
    
    cv.delete(ALL)
    brd,hand_box,final_box = show_results_game()
    
    for h_num in range(len(hand_box)):
        col = colors[h_num]
        if coord_box[h_num][0] < w/2 and coord_box[h_num][1] < h/2:
            show_hand_top_left(hand_box[h_num],coord_box[h_num],col) 
        elif coord_box[h_num][0] < w/2 and coord_box[h_num][1] > h/2:
            show_hand_bot_left(hand_box[h_num],coord_box[h_num],col)
        elif coord_box[h_num][0] > w/2 and coord_box[h_num][1] > h/2:
            show_hand_bot_right(hand_box[h_num],coord_box[h_num],col)
        else:
            show_hand_top_right(hand_box[h_num],coord_box[h_num],col)
            
            
def show_finaly(coord_box,final_box,h,w):
    
    for h_num in range(len(final_box)):
        if coord_box[h_num][0] < w/2 and coord_box[h_num][1] < h/2:
            show_end_top_left(final_box[h_num],coord_box[h_num])
        elif coord_box[h_num][0] < w/2 and coord_box[h_num][1] > h/2:
            show_end_bot_left(final_box[h_num],coord_box[h_num])
        elif coord_box[h_num][0] > w/2 and coord_box[h_num][1] > h/2:
            show_end_bot_right(final_box[h_num],coord_box[h_num])
        else:
            show_end_top_right(final_box[h_num],coord_box[h_num])


def show_result(board,hand_box,coord_box,colors,h,w):
    show_finaly(coord_box,final_box,h,w)
    show_board(board,h,w,hand_box)
    
    
def show_match():
    
    cv.delete(ALL)
    a,b,c,d = [320, 120, 880, 620]
    score_count,game_count,fish_count,goats = show_result_match()
    cv.create_rectangle(a, b, c, d, fill='orange', outline='black',activedash=(5, 4))
    a = a + 275
    b = b + 25
    cv.create_text(a, b, text='Результат матча до 101 очка:',justify=CENTER, font=bold_font)
    for p,t in score_count.items():
        b += 30
        cv.create_text(a, b, text=f'Игрок {p}:',justify=LEFT, font=bold_font)
        for k,r in t.items():
            b += 20
            cv.create_text(a, b, text=f'{k} : {r}',justify=LEFT, font="Verdana 12")
    b += 30
    cv.create_text(a, b, text=f'Всего игр : {game_count}',justify=LEFT, font=bold_font)
    b += 30
    cv.create_text(a, b, text=f'Из них рыба : {fish_count}',justify=LEFT, font=bold_font)
    b += 30
    cv.create_text(a, b, text=f"Козлами стали игроки с номерами: {','.join([str(i) for i in goats])}",justify=LEFT, font=bold_font)   
    
def clear():
    cv.delete(ALL)

    

  
w = 1200
h = 750
window = Tk() 
window.resizable(0,0)
window.title('Симуляция партии в домино')
cv = Canvas(window, width=1200, height=750, bg='#1E2027')
cv.pack()

coord_box = [[40, 40, 80, 80],[40, h-40, 80, h-80],[w-40, h-40, w-80, h-80],[w-40, 40, w-80, 80]]  
colors = {0 : '#ffa500',1:'#ff8c13',2:'#ff7124',3:'#ff5533'}
brd,hand_box,final_box = show_results_game()

butn_font = tkFont.Font(family='Verdana', size=12)
bold_font = tkFont.Font(family='Verdana', size=12, weight="bold")

btn = Button(window, text="Раздать \nруки",bg='#ffff66',height=3, width=8,command=lambda: show_roll(coord_box,h,w,colors)) 
btn['font'] =  butn_font
btn.place(x=380,y=40)

btn2 = Button(window, text="Показать \nрезультат",bg='#ffff66',height=3, width=10, command=lambda: show_result(brd,hand_box,coord_box,colors,h,w))  
btn2['font'] =  butn_font
btn2.place(x=540,y=40)

btn3 = Button(window, text="Очистить",bg='#ff3333',height=3, width=8, command=lambda: clear()) 
btn3['font'] =  butn_font
btn3.place(x=720,y=40)

btn4 = Button(window, text="Симуляция \nматча",bg='#99e600',height=3, width=10, command=lambda: show_match()) 
btn4['font'] =  butn_font
btn4.place(x=540,y=630)

window.mainloop()   