# Import the Flask class, render_template function for rendering HTML templates, 
# and request object for handling incoming HTTP request data from the 'flask' package.
from flask import Flask, render_template, request

# Import the 'smtplib' module, which defines an SMTP client session object 
# that can be used to send email to any internet machine with an SMTP or ESMTP listener daemon.
import smtplib

# Import the 'requests' library, which allows sending HTTP requests using Python 
# to fetch external data (in this case, from a remote JSON endpoint).
import requests

# Create a Flask web application instance. __name__ is a special Python variable 
# that represents the name of the current module. It helps Flask locate resources like templates and static files.
app = Flask(__name__)

# Make a GET request to the specified npoint API URL to fetch a list of blog posts in JSON format,
# and parse the response immediately into a Python list of dictionaries using the .json() method.
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

# Define a placeholder string for the sender/recipient email address used to send the contact form messages.
OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"

# Define a placeholder string for the email account password or App Password used for SMTP authentication.
OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"


# Define a route handler for the root URL ('/') of the website. 
# This handles the main landing page of the blog.
@app.route('/')
def get_all_posts():
    # Render the "index.html" template and pass the list of retrieved blog posts 
    # as the template variable 'all_posts'.
    return render_template("index.html", all_posts=posts)


# Define a route handler for the "/about" page URL.
# This page displays biographical information about the blog owner.
@app.route("/about")
def about():
    # Render and return the "about.html" template layout.
    return render_template("about.html")


# Define a route handler for the "/contact" URL supporting both GET and POST requests.
# GET is used to load the form page; POST is used when submitting the contact form.
@app.route("/contact", methods=["GET", "POST"])
def contact():
    # Check if the current request method is 'POST', indicating form submission.
    if request.method == "POST":
        # Extract the dictionary-like form data submitted in the HTTP POST request body.
        data = request.form
        
        # Call the send_email helper function, passing the submitted name, email, phone number, and message.
        send_email(data["name"], data["email"], data["phone"], data["message"])
        
        # Render the contact form page again, passing 'msg_sent=True' to show a success message to the user.
        return render_template("contact.html", msg_sent=True)
        
    # If the request method is GET, render the contact page normally, passing 'msg_sent=False' to display the blank form.
    return render_template("contact.html", msg_sent=False)


# Define a helper function to send an email notification using SMTP.
# Parameters: name, email, phone, and message collected from the contact form.
def send_email(name, email, phone, message):
    # Construct the raw email message content, including a Subject header and double newline to separate the headers from the body.
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    
    # Establish a connection to the Gmail SMTP server on the standard port using a context manager ('with') for safe resource cleanup.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Put the SMTP connection in TLS (Transport Layer Security) mode to encrypt all subsequent communication.
        connection.starttls()
        
        # Log in to the email provider's SMTP server using the configured email credentials.
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        
        # Send the email. The first argument is the sender, the second is the recipient, and the third is the formatted message text.
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


# Define a dynamic route handler for showing a single blog post. 
# The '<int:index>' syntax captures an integer from the URL and passes it as the parameter 'index'.
@app.route("/post/<int:index>")
def show_post(index):
    # Initialize a variable to store the found post, starting as None.
    requested_post = None
    
    # Iterate through the list of posts loaded from the external JSON file.
    for blog_post in posts:
        # Check if the current post's ID matches the requested integer index from the URL path.
        if blog_post["id"] == index:
            # Assign the matching post dictionary to requested_post.
            requested_post = blog_post
            
    # Render the "post.html" template and pass the matching post dictionary to the template context.
    return render_template("post.html", post=requested_post)


# Check if this script is run directly by Python as the main program, rather than being imported as a module.
if __name__ == "__main__":
    # Start the Flask development server in debug mode, which enables auto-reloading and an interactive debugger in the browser.
    app.run(debug=True)
