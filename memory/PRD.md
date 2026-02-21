# KNOTS Wedding Planner & Organizer - Product Requirements Document

## Project Overview
**Project Name:** KNOTS Wedding Planner & Organizer  
**Location:** Jakarta & Bandung, Indonesia  
**Style:** Modern Minimalist, High-End Luxury, Professional  
**Launch Date:** February 2026  
**Type:** Single Page Application (SPA) - Landing Page

## Original Problem Statement
Generate a responsive Single Page Application (SPA) with a clean, magazine-style layout for KNOTS, a luxury wedding planning and organizing service. The website should showcase services, gallery, testimonials, and provide contact options with email and Instagram integration.

## User Personas
1. **Engaged Couples (Primary)**
   - Age: 25-40
   - Income: High-end luxury market
   - Location: Jakarta & Bandung
   - Needs: Professional wedding planning, traditional ceremony coordination, stress-free execution

2. **Family Decision Makers**
   - Parents helping plan traditional ceremonies
   - Cultural protocol guidance needed
   - Quality and reputation focused

## Core Requirements (Static)
- Responsive design (mobile, tablet, desktop)
- Luxury minimalist aesthetic
- Warm neutral color palette (White, Beige, Champagne Gold, Black)
- Smooth scroll navigation
- High-quality imagery
- Professional contact form
- Social media integration (Email + Instagram)

## Architecture & Tech Stack
- **Frontend:** React 19.0.0
- **Styling:** Tailwind CSS + Custom CSS
- **Components:** Shadcn/UI, Lucide React icons
- **Fonts:** Crimson Text (serif) + Inter (sans-serif)
- **Toast Notifications:** Sonner
- **Images:** Unsplash/Pexels luxury wedding photography

## Design System
- **Colors:**
  - Primary Background: #fffef2 (warm white)
  - Secondary Background: #f6f5e8 (light beige)
  - Text Primary: #333333
  - Text Secondary: #666666
  - Accent Gold: #d4af37
  
- **Typography:**
  - Hero: 56px Crimson Text
  - Headings: 36px, 24px, 20px Crimson Text
  - Body: 18px, 16px, 14px Inter
  
- **Buttons:**
  - Border radius: 0px (sharp edges)
  - Hover: transform translateY(-2px)
  - Transition: 0.3s ease

## What's Been Implemented (February 9, 2026)

### Phase 1: Frontend Landing Page with Mock Data ✓
1. **Navigation Section**
   - Sticky header with logo
   - Smooth scroll menu links (Home, About, Services, Gallery, Testimonials, Contact)
   - Responsive design

2. **Hero/Jumbotron Section**
   - Full-width luxury ballroom background image
   - Headline: "KNOTS: Crafting Timeless Legacies"
   - Sub-headline with location info
   - CTA button: "Begin Your Journey"

3. **About Us Section**
   - "The Art of Celebration" heading
   - Company story and mission
   - Centered layout on beige background

4. **Services Section**
   - 3-column responsive grid
   - Service cards with icons (Lucide React)
   - Services:
     * Wedding Planner (full conceptualization)
     * Wedding Organizer (day-of management)
     * Sangjit Service (traditional ceremonies)
   - Feature lists for each service

5. **Gallery Section**
   - 3-column masonry grid
   - 6 luxury wedding images
   - Hover effects with image zoom
   - Lazy loading implemented

6. **Testimonials Section** (NEW)
   - 3-column responsive grid
   - 3 client testimonials with ratings
   - Client name, location, and date
   - Hover card effects

7. **Contact Section**
   - Two-column layout (info + form)
   - Contact information:
     * Email: hello@knots-wedding.com
     * Instagram: @knots.wedding
     * Locations: Jakarta • Bandung
   - Contact form with fields:
     * Name (required)
     * Email (required)
     * Event Date
     * Preferred Location (dropdown)
     * Message
   - Form submission with toast notification (MOCK)

