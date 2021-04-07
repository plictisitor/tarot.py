# tarot.py
First Occult Related Python Library  
##### Soon on pypi.org

# How to use
Download the `tarot` folder and place it in your project dir. Then you can use `from tarot import *`

# Examples

### Create cards
```py
from tarot import *

# create cards
cardA = Card("The Fool", 0) 
cardB = Card("The Magician", 1)
cardC = Card("The High Priestess", 2)
```

### Create Decks

```py
# create a deck with these cards
deck1 = cardA + cardB
# create a deck with only 1 card
deck2 = Deck([cardC])
```

### Reverse cards

```py
print(", ".join((deck1.reveal()))) # The Fool, The Magician
-deck1[0] # reverse the first card in deck1
print(", ".join((deck1.reveal()))) # The Fool Reversed, The Magician
-deck1 # reverse all the cards in deck1 (rotate 180)
print(", ".join((deck1.reveal()))) # The Fool, The Magician Reversed
```

### Merge 2 Decks Together

```py
deck1 += deck2 # merge deck1 with deck2
print(", ".join((deck1.reveal()))) # The Fool, The Magician Reversed, The High Priestess
```

### Calculate numerologic value of a deck

```py
# sum the numbers on each card (for numerology) 
print(+deck1) # 3
```

### Check if a deck contains a specified card

```py
# check if a deck contains a card (doesn't matter if it's reversed)
print(cardA in deck1) # True
print(cardB in deck2) # False
```

### Get cards from a deck

```py
# get a random card from deck1
print((deck1 >> 1).name) # The Magician Reversed

# get two random cards from deck1
print((deck1 >> 2).reveal()) # ['The Fool', 'The Magician Reversed']

# take the last 2 cards in deck1 and print the remaining card
print((deck1-2).reveal()) # ['The High Priestess', 'The Magician Reversed']
print(deck1.reveal()) # ['The Fool']
```

### Shuffle a Deck

```py
print(deck1.reveal()) # ['The Fool', 'The Magician', 'The High Priestess']

~deck1 # shuffle
print(deck1.reveal()) # ['The Magician Reversed', 'The High Priestess', 'The Fool Reversed']
```

### Pop Cards from a Deck

```py
# pop the last card from the deck
print((deck1-1).name) # The Fool Reversed
# pop the other 2 cards from the deck
print((deck1-2).reveal()) # ['The High Priestess', 'The Magician']
```

### Check if a deck is empty

```py
# check if deck is empty
if len(deck1) == 0:
	print("Deck 1 is empty.")
```

### Duplicate a Card

```py
deck2 += deck2[0] # duplicate the first card in deck2
print("Deck 2 has %s cards." % len(deck2))
```

### Create Spreads and Read it
```py
spread = RWDeck>>3 # extract 3 random cards, all upright
print(spread.format("Past: %s, present: %s, future: %s")) # add the cards to the string
# Past: Judgement Reversed, present: Three of Cups, future: Nine of Swords

print("Numerological reading: %d" % ((+spread)%10))
# Numerological reading: 32

print("How many hours will I sleep? %d" % +(RWDeck>>1)) # 9

rotd = (~EFRunes)>>1;
print("Rune of the day? %s\nMeaning: %s" % (rotd.name, rotd.assoc[0])) # Ehwaz, ....
print("Classic cartomancy? %s" % (PCDeck>>1).name) # King of Clubs
```
