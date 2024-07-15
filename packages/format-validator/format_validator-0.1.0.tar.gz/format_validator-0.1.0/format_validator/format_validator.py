import re 

def validate_email(email):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    found_emails = re.findall(email_pattern, email)
    
    if found_emails:
        return True
    else:
        return False


def validate_phone(phone_number):
    # Define the regular expression patterns for various formats
    patterns = [
        r'^\(\d{3}\) \d{3}-\d{4}$',        # (123) 456-7890
        r'^\d{3}-\d{3}-\d{4}$',             # 123-456-7890
        r'^\d{3}\.\d{3}\.\d{4}$',           # 123.456.7890
        r'^\d{10}$',                        # 1234567890
        r'^\+\d{11,15}$',                   # +31636363634
        r'^\d{3}-\d{8}$',                   # 075-63546725
    ]
    
    # Check each pattern
    for pattern in patterns:
        if re.match(pattern, phone_number):
            return True
    
    # If no pattern matches
    return False


def validate_date(date_string):
    # Define the regular expression patterns for various formats
    patterns = [
        r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$',      # MM/DD/YYYY
        r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$',      # DD/MM/YYYY
        r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$',      # YYYY-MM-DD
        r'^(0[1-9]|[12][0-9]|3[01])-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{4}$'  # DD-MMM-YYYY
    ]
    
    # Check each pattern
    for pattern in patterns:
        if re.match(pattern, date_string):
            return True
    
    # If no pattern ma
    




