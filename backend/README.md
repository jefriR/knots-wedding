# KNOTS Wedding Planner - Backend Setup Guide

## Prerequisites
- Python 3.9+ installed
- MySQL Server installed and running
- pip (Python package manager)

---

## Step 1: Set Up MySQL Database

### 1.1 Create the Database
Open MySQL command line or MySQL Workbench and run:

```sql
CREATE DATABASE IF NOT EXISTS knots_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 1.2 Create the Table
Run the SQL in `database/schema.sql` or copy-paste this:

```sql
USE knots_db;

CREATE TABLE IF NOT EXISTS contact_submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    event_date DATE NULL,
    location VARCHAR(50) NOT NULL DEFAULT 'Jakarta',
    message TEXT NULL,
    status ENUM('new', 'read', 'replied', 'archived') DEFAULT 'new',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    INDEX idx_email (email),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

---

## Step 2: Configure Environment

### 2.1 Create .env file
Copy the example and fill in your credentials:

```bash
cp .env.example .env
```

### 2.2 Edit .env file
Open `.env` and update these values:

```ini
# MySQL - Update with your credentials
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=YOUR_MYSQL_PASSWORD_HERE
MYSQL_DATABASE=knots_db

# SMTP Email - From your hosting (Rumahweb)
SMTP_HOST=mail.yourdomain.com
SMTP_PORT=465
SMTP_USER=info@yourdomain.com
SMTP_PASSWORD=YOUR_EMAIL_PASSWORD_HERE
SMTP_USE_SSL=true

# Where to receive notifications
NOTIFICATION_EMAIL=knots.wo@gmail.com

# CORS - Frontend URL
CORS_ORIGINS=http://localhost:3000
```

### Finding Your SMTP Settings (Rumahweb)
1. Login to cPanel at rumahweb.com
2. Go to **Email Accounts** → Create or use existing email
3. Click **Connect Devices** to see SMTP settings:
   - **SMTP Host**: Usually `mail.yourdomain.com`
   - **SMTP Port**: 465 (SSL) or 587 (TLS)
   - **Username**: Your full email address
   - **Password**: Your email account password

---

## Step 3: Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

**Required packages:**
- fastapi
- uvicorn
- mysql-connector-python
- python-dotenv
- email-validator
- pydantic

---

## Step 4: Run the Server

```bash
cd backend
uvicorn server:app --reload --port 8001
```

The API will be available at: `http://localhost:8001`

---

## Step 5: Test the API

### Health Check
```bash
curl http://localhost:8001/api/health
```

### Submit Contact Form (Test)
```bash
curl -X POST http://localhost:8001/api/contact/submit \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "event_date": "2025-06-15",
    "location": "Jakarta",
    "message": "This is a test message"
  }'
```

### View All Submissions
```bash
curl http://localhost:8001/api/contact/submissions
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/` | Welcome message |
| GET | `/api/health` | Health check |
| POST | `/api/contact/submit` | Submit contact form |
| GET | `/api/contact/submissions` | Get all submissions (admin) |

---

## Frontend Configuration

Update `frontend/.env`:

```ini
REACT_APP_BACKEND_URL=http://localhost:8001
```

Then run the frontend:
```bash
cd frontend
npm install
npm start
```

---

## Troubleshooting

### MySQL Connection Error
- Make sure MySQL server is running
- Check username/password in .env
- Ensure `knots_db` database exists

### Email Not Sending
- Verify SMTP credentials with your hosting provider
- Check if port 465 is blocked by firewall
- Try port 587 with `SMTP_USE_SSL=false`

### CORS Error
- Make sure `CORS_ORIGINS` includes your frontend URL
- For development: `CORS_ORIGINS=http://localhost:3000`

---

## File Structure

```
backend/
├── server.py              # Main FastAPI application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env.example          # Environment template
├── .env                  # Your local config (create this)
├── database/
│   ├── __init__.py
│   ├── schema.sql        # SQL to create tables
│   └── mysql_connection.py
├── services/
│   ├── __init__.py
│   ├── contact_service.py
│   └── email_service.py
└── routes/
    ├── __init__.py
    └── contact_routes.py
```
