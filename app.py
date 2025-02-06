from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'bhattshrutik36@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'iowb haof cqho ouvw'  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'bhattshrutik36@gmail.com'  # Replace with your email

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        # Get form data
        user_email = request.form["email"]
        user_message = request.form["message"]
        
        # Admin's email address
        admin_email = "bhattshrutik36@gmail.com"  # Replace with the admin's email

        # Create the email message
        msg = Message("New Message from Portfolio Contact Form", recipients=[admin_email])
        msg.body = f"Email: {user_email}\nMessage: {user_message}"

        # Send the email
        try:
            mail.send(msg)
            return redirect(url_for("home"))  # Redirect back to the home page after submission
        except Exception as e:
            return f"An error occurred while sending the email: {e}"

if __name__ == "__main__":
    app.run(debug=True)
