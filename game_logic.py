from itertools import combinations_with_replacement
import random as rand

class knuckle():
    def __init__(self,left,right):
        self.left = left
        self.right = right
    
    def k_sum(self):
        return self.left + self.right

    
    def flip(self):
        self.left, self.right = self.right, self.left
        return self.left, self.right
    
    def knuck(self):
        return (self.left, self.right)

        
class player():
    def __init__(self,draw):
        self.hand = draw
        
    def reveal_hand(self):
        return [i.knuck() for i in self.hand]


    def play(self,knuck_num):
        return self.hand[knuck_num]
    
    def discard(self,knuck_num):
        self.hand[knuck_num],self.hand[-1] = self.hand[-1],self.hand[knuck_num]
        self.hand.pop()
        return self.hand
    
    
    def win(self):
        if len(self.hand) == 0:
            return True 
        return False

def make_box():     
    ints = [0,1,2,3,4,5,6]
    combs = [i for i in combinations_with_replacement(ints,2)]
    knuckle_box = ['' for i in range(len(combs))]
    for k in range(len(knuckle_box)):
        l,r = combs[k]
        knuckle_box[k] = knuckle(l,r)
    return knuckle_box



def shuffle(box,players):
    if players > 4:
        return 'слишком много игроков'
    done = []
    draw = [[] for p in range(players)]
    for i in range(players):
        box = list(filter(lambda x: x not in done,box))
        hand = rand.sample(box,7)
        for k in hand:
            done.append(k)
            draw[i].append(k)
    return draw
        
        
def init_game(box,players):
    participants = {}
    draw = shuffle(box,players)
    for i in range(players):
        participants[i+1] = player(draw[i])
    return participants
    
def roll(participants):
    for i in range(len(participants)):
        for s in participants[i+1].hand:
            if s.k_sum() == 12:
                num = participants[i+1].hand.index(s)
                return i+1,num
    return 'ошибка'
                
def take_turn(curr_player,players):
    if curr_player < players:
        return curr_player + 1
    return 1

def take_action(curr_player,participants,board,l_pos,r_pos):
    participantss = participants.copy()
    
    for k in range(len(participantss[curr_player].hand)):
        
        if participantss[curr_player].hand[k].right == board[r_pos].right:
            participantss[curr_player].hand[k].left, participantss[curr_player].hand[k].right = participantss[curr_player].hand[k].flip()
            board[r_pos+1] = participantss[curr_player].play(k)
            participantss[curr_player].discard(k)
            r_pos = r_pos + 1
            return participantss,board,l_pos,r_pos,0
        
        if participantss[curr_player].hand[k].right == board[l_pos].left:
            board[l_pos-1] = participantss[curr_player].play(k)
            participantss[curr_player].discard(k)
            l_pos = l_pos - 1
            return participantss,board,l_pos,r_pos,0
        
        if participantss[curr_player].hand[k].left == board[r_pos].right:
            board[r_pos+1] = participantss[curr_player].play(k)
            participantss[curr_player].discard(k)
            r_pos = r_pos + 1
            return participantss,board,l_pos,r_pos,0
        
        if participantss[curr_player].hand[k].left == board[l_pos].left:
            participantss[curr_player].hand[k].left, participantss[curr_player].hand[k].right = participantss[curr_player].hand[k].flip()
            board[l_pos-1] = participantss[curr_player].play(k)
            participantss[curr_player].discard(k)
            l_pos = l_pos - 1
            return participantss,board,l_pos,r_pos,0
    
    
    return participantss,board,l_pos,r_pos,1


def stage_game(players):
    box = make_box()
    starting_hands = {}
    board = [0 for i in range(58)]
    participants = init_game(box,players)
    for k,v in participants.items():
        starting_hands[k] = [i.knuck() for i in v.hand]
    l_pos = 29
    r_pos = 29
    fish = 0
    p,k = roll(participants)
    board[l_pos] = participants[p].play(k)
    participants[p].discard(k)
    curr_player = p
    first_turn = p
    
    while True:
        curr_player = take_turn(curr_player,players)
        participants,board,l_pos,r_pos,is_pass = take_action(curr_player,participants,board,l_pos,r_pos)
        if is_pass == 0:
            fish = 0
        else:
            fish += is_pass
        if participants[curr_player].win() or fish == players:
            return participants,list(filter(lambda x: x!= 0,[i.knuck() if i != 0 else 0 for i in board])),fish,curr_player,first_turn,starting_hands
        
        
def simulate_match(players,score):
    score_count = {}
    for i in range(players):
        score_count[i+1] = {'очки':0, 'победы':0,'право первого хода':0}
            
    game_count = 0
    fish_count = 0
    
    while all([u['очки'] < score for u in [i for i in score_count.values()]]):
        game_count += 1
        participants,board,fish,curr_player,first_turn,starting_hands = stage_game(players)
            
        for p,s in participants.items():
            for k in s.hand:
                score_count[p]['очки'] += k.k_sum()
        if fish != players:
            score_count[curr_player]['победы'] += 1
        else:
            fish_count += 1
            
        score_count[first_turn]['право первого хода'] += 1
        
    pre_goats = list(filter(lambda x: x >= score,[i['очки'] for i in score_count.values()]))
    goats = list(filter(lambda x: x!=0,[i if score_count[i]['очки'] in pre_goats else 0 for i in score_count.keys()]))
    return score_count,game_count,fish_count,goats
                    
            
           
def show_result_match():
    score_count,game_count,fish_count,goats = simulate_match(4,101)  
    return score_count,game_count,fish_count,goats

def show_results_game():
    participants,board,fish,curr_player,first_turn,starting_hands = stage_game(4)
    return board, [i for i in starting_hands.values()],[i.reveal_hand() for i in participants.values()]


    
