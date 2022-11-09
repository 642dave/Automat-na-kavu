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
    kc1 = int(input("Kolik 1 Kc chcete vlozit?: ")) * 1
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

def fill_in_ingredients():
    return(resources)

def calculate_ingredients(drink_name):
    if drink_name == "espresso":
        rest_of_ingredience["water"] = rest_of_ingredience["water"] - MENU["espresso"]["ingredients"]["water"]
        rest_of_ingredience["milk"] = rest_of_ingredience["milk"] - MENU["espresso"]["ingredients"]["milk"]
        rest_of_ingredience["coffee"] = rest_of_ingredience["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        print(f"Zbyle ingredience {rest_of_ingredience}")
    elif drink_name == "latte":
        rest_of_ingredience["water"] = rest_of_ingredience["water"] - MENU["latte"]["ingredients"]["water"]
        rest_of_ingredience["milk"] = rest_of_ingredience["milk"] - MENU["latte"]["ingredients"]["milk"]
        rest_of_ingredience["coffee"] = rest_of_ingredience["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        print(f"Zbyle ingredience {rest_of_ingredience}")
    elif drink_name == "cappuccino":
        rest_of_ingredience["water"] = rest_of_ingredience["water"] - MENU["cappuccino"]["ingredients"]["water"]
        rest_of_ingredience["milk"] = rest_of_ingredience["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        rest_of_ingredience["coffee"] = rest_of_ingredience["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        print(f"Zbyle ingredience {rest_of_ingredience}")



# ==Kod automatu==
# Volba uzivatele, jaky chce napoj
user_choice = input("Co byste si dal/a? (espresso/latte/cappuccino): ")

# Nacitame puvodni mnozstvi ingredienci
rest_of_ingredience = fill_in_ingredients()


# Vypocita, kolik zbyva ingredienci
calculate_ingredients(user_choice)


# Kontrolni report
if user_choice == "report":
    report(rest_of_ingredience)

# Hlavni kod automatu
if user_choice == "espresso":
    sum = coins()
    print(f"Cena espressa je {espresso_price}")
    calculate_change(sum, espresso_price)
elif user_choice == "latte":
    sum = coins()
    print(f"Cena latte je {latte_price}")
    calculate_change(sum, latte_price)
elif user_choice == "cappuccino":
    sum = coins()
    print(f"Cena cappuccina je {cappuccino_price}")
    calculate_change(sum, cappuccino_price)