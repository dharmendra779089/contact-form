# Flask Clean Blog & Contact Form

A fully annotated, lightweight, dynamic blog application built with the Python **Flask** framework, featuring a contact form integrated with **SMTP** for email notifications, responsive templates, and a dynamic database loaded via external APIs.

---

## 🚀 Features

*   **Dynamic Article Loading**: Fetches blog posts from a remote REST API (`npoint.io`) on application startup.
*   **Dynamic URL Routing**: Parametric routing for individual blog posts (`/post/<id>`).
*   **Fully Functional Contact Form**: Validates user details and submits them to the backend.
*   **Automated SMTP Mailer**: Form submissions trigger secure email notifications via Gmail SMTP (`smtplib` with SSL/TLS encryption).
*   **Modern Responsive Design**: Built on top of the Bootstrap 5 clean blog layout.
*   **Interactive Header Transition**: JavaScript event handlers automatically slide the header navbar out of the viewport on scroll-down and slide it in on scroll-up.

---

## 🛠️ Tech Stack

*   **Backend**: Python, Flask, requests, smtplib
*   **Frontend**: Jinja2 Templates, HTML5, Bootstrap 5, Font Awesome (Icons)
*   **Styling & Interactions**: Vanilla CSS, Modern JavaScript DOM APIs

---

## 📋 Installation & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/flask-clean-blog.git
cd flask-clean-blog
```

### 2. Set Up a Virtual Environment (Recommended)
**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Email Credentials
Open the [main.py](file:///c:/Users/dsdha/PycharmProjects/contact%20form/main.py) file and replace the credentials placeholders with your actual Gmail account and App Password:
```python
# main.py
OWN_EMAIL = "your-email@gmail.com"
OWN_PASSWORD = "your-gmail-app-password"
```
> ⚠️ **Note**: For security, it is highly recommended to use a Gmail **App Password** instead of your primary password. Ensure you enable 2-step verification on your Google account first.

### 5. Run the Application
```bash
python main.py
```
After executing, navigate to `http://127.0.0.1:5000` in your web browser.

---

## 📁 Repository Structure

*   [main.py](file:///c:/Users/dsdha/PycharmProjects/contact%20form/main.py): Contains application configuration, routing patterns, and email handler logic.
*   [requirements.txt](file:///c:/Users/dsdha/PycharmProjects/contact%20form/requirements.txt): Lists all library requirements (`Flask`, `requests`).
*   `templates/`: Layout views.
    *   [header.html](file:///c:/Users/dsdha/PycharmProjects/contact%20form/templates/header.html): Head tags, scripts, and navbar.
    *   [footer.html](file:///c:/Users/dsdha/PycharmProjects/contact%20form/templates/footer.html): Shared footer container and Bootstrap/Theme JS scripts.
    *   [index.html](file:///c:/Users/dsdha/PycharmProjects/contact%20form/templates/index.html): Lists blog post previews using Jinja loops.
    *   [about.html](file:///c:/Users/dsdha/PycharmProjects/contact%20form/templates/about.html): Profile page details.
    *   [contact.html](file:///c:/Users/dsdha/PycharmProjects/contact%20form/templates/contact.html): Renders form fields and success alerts.
    *   [post.html](file:///c:/Users/dsdha/PycharmProjects/contact%20form/templates/post.html): Shows single post views.
*   `static/`: Theme stylesheet (`css/styles.css`), favicon, images, and navbar scroll interactions (`js/scripts.js`).

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE page details for permissions.
