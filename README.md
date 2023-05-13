# PassCheck
PassCheck is a simple web application that checks if a password has been breached before using the Have I Been Pwned API. If the password has been breached, the application suggests a new password using the passlib library.
## Features
- Check if a password has been breached before using the Have I Been Pwned API.
- Generate a new password using the passlib library if the password has been breached.
- Display the number of times the password has been breached (if any).
- Display a suggestion for a new password (if any).

## Installation

1. Clone the repository
```python
git clone https://github.com/<username>/flask-password-checker.git 
```
2. Install the required packages:
```python
pip install -r requirements.txt
```
3. Run the application
```
python app.py
```
4. Open your web browser and go to http://localhost:5000

## Usage
1. Enter a password in the input field and click the "Check" button.
2. If the password has been breached before, the application suggests a new password.
3. If the password has not been breached before, the application displays a success message.
