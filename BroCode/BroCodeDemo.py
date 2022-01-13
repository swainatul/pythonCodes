import time

# for loop for cojuntdown
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy new year!!!")

#nested loop
# from builtins import range
#
# rows = int(input("Enter the number off rows: "))
# columns = int(input("Enter the number off columns: "))
# symbol = input("Enter the symbol: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol,end="")
#     print()

#lists

food = ["banana", "Apple","pizza"]

food.append("peach")
food.append("sushi")
food.remove("banana")
#food.pop()
food.insert(0,"Cardamom")
food.sort()
food.clear()

for i in food:
    print(i)