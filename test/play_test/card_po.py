import random

# ranking을 알려주고 리턴함
def ranking(Player):
    if isFlush(Player.hand) is not None:
        return isFlush(Player.hand)
    elif isStraight(Player.hand) is not None:
        return isStraight(Player.hand)
    elif isFourCard(Player.hand) is not None:
        return isFourCard(Player.hand)
    else:
        return None

# 로얄플러쉬인지 알려주는 함수
def isFlush (hand):
    # 종류가 같으면
    if (hand[0].suit == hand[1].suit and
        hand[1].suit == hand[2].suit and
        hand[2].suit == hand[3].suit and
        hand[3].suit == hand[4].suit):

        valList = []
        for card in hand:
            valList.append(card.value)
        valList.sort()

        # 10, J, Q, K, A가 있는지
        if (valList[0] == 1 and
            valList[1] == 10 and
            valList[2] == 11 and
            valList[3] == 12 and
            valList[4] == 13):
            return "Royal Flush"
    return None

# 스트레이트 플러쉬인지
def isStraight(hand):
    # 종류가 같으면
    if (hand[0].suit == hand[1].suit and
        hand[1].suit == hand[2].suit and
        hand[2].suit == hand[3].suit and
        hand[3].suit == hand[4].suit):

        valList = []
        for card in hand:
            valList.append(card.value)
        valList.sort()

        # 연속되는 숫자가 있는지
        if (valList[0] + 1 == valList[1] and
            valList[1] + 1 == valList[2] and
            valList[2] + 1 == valList[3] and
            valList[3] + 1 == valList[4] ):
            return "Straight Flush"

    return None

# 포카드인지
def isFourCard(hand):

    valList = []
    for card in hand:
        valList.append(card.value)
    valList.sort()

    # 같은 숫자가 4개인 경우
    for i in range(1, 14):
        if valList.count(i) == 4:
            return "Four of a Kind"
    return None


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

    # 전체 카드 섞기
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            random.shuffle(self.cards)

    # card 한개를 뽑아 반환해주는 함수
    def deal(self):
        return self.cards.pop()

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
    def discard(self):
        return self.hand.pop()

while True:
    myDeck = Deck()
    myDeck.shuffle()

    kim = Player("kim")
    kim.draw(myDeck, 5)
    kim.showHand()

    kwon = Player("kwon")
    kwon.draw(myDeck, 5)
    kwon.showHand()

    shim = Player("shim")
    shim.draw(myDeck, 5)
    shim.showHand()

    mun = Player("mun")
    mun.draw(myDeck, 5)
    mun.showHand()

    han = Player("han")
    han.draw(myDeck, 5)
    han.showHand()

    chae = Player("chae")
    chae.draw(myDeck, 5)
    chae.showHand()

    break

