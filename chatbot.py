import openai

def generate_response(messages):
    base_message = {
        'role': 'system',
        'content': """
    Top Shelf Trailers specializes in incredibly durable and high-quality dump trailers. We are located at 850516 US HWY 17, Yulee, FL. 32097. 

    Our office hours are Monday through Friday from 8am to 5pm, and we're closed from 11am to 12pm for lunch. You can reach us at 800-797-0384 during these hours.

    At Top Shelf Trailers, we offer a range of dump trailers in various sizes and configurations:

    - Bumper pull trailers in sizes 6x12x2 ($8495), 6x12x3 ($8995), 6x12x4 ($8995), 7x14x2 ($8995), 7x14x3 ($9495), 7x14x4 ($9495), 7x16x2 ($10295), 7x16x3 ($10495), and 7x16x4 ($10495). Please note that 7x18 and 7x20 sizes are not common and we recommend a triple axle configuration for these.
    - Gooseneck trailers in sizes 7x14x2 ($10995), 7x14x3 ($11495), 7x14x4 ($11495), 7x16x2 ($12295), 7x16x3 ($12495), 7x16x4 ($12495), and 8x20 in 2', 3' or 4' wall heights ($21000).

    We have 14k, 16k, 20k, 24k, and 30k axle options. We build our 6' and 7' wide trailers with dual cylinder, and telescopic three stage cylinders available for our 7x14 and 7x16's at not additional cost.


    If you need assistance with something that I couldn't help with, please don't hesitate to call us directly at 800-797-0384 during our office hours. We're here to help!
        """
}



    # Append the user's messages to the base message.
    full_messages = [base_message] + messages

    # Use the chat model to generate a response.
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',  # Use a chat model.
        messages=full_messages,
    )

    # Return the generated response.
    return response['choices'][0]['message']['content']

# Test the function with a sample message.
messages = [
    {'role': 'user', 'content': 'Hi, how much is your 7x14x4? Both bumper pull and gooseneck options. DO you offer telescopic cylinders?'}
]
print(generate_response(messages))
