from collections import Counter

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

def cards_type(cards):
    counter = Counter(cards)
    if len(counter) == 1:
        return FIVE_OF_A_KIND
    if len(counter) == 2:
        for _, v in counter.items():
            if v == 4:
                return FOUR_OF_A_KIND
        return FULL_HOUSE
    
    if len(counter) == 3:
        for _, v in counter.items():
            if v == 3:
                return THREE_OF_A_KIND
        return TWO_PAIR
    
    return ONE_PAIR if len(counter) == 4 else HIGH_CARD
    

def part1():
    CARD_VALUES = {
        "A" : 14, 
        "K": 13 ,
        "Q": 12, 
        "J": 11, 
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6, 
        "5": 5, 
        "4": 4,
        "3": 3, 
        "2": 2,
    }
    

    def solve(data):
        ranks = []
        for cards, bid in data:
            res = [cards_type(cards)] + [CARD_VALUES[x] for x in cards] + [int(bid)]
            ranks.append(tuple(res))
        
        ranks.sort()
        ans = 0
        for i in range(len(ranks) - 1, -1, -1):
            ans += (i + 1) * ranks[i][-1]
        return ans 
    
    data = []
    with open("input.txt", "r") as fp:
        for line in fp.readlines():
            data.append(line.strip().split())
    
    return solve(data)

def part2():
    CARD_VALUES = {
        "A" : 14, 
        "K": 13 ,
        "Q": 12,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6, 
        "5": 5, 
        "4": 4,
        "3": 3, 
        "2": 2,
        "J": 1,
    }

    def parse(cards):
        counter = Counter(cards)
        if counter["J"] == 0 or counter["J"] == 5:
            return cards
        
        new_cards = ""
        mx_card, mx_value = "", 0
        for card, val in counter.items():
            if card != "J":
                new_cards += card * val 
                if val > mx_value:
                    mx_value = val 
                    mx_card = card 
        new_cards += (mx_card * counter["J"])
        return new_cards
    
    def solve(data):
        ranks = []
        for cards, bid in data:
            res = [cards_type(parse(cards))] + [CARD_VALUES[x] for x in cards] + [int(bid)]
            ranks.append(tuple(res))
        
        ranks.sort()
        ans = 0
        for i in range(len(ranks) - 1, -1, -1):
            ans += (i + 1) * ranks[i][-1]
        return ans  

    data = []
    with open("input.txt", "r") as fp:
        for line in fp.readlines():
            data.append(line.strip().split())

    return solve(data)

if __name__ == "__main__":
    # print(part1())
    print(part2())