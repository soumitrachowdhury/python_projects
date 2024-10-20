import art
print("************* Welcome to Blind Auction *************")
print(art.logo)

def start():
    name=input("What is your name? ")
    money=int(input("How much do you want to bid? $"))
    user_data[name]=money
    response=input("Is there anyone else? Type 'Yes' or 'No':\n").lower()
    print("\n" * 1000)
    if response=="yes":
        start()
    else:
        compare=0
        bidder_name=""
        for data in user_data:
           if compare<user_data[data]:
               compare=user_data[data]
               bidder_name = data

        print(f"The winner is {bidder_name} and the bid is {compare}")
        print("\n"*5)

user_data={}
start()