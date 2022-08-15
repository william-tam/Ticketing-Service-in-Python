# This is the aviation ticketing service system in Python, I am doing this in Python and not in Java because I want to get a better sense of this language
# before my assessments for jobs, since I think this is my best language that I know. 

import json

# opening json file that contains the flight info. 
# ['Bali']['Flight_1'][0]
f = open('Ticket_Info.json')
data = json.load(f)
flight_options = data['destinations']
# CLI 
print("Hello traveler, welcome to Tam's Airlines, where would you like to go? \n")
for i in data['destinations']:
    print(i)

received_prompt = False
while received_prompt == False:
# Receive input from user. 
    input_flight = input("prompt: ")
    if input_flight not in data['destinations']: 
        print("Sorry, this destination is not available, please try again.")    
    else:
        received_prompt = True
        picked_flight = input_flight
        print("Checking flights for:", picked_flight)

# Showing flight options for the picked flight. 
for i in data['destinations'][picked_flight]:
    print(i)
    

# Show the time and price (all options) for the picked flight. 
# i = 0 
# for i in data['destinations']['Option_' + i]:
#     print(i)
#     i = i + 1

