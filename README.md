# Twilio SMS Bulk Sender

This project provides a Python script to send bulk SMS messages using the [Twilio API](https://www.twilio.com/docs/sms). The script reads a list of phone numbers and messages from a JSON file and sends each message individually.

## Features

- **Twilio Integration**: Sends SMS messages via Twilio's REST API.
- **Bulk SMS**: Reads multiple phone numbers and messages from a JSON file.
- **Logging**: Displays status messages for each SMS sent, including errors.
- **Rate Limiting**: Adds a delay between messages to avoid exceeding API limits.

## Prerequisites

1. Python 3.x
2. [Twilio Python Library](https://www.twilio.com/docs/libraries/python)

## Installation

### 1. Clone the repository:
   ```bash
   git clone https://github.com/0xbassiouny1337/SMS_Bulk.git

### 2.Install the required dependencies:
```bash
pip install twilio   
