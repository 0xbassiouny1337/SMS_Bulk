import json
from twilio.rest import Client
import time

# Your Twilio credentials
ACCOUNT_SID = ''
AUTH_TOKEN = ''
TWILIO_PHONE = ''

# Function to send SMS with phone and message
def send_sms(phone, message):
    try:
        # Initialize Twilio client
        print("Initializing Twilio client...")
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        print("Successfully authenticated with Twilio!")
        
        # Send message
        print(f"Sending message to {phone}...")
        sent_message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=phone
        )
        print(f"Message sent successfully to {phone} with SID: {sent_message.sid}")
        return sent_message.sid
    except Exception as e:
        print(f"Error sending message to {phone}: {e}")
        return None

# Function to handle sending bulk SMS from JSON file
def send_bulk_sms(json_file):
    try:
        print(f"Loading data from {json_file}...")
        with open(json_file, 'r') as file:
            data = json.load(file)
        print(f"Data loaded successfully: {len(data)} entries found.")
        
        # Send SMS for each entry
        for entry in data:
            phone = entry.get("phone")
            message = entry.get("message")
            if phone and message:
                print(f"Processing entry - Phone: {phone}, Message: {message}")
                sid = send_sms(phone, message)
                if sid:
                    print(f"Message successfully sent to {phone}, SID: {sid}")
                else:
                    print(f"Failed to send message to {phone}.")
            else:
                print("Invalid entry found in data: Missing phone or message.")
            # Small delay to avoid API rate limits (if necessary)
            time.sleep(1)
    except FileNotFoundError:
        print(f"Error: The file {json_file} was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse {json_file}. Make sure it's valid JSON.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
if __name__ == "__main__":
    json_file = 'data.json'
    print("Starting bulk SMS sending process...")
    send_bulk_sms(json_file)
    print("Bulk SMS sending process completed.")
