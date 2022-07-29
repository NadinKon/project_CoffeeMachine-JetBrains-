class CoffeeMachine:
    def __init__(self, money=550, water=400, milk=540, beans=120, cups=9):
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups

    def buying(self, coffee_choices):
        if coffee_choices == '1' and self.water >= 250 and self.beans >= 16 and self.cups >= 1:
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
            print('I have enough resources, making you a coffee!')
        elif coffee_choices == '2' and self.water >= 350 and self.beans >= 20 and self.cups >= 1 and self.milk >= 75:
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
        elif coffee_choices == '3' and self.water >= 200 and self.beans >= 12 and self.cups >= 1 and self.milk >= 100:
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6
        else:
            print('Sorry, not enough water!')


    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input())
        print()


    def take(self):
        print(f"I gave you ${self.money}")
        print()
        self.money = 0

    def remaining(self):
        return f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money"""

    def action(self):
        while True:
            choice = input("Write action (buy, fill, take, remaining, exit):")
            print()
            if choice.lower() == "buy":
                #print()
                coffee_choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
                if coffee_choice == "back":
                    continue
                else:
                    self.buying(coffee_choice)
            elif choice.lower() == "fill":
                self.fill()
            elif choice.lower() == "take":
                self.take()
            elif choice.lower() == "remaining":
                print(self.remaining())
                print()
            else:
                exit()


f = CoffeeMachine()
f.action()