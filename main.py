import random

responses = {
    "hello": ["Yeah Boss", "hey", "how can I suggest"],
    "hii": ["Yeah what's up", "hey", "how can I suggest"],
    "status": ["I am still training"],
    "open": ["Youtube", "WhatsApp"]
}

def get_response(message):
    message = message.lower()
    
    if message in responses:
        return random.choice(responses[message])
    else:
        return random.choice(["jsdhnfnldlkn", "ijgsdfiugauighh","jhgbsdifhgbvibh"])  
    
     
    while True:
        user_input = input("You :")
        response = get_response(user_input)
        print("IVAN :", response)