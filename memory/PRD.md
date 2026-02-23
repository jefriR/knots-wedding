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
- Frontend-only (no backend yet)
- React.js with Tailwind CSS

## What's Been Implemented ✅

### Completed (December 2025)
- [x] Complete SPA structure with all sections
- [x] Burgundy/maroon and cream color theme
- [x] Sticky navigation with smooth scroll
- [x] Hero section with CTA
- [x] Two-column About Us section
- [x] Three-column Services with detailed feature lists
- [x] Portfolio section with non-personnel images
- [x] FAQ section with accordion (4 questions)
- [x] Contact form (frontend mock)
- [x] Responsive footer with centered logo on mobile
- [x] Updated location from Bandung to Tangerang
- [x] KNOTS maroon logo
- [x] FAQ #3 updated: "Do you handle weddings outside Jakarta and Tangerang?"

## Pending Items

### P0 - High Priority
- [ ] User verification of FAQ section
- [ ] User verification of mobile footer

### P1 - Medium Priority  
- [ ] Backend implementation for contact form (save submissions/send emails)
- [ ] Push code to GitHub

### P2 - Low Priority / Future
- [ ] Production deployment
- [ ] Code refactoring (split AppWhite.js into components)
- [ ] Consolidate CSS files

## Architecture

```
/app/frontend/
├── src/
│   ├── App.js              # Router, renders AppWhite
│   ├── AppWhite.js         # Main page component (all sections)
│   ├── mockData.js         # All content data (services, FAQs, portfolio)
│   ├── App-white.css       # Component styles (burgundy theme)
│   ├── index-white.css     # Global CSS variables
│   └── components/ui/      # Shadcn UI components
└── package.json
```

## Key Files
- `/app/frontend/src/AppWhite.js` - Main page component
- `/app/frontend/src/mockData.js` - All dynamic content
- `/app/frontend/src/App-white.css` - Theme styles

## Contact Information (from mockData.js)
- Email: knots.wo@gmail.com
- WhatsApp: 0819 3085 3332
- Instagram: knots.wedding
- Locations: Jakarta, Tangerang

## Notes
- Contact form is currently a frontend mock (no backend)
- All content is managed in mockData.js for easy updates
- No third-party integrations yet
