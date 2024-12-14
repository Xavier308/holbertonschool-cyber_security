# Holberton School Domain Analysis Report

## Infrastructure Overview

### Geographic Distribution
- **France** (14 instances)
  - Primary location for application servers
  - Hosts apply.holbertonschool.com and read.holbertonschool.com
- **United States** (8 instances)
  - Ashburn region (Amazon NoVa)
  - Hosts main domain infrastructure
- **India** (11 instances)
  - Mumbai region
  - CDN and assets distribution

### Cloud Infrastructure
- **Amazon Web Services (AWS)**
  - Amazon Data Services France (14 instances)
  - Amazon.com, Inc. (14 instances)
  - Amazon Data Services NoVa (3 instances)
  - Amazon Technologies Inc. (2 instances)

### Server Distribution
- **Main Production Servers**
  - holbertonschool.com (US)
  - apply.holbertonschool.com (France)
  - read.holbertonschool.com (France)
- **Staging Environment**
  - staging-apply.holbertonschool.com
  - Level2 Forum (yriry2.holbertonschool.com)

## Technology Stack

### Backend Technologies
- **Core Framework**
  - Ruby (6 instances)
  - Ruby on Rails (6 instances)
- **Forum System**
  - Discourse (2 instances)

### Frontend Technologies
- **JavaScript Libraries & Frameworks**
  - jQuery (4 instances)
  - Slick (4 instances - carousel/slider)
  - jsDelivr (4 instances - CDN)

### Marketing & Analytics
- Google Tag Manager (4 instances)
- Klaviyo (4 instances - email marketing/CRM)

### Typography & Design
- Adobe Fonts (4 instances)
- Typekit (4 instances - font service)

### E-commerce
- Abicart (2 instances - shopping platform)

### Infrastructure
- **Web Servers**
  - Nginx (31 instances)
  - AWS ELB (2 instances)

### Content Delivery
- CDN services (13 instances)
  - jsDelivr implementation
  - AWS CloudFront distribution

### Security Configuration

#### SSL/TLS Implementation
- **Supported Versions**
  - TLSv1.2 (33 instances)
  - TLSv1.3 (16 instances)
  - TLSv1 and TLSv1.1 (5 instances each)

#### Security Headers
- X-Frame-Options: SAMEORIGIN
- X-XSS-Protection: 1; mode=block
- X-Content-Type-Options: nosniff
- X-Download-Options: noopen

### Service Architecture
- **Tags**
  - cloud (33 instances)
  - eol-product (28 instances)
  - cdn (13 instances)

### Certificate Information
- Primary SSL provider: Amazon RSA 2048
- Secondary provider: Let's Encrypt (for specific services)
- Individual certificates for subdomains

## Port Analysis
- Port 443 (HTTPS): 33 instances
- All services properly configured for secure communication

## Notable Findings

### Website Status
1. Production Services
   - Apply Portal: Fully operational
   - Level2 Forum: Active
   - Rails Assets: CDN distribution active

2. Service Availability
   - Some instances reported 503 Service Temporarily Unavailable
   - Evidence of load balancing (AWS ELB)

### Security Posture
1. No public vulnerabilities reported
2. Consistent security header implementation
3. Strong SSL/TLS configuration
4. Multiple JARM fingerprints indicating diverse security configurations:
   - 13 instances with standardized configuration
   - 12 instances with enhanced security settings
   - 5 instances with custom configurations

## Recommendations
1. Consider deprecating TLSv1 and TLSv1.1 support
2. Standardize nginx versions across all instances
3. Review and consolidate JARM fingerprints for consistent security posture
4. Monitor and optimize 503 error responses
