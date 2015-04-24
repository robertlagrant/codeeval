import sys
from collections import Counter

ranks = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14 }
of_a_kind_ranks = { 4: 5, 5: 4, 3: 3, 2: 2 }
hand_ranks = { 'HC': 1, 'P': 2, 'TP': 3, 'TOAK': 4, 'S': 5, 'F': 6, 'FH': 7, 'FOAK': 8, 'SF': 9, 'RF': 10}

def remove_from_hand_by_value(hand, value):
    count = 0
    out = []
    for i, (card, suit) in enumerate(hand):
        if count == 0 and value == card:
            count = 1 
        else:
            out.append((card,suit))
    return out
        

def process_high_card(left, right):
    left_vals = sorted((ranks[card] for card, _ in left), reverse=True)
    right_vals = sorted((ranks[card] for card, _ in right), reverse=True)
    
    for l, r in zip(left_vals, right_vals):
        if l > r:
            return 'left'
        elif r > l:
             return 'right'

    return 'none'

def detect_flush(hand):
    s = None
    for _, suit in hand:
        if s is None:
            s = suit
        elif suit != s:
            return False
            
    return True
    
def detect_straight(hand):
    vals = sorted((int(ranks[v]) for v, _ in hand))
    previous = None
    for v in vals:
        if previous != None and v-previous != 1:
            return False, None

        previous = v

    return True, vals[4]

def detect_of_a_kind(hand):
    counts = Counter(val for val, _ in hand)
    [(mc, c)] = counts.most_common(1)
    if c > 1:
        if c == 4:
            return True, 'FOAK', (mc,)
        else:
            del counts[mc]
            [(mc2, c2)] = counts.most_common(1)
            if c2 == 2:
                if c == 3:
                    return True, 'FH', (mc,mc2)
                else:
                    return True, 'TP', (mc, mc2)
            else:
                if c == 3:
                    return True, 'TOAK', (mc,) 
                else:
                    return True, 'P', (mc,)

    else:
        return False, None, None
    

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        #print(line)

        params = line.split()
        hands = { 'left': [(s[0], s[1]) for s in params[0:5]], 'right': [(s[0], s[1]) for s in params[5:11]] }
        hand_results = { 'left': None, 'right': None }

        for side, hand in hands.items():
            hand_result = None
        
            result, hand_type, value  = detect_of_a_kind(hand)
            if result:
                hand_result = hand_type, value
            
            # Try for a flush
            if hand_result is None or hand_ranks[hand_result[0]] < hand_ranks['F']:
                if detect_flush(hand):
                    hand_result = 'F',
                   
            # Try for a straight or straight flush
            if hand_result is None or hand_result == ('F',) or hand_ranks[hand_result[0]] < hand_ranks['S']:
                result, highest = detect_straight(hand)
                # If there's an ace, replace it with a 1 and try again
                if not result:
                    low_ace_hand = []
                    for v,s in hand:
                        if v == 'A':
                            low_ace_hand.append(('1', s))
                        else:
                            low_ace_hand.append((v,s))
                    
                    result, highest = detect_straight(low_ace_hand)
                    
                if result:
                    if hand_result == ('F',):
                        if highest == 'A':
                            hand_result = 'RF',
                        else:
                            hand_result = 'SF', highest
                    else:
                        hand_result = 'S', highest
            
            # It's a high card
            if hand_result is None:
                hand_result = 'HC',
        
            hand_results[side] = hand_result
        
        #print("Left: " + str(hand_results['left']) + " Right: " + str(hand_results['right']))
        
        left_result_hand = hand_results['left'][0]
        left_result_rank = hand_ranks[left_result_hand]
        
        right_result_hand = hand_results['right'][0]
        right_result_rank = hand_ranks[right_result_hand]
        
        #print(left_result_hand + " vs " + right_result_hand)
        
        if left_result_rank > right_result_rank:
            print('left')
        elif right_result_rank > left_result_rank:
            print('right')
        else:
            rank = left_result_hand
            #print("C-C-C-COMBOBREEEEEAAAAAAAKEERRR!")
            if rank in ['HC', 'F', 'S', 'SF', 'RF']:
                print(process_high_card(hands['left'], hands['right']))
                
            elif rank in ['FH', 'TP']:
                left_major, left_minor = hand_results['left'][1]
                right_major, right_minor = hand_results['right'][1]
                
                if ranks[left_major] > ranks[right_major]:
                    print('left')
                elif ranks[right_major] > ranks[left_major]:
                    print('right')
                else:
                    if ranks[left_minor] > ranks[right_minor]:
                        print('left')
                    elif ranks[right_minor] > ranks[left_minor]:
                        print('right')
                    else:
                        if rank == 'FH':
                            print('none')
                        else:
                            for value in [left_major, left_major, left_minor, left_minor]:
                                hands['left'] = remove_from_hand_by_value(hands['left'], value)
                            for value in [right_major, right_major, right_minor, right_minor]:
                                hands['right'] = remove_from_hand_by_value(hands['right'], value)
                            
                            print(process_high_card(hands['left'], hands['right']))
                            
            elif rank in ['P', 'TOAK', 'ROAK']:
                left_major = hand_results['left'][1][0]
                right_major = hand_results['right'][1][0]
                
                if ranks[left_major] > ranks[right_major]:
                    print('left')
                elif ranks[right_major] > ranks[left_major]:
                    print('right')
                else:
                    for value in [left_major, left_major]:
                        hands['left'] = remove_from_hand_by_value(hands['left'], value)
                    for value in [right_major, right_major]:
                        hands['right'] = remove_from_hand_by_value(hands['right'], value)
                        
                    print(process_high_card(hands['left'], hands['right']))
                
            else:
                print("HUH?")