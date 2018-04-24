welcome_message = "Hi there, Please enter first city which on your opinion will be a good start for the game:"
exit_message_info = "Enter 'again' to continue playing, or 'exit' to leave the game."
list_of_cities_message = "Here is the list of cities you've already used and can't use again:"
continue_message = "We are glad you liked the game and want to continue... Please enter new city"
error_message = "City starts on incorrect character, or was already used, please try again."


print(welcome_message)
city = input()
city_list = list(city)
print("Here we go...the first city to start from is '%s'" % city +
      "\nNow you have to enter another city which starts on same character previous city ends on:")
list_of_cities = []

def is_city_correct(city, list_of_cities):

    new_city = input()
    new_city_list = list(new_city)
    city_list = list(city)

    if new_city_list[0] == city_list[-1] and not any(new_city in s for s in list_of_cities):
        city = new_city
        list_of_cities.append(city)
        print("Good job!")

    else:
        print(error_message + " New city should start on '%s'..." %city_list[-1])
        print("Check out list of cities which were already used: %s" %list_of_cities)
        while new_city_list[0] != city_list[-1]:
            is_city_correct(city, list_of_cities)

    print(exit_message_info)
    decision = input()

    while decision != 'again' and decision != 'exit':
        print("You should enter either 'again' or 'exit'")
        decision = input()

    if decision == 'again':
        print(continue_message)
        print("\nLast city entered is '%s'." % city)
        print(list_of_cities_message + "%s\n" % list_of_cities)
        is_city_correct(city, list_of_cities)

    elif decision == 'exit':
        print("It's sad you're leaving the game...Bye!")
        exit(1)

    else:
        print("Unknown error.")
        exit(1)

is_city_correct(city, list_of_cities)