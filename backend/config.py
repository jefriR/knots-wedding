"""
KNOTS Wedding Planner - Configuration
=====================================
Fill in your credentials below or use environment variables
"""

import os
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# =====================================================
# MySQL Database Configuration
# =====================================================
MYSQL_CONFIG = {
    "host": os.environ.get("MYSQL_HOST", "localhost"),
    "port": int(os.environ.get("MYSQL_PORT", 3306)),
    "user": os.environ.get("MYSQL_USER", "root"),
    "password": os.environ.get("MYSQL_PASSWORD", ""),  # <-- Fill your MySQL password
    "database": os.environ.get("MYSQL_DATABASE", "knots_db"),
}

# =====================================================
# SMTP Email Configuration (from your hosting)
# =====================================================
SMTP_CONFIG = {
    "host": os.environ.get("SMTP_HOST", "mail.yourdomain.com"),  # <-- Fill your SMTP host
    "port": int(os.environ.get("SMTP_PORT", 465)),  # Usually 465 (SSL) or 587 (TLS)
    "user": os.environ.get("SMTP_USER", "info@yourdomain.com"),  # <-- Fill your email
    "password": os.environ.get("SMTP_PASSWORD", ""),  # <-- Fill your email password
    "use_ssl": os.environ.get("SMTP_USE_SSL", "true").lower() == "true",  # true for port 465
}

# Email recipient (where you want to receive notifications)
NOTIFICATION_EMAIL = os.environ.get("NOTIFICATION_EMAIL", "knots.wo@gmail.com")

# =====================================================
# Application Settings
# =====================================================
APP_NAME = "KNOTS Wedding Planner"
CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*").split(",")
