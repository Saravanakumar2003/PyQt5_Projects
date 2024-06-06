import smtplib, ssl # Import smtplib for the actual sending function and ssl for secure connection 

# Function to send email
def send_email(recipient, subject, email):    
    port = 465  # For SSL (Secure Socket Layer)
    smtp_server = "smtp.gmail.com" # Server to send email from (Gmail)
    sender = "saravanakumar.testmail@gmail.com" # Email address of the sender 
    password = "jvot pork skqs ykue" # Password of the sender's email address 

    message = f"Subject: {subject}\n\n{email}" # Message to be sent
    
    context = ssl.create_default_context() # Create a secure SSL context 
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp: # Connect to the server and send the email   
        smtp.login(sender, password) # Login to the server
        smtp.sendmail(sender, recipient, message) # Send the email to the recipient 
