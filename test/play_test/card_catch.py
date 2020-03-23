import random

class Card(object):
    # card 클래스 생성자, 멤버 변수 초기화
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # show() 함수 출력
    def __unicode__(self):
        return self.show()

    # show() 함수 출력
    def __str__(self):
        return self.show()

    # show() 함수 출력
    def __repr__(self):
        return self.show()

    # show() 함수 출력
    def show(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value
        return "{} of {}".format(val, self.suit)

class Deck(object):
    # 덱 생성자 함수 호출
    def __init__(self):
        self.cards = []
        self.build()

    # 내부 카드 정보 출력
    def show(self):
        for card in self.cards:
           print(card.show())

    # 전체 카드 삽입
    def build(self):
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))
        self.cards.append(Card("#JOKER#", 1))
        length = len(self.cards)
        print(length)

    # 전체 카드 섞기
    def shuffle(self, num=1):
        length = len(self.cards)
        
        for _ in range(num):
            random.shuffle(self.cards)

    # card 한개를 뽑아 반환해주는 함수
    def deal(self):
        return self.cards.pop()

    def check_Deck(self):
        if "Ace of #JOCKER#" in (self.cards):
            print("Restart")
        else:
            print("CHECK OK")



class Player(object):
    # player 생성자 함수 호출
    def __init__(self, name):
        self.name = name
        self.hand = []

    # 플레이어 이름 출력
    def sayHello(self):
        print("Hi! My name is {}".format(self.name))
        return self

    # 카드를 하나 뽑아, 사용자에게 추가해주는 함수
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False
        return True

    # 플레이어의 카드 정보 출력
    def showHand(self):
        print("{}'s hand: {}".format(self.name, self.hand))
        return self

    # 받은 카드 하나를 버림
    def discard(self, sequence):
        return self.hand.pop(sequence)

    # 상대방 카드 가져오고 내 카드에 추가 
    def take(self, user , sequence):
        print(user.hand[sequence])
        card = user.discard(sequence)
        return self.hand.append(card)

    

    


while True:
    myDeck = Deck()
    #myDeck.show()
    myDeck.shuffle()
    
    player_num = 2
    cards_of_persion = int(53 / player_num)
    

    kim = Player("kim")
    kim.draw(myDeck, cards_of_persion)
    kim.showHand()

    kwon = Player("kwon")
    kwon.draw(myDeck, cards_of_persion)
    kwon.showHand()

    myDeck.check_Deck()

    kwon.take(kim, 0)
    kim.showHand()
    kwon.showHand()

    # shim = Player("shim")
    # shim.draw(myDeck, 5)
    # shim.showHand()

    # mun = Player("mun")
    # mun.draw(myDeck, 5)
    # mun.showHand()

    # han = Player("han")
    # han.draw(myDeck, 5)
    # han.showHand()

    # chae = Player("chae")
    # chae.draw(myDeck, 5)
    # chae.showHand()

    break
