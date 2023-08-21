# no_of_visits = 4
# no_of_items = 12
# if no_of_visits < 5:
#     print("New customers")
#     if no_of_items > 10:
#         print("Will get 10 percent discount")
#     else:
#         print("Will get 5 percent discount")
# elif no_of_visits == 5:
#     print("Average customers")
# elif no_of_visits > 20:
#     print("Super Loyal customers")
# else:
#     print("Loyal customers")

no_of_visits = 4
no_of_items = 3
if no_of_visits < 5 and no_of_items > 10:
    print("New customers will get 10 percent discount")
elif no_of_visits < 5 or no_of_items > 10:
    print("New customers will get 5 percent discount")
elif no_of_visits == 5:
    print("Average customers")
elif no_of_visits > 20:
    print("Super Loyal customers")
else:
    print("Loyal customers")

