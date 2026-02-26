-- =====================================================
-- KNOTS Wedding Planner - Database Schema
-- =====================================================

-- Create database (run this first if not exists)
CREATE DATABASE IF NOT EXISTS knots_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE knots_db;

-- =====================================================
-- Contact Submissions Table
-- =====================================================
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

-- =====================================================
-- Optional: View all submissions
-- =====================================================
-- SELECT * FROM contact_submissions ORDER BY created_at DESC;
