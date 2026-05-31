def smart_bot():

    print("Welcome to Smart Assistant")
    print("Type 'terminate' to stop the chat.\n")

    while True:

        visitor_input= input("You: ").strip().lower()

        if visitor_input in ["hi", "hello", "hey"]:
            print("Assistant: Hello! Nice to meet you.")

        elif "name" in visitor_input:
            print("Assistant: I am Smart Assistant.")

        elif "college" in visitor_input:
            print("Assistant: I can help with simple questions.")

        elif "course" in visitor_input:
            print("Assistant: Artificial Intelligence is an exciting field.")

        elif "time" in visitor_input:
            print("Assistant: Sorry, I cannot check the current time.")

        elif "thank you" in visitor_input or "thanks" in visitor_input:
            print("Assistant: You're welcome!")
            
        elif "bye"   in  visitor_input:
            print("Assistant: Good night")

        elif visitor_input == "terminate":
            print("Assistant: Chat terminated successfully.")
            break

        else:
            print("Assistant: I don't have an answer for that question.")

smart_bot()