8. **Footer**
   - Logo and tagline
   - Navigation links
   - Copyright info
   - Dark background (#333333)

### Files Created
- `/app/frontend/src/App.js` - Main SPA component
- `/app/frontend/src/App.css` - Component styles
- `/app/frontend/src/index.css` - Design system & global styles
- `/app/frontend/src/mockData.js` - Mock data (testimonials, services, gallery, contact info)

## Prioritized Backlog

### P0 Features (Critical - Not Started)
- [ ] Backend API development (when user requests)
- [ ] Database integration for contact form submissions
- [ ] Email notification system for inquiries

### P1 Features (High Priority - Deferred)
- [ ] Mobile hamburger menu (currently hidden on mobile)
- [ ] Gallery lightbox/modal for full-size image viewing
- [ ] Form validation improvements
- [ ] Loading states for form submission
- [ ] SEO optimization (meta tags, structured data)

### P2 Features (Enhancement Ideas)
- [ ] Blog/articles section for wedding planning tips
- [ ] Pricing/packages showcase
- [ ] Animated page transitions
- [ ] WhatsApp integration (currently only Instagram)
- [ ] Multi-language support (Bahasa Indonesia)
- [ ] Testimonial carousel/slider
- [ ] Instagram feed integration
- [ ] Image lazy loading optimization

## Next Action Items
1. User review and feedback on frontend design
2. Mobile responsive testing and refinements
3. Consider backend development when ready
4. Gather real testimonials and update mock data
5. Add WhatsApp integration if business number available
6. Consider adding case studies or featured weddings section

## Notes
- All form submissions are currently MOCKED (frontend only)
- Images sourced from Unsplash/Pexels (royalty-free)
- Design follows Luxury Minimalist Design System guidelines
- Logo provided by user (hosted on Emergent CDN)
- No backend or database implemented yet

## Update: February 9, 2026 - Color Scheme Comparison

### New Features Added:
1. **Logo Transparency Enhancement**
   - Applied CSS `mix-blend-mode: darken` to logo for transparent background
   - Logo now seamlessly blends with any background color
   - Maintains visibility on both light backgrounds and dark footer

2. **WHITE/BLACK/GOLD Alternative Version**
   - Created complete alternative color scheme for comparison
   - New color palette:
     * Background: Pure white (#ffffff)
     * Text: Pure black (#000000)
     * Accent: Champagne gold (#d4af37)
   - Higher contrast design
   - Bold gold CTA buttons
   - Black borders (2px) for stronger definition
   - Gold underlines on section titles
   - Enhanced hover states with gold highlights

3. **Interactive Comparison Tool**
   - Live color scheme switcher in top-right corner
   - Toggle between "Warm Beige" and "White/Gold" versions
   - Instant theme switching without page reload
   - Visual button states to show active selection

### Files Added:
- `/app/frontend/src/index-white.css` - White/Black/Gold design system
- `/app/frontend/src/App-white.css` - White/Black/Gold component styles
- `/app/frontend/src/AppWhite.js` - White/Black/Gold version component
- `/app/frontend/src/Comparison.js` - Interactive switcher component

### Design Comparison Summary:

**Warm Beige Version:**
- Softer, more organic feel
- Warm neutral palette (#fffef2, #f6f5e8)
- Subtle borders and separators
- Quiet luxury aesthetic
- Better for traditional/classic brand positioning

**White/Black/Gold Version:**
- Bold, high-contrast design
- Modern luxury aesthetic
- Strong visual hierarchy
- Gold accents create premium feel
- Better for contemporary/bold brand positioning

### User Decision Required:
Choose preferred color scheme to set as primary version.

## Update: February 9, 2026 - White/Gold Theme Refinements

### User-Requested Adjustments Completed:

1. **New Logo Implementation ✓**
   - Replaced with new transparent PNG logo (gold knot on black background)
   - Clean display on white navigation header
   - Removed mix-blend-mode for true transparency
   - Logo URL: https://customer-assets.emergentagent.com/job_knots-jakarta/artifacts/2hpauqgp_knots.png

2. **New Hero Banner ✓**
   - Changed from busy chandelier to minimalist couple silhouette
   - Elegant architectural space with clean lines
   - Better alignment with white/black/gold aesthetic
   - Image: https://images.unsplash.com/photo-1640439505734-3851b53e5035

3. **2-Column About Section ✓**
   - Left column: Company description and mission text
   - Right column: Elegant luxury venue image with gold border (3px)
   - Responsive: stacks to single column on mobile
   - Image with hover zoom effect
   - About image: https://images.unsplash.com/photo-1646734643617-3812fd3cc095

### Design Improvements:
- Cleaner, more sophisticated hero section
- Better visual balance with 2-column about layout
- Gold border on about image reinforces brand colors
- Minimalist aesthetic throughout maintains luxury feel

### Primary Theme Selected:
**White/Black/Gold** chosen as primary design direction
- High contrast for modern luxury positioning
- Gold accents create premium brand perception
- Clean white backgrounds for contemporary feel
- Strong visual hierarchy with black text

### Files Modified:
- `/app/frontend/src/AppWhite.js` - Updated logo, hero, and about section structure
- `/app/frontend/src/App-white.css` - Added 2-column about grid, image styling, responsive rules

### User Preference Confirmed:
White/Black/Gold theme set as the primary version for KNOTS website.

## Final Update: February 9, 2026 - Production Ready

### User-Requested Final Changes Completed:

1. **Color Scheme Switcher Removed ✓**
   - Deleted comparison component and switcher UI
   - Set White/Black/Gold as the primary and only theme
   - Updated index.js to render AppWhite directly
   - Clean, distraction-free user experience

2. **About Section Image Updated ✓**
   - Changed from venue/architecture to wedding rings detail
   - Softer, more romantic aesthetic
   - Gold wedding rings perfectly align with brand colors
   - Image: https://images.unsplash.com/photo-1606800052052-a08af7148866

### Current Production State:
- Single theme: White/Black/Gold (no switcher)
- All sections complete and polished
- Responsive design tested
- Clean navigation without clutter
- Professional, luxury aesthetic throughout

### Ready for:
- Client presentation
- User testing
- Backend development (contact form functionality)
- Mobile menu implementation
- SEO optimization
- Production deployment

Website is now in production-ready state for KNOTS Wedding Planner.

## Content Update: February 9, 2026

### Content Updates Completed:

1. **About Us Section ✓**
   - Updated with new comprehensive description
   - Focus on personalized service and couple's happiness
   - Emphasizes sincerity, clear communication, and thoughtful planning
   - Maintains 2-column layout with wedding rings image

2. **Services Section ✓**
   - Updated service names:
     * Wedding Planner (comprehensive planning)
     * Wedding Organizer (day-of coordination)
     * Engagement Organizer (replacing Sangjit Service)
   - Added detailed features for each service
   - Included guest capacity information:
     * Wedding Organizer: Standing 400 / Seated 150 guests
     * Engagement Organizer: up to 70 guests

3. **Contact Information ✓**
   - Added WhatsApp: 0819 3085 3332 (with clickable link)
   - Updated Email: knots.wo@gmail.com
   - Updated Instagram: knots.wedding (without @ symbol)
   - Maintained Jakarta & Bandung locations

### Service Features Breakdown:

**Wedding Planner:**
- Financial Budgeting
- Wedding Timeline & Monitoring Preparation
- Vendor Suggestion, Coordination & Negotiation Assistance
- Unlimited Consultations via WhatsApp
- Unlimited Meetings (as needed)
- Holy Matrimony Rehearsal (as needed)
- Includes Engagement & Wedding Organizer Services

**Wedding Organizer:**
- Financial Budgeting
- Vendor Suggestions
- Unlimited Consultations via WhatsApp
- Rundown Arrangement & Detail Coordination
- Holy Matrimony Rehearsal (as needed)
- Vendor Coordination for Technical Meeting (H-1 month)
- Family Coordination for Event Details
- Guest Capacity: Standing up to 400 | Seated up to 150

**Engagement Organizer:**
- Vendor Suggestions
- Unlimited Consultations via WhatsApp
- Rundown Arrangement & Detail Coordination
- Vendor Coordination for Technical Meeting (H-2 weeks)
- Family Coordination for Event Details
- Guest Capacity: up to 70 guests

All content now reflects KNOTS' current service offerings and contact information.
