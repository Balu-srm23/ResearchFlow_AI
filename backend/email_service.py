import os

from dotenv import load_dotenv

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key["api-key"] = BREVO_API_KEY

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
    sib_api_v3_sdk.ApiClient(configuration)
)


def send_otp_email(recipient_email: str, otp: str):

    if not BREVO_API_KEY:
        raise ValueError("BREVO_API_KEY is missing.")

    if not SENDER_EMAIL:
        raise ValueError("SENDER_EMAIL is missing.")

    html = f"""
    <html>
      <body style="font-family:Arial;padding:40px;background:#f4f4f4;">
          <div style="background:white;padding:30px;border-radius:10px;max-width:600px;margin:auto;">
              <h2>ResearchFlow AI</h2>

              <p>Your One-Time Password is:</p>

              <h1 style="font-size:40px;letter-spacing:6px;color:#4CAF50;">
                  {otp}
              </h1>

              <p>This OTP expires in 10 minutes.</p>

              <p>If you didn't request this email, ignore this message.</p>

          </div>
      </body>
    </html>
    """

    email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": recipient_email}],
        sender={
            "name": "ResearchFlow AI",
            "email": SENDER_EMAIL
        },
        subject="ResearchFlow AI Login OTP",
        html_content=html
    )

    try:
        api_instance.send_transac_email(email)

    except ApiException as e:
        raise Exception(f"Failed to send email: {e}")