from mtgsdk import Card

# partial name match
#search = input("Input card search: \n")
cards = Card.where(name="black lotus").all()
#print(cards)

for card in cards:
    if card.image_url:
        print(card.image_url)
        break
    #print(card.name, card.set_name, card.image_url)
#print(cardimage)