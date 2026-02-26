"""
Email Service
=============
Send email notifications via SMTP
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

from config import SMTP_CONFIG, NOTIFICATION_EMAIL, APP_NAME

logger = logging.getLogger(__name__)

def send_contact_notification(contact_data: dict) -> bool:
    """
    Send email notification when someone submits the contact form
    
    Args:
        contact_data: dict with name, email, event_date, location, message
    
    Returns:
        bool: True if email sent successfully
    """
    try:
        # Create message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"[{APP_NAME}] New Inquiry from {contact_data['name']}"
        msg["From"] = SMTP_CONFIG["user"]
        msg["To"] = NOTIFICATION_EMAIL

        # Plain text version
        text_content = f"""
New Contact Form Submission
===========================

Name: {contact_data['name']}
Email: {contact_data['email']}
Event Date: {contact_data.get('event_date', 'Not specified')}
Location: {contact_data.get('location', 'Not specified')}

Message:
{contact_data.get('message', 'No message provided')}

---
This email was sent automatically from your website contact form.
        """

        # HTML version
        html_content = f"""
        <html>
        <body style="font-family: Georgia, serif; max-width: 600px; margin: 0 auto; padding: 20px;">
            <div style="background-color: #8B4557; color: white; padding: 20px; text-align: center;">
                <h1 style="margin: 0;">KNOTS</h1>
                <p style="margin: 5px 0 0 0; font-size: 14px;">Wedding Planner & Organizer</p>
            </div>
            
            <div style="padding: 30px; background-color: #FDF8F5;">
                <h2 style="color: #8B4557; margin-top: 0;">New Contact Form Submission</h2>
                
                <table style="width: 100%; border-collapse: collapse;">
                    <tr>
                        <td style="padding: 10px 0; border-bottom: 1px solid #ddd; font-weight: bold; width: 120px;">Name:</td>
                        <td style="padding: 10px 0; border-bottom: 1px solid #ddd;">{contact_data['name']}</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px 0; border-bottom: 1px solid #ddd; font-weight: bold;">Email:</td>
                        <td style="padding: 10px 0; border-bottom: 1px solid #ddd;">
                            <a href="mailto:{contact_data['email']}" style="color: #8B4557;">{contact_data['email']}</a>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 10px 0; border-bottom: 1px solid #ddd; font-weight: bold;">Event Date:</td>
                        <td style="padding: 10px 0; border-bottom: 1px solid #ddd;">{contact_data.get('event_date', 'Not specified')}</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px 0; border-bottom: 1px solid #ddd; font-weight: bold;">Location:</td>
                        <td style="padding: 10px 0; border-bottom: 1px solid #ddd;">{contact_data.get('location', 'Not specified')}</td>
                    </tr>
                </table>
                
                <div style="margin-top: 20px;">
                    <h3 style="color: #8B4557;">Message:</h3>
                    <p style="background-color: white; padding: 15px; border-radius: 5px; border-left: 4px solid #8B4557;">
                        {contact_data.get('message', 'No message provided')}
                    </p>
                </div>
            </div>
            
            <div style="background-color: #333; color: #999; padding: 15px; text-align: center; font-size: 12px;">
                This email was sent automatically from your website contact form.
            </div>
        </body>
        </html>
        """

        msg.attach(MIMEText(text_content, "plain"))
        msg.attach(MIMEText(html_content, "html"))

        # Send email
        if SMTP_CONFIG["use_ssl"]:
            # SSL connection (port 465)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(SMTP_CONFIG["host"], SMTP_CONFIG["port"], context=context) as server:
                server.login(SMTP_CONFIG["user"], SMTP_CONFIG["password"])
                server.sendmail(SMTP_CONFIG["user"], NOTIFICATION_EMAIL, msg.as_string())
        else:
            # TLS connection (port 587)
            with smtplib.SMTP(SMTP_CONFIG["host"], SMTP_CONFIG["port"]) as server:
                server.starttls()
                server.login(SMTP_CONFIG["user"], SMTP_CONFIG["password"])
                server.sendmail(SMTP_CONFIG["user"], NOTIFICATION_EMAIL, msg.as_string())

        logger.info(f"Email notification sent successfully to {NOTIFICATION_EMAIL}")
        return True

    except Exception as e:
        logger.error(f"Failed to send email notification: {e}")
        return False
