# Travel Guide Web Application

## Overview

This project is a travel guide web application designed to introduce tourist destinations in Australia and China during the COVID-19 period.

The platform provides travel information, safety guidelines, and an interactive commenting system to enhance user engagement.

---

## Objective

The Travel Information Platform was developed to help users explore destinations in Australia and China while accessing important travel guidance.
The system emphasizes:

- Clear information architecture  
- Reliable backend design  
- User-centered functionality
- Maintainable code structure  

---

## Key Features

### Travel Information
- Structured destination pages with detailed descriptions  
- Safety and travel advisory content  
- Clean and intuitive UI  

### Authentication System
- User registration and login
- Session-based authentication  
- Secure data handling  

### Comment Management
- Users can post comments on destination pages  
- Full CRUD functionality for administrators
- Moderation-friendly database structure  

---

## Tech Stack

**Frontend**  
- HTML  
- CSS  
- JavaScript  

**Backend**  
- Django  

**Database**  
- SQLite  
- Django ORM  

---

## What I Focused On

- Improved UI/UX by implementing interactive components such as carousels and dropdown menus using Bootstrap, jQuery, and Popper.js  
- Designed a clean layout balancing text and images to enhance readability and visual appeal  

---

## Architecture

The system follows a classic Django MVT (Model–View–Template) architecture, ensuring clear separation of concerns and maintainable code structure.

Browser → Django URL Router → Views → Models(ORM) → SQLite Database

---

## How to Run

### 1. Clone the repository
git clone https://github.com/LumpyFugu/Travel-website.git  
cd Travel-website

### 2. Create a virtual environment
(For MacOS)  
python -m venv venv  
source venv/bin/activate  

(For Windows)  
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt  

### 4. Run migrations
python manage.py migrate  

### 5. Start the server
python manage.py runserver  
Open: http://127.0.0.1:8000  

