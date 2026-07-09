import os
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp-relay.brevo.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
SENDER_EMAIL = os.getenv("SENDER_EMAIL", EMAIL_USER)


def send_otp_email(recipient_email: str, otp: str):
    if not EMAIL_USER:
        raise ValueError("EMAIL_USER is not set in environment variables.")
    if not EMAIL_PASS:
        raise ValueError("EMAIL_PASS is not set in environment variables.")
    if not SENDER_EMAIL:
        raise ValueError("SENDER_EMAIL is not set in environment variables.")

    subject = "Your ResearchFlow AI Login Code"

    html = f"""
    <html>
      <body style="font-family: Arial, sans-serif; background:#f4f4f5; padding:20px;">
        <div style="max-width:600px;margin:auto;background:white;padding:40px;border-radius:10px;">
            <h2 style="text-align:center;color:#111827;">
                ResearchFlow AI Login
            </h2>

            <p>Hello,</p>

            <p>
                Use the following One-Time Password to login.
            </p>

            <div style="
                font-size:36px;
                text-align:center;
                font-weight:bold;
                letter-spacing:8px;
                margin:30px;
                color:#4f46e5;
            ">
                {otp}
            </div>

            <p>This OTP expires in 10 minutes.</p>

            <p>If you didn't request this email, simply ignore it.</p>
        </div>
      </body>
    </html>
    """

    text = f"Your ResearchFlow AI login code is: {otp}\nThis OTP expires in 10 minutes."

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = SENDER_EMAIL
    message["To"] = recipient_email

    message.attach(MIMEText(text, "plain"))
    message.attach(MIMEText(html, "html"))

    try:
        if EMAIL_PORT == 465:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT, context=context) as server:
                server.login(EMAIL_USER, EMAIL_PASS)
                server.sendmail(SENDER_EMAIL, recipient_email, message.as_string())
        else:
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                server.ehlo()
                server.starttls(context=ssl.create_default_context())
                server.ehlo()
                server.login(EMAIL_USER, EMAIL_PASS)
                server.sendmail(SENDER_EMAIL, recipient_email, message.as_string())

    except Exception as e:
        raise Exception(f"Failed to send email: {e}")