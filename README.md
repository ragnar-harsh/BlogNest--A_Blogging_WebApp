# BlogNest - A Blogging WebApp

## Overview
BlogNest is a blogging web application built using the Django framework. It allows users to create, edit, delete, and manage blogs with a proper authentication and security layer. 
The application also tracks blog views and interactions while ensuring a seamless user experience with a beautifully designed UI.

## Features
- **User Authentication & Authorization**
  - Secure user registration and login.
  - Password hashing and user session management.
  - Access control for creating, editing, and deleting blogs.

- **Blog Management**
  - Create new blog posts with rich content.
  - Edit and update existing blogs.
  - Delete blogs with confirmation prompts.
  - Track and count blog views.
  
- **Security**
  - CSRF protection for form submissions.
  - Secure authentication mechanisms.
  - Protection against unauthorized actions.
  
- **Database Integration**
  - Uses Django's ORM with a structured database schema.
  - Stores user data, blog posts, views, and interactions efficiently.
  
- **User-Friendly UI**
  - Responsive and modern interface.
  - Easy-to-navigate blog dashboard.
  - Clean and intuitive design for seamless user experience.

## Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite / PostgreSQL (configurable)
- **Authentication:** Django's built-in authentication system
- **Security:** Django security features (CSRF, XSS protection, authentication layers)

## Installation & Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/blognest.git
   cd blognest
   ```

2. **Create a Virtual Environment and Activate It**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```sh
   python manage.py migrate
   ```

5. **Create a Superuser (For Admin Panel)**
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin user.

6. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/`.

## Usage
- Users can register and log in to manage their blogs.
- Authenticated users can create, edit, and delete blogs.
- Blogs display a view count and user engagement.
- Admin users can manage all blog posts from the Django admin panel.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve BlogNest.

## License
This project is licensed under the MIT License.

---
Made with ❤️ using Django.

