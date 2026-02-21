import React, { useState } from "react";
import "./App-white.css";
import { testimonials, services, galleryImages, contactInfo } from "./mockData";
import { Star, Calendar, ClipboardList, Sparkles, Mail, Instagram, Send } from "lucide-react";
import { Toaster } from "./components/ui/sonner";
import { toast } from "sonner";

const LOGO_URL = "https://customer-assets.emergentagent.com/job_knots-jakarta/artifacts/2hpauqgp_knots.png";
const HERO_IMAGE = "https://images.unsplash.com/photo-1640439505734-3851b53e5035";
const ABOUT_IMAGE = "https://images.unsplash.com/photo-1606800052052-a08af7148866?w=800";

function AppWhite() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    eventDate: "",
    location: "Jakarta",
    message: ""
  });

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Mock form submission
    console.log("Form submitted:", formData);
    
    toast.success("Thank you for your inquiry!", {
      description: "We'll get back to you within 24 hours to discuss your special day.",
      duration: 5000,
    });

    // Reset form
    setFormData({
      name: "",
      email: "",
      eventDate: "",
      location: "Jakarta",
      message: ""
    });
  };

  return (
    <div className="App">
      <Toaster position="top-center" richColors />

      {/* Navigation */}
      <nav className="navigation-header">
        <div className="navigation-container">
          <img 
            src={LOGO_URL} 
            alt="KNOTS Wedding Planner" 
            className="navigation-logo"
          />
          <ul className="navigation-menu">
            <li>
              <a className="navigation-link" onClick={() => scrollToSection('home')}>
                Home
              </a>
            </li>
            <li>
              <a className="navigation-link" onClick={() => scrollToSection('about')}>
                About
              </a>
            </li>
            <li>
              <a className="navigation-link" onClick={() => scrollToSection('services')}>
                Services
              </a>
            </li>
            <li>
              <a className="navigation-link" onClick={() => scrollToSection('gallery')}>
                Gallery
              </a>
            </li>
            <li>
              <a className="navigation-link" onClick={() => scrollToSection('testimonials')}>
                Testimonials
              </a>
            </li>
            <li>
              <a className="navigation-link" onClick={() => scrollToSection('contact')}>
                Contact
              </a>
            </li>
          </ul>
        </div>
      </nav>

      {/* Hero Section */}
      <section id="home" className="hero-section">
        <img 
          src={HERO_IMAGE} 
          alt="Luxury Wedding Ballroom" 
          className="hero-background"
        />
        <div className="hero-overlay"></div>
        <div className="hero-content">
          <h1 className="hero-title">KNOTS: Crafting Timeless Legacies</h1>
          <p className="hero-subtitle">
            Premier Wedding Planning & Organizing in Jakarta and Tangerang. 
            Where modern luxury meets honored tradition.
          </p>
          <button 
            className="btn-primary hero-cta"
            onClick={() => scrollToSection('contact')}
          >
            Begin Your Journey
          </button>
        </div>
      </section>

      {/* About Section */}
      <section id="about" className="section about-section">
        <div className="container">
          <h2 className="heading-1 section-title">The Art of Celebration</h2>
          <div className="about-grid">
            <div className="about-text">
              <p className="body-large" style={{ marginBottom: '24px', textAlign: 'justify' }}>
                At KNOTS WEDDING ORGANIZER & PLANNER, we believe every love story is unique and deserves to be celebrated beautifully. We are a wedding planning team dedicated to helping couples create a meaningful, elegant, and stress-free wedding day.
              </p>
              <p className="body-large" style={{ marginBottom: '24px', textAlign: 'justify' }}>
                From the first idea until the final moment of your celebration, we walk with you step by step to make sure every detail reflects your story, your dreams, and your personality.
              </p>
              <p className="body-large" style={{ marginBottom: '24px', textAlign: 'justify' }}>
                We focus on sincerity, clear communication, and thoughtful planning – so you can truly enjoy your special day with your loved ones.
              </p>
              <p className="body-large" style={{ fontWeight: '500', textAlign: 'justify' }}>
                Your happiness is our priority.
              </p>
              <p className="body-large" style={{ fontStyle: 'italic', marginTop: '16px', textAlign: 'justify' }}>
                Let us take care of the details, while you enjoy every moment of your journey to "I do".
              </p>
            </div>
            <div className="about-image-container">
              <img 
                src={ABOUT_IMAGE} 
                alt="Luxury Wedding Venue" 
                className="about-image"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section id="services" className="section">
        <div className="container">
          <h2 className="heading-1 section-title">Our Services</h2>
          <p className="body-regular section-subtitle">
            Comprehensive wedding solutions tailored to your unique vision, 
            from initial concept to the final moment of celebration.
          </p>
          
          <div className="services-grid">
            {services.map((service, index) => {
              const icons = [ClipboardList, Calendar, Sparkles];
              const Icon = icons[index];
              
              return (
                <div key={service.id} className="service-card">
                  <Icon className="service-icon" strokeWidth={1.5} />
                  <h3 className="heading-3 service-title">{service.title}</h3>
                  <p className="body-small service-description">
                    {service.description}
                  </p>
                  <ul className="service-features">
                    {service.features.map((feature, idx) => (
                      <li key={idx}>{feature}</li>
                    ))}
                  </ul>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Gallery Section */}
      <section id="gallery" className="section gallery-section">
        <div className="container">
          <h2 className="heading-1 section-title">The Portfolio</h2>
          <p className="body-regular section-subtitle">
            A curated collection of our most cherished moments, 
            showcasing the elegance and emotion of celebrations we've orchestrated.
          </p>
          
          <div className="gallery-grid">
            {galleryImages.map((image) => (
              <div key={image.id} className="gallery-item">
                <img 
                  src={image.url} 
                  alt={image.alt} 
                  className="gallery-image"
                  loading="lazy"
                />
                <div className="gallery-overlay"></div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section id="testimonials" className="section">
        <div className="container">
          <h2 className="heading-1 section-title">Client Testimonials</h2>
          <p className="body-regular section-subtitle">
            The words of our couples speak to the care, precision, 
            and artistry we bring to every celebration.
          </p>
          
          <div className="testimonials-grid">
            {testimonials.map((testimonial) => (
              <div key={testimonial.id} className="testimonial-card">
                <div className="testimonial-rating">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <Star key={i} size={16} fill="currentColor" />
                  ))}
                </div>
                <p className="testimonial-review">"{testimonial.review}"</p>
                <div className="testimonial-author">{testimonial.name}</div>
                <div className="testimonial-meta">
                  {testimonial.location} • {testimonial.date}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="section contact-section">
        <div className="container">
          <h2 className="heading-1 section-title">Connect With Us</h2>
          <p className="body-regular section-subtitle">
            Let's begin the journey of creating your perfect celebration. 
            Reach out to discuss your vision.
          </p>
          
          <div className="contact-container">
            <div className="contact-grid">
              {/* Contact Information */}
              <div className="contact-info">
                <div className="contact-info-item">
                  <div className="contact-info-label">WhatsApp</div>
                  <div className="contact-info-value">
                    <a href={`https://wa.me/62${contactInfo.whatsapp.replace(/^0/, '').replace(/\s/g, '')}`} target="_blank" rel="noopener noreferrer">
                      {contactInfo.whatsapp}
                    </a>
                  </div>
                </div>

                <div className="contact-info-item">
                  <div className="contact-info-label">Email</div>
                  <div className="contact-info-value">
                    <a href={`mailto:${contactInfo.email}`}>
                      {contactInfo.email}
                    </a>
                  </div>
                </div>

                <div className="contact-info-item">
                  <div className="contact-info-label">Locations</div>
                  <div className="contact-info-value">
                    {contactInfo.locations.join(" • ")}
                  </div>
                </div>

                <div className="contact-info-item">
                  <div className="contact-info-label">Follow Us</div>
                  <div className="social-links">
                    <a 
                      href={`https://instagram.com/${contactInfo.instagram}`}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="social-link"
                    >
                      <Instagram size={20} />
                      @{contactInfo.instagram}
                    </a>
                  </div>
                </div>
              </div>

              {/* Contact Form */}
              <div>
                <form className="contact-form" onSubmit={handleSubmit}>
                  <div className="form-group">
                    <label htmlFor="name" className="form-label">Name *</label>
                    <input
                      type="text"
                      id="name"
                      name="name"
                      className="form-input"
                      value={formData.name}
                      onChange={handleInputChange}
                      required
                      placeholder="Your full name"
                    />
                  </div>

                  <div className="form-group">
                    <label htmlFor="email" className="form-label">Email *</label>
                    <input
                      type="email"
                      id="email"
                      name="email"
                      className="form-input"
                      value={formData.email}
                      onChange={handleInputChange}
                      required
                      placeholder="your@email.com"
                    />
                  </div>

                  <div className="form-group">
                    <label htmlFor="eventDate" className="form-label">Event Date</label>
                    <input
                      type="date"
                      id="eventDate"
                      name="eventDate"
                      className="form-input"
                      value={formData.eventDate}
                      onChange={handleInputChange}
                    />
                  </div>

                  <div className="form-group">
                    <label htmlFor="location" className="form-label">Preferred Location *</label>
                    <select
                      id="location"
                      name="location"
                      className="form-select"
                      value={formData.location}
                      onChange={handleInputChange}
                      required
                    >
                      <option value="Jakarta">Jakarta</option>
                      <option value="Bandung">Bandung</option>
                      <option value="Both">Both Locations</option>
                    </select>
                  </div>

                  <div className="form-group">
                    <label htmlFor="message" className="form-label">Message</label>
                    <textarea
                      id="message"
                      name="message"
                      className="form-textarea"
                      value={formData.message}
                      onChange={handleInputChange}
                      placeholder="Tell us about your vision for your special day..."
                    ></textarea>
                  </div>

                  <button type="submit" className="btn-primary form-button">
                    <Send size={16} style={{ marginRight: '8px' }} />
                    Send Inquiry
                  </button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="footer">
        <div className="footer-content">
          <img 
            src={LOGO_URL} 
            alt="KNOTS Wedding Planner" 
            className="footer-logo"
          />
          <p className="footer-tagline">
            Crafting Timeless Legacies • Jakarta & Bandung
          </p>
          
          <nav className="footer-nav">
            <a className="footer-link" onClick={() => scrollToSection('home')}>Home</a>
            <a className="footer-link" onClick={() => scrollToSection('about')}>About</a>
            <a className="footer-link" onClick={() => scrollToSection('services')}>Services</a>
            <a className="footer-link" onClick={() => scrollToSection('gallery')}>Gallery</a>
            <a className="footer-link" onClick={() => scrollToSection('testimonials')}>Testimonials</a>
            <a className="footer-link" onClick={() => scrollToSection('contact')}>Contact</a>
          </nav>

          <div className="footer-bottom">
            © 2026 KNOTS Wedding Planner & Organizer. All rights reserved.
          </div>
        </div>
      </footer>
    </div>
  );
}

export default AppWhite;
