# KNOTS Wedding Planner - Product Requirements Document

## Original Problem Statement
Build a responsive Single Page Application (SPA) for a high-end luxury wedding planning business called "KNOTS" based in Jakarta & Tangerang. Style: modern minimalist with professional, magazine-style layout.

## Project Overview
- **Project Name**: KNOTS Wedding Planner & Organizer
- **Location**: Jakarta & Tangerang, Indonesia
- **Style**: Modern Minimalist, High-End Luxury, Professional
- **Color Palette**: Burgundy/Maroon (#8B4557) and Cream theme

## Core Requirements

### Sections
1. **Navigation (Sticky)**: Home, About, Services, Portfolio, FAQ, Contact
2. **Hero Section**: Headline, sub-headline, CTA button
3. **About Us**: Two-column layout with company description
4. **Services (3-Column)**: Wedding Planner, Wedding Organizer, Engagement Organizer
5. **Portfolio**: Masonry grid of wedding decoration images (non-personnel)
6. **FAQ**: Accordion-style frequently asked questions
7. **Contact**: Contact form + social media links
8. **Footer**: Logo, navigation, contact info, copyright

### Technical Requirements
- Responsive design (mobile-first)
- Elegant serif fonts
- React.js frontend with Tailwind CSS
- Python FastAPI backend with MySQL database
- SMTP email notifications

## What's Been Implemented ✅

### Frontend (December 2025)
- [x] Complete SPA structure with all sections
- [x] Burgundy/maroon and cream color theme
- [x] Sticky navigation with smooth scroll
- [x] Hero section with CTA
- [x] Two-column About Us section
- [x] Three-column Services with detailed feature lists
- [x] Portfolio section with non-personnel images
- [x] FAQ section with accordion (4 questions)
- [x] Contact form with API integration
- [x] Responsive footer with centered logo on mobile
- [x] Updated location from Bandung to Tangerang
- [x] KNOTS maroon logo
- [x] FAQ #3 updated: "Do you handle weddings outside Jakarta and Tangerang?"
- [x] Loading state on submit button

### Backend (February 2026)
- [x] FastAPI server with MySQL support
- [x] Contact form submission API (`/api/contact/submit`)
- [x] Contact submissions retrieval API (`/api/contact/submissions`)
- [x] SMTP email notification service
- [x] MySQL database schema
- [x] Configuration via .env file
- [x] Comprehensive README for local setup

## Pending Items

### P1 - Medium Priority  
- [ ] Test contact form with actual MySQL & SMTP setup locally
- [ ] Production deployment to Rumahweb

### P2 - Low Priority / Future
- [ ] Admin dashboard to view/manage submissions
- [ ] Code refactoring (split AppWhite.js into components)
- [ ] Consolidate CSS files

## Architecture

```
/app/
├── frontend/
│   ├── src/
│   │   ├── App.js              # Router, renders AppWhite
│   │   ├── AppWhite.js         # Main page component (all sections)
│   │   ├── mockData.js         # Content data (services, FAQs, portfolio)
│   │   ├── App-white.css       # Component styles (burgundy theme)
│   │   ├── index-white.css     # Global CSS variables
│   │   └── components/ui/      # Shadcn UI components
│   └── build/                  # Production build for deployment
│
└── backend/
    ├── server.py               # Main FastAPI application
    ├── config.py               # Configuration settings
    ├── .env.example            # Environment template
    ├── README.md               # Setup guide
    ├── database/
    │   ├── schema.sql          # SQL to create tables
    │   └── mysql_connection.py # MySQL connection pool
    ├── services/
    │   ├── contact_service.py  # Contact form logic
    │   └── email_service.py    # SMTP email sender
    └── routes/
        └── contact_routes.py   # API endpoints
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/` | Welcome message |
| GET | `/api/health` | Health check |
| POST | `/api/contact/submit` | Submit contact form |
| GET | `/api/contact/submissions` | Get all submissions |

## Contact Information (from mockData.js)
- Email: knots.wo@gmail.com
- WhatsApp: 0819 3085 3332
- Instagram: knots.wedding
- Locations: Jakarta, Tangerang

## Database Schema

```sql
CREATE TABLE contact_submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    event_date DATE NULL,
    location VARCHAR(50) DEFAULT 'Jakarta',
    message TEXT NULL,
    status ENUM('new', 'read', 'replied', 'archived') DEFAULT 'new',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

## Local Setup Summary
1. Create MySQL database `knots_db`
2. Run `database/schema.sql` to create table
3. Copy `.env.example` to `.env` and fill credentials
4. Install deps: `pip install -r requirements.txt`
5. Run server: `uvicorn server:app --reload --port 8001`
6. Frontend: Update `REACT_APP_BACKEND_URL=http://localhost:8001`
