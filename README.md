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
![Screenshot 2025-02-11 001548](https://github.com/user-attachments/assets/b0be11cd-137b-4865-956a-487e7994616e)
![Screenshot 2025-02-11 001121](https://github.com/user-attachments/assets/cce94099-bdc9-45fc-bea6-8b7c49bae6f4)
![Screenshot 2025-02-11 001208](https://github.com/user-attachments/assets/85f08cdf-d002-49a4-ba5b-2d3388557813)
![Screenshot 2025-02-11 001230](https://github.com/user-attachments/assets/70ed9863-ccd3-4a2b-a3e4-457ef33bbcbf)
![Screenshot 2025-02-11 001313](https://github.com/user-attachments/assets/b70469e6-00e7-42cb-b839-8726238eb638)
![Screenshot 2025-02-11 001339](https://github.com/user-attachments/assets/80d71555-809a-4819-a7f4-7dc9693e6840)
![Screenshot 2025-02-11 001350](https://github.com/user-attachments/assets/503ef140-e55e-4a4c-a1ea-a15708d342fc)
![Screenshot 2025-02-11 001426](https://github.com/user-attachments/assets/2d5277e8-e667-4b77-b00b-f84ea032928b)
![Screenshot 2025-02-11 001447](https://github.com/user-attachments/assets/256754ec-08df-4adc-806a-e5b2ad7022d0)


