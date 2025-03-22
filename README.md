Selenium Automation Script

Overview

This project is a Selenium-based automation script written in Python that automates login and new customer registration on the CRM platform of https://automationplayground.com/crm/login.html.

Prerequisites

Ensure you have the following installed on your system before running the script:

Python (>= 3.x)

Google Chrome browser

Chrome WebDriver (Ensure the WebDriver version matches your Chrome browser version)

Required Python libraries:

selenium

time

Installation

Install Python (if not already installed) from Python's official website.

Install Selenium using pip:

pip install selenium

Download Chrome WebDriver from ChromeDriver official site and add it to your system's PATH.

Usage

Clone or download this repository.

Open a terminal or command prompt in the project directory.

Run the script:

python script_name.py

Functionality

The script performs the following automated actions:

Launches Chrome browser and opens the CRM login page.

Logs in with predefined credentials.

Navigates to the new customer registration page.

Fills out and submits the registration form.

Closes the browser after execution.

Code Breakdown

Login Automation: Enters the email and password to log in.

New Customer Registration: Fills out user details including email, first name, last name, city, and state.

Form Submission: Clicks submit buttons for login and registration.

Configuration

Modify Email_id and password variables in the script to match your credentials.

Adjust the wait time to control script execution speed.

Notes

Ensure pop-ups and browser alerts are disabled to avoid execution interruptions.

If using a different browser, update the webdriver initialization accordingly.

Author

Tosin A. Williams

License

This project is open-source and available for use under the MIT License.
