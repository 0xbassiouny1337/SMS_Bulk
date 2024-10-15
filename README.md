# Twilio SMS Bulk Sender

This project provides a Python script to send bulk SMS messages using the [Twilio API](https://www.twilio.com/docs/sms). The script reads a list of phone numbers and messages from a JSON file and sends each message individually.

## Features

- **Twilio Integration**: Sends SMS messages via Twilio's REST API
- **Bulk SMS**: Reads multiple phone numbers and messages from a JSON file
- **Logging**: Displays status messages for each SMS sent, including errors
- **Rate Limiting**: Adds a delay between messages to avoid exceeding API limits

## Prerequisites

- Python 3.x
- [Twilio Python Library](https://www.twilio.com/docs/libraries/python)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/0xbassiouny1337/SMS_Bulk.git
   ```

###Navigate into the project directory:
   ```bash
   cd SMS_Bulk
   ```


###Install the required dependencies:
   ```bash
   pip install twilio
   ```
##Setup Twilio Credentials

Set up your Twilio account and obtain your credentials:

- Account SID
- Auth Token
- Twilio Phone Number


Open the script and fill in the following variables with your Twilio credentials:
   ```python
   ACCOUNT_SID = 'your_account_sid'
   AUTH_TOKEN = 'your_auth_token'
   TWILIO_PHONE = 'your_twilio_phone_number'
   ```


Usage

Create a JSON file (data.json) with the following structure:

   ```json
  {
    "phone": "+1234567890",
    "message": "Hello, this is your message."
  },
  {
    "phone": "+0987654321",
    "message": "Another message."
  }
  ```

Run the script to start sending SMS messages:
   ```bash
   python script.py
   ```
** The script will load phone numbers and messages from the data.json file and send each message. **


### Error Handling

- ** Invalid JSON File **: The script will notify you if the JSON file is missing or contains errors.
- ** Missing Phone or Message**: If any phone or message fields are missing in the JSON file, the script will log an error for that entry.

### Additional Notes

- A ** 1-second delay ** is added between each SMS message to prevent exceeding Twilio's rate limits.
Ensure that your Twilio account is properly configured to send messages to the phone numbers provided in your JSON file.


### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

### Support
If you have any questions or run into any issues, please open an issue in this repository.

Made with ❤️ by [Bassiouny]
