import random


class Card(object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)  # Define possible card ranks
    SUITS = ('♠', '♦', '♥', '♣')  # Define possible card suits

    def __init__(self, rank, suit):
        self.rank = rank  # Initialize card rank
        self.suit = suit  # Initialize card suit

    def __str__(self):
        # Convert numeric rank to corresponding letter for face cards
        if self.rank == 14:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 11:
            rank = 'J'
        else:
            rank = self.rank
        return str(rank) + self.suit

    # Methods for comparing cards based on rank
    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank


class Deck(object):
    def __init__(self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(rank, suit)
                self.deck.append(card)  # Create a deck of cards

    def shuffle(self):
        random.shuffle(self.deck)  # Shuffle the deck

    def __len__(self):
        return len(self.deck)  # Get the number of cards remaining in the deck

    def deal(self):
        if len(self) == 0:
            return None
        else:
            return self.deck.pop(0)  # Deal a card from the deck


def point(hand):
    sortedHand = sorted(hand, reverse=True)
    c_sum = 0
    rankList = []
    for card in sortedHand:
        rankList.append(card.rank)
    c_sum = rankList[0] * 13 ** 4 + rankList[1] * 13 ** 3 + rankList[2] * 13 ** 2 + rankList[3] * 13 + rankList[4]
    return c_sum  # Calculate player's total point


class Poker(object):
    def __init__(self, numHands):
        self.deck = Deck()
        self.deck.shuffle()  # Initialize and shuffle the deck
        self.hands = []
        self.tlist = []  # Create a list to store total_point
        numCards_in_Hand = 5

        for i in range(numHands):
            hand = []
            for j in range(numCards_in_Hand):
                hand.append(self.deck.deal())  # Deal cards to each player
            self.hands.append(hand)

    def isRoyal(self, hand):
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 10
        curSuit = sortedHand[0].suit
        curRank = 14
        total_point = h * 13 ** 5 + point(sortedHand)  # Calculate total point for hand
        for card in sortedHand:
            if card.suit != curSuit or card.rank != curRank:
                flag = False
                break
            else:
                curRank -= 1
        if flag:
            print('Royal Flush')
            self.tlist.append(total_point)
        else:
            self.isStraightFlush(sortedHand)  # Check for Royal Flush, else check for Straight Flush

    def isStraightFlush(self, hand):
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 9
        curSuit = sortedHand[0].suit
        curRank = sortedHand[0].rank
        total_point = h * 13 ** 5 + point(sortedHand)  # Calculate total point for hand
        for card in sortedHand:
            if card.suit != curSuit or card.rank != curRank:
                flag = False
                break
            else:
                curRank -= 1
        if flag:
            print('Straight Flush')
            self.tlist.append(total_point)
        else:
            self.isFour(sortedHand)  # Check for Straight Flush, else check for Four of a Kind

    def isFour(self, hand):
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 8
        curRank = sortedHand[1].rank
        count = 0
        total_point = h * 13 ** 5 + point(sortedHand)  # Calculate total point for hand
        for card in sortedHand:
            if card.rank == curRank:
                count += 1
        if not count < 4:
            flag = True
            print('Four of a Kind')
            self.tlist.append(total_point)
        else:
            self.isFull(sortedHand)  # Check for Four of a Kind, else check for Full House

    def isFull(self, hand):
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 7
        total_point = h * 13 ** 5 + point(sortedHand)  # Calculate total point for hand
        mylist = []  # Create a list to store ranks
        for card in sortedHand:
            mylist.append(card.rank)
        rank1 = sortedHand[0].rank
        rank2 = sortedHand[-1].rank
        num_rank1 = mylist.count(rank1)
        num_rank2 = mylist.count(rank2)
        if (num_rank1 == 2 and num_rank2 == 3) or (num_rank1 == 3 and num_rank2 == 2):
            flag = True
            print('Full House')
            self.tlist.append(total_point)
        else:
            flag = False
            self.isFlush(sortedHand)  # Check for Full House, else check for Flush

    def isFlush(self, hand):
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 6
        total_point = h * 13 ** 5 + point(sortedHand)  # Calculate total point for hand
        curSuit = sortedHand[0].suit
        for card in sortedHand:
            if not (card.suit == curSuit):
                flag = False
                break
        if flag:
            print('Flush')
            self.tlist.append(total_point)
        else:
            self.isStraight(sortedHand)  # Check for Flush, else check for Straight

    def isStraight(self, hand):
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 5
        total_point = h * 13 ** 5 + point(sortedHand)  # Calculate total point for hand
        curRank = sortedHand[0].rank
        for card in sortedHand:
            if card.rank != curRank:
                flag = False
                break
            else:
                curRank -= 1
        if flag:
            print('Straight')
            self.tlist.append(total_point)
        else:
            self.isThree(sortedHand)  # Check for Straight, else check for Three of a Kind

    def isThree(self, hand):
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 4
        total_point = h * 13 ** 5 + point(sortedHand)  # Calculate total point for hand
        curRank = sortedHand[2].rank
        mylist = []
        for card in sortedHand:
            mylist.append(card.rank)
        if mylist.count(curRank) == 3:
            flag = True
            print("Three of a Kind")
            self.tlist.append(total_point)
        else:
            flag = False
            self.isTwo(sortedHand)  # Check for Three of a Kind, else check for Two Pair

    def isTwo(self, hand):
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 3
        total_point = h * 13 ** 5 + point(sortedHand)  # Calculate total point for hand
        rank1 = sortedHand[1].rank
        rank2 = sortedHand[3].rank
        mylist = []
        for card in sortedHand:
            mylist.append(card.rank)
        if mylist.count(rank1) == 2 and mylist.count(rank2) == 2:
            flag = True
            print("Two Pair")
            self.tlist.append(total_point)
        else:
            flag = False
            self.isOne(sortedHand)  # Check for Two Pair, else check for One Pair

    def isOne(self, hand):
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 2
        total_point = h * 13 ** 5 + point(sortedHand)  # Calculate total point for hand
        mylist = []
        mycount = []
        for card in sortedHand:
            mylist.append(card.rank)
        for each in mylist:
            count = mylist.count(each)
            mycount.append(count)
        if mycount.count(2) == 2 and mycount.count(1) == 3:
            flag = True
            print("One Pair")
            self.tlist.append(total_point)
        else:
            flag = False
            self.isHigh(sortedHand)  # Check for One Pair, else check for High Card

    def isHigh(self, hand):
        sortedHand = sorted(hand, reverse=True)
        flag = True
        h = 1
        total_point = h * 13 ** 5 + point(sortedHand)  # Calculate total point for hand
        mylist = []
        for card in sortedHand:
            mylist.append(card.rank)
        print("High Card")
        self.tlist.append(total_point)  # Identify High Card and calculate total point


class Player(object):
    def __init__(self, balance):
        self.balance = balance  # Initialize player's balance

    def place_bet(self, amount):
        self.balance -= amount
        return amount  # Deduct bet amount from player's balance

    def receive_winnings(self, amount):
        self.balance += amount  # Add winning amount to player's balance


class Bets(object):
    def __init__(self, players):
        self.players = players
        self.current_bets = {player: 0 for player in players}  # Initialize current bets for each player

    def place_bet(self, player, amount):
        if player in self.players and amount <= player.balance:
            self.current_bets[player] += player.place_bet(amount)
            return True
        return False  # Place a bet for a player if conditions are met

    def payout(self, winner):
        total_pot = sum(self.current_bets.values())
        for player, bet_amount in self.current_bets.items():
            if player == winner:
                winnings = total_pot - bet_amount
                player.receive_winnings(winnings)
            self.current_bets[player] = 0  # Distribute winnings to the winner and reset current bets


def main():
    start = ''
    while start != 'start':
        start = input('Type "start" to play (2 player): ')
    if start.lower() == 'start':
        num_players = 2
        players = [Player(100) for _ in range(num_players)]
        bets = Bets(players)
        game = Poker(num_players)  # Start the poker game with specified number of players

        num_cards_in_hand = len(game.hands[0])

        for card_index in range(num_cards_in_hand):
            for player_index in range(num_players):
                hand = game.hands[player_index][:card_index + 1]
                sorted_hand = sorted(hand, reverse=True)

                print(f"Hand {player_index + 1}: ", end="")
                for card in sorted_hand:
                    print(card, end=' ')

                bet_amount = int(input(f"\nPlayer {player_index + 1}, place your bet: "))
                bets.place_bet(players[player_index], bet_amount)

                print()
            print(f'Current pot: {sum(bets.current_bets.values())}')  # Display current pot

        for i in range(num_players):
            cur_hand = game.hands[i]
            game.isRoyal(cur_hand)  # Evaluate hands and determine winner

        if game.tlist:
            max_point = max(game.tlist)
            max_index = game.tlist.index(max_point)
            winner = players[max_index]

            total_pot = sum(bets.current_bets.values())

            bets.payout(winner)

            print(f'\nHand {max_index + 1} wins')
            print(f'Player {max_index + 1} wins: {total_pot}')  # Identify and display winner
        else:
            print("No hands evaluated.")


main()
