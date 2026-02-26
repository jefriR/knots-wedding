"""
KNOTS Wedding Planner - Backend Server
======================================
FastAPI application with MySQL database and SMTP email
"""

from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
import logging
from pathlib import Path

from config import CORS_ORIGINS, APP_NAME

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create the main app
app = FastAPI(
    title=APP_NAME,
    description="Backend API for KNOTS Wedding Planner website",
    version="1.0.0"
)

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Health check endpoint
@api_router.get("/")
async def root():
    return {"message": f"Welcome to {APP_NAME} API", "status": "running"}

@api_router.get("/health")
async def health_check():
    return {"status": "healthy", "service": APP_NAME}

# Include the router in the main app
app.include_router(api_router)

# Try to import and initialize MySQL-dependent routes
try:
    from database.mysql_connection import init_connection_pool, test_connection
    from routes.contact_routes import router as contact_router
    
    # Initialize database connection pool
    if init_connection_pool():
        if test_connection():
            logger.info("MySQL database connected successfully")
            # Include contact routes only if DB is connected
            app.include_router(contact_router, prefix="/api")
        else:
            logger.warning("MySQL database connection test failed - contact routes disabled")
    else:
        logger.warning("MySQL connection pool initialization failed - contact routes disabled")
        
except ImportError as e:
    logger.warning(f"MySQL dependencies not available: {e}")
    logger.info("Running without database features. Install mysql-connector-python to enable.")
except Exception as e:
    logger.warning(f"Could not initialize database: {e}")
    logger.info("Running without database features. Check your MySQL configuration.")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=CORS_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logger.info(f"{APP_NAME} API started")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info(f"{APP_NAME} API shutting down")
