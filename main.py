from source_data import MENU
from source_data import resources



# Zakladni nastaveni
espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]


# Funkce
def report(data):
    print(f"Voda: {data['water']}")
    print(f"Mleko: {data['milk']}")
    print(f"Kava: {data['coffee']}")

def coins():
    print("Prosim vlozte mince 1. 2, 5, 10, 20, 50")
    kc1 = int(input("Kolik 1 Kc chcete vlozit?: "))
    kc2 = int(input("Kolik 2 Kc chcete vlozit?: ")) * 2
    kc5 = int(input("Kolik 5 Kc chcete vlozit?: ")) * 5
    kc10 = int(input("Kolik 10 Kc chcete vlozit?: ")) * 10
    kc20 = int(input("Kolik 20 Kc chcete vlozit?: ")) * 20
    kc50 = int(input("Kolik 50 Kc chcete vlozit?: ")) * 50
    suma = kc1 + kc2 + kc5 + kc10 + kc20 + kc50
    print(f"Celkem jste vlozili {suma} Kc")
    return(suma)

def calculate_change(user_sum_coins, price):
    refund = user_sum_coins - price
    if refund >= 0:
        print("Napoj se pripravuje.")
        if refund > 0:
            print(f"Zde jsou penize zpet: {refund} Kc")
    else:
        print(f"Nevhodili jste dostatek penez, je zapotrebi vlozit jeste {price - user_sum_coins} Kc")




# Kod automatu
user_choice = input("Co byste si dal/a? (espresso/latte/cappuccino): ")

if user_choice == "report":
    report(resources)

if user_choice == "espresso":
    sum = coins()
elif user_choice == "latte":
    sum = coins()
elif user_choice == "cappuccino":
    sum = coins()