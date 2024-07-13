# Open Redirect Vulnerability Checker

## Description

The Open Redirect Vulnerability Checker is a Python tool designed to check URLs for potential open redirect vulnerabilities. This tool allows users to check a single URL or a list of URLs from a file, and it can notify the user via WhatsApp if any URLs are found to be vulnerable.

## Features

- Check single or multiple URLs for open redirect vulnerabilities.
- Validate URLs to ensure they are properly formatted.
- Send notifications via WhatsApp if any URLs are found to be vulnerable.
- Optionally save the results to an output file.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/YASHRVY7/openredirect7.git
    cd openredirect7
    ```

2. **Install the required dependencies:**
    ```bash
    pip install twilio
    pip install argparse
    pip install urllib3 
    pip install requests 
    pip install validators 
    pip install colorama 
    ```

3. **Fill Twilio credentials:**
    Open `main.py` and add your Twilio credentials:
    ```python
    # Twilio credentials
    TWILIO_SID = "your_twilio_sid"
    TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
    TWILIO_FROM_WHATSAPP = "your_twilio_whatsapp_number"
    TWILIO_TO_WHATSAPP = "your_whatsapp_number"
    ```

## Usage

### Command Line Arguments

- `-u, --url`: URL to check for open redirect vulnerability.
- `-i, --input`: File containing URLs to check.
- `-o, --output`: File to save the output results.
- `-p, --payloads`: Additional payloads to test for open redirect.
- `-b, --blog`: Open the blog to read about the bug.

### Examples

1. **Check a single URL:**
    ```bash
    python main.py -u "https://example.com"
    ```

2. **Check URLs from a file:**
    ```bash
    python main.py -i urls.txt
    ```

3. **Save results to an output file:**
    ```bash
    python main.py -u "https://example.com" -o results.txt
    ```

4. **Check a URL with additional payloads:**
    ```bash
    python main.py -u "https://example.com" -p "add site"
    ```

5. **Open the blog:**
    ```bash
    python main.py -b
    ```

