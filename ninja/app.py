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
        "description": "Hate doing laundry? Let Manor Lane take care of your shirts! Our popular Shirt Service includes washing and hand-pressing —just £12.50 for 5 shirts. We use gentle temperatures and custom emulsifiers to remove oily residue, especially on collars and cuffs. Each shirt is hand-pressed for a quality finish that keeps your clothes lasting longer.",
        "emoji": "👔",
        "short_description": "Relax and Let Us Handle It"
    },
    {
        "title": "Dry Cleaning",
        "description": "At Manor Lane Dry Cleaners in Hither Green, we take extra care with every item. Before cleaning, we check for stains and spot them with specialized dry cleaning chemicals to clean well. This way, your clothes come out fresh and spotless the first time. Better yet, we offer same-day service—all done on-site in Hither Green.",
        "emoji": "🧼",
        "short_description": "Dry Cleaning Done Right! "
    },
    {
        "title": "Alterations & Repairs",
        "description": "At Manor Lane Dry Cleaners, we offer expert clothing alterations and repairs. Our specialist tailor is available Monday to Saturday, providing on-site fittings for your convenience. From replacing buttons to adjusting jacket lengths—especially wedding dress, jeans zips to patch, jacket, bag zip & repairs and curtain shortening & re-lining. Just bring in your ideas, and we’ll make them happen!",
        "emoji": "✂️",
        "short_description": "Don’t Toss It—Repair or Alter It!"
    },
    {
        "title": "Ironing Service",
        "description": "Our skilled pressers are available daily, offering a competitive Iron-Only service. With equipment gentle on delicate fabrics and perfect for a crisp finish on linens, we make your ironing effortless!",
        "emoji": "👕",
        "short_description": "We’ll Iron Away Your Clothes’ Creases "
    },
    {
        "title": "Upholstery Service",
        "description": "We treat your sofa covers and upholstery items individually for a deep clean. If your sofa or upholstery looks worn, bring it in for a complete clean and press!",
        "emoji": "🛋️",
        "short_description": "Clean Sofa, Happy Life"
    },
    {
        "title": "Laundry Service",
        "description": "At Manor Lane Dry Cleaners in Hither Green, we offer a Wash, Dry, and Fold service. With competitive rates and top-quality machines, we help your clothes look great for longer. ",
        "emoji": "🧺",
        "short_description": "Just stop by and drop off your laundry! "
    },
    {
        "title": "Rug Cleaning",
        "description": "We clean all types of rugs. Depending on the type of rug, we’ll either clean it on-site or off-site.",
        "emoji": "🧶",
        "short_description": "Fresh Rug, Joy of Walking "
    },
    {
        "title": "Skiwear Cleaning",
        "description": "We clean everything from suits and jackets to trousers, gloves, hats, sleeping bags and tents. We specialize in cleaning delicate materials and luxury brands, down jackets and coats, including Canada Goose and Moncler, leaving them fresh and looking like new and fluffy.",
        "emoji": "🎿",
        "short_description": "Luxury brands  "
    },
    {
        "title": "Dye Service",
        "description": "With a range of popular colors in stock, we can dye most items that are safe for water treatment—cotton works best for vibrant results.",
        "emoji": "🎨",
        "short_description": "We can even dye your clothes!"
    },
    {
        "title": "School Uniform",
        "description": "We clean all types of school uniforms—from skirts to blazers—at competitive prices, with special offers available year-round. Plus, kids get a sweet treat on us.",
        "emoji": "🎒",
        "short_description": "Keep uniforms looking their best!"

    },
    {
        "title": "Wedding Dress",
        "description": "Choosing the right dry cleaner is essential, and our specialized technique ensures your gown is treated with the utmost care. We hand-treat stains, use distilled solvents, clean each dress individually, and press each layer by hand. Your gown will be returned in your wedding dress bag or folded in an acid-free box, ideal for storage or travel.",
        "emoji": "👗",
        "short_description": "Choose Manor Lane for your wedding dress care! "
    },
    {
        "title": "Shoe Repairs",
        "description": "Our skilled cobbler ensures top-quality repairs using only premium materials.",
        "emoji": "👞",
        "short_description": "Re-heel, save your soles, and restore comfort to your step!"
    },
    {
        "title": "Curtain Cleaning",
        "description": "Curtains collect a surprising amount of dust, odors, pet hair, smoke, and even dead skin—though you may not see it, we find it all in our machine filters. We also clean blinds!",
        "emoji": "🧹",
        "short_description": "Time to drop the curtains and keep allergens away! "
    },
    {
        "title": "Leather & Suede",
        "description": " At Manor Lane Dry Cleaners, we expertly clean and repair leather and suede items to the highest standards. Unlike regular dry cleaning, leather and suede require a gentler process with specialized solvents to preserve their shape and softness. ",
        "emoji": "🧥",
        "short_description": "Trust your leather care to the experts! "

    }
]

price_list = [
        {"service": "Shirt (Wash & Press)", "price": "2.50"},
        {"service": "2 pc Suit", "price": "12.00"},
        {"service": "Dress Suit", "price": "15.00"},
        {"service": "Blouse", "price": "6.00"},
        {"service": "Trouser", "price": "6.00"},
        {"service": "Dress", "price": "10.00"},
        {"service": "Suit Jacket", "price": "9.50"},
        {"service": "Waistcoat", "price": "5.50"},
        {"service": "Coat", "price": "15.00"},
        {"service": "Jumper", "price": "6.50"},
        {"service": "Skirt", "price": "6.00"},
        {"service": "Scarf", "price": "5.50"},
        {"service": "Tie", "price": "3.00"}
    ]


@app.route('/')
def index():
    return render_template('index.html', services=services, price_list=price_list)


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

