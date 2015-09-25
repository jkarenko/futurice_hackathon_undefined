def solve2(hand):

    hand = map(int, hand.split())
    for i in range(1,5):
        if i not in hand:
            print "Fold"
            return
    print "Bet"
    return



    
