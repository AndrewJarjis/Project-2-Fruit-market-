print("Welcome to the GC Fruit Market!")
print("What is your name?")
name = input()
fruits = ["Apple", "Grape", "Orange"]
fruits_bought = [0, 0, 0]
prices = [2, 1, 3]
running = True
while running:
    print("Welcome " + name + ". Which fruit would you like to buy?")

    print("1. " + fruits[0] + " $" + str(prices[0]))
    print("2. " + fruits[1] + " $" + str(prices[1]))
    print("3. " + fruits[2] + " $" + str(prices[2]))
    fruit = int(input()) - 1
    fruits_bought[fruit] += 1
    print(f"You bought 1 {fruits[fruit]} at ${prices[fruit]}")
    print("Would you like to buy another piece of fruit?")
    yes_no = input()
    if yes_no == "y":
        running = True
    elif yes_no == "n":
        running = False
print("Order for " + name)
print(str(fruits_bought[0]) + " apple(s) at $2 apiece")
print(str(fruits_bought[1]) + " grape(s) at $1 apiece")
print(str(fruits_bought[2]) + " orange(s) at $3 apiece")

sub_total = 0
for numb in range(3):
    sub_total += fruits_bought[numb]*prices[numb]
print(f"Sub Total: ${sub_total} ")
tax = sub_total * 0.05
print(f"5% tax: ${tax:0.2f}")
total = tax + sub_total
print(f"Total: ${total:0.2f}")

