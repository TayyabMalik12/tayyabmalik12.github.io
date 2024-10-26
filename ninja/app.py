from flask import Flask, render_template, request, redirect, flash
import smtplib  # Use this for sending emails
from email.mime.text import MIMEText
import mimetypes
mimetypes.add_type('image/webp', '.webp')

app = Flask(__name__)
app.secret_key = 'tayyab12'

services = [
    {
        "title": "Shirt Service",
        "description": "Specialized cleaning and pressing for all types of shirts, ensuring they look crisp and fresh.",
        "image": "shirt-service.webp"
    },
    {
        "title": "Dry Cleaning",
        "description": "Gentle cleaning method for delicate fabrics using specialized solvents that protect garment integrity.",
        "image": "dry-cleaning.webp"
    },
    {
        "title": "Alterations & Repairs",
        "description": "Professional alterations and repairs to ensure your garments fit perfectly and look their best.",
        "image": "alternations.webp"
    },
    {
        "title": "Ironing Service",
        "description": "Expert ironing service to eliminate wrinkles and give your clothes a polished finish.",
        "image": "ironing.webp"
    },
    {
        "title": "Sofa Covers",
        "description": "Thorough cleaning of sofa covers to refresh your living space and maintain fabric quality.",
        "image": "sofa.webp"
    },
    {
        "title": "Laundry Service",
        "description": "Complete laundry service for all types of clothing, ensuring clean, fresh-smelling results.",
        "image": "laundry.webp"
    },
    {
        "title": "Rugs",
        "description": "Specialized cleaning for area rugs, using techniques that preserve colors and textures.",
        "image": "rugs.webp"
    },
    {
        "title": "SKI Wear",
        "description": "Professional cleaning of ski gear to remove dirt and odors while maintaining water repellency.",
        "image": "skiway.webp"
    },
    {
        "title": "Bag Cleaning",
        "description": "Thorough cleaning of bags, ensuring they remain stylish and functional without damage.",
        "image": "bag.webp"
    },
    {
        "title": "Dye Service",
        "description": "Color restoration or change service for garments that need a fresh look or touch-up.",
        "image": "dye.webp"
    },
    {
        "title": "Bedding",
        "description": "Comprehensive cleaning of all bedding items, including sheets, comforters, and pillowcases.",
        "image": "bedding.webp"
    },
    {
        "title": "School Uniform",
        "description": "Dedicated service for cleaning and maintaining school uniforms, keeping them looking sharp.",
        "image": "uniform.webp"
    },
    {
        "title": "Wedding Dress",
        "description": "Specialized cleaning and preservation for wedding dresses to maintain their beauty and condition.",
        "image": "wedding.webp"
    },
    {
        "title": "Shoe Repairs",
        "description": "Expert repairs and maintenance for all types of footwear, ensuring longevity and comfort.",
        "image": "shoe.webp"
    },
    {
        "title": "Curtains",
        "description": "Professional cleaning of curtains to keep your home decor looking fresh and inviting.",
        "image": "curtains.webp"
    },
    {
        "title": "Leather & Suede",
        "description": "Specialized cleaning and conditioning for leather and suede items to preserve their quality.",
        "image": "leather.webp"
    }
]


@app.route('/')
def index():
    return render_template('index.html', services=services)


@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Optional: Flash a message that the form was submitted
    flash(f'Thank you {name}, your message has been sent!', 'success')

    # Sending the message via email (simple example using SMTP)
    try:
        send_email(name, email, message)
        return redirect('/')  # Redirect back to home after submission
    except:
        flash('Error sending message. Please try again later.', 'danger')
        return redirect('/')


def send_email(name, email, message):
    # Set up your email server here (Gmail SMTP, etc.)
    sender = 'maryventurres@gmail.com'
    receiver = 'maryventurres@gmail.com'
    password = 'srox fzjy mlox kfbe'

    msg = MIMEText(f'From: {name} ({email})\n\nMessage:\n{message}')
    msg['Subject'] = 'New Contact Message'
    msg['From'] = sender
    msg['To'] = receiver

    # Using Gmail as an example (use your own SMTP provider details)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())


if __name__ == '__main__':
    app.run()

