#exs1
class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        # Format the call record
        call_record = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_record)
        
        # Add to call history
        self.call_history.append(call_record)
        # Traditionally, the receiver would also have a record
        other_phone.call_history.append(f"{self.phone_number} called you")

    def show_call_history(self):
        print(f"\n--- Call History for {self.phone_number} ---")
        for entry in self.call_history:
            print(entry)

    def send_message(self, other_phone, content):
        message_data = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        # Add message to both the sender and the receiver's list
        self.messages.append(message_data)
        other_phone.messages.append(message_data)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}")

    def show_outgoing_messages(self):
        print(f"\n--- Outgoing Messages from {self.phone_number} ---")
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(f"To: {msg['to']} | Content: {msg['content']}")

    def show_incoming_messages(self):
        print(f"\n--- Incoming Messages to {self.phone_number} ---")
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(f"From: {msg['from']} | Content: {msg['content']}")

    def show_messages_from(self, other_phone):
        print(f"\n--- Messages from {other_phone.phone_number} to {self.phone_number} ---")
        for msg in self.messages:
            if msg["from"] == other_phone.phone_number and msg["to"] == self.phone_number:
                print(f"Content: {msg['content']}")
                
#exs2
# 1. Instantiate two phone objects
iphone = Phone("555-0101")
pixel = Phone("555-0202")

# 2. Test Calling
iphone.call(pixel)
pixel.call(iphone)
iphone.show_call_history()

# 3. Test Messaging
iphone.send_message(pixel, "Hey! Are we still meeting at 5?")
pixel.send_message(iphone, "Yes, see you there!")
iphone.send_message(pixel, "Don't forget the snacks.")

# 4. Test Filtering Methods
pixel.show_incoming_messages()   # Should show 2 messages from iphone
iphone.show_outgoing_messages()   # Should show 2 messages to pixel
iphone.show_messages_from(pixel)  # Should show 1 message: "Yes, see you there!"