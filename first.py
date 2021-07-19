def conversion():
    user_coin = input('what coin do you use?')
    if user_coin != "shekel" or user_coin != "dollar" :
        print("wrong coin")
    else:
        conv = input('to which currency you would like to convert?')
        if conv != "shekel" or conv != "dollar" :
            print("wrong coin")
        else:
            if user_coin == shekel and conv == dollar:
                return shekel*3.28
            if user_coin== dollar and conv == shekel:
                return dollar/3.28
def main():
    conversion()
                    
    