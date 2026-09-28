import random

try:
    print()
    print("Welcome to the Thanksgiving Farm Simulator! 🌽 ")
    print()
    farmerName = input("What is your name, farmer? (enter name): ")
    print(f"Farmer {farmerName}, your goal is to plant, harvest, and sell crops. However, the weather may prevent farming.")
    print()

    yourCash = 0
    yourCrops = []
    cropList = ["corn cobs", "pumpkins", "squash", "potatoes", "green beans"]
    weatherList = ["sunny", "rainy", "windy", "cloudy"]
    print("----- BEGIN FARMING -----")
    print()

    class Farmer:
        def __init__(self, name):
            self.name = name
            self.crop = ()
            self.weather = None

        def plantCrop(self):
            weather = random.choice(weatherList)
            self.weather = weather

            if weather == "windy":
                print("It is too windy. You cannot plant any crops!")
                print()

            else:
                crop = input(f"It is {weather}. What crop do you want to plant? (corn cobs / pumpkins / squash / potatoes / green beans): ")
                if crop in cropList:
                    print(f"You planted the {crop}!")
                    yourCrops.append(crop)
                    self.crop = crop
                    print()
                else:
                    print("That was not one of the crops you could plant!")
                    print()

        def harvestCrop(self):
            if self.weather == "windy":
                print("You cannot harvest any crops because you planted none!")
                print()

            else:
                print(f"Your {self.crop} are ready to be harvested! You recieved the {self.crop}!")
                print()

            print(f"Your current crops: {yourCrops}")
            print()

        def sellCrop(self):

            global yourCash

            if yourCrops != []:
                sellChoice = input("Would you like to try selling your crops? (yes/no): ")

                if sellChoice == "yes":
                    print()
                    print("Your customer is here.")
                    customer.describeCustomer()

                    if customer.request in yourCrops:
                        print(f"You sold the {customer.request} to your customer. Your customer payed you ${customer.payment}.")
                        yourCash += customer.payment
                        yourCrops.remove(customer.request)
                        print()

                    else:
                        print("You don't have the crop your customer wanted.")
                        print()

                else:
                    print()
                    print("Okay!")
                    print()

            else:
                pass

            print(f"Your current cash: ${yourCash}")
            print(f"Your current crops: {yourCrops}")
            print()

    class Customer:
      def __init__(self, payment, *request):
        self.payment = payment
        self.request = None

      def describeCustomer(self):
        request = random.choice(cropList)
        self.request = request
        print(f"Your customer will pay ${self.payment} for {self.request}.")

    player = Farmer(farmerName)

    customer = Customer(10.00)

    while yourCash < 100.00:
        player.plantCrop()
        player.harvestCrop()
        player.sellCrop()

    print("Congratulations! You reached $100!")

    while True:
        print()
        keepGoing = input("Do you want to keep farming? (yes/no): ")
        if keepGoing == "yes":
            print()
            player.plantCrop()
            player.harvestCrop()
            player.sellCrop()
            print()
        else:
            print("Okay!")
            break

    print("")
    print("----- END FARMING -----")
    print("")

    print("The farming season is over!")
    print(f"Your current cash: ${yourCash}")
    print(f"Your current crops: {yourCrops}")
    print("Great job!")
    print()
    print("Thanks for playing!")
    print()
    print("----- HAPPY THANKSGIVING -----")
    print()

except:
    print()
    print("Error - please try again later")
    print()