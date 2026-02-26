"""
Contact Service
===============
Handle contact form submissions
"""

from datetime import datetime
import logging

from database.mysql_connection import get_db_cursor
from services.email_service import send_contact_notification

logger = logging.getLogger(__name__)

def save_contact_submission(data: dict) -> dict:
    """
    Save contact form submission to database
    
    Args:
        data: dict with name, email, event_date, location, message
    
    Returns:
        dict with id and success status
    """
    try:
        with get_db_cursor() as cursor:
            query = """
                INSERT INTO contact_submissions 
                (name, email, event_date, location, message, status, created_at)
                VALUES (%s, %s, %s, %s, %s, 'new', NOW())
            """
            
            # Handle event_date - convert to proper format or None
            event_date = data.get('event_date')
            if event_date and event_date.strip():
                try:
                    # Parse the date string
                    event_date = datetime.strptime(event_date, '%Y-%m-%d').date()
                except ValueError:
                    event_date = None
            else:
                event_date = None
            
            values = (
                data['name'],
                data['email'],
                event_date,
                data.get('location', 'Jakarta'),
                data.get('message', '')
            )
            
            cursor.execute(query, values)
            submission_id = cursor.lastrowid
            
            logger.info(f"Contact submission saved with ID: {submission_id}")
            
            return {
                "id": submission_id,
                "success": True
            }
            
    except Exception as e:
        logger.error(f"Failed to save contact submission: {e}")
        raise

def process_contact_submission(data: dict) -> dict:
    """
    Process a contact form submission:
    1. Save to database
    2. Send email notification
    
    Args:
        data: dict with name, email, event_date, location, message
    
    Returns:
        dict with success status and messages
    """
    result = {
        "success": False,
        "saved": False,
        "email_sent": False,
        "message": ""
    }
    
    try:
        # Step 1: Save to database
        save_result = save_contact_submission(data)
        result["saved"] = save_result["success"]
        result["id"] = save_result.get("id")
        
        # Step 2: Send email notification
        email_sent = send_contact_notification(data)
        result["email_sent"] = email_sent
        
        # Determine overall success
        if result["saved"]:
            result["success"] = True
            if result["email_sent"]:
                result["message"] = "Thank you for your inquiry! We'll get back to you within 24 hours."
            else:
                result["message"] = "Thank you for your inquiry! We received your message and will contact you soon."
                logger.warning("Contact saved but email notification failed")
        else:
            result["message"] = "Sorry, there was an error. Please try again or contact us directly."
            
    except Exception as e:
        logger.error(f"Error processing contact submission: {e}")
        result["message"] = "Sorry, there was an error. Please try again or contact us directly."
        
    return result

def get_all_submissions(status: str = None, limit: int = 100) -> list:
    """
    Get all contact submissions (for admin purposes)
    
    Args:
        status: Filter by status (new, read, replied, archived)
        limit: Maximum number of records to return
    
    Returns:
        list of contact submissions
    """
    try:
        with get_db_cursor() as cursor:
            if status:
                query = """
                    SELECT id, name, email, event_date, location, message, status, created_at
                    FROM contact_submissions
                    WHERE status = %s
                    ORDER BY created_at DESC
                    LIMIT %s
                """
                cursor.execute(query, (status, limit))
            else:
                query = """
                    SELECT id, name, email, event_date, location, message, status, created_at
                    FROM contact_submissions
                    ORDER BY created_at DESC
                    LIMIT %s
                """
                cursor.execute(query, (limit,))
            
            results = cursor.fetchall()
            
            # Convert datetime objects to strings for JSON serialization
            for row in results:
                if row.get('event_date'):
                    row['event_date'] = row['event_date'].isoformat()
                if row.get('created_at'):
                    row['created_at'] = row['created_at'].isoformat()
            
            return results
            
    except Exception as e:
        logger.error(f"Failed to get submissions: {e}")
        return []
