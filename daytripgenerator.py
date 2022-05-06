import random

destinations = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',  'Wisconsin', 'Wyoming']
restaurants = ['Steak House', 'Italian', 'Indian', 'McDonalds', 'Starbucks', 'Chick-fil-A', 'Taco Bell', 'Wendys', 'Burger King', 'Dunkin Donuts', 'Subway', 'Dominos', 'Chipotle Mexican Grill', 'Sonic Drive-In', 'Pizza Hut', 'Panera Bread', 'KFC', 'Popeyes Louisiana Kitchen', 'Arbys', 'Dairy Queen', 'Little Caesars', 'Panda Express', 'Jack in the Box', 'Olive Garden', 'Papa Johns', 'Buffalo Wild Wings', 'Applebees', 'Chilis Grill & Bar']
transportation = ['Rental Car', 'Bus Pass', 'Limo', 'Airplane', 'Helicopter', 'By Foot', 'Trolley', 'Train', 'Horse Drawn Cart', 'Bicycle', 'Motorcycle']
entertainment = ['Live Theatre', 'Amusement Park', 'Bird Watching', 'Movie Theater', 'Comedy Show', 'Live Concert', 'Poetry reading', 'Art Class', 'Sporting event', 'Arcade', 'Circus', 'Magic Show', 'Food Festival', 'Shopping', 'Skydiving']

#randomly select destination
def generate_destination():
    return random.choice(destinations)

#randomly select restaurant
def generate_restaurant():
    return random.choice(restaurants)

#randomly select transportation
def generate_transportation():
    return random.choice(transportation)

#randomly select entertainment
def generate_entertainment():
    return random.choice(entertainment)

#confirm selections or reselect, print finalized trip, 
def confirm_generated_selections(destination, restaurant, mode_of_travel, recreation):
    trip_confirmed = False
    while trip_confirmed == False:
        
        destination_confirm = 'n'
        while destination_confirm == 'n':
            destination_confirm = input(f'We selected {destination} for you, do you accept? y/n ')
            if destination_confirm == 'n':
                destinations.remove(destination)
                destination = generate_destination()
            elif destination_confirm == 'y':
                print(f'Great {destination} it is')
                destination_confirm = 'y'

        restaurant_confirm = 'n'
        while restaurant_confirm == 'n':
            restaurant_confirm = input(f'We selected {restaurant} for you, do you accept? y/n ')
            if restaurant_confirm == 'n':
                restaurants.remove(restaurant)
                restaurant = generate_restaurant()
            elif restaurant_confirm == 'y':
                print(f'Great {restaurant} it is')
                restaurant_confirm = 'y'
        
        transportation_confirm = 'n'
        while transportation_confirm == 'n':
            transportation_confirm = input(f'We selected {mode_of_travel} for you, do you accept? y/n ')
            if transportation_confirm == 'n':
                transportation.remove(mode_of_travel)
                mode_of_travel = generate_transportation()
            elif transportation_confirm == 'y':
                print(f'Great {mode_of_travel} it is')
                transportation_confirm = 'y'

        entertainment_confirm = 'n'
        while entertainment_confirm == 'n':
            entertainment_confirm = input(f'We selected {recreation} for you, do you accept? y/n ')
            if entertainment_confirm == 'n':
                entertainment.remove(recreation)
                recreation = generate_entertainment()
            elif entertainment_confirm == 'y':
                print(f'Great {recreation} it is')
                entertainment_confirm = 'y'

        if destination_confirm == 'y' and restaurant_confirm == 'y' and transportation_confirm == 'y' and entertainment_confirm == 'y':
            trip_confirmed = True

    print('The trip generated for you is: ')
    print(f'Destination: {destination}')
    print(f'Transportation: {mode_of_travel}')
    print(f'Restaraunt: {restaurant}')
    print(f'Entertainment: {recreation}')
    
    #finalizes trip 
    confirm_final = input('Would you like to finalize this trip? y/n ')
    if confirm_final == 'n':
        startover = input('Ok do you want to start over? y/n ')
        if startover =='y':
            confirm_generated_selections(destination, restaurant, mode_of_travel, recreation)
        else:
            print('Ok, exiting program. Please try again later')
    else:
        print(f'Your completed trip is to {destination} with dinner at {restaurant}, transportation will be {mode_of_travel} and {recreation} for entertainment.')


#calls functions to generate options and store values
destination = generate_destination()
restaurant = generate_restaurant()
mode_of_travel = generate_transportation()
recreation = generate_entertainment()

#calls function to confirm previously generated trip options
confirm_generated_selections(destination, restaurant, mode_of_travel, recreation)

