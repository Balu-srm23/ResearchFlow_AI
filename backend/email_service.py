import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.getenv("RESEND_API_KEY")

SENDER_EMAIL = "ResearchFlow <onboarding@resend.dev>"


def send_otp_email(recipient_email: str, otp: str):

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

    try:

        resend.Emails.send(
            {
                "from": SENDER_EMAIL,
                "to": recipient_email,
                "subject": "Your ResearchFlow AI Login Code",
                "html": html,
            }
        )

    except Exception as e:
        raise Exception(f"Failed to send email: {e}")