"""
Contact Routes
==============
API endpoints for contact form
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import logging

from services.contact_service import process_contact_submission, get_all_submissions

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/contact", tags=["contact"])

# Request/Response Models
class ContactSubmission(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    event_date: Optional[str] = None  # Format: YYYY-MM-DD
    location: str = Field(default="Jakarta", max_length=50)
    message: Optional[str] = Field(default="", max_length=2000)

class ContactResponse(BaseModel):
    success: bool
    message: str
    id: Optional[int] = None

# Routes
@router.post("/submit", response_model=ContactResponse)
async def submit_contact_form(submission: ContactSubmission):
    """
    Submit contact form
    - Saves to database
    - Sends email notification
    """
    try:
        logger.info(f"Received contact submission from: {submission.email}")
        
        # Process the submission
        result = process_contact_submission(submission.model_dump())
        
        if not result["success"]:
            raise HTTPException(status_code=500, detail=result["message"])
        
        return ContactResponse(
            success=True,
            message=result["message"],
            id=result.get("id")
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing contact form: {e}")
        raise HTTPException(
            status_code=500,
            detail="Sorry, there was an error processing your request. Please try again."
        )

@router.get("/submissions")
async def get_submissions(status: Optional[str] = None, limit: int = 100):
    """
    Get all contact submissions (admin endpoint)
    Optional filter by status: new, read, replied, archived
    """
    try:
        submissions = get_all_submissions(status=status, limit=limit)
        return {
            "success": True,
            "count": len(submissions),
            "submissions": submissions
        }
    except Exception as e:
        logger.error(f"Error fetching submissions: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch submissions")
