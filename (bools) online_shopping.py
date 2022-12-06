# online_shopping.py
#
# @ author: J. T. Cotterill
# date: October 2022

shopping_cart = int(input('Enter number of items in cart:\n'))
guest_login = str(input('Is the shopper using a guest login? (yes or no):\n')).lower()
registered = str(input('Is the shopper registered? (yes or no):\n')).lower()
gift_card = str(input('Is the shopper purchasing a giftcard? (yes or no):\n')).lower()

#Shopping cart is empty?

if shopping_cart >= 1:
    shopping_cart_full = True

else:
    shopping_cart_full = False

#Using a guest login?

if guest_login == 'yes':
    guest_login_used = True

else:
    guest_login_used = False

#Is the shopper registered?

if registered == 'yes':
    is_registered = True

else:
    is_registered = False

#Buying a giftcard?

if gift_card == 'yes':
    gift_card_purchased = True

else:
    gift_card_purchased = False

if (is_registered or guest_login_used) and (shopping_cart_full or gift_card_purchased) == True:
    print('Purchase processed.')

else:
    print('Payment failed.')

#This code was also one of my creations with boolean logic. It has the same pitfall as the other practice task. It uses longform code to do
#something which could be achieved with shorter code.
