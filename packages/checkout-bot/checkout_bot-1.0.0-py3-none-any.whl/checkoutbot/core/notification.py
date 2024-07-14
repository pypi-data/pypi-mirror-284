import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email, from_email, password, smtp_server, smtp_port):
    """
    Send an email notification.

    Args:
        subject (str): The email subject.
        body (str): The email body.
        to_email (str): The recipient's email address.
        from_email (str): The sender's email address.
        password (str): The sender's email password.
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.

    Returns:
        None
    """
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")
