# Created by: Mr. Coxall
# Created on: Nov 2017
# Created for: ICS3U
# This program just shows cards ...

import ui

# global varibles
user_card1_image = None
user_card2_image = None
user_card3_image = None
dealer_card1_image = None
dealer_card2_image = None
dealer_card3_image = None

def show_cards(sender):
    # show cards
    
    user_card1_image = ui.Image.named('card:BackBlue2')
    view['user_card1_imageview'].image = user_card1_image
    user_card2_image = ui.Image.named('card:BackBlue2')
    view['user_card2_imageview'].image = user_card2_image
    user_card3_image = ui.Image.named('card:BackBlue2')
    view['user_card3_imageview'].image = user_card3_image
    view['user_card3_imageview'].alpha = 0.1
    dealer_card1_image = ui.Image.named('card:BackBlue2')
    view['dealer_card1_imageview'].image = user_card1_image
    dealer_card2_image = ui.Image.named('card:BackBlue2')
    view['dealer_card2_imageview'].image = user_card2_image
    dealer_card3_image = ui.Image.named('card:BackBlue2')
    view['dealer_card3_imageview'].image = user_card3_image
    
    
view = ui.load_view()
view.present('fullscreen')

show_cards(None)
