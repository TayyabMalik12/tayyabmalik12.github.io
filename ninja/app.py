from flask import Flask, render_template, request, redirect, flash, send_from_directory, jsonify
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
        "images": ["/static/images/shirt_service.jpg"],
        "short_description": "Relax and Let Us Handle It"
    },
    {
        "title": "Dry Cleaning",
        "description": "At Manor Lane Dry Cleaners in Hither Green, we take extra care with every item. Before cleaning, we check for stains and spot them with specialized dry cleaning chemicals to clean well. This way, your clothes come out fresh and spotless the first time. Better yet, we offer same-day service—all done on-site in Hither Green.",
        "images": ["/static/images/dry_cleaning.jpg", "/static/images/dry_clean_1.jpg"],
        "short_description": "Dry Cleaning Done Right! "
    },
    {
        "title": "Alterations & Repairs",
        "description": "At Manor Lane Dry Cleaners, we offer expert clothing alterations and repairs. Our specialist tailor is available Monday to Saturday, providing on-site fittings for your convenience. From replacing buttons to adjusting jacket lengths—especially wedding dress, jeans zips to patch, jacket, bag zip & repairs and curtain shortening & re-lining. Just bring in your ideas, and we’ll make them happen!",
        "images": ["/static/images/alternations_repairs_onsite.jpg", "/static/images/alternation_repairs.jpg", "/static/images/alternation_repairs_bag.jpg", "/static/images/alternation_repairs_kits.jpg", "/static/images/alternation_repairs_lady.jpg", "/static/images/alternation_repairs_scissor.jpg", "/static/images/alternation_repairs_strips.jpg", "/static/images/alternation_repairs_dress.jpg"],
        "short_description": "Don’t Toss It—Repair or Alter It!"
    },
    {
        "title": "Wedding Dress",
        "description": "Choosing the right dry cleaner is essential, and our specialized technique ensures your gown is treated with the utmost care. We hand-treat stains, use distilled solvents, clean each dress individually, and press each layer by hand. Your gown will be returned in your wedding dress bag or folded in an acid-free box, ideal for storage or travel.",
        "images": ["/static/images/wedding_dress.jpg", "/static/images/wedding_dress1.jpg",
                   "/static/images/wedding_dress2.jpg"],
        "short_description": "Choose Manor Lane for your wedding dress care! "
    },
    {
        "title": "Natives Cleaning",
        "description": "We specialize in cleaning all types of traditional and native attire. From Scottish kilt to African native and Asian sari, we provide professional dry-cleaning services for all.",
        "images": ["/static/images/natives_clean1.jpg", "/static/images/natives_clean2.jpg", "/static/images/natives_clean3.jpg"],
        "short_description": "Preserving Heritage, One Garment at a Time"

    },
    {
        "title": "Ironing Service",
        "description": "Our skilled pressers are available daily, offering a competitive Iron-Only service. With equipment gentle on delicate fabrics and perfect for a crisp finish on linens, we make your ironing effortless!",
        "images": ["/static/images/ironing.jpg"],
        "short_description": "We’ll Iron Away Your Clothes’ Creases "
    },
    {
        "title": "Upholstery Service",
        "description": "We treat your sofa covers and upholstery items individually for a deep clean. If your sofa or upholstery looks worn, bring it in for a complete clean and press!",
        "images": ["/static/images/upholstery1.jpg", "/static/images/upholstery2.jpg", "/static/images/upholstery3.jpg", "/static/images/upholstery4.jpg", "/static/images/upholstery5.jpg", "/static/images/upholstery6.jpg"],
        "short_description": "Clean Sofa, Happy Life"
    },
    {
        "title": "Laundry Service",
        "description": "At Manor Lane Dry Cleaners in Hither Green, we offer a Wash, Dry, and Fold service. With competitive rates and top-quality machines, we help your clothes look great for longer. ",
        "images": ["/static/images/laundary_service.jpg"],
        "short_description": "Just stop by and drop off your laundry! "
    },
    {
        "title": "Rug Cleaning",
        "description": "We clean all types of rugs. Depending on the type of rug, we’ll either clean it on-site or off-site.",
        "images": ["/static/images/rugs_cleaning.jpg",],
        "short_description": "Fresh Rug, Joy of Walking "
    },
    {
        "title": "Skiwear Cleaning",
        "description": "We clean everything from suits and jackets to trousers, gloves, hats, sleeping bags and tents. We specialize in cleaning delicate materials and luxury brands, down jackets and coats, including Canada Goose and Moncler, leaving them fresh and looking like new and fluffy.",
        "images": ["/static/images/skiwear1.jpg", ],
        "short_description": "Luxury brands  "
    },
    {
        "title": "Dye Service",
        "description": "With a range of popular colors in stock, we can dye most items that are safe for water treatment—cotton works best for vibrant results.",
        "images": ["/static/images/dye_service.jpg"],
        "short_description": "We can even dye your clothes!"
    },
    {
        "title": "School Uniform",
        "description": "We clean all types of school uniforms—from skirts to blazers—at competitive prices, with special offers available year-round. Plus, kids get a sweet treat on us.",
        "images": ["/static/images/uniform.jpg", "/static/images/school_blazer.jpg", "/static/images/school_shirt.jpg" ],
        "short_description": "Keep uniforms looking their best!"

    },

    {
        "title": "Shoe Repairs",
        "description": "Our skilled cobbler ensures top-quality repairs using only premium materials.",
        "images": ["/static/images/shoe_repair.jpg"],
        "short_description": "Re-heel, save your soles, and restore comfort to your step!"
    },
    {
        "title": "Curtain Cleaning",
        "description": "Curtains collect a surprising amount of dust, odors, pet hair, smoke, and even dead skin—though you may not see it, we find it all in our machine filters. We also clean blinds!",
        "images": ["/static/images/curtains_cleaning.jpg"],
        "short_description": "Time to drop the curtains and keep allergens away! "
    },
    {
        "title": "Leather & Suede",
        "description": " At Manor Lane Dry Cleaners, we expertly clean and repair leather and suede items to the highest standards. Unlike regular dry cleaning, leather and suede require a gentler process with specialized solvents to preserve their shape and softness. ",
        "images": ["/static/images/leather_suade_cleaning.jpg"],
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
slides = [
    {
        'image': '/static/images/front1.png',
    },
    {
        'image': '/static/images/front2.png',
    },
    {
        'image': '/static/images/front3.png',
    }
]

media_items = [
        {'type': 'video', 'src': '/static/images/wedding_dress_cleaning.mp4', 'thumbnail': '/static/images/thumbnail_wedding_dress_cleaning.png', 'alt': 'Wedding Dress Cleaning', 'title': 'Wedding Dress Cleaning'},
        {'type': 'video', 'src': '/static/images/wedding_dress_clean.mp4', 'thumbnail': '/static/images/thumbnail_wedding_dress_cleaning.png', 'alt': 'Wedding Dress Cleaning', 'title': 'Wedding Dress Cleaning'},
        {'type': 'video', 'src': '/static/images/sewing.mp4', 'thumbnail': '/static/images/sewing.png', 'alt': 'Alternations', 'title': 'Alternations & Repairs'},
        {'type': 'video', 'src': '/static/images/native_dress_cleaning.mp4', 'thumbnail': '/static/images/thumbnail_dress_cleaning.png', 'alt': 'Native Dress Cleaning', 'title': 'Native Dress Cleaning'},
        {'type': 'video', 'src': '/static/images/dress_short.mp4', 'thumbnail': '/static/images/dress_shortening_thumbnail.png', 'alt': 'dress shortening', 'title': 'Dress Shortening'},
        {'type': 'video', 'src': '/static/images/shoe_repair.mp4', 'thumbnail': '/static/images/shoe_repairs_thumbnail.png', 'alt': 'Shoe Repairs', 'title': 'Shoe Repairs'},
        {'type': 'video', 'src': '/static/images/toy_before_repair.mp4', 'thumbnail': '/static/images/thumbnail_before_repair.png', 'alt': 'Toy Before Repair', 'title': 'Toy Before Repair'},
        {'type': 'video', 'src': '/static/images/toy_after_repair.mp4', 'thumbnail': '/static/images/thumbnail_after_repair.png', 'alt': 'Toy After Repair', 'title': 'Toy After Repair'},
        {'type': 'video', 'src': '/static/images/kilt_alternations.mp4','thumbnail': '/static/images/kilt_alternations_thumbnail.png', 'alt': 'kilt alternations', 'title': 'Kilt Alternations'},
        {'type': 'video', 'src': '/static/images/cushion_cover_making.mp4', 'thumbnail': '/static/images/thumbnail_cushion_making.png', 'alt': 'Cushion Making', 'title': 'Cushion Making'},

    ]

@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/')
def index():
    return render_template('index.html', services=services, price_list=price_list, slides=slides, media_items=media_items)

@app.route('/gallery')
def gallery():
    media_items = [
        {'type': 'image', 'src': '/static/images/image1.jpg', 'thumbnail': '/static/images/image1.jpg', 'alt': 'Image 1', 'title': 'Repairs & Alternations'},
        {'type': 'image', 'src': '/static/images/image2.jpg', 'thumbnail': '/static/images/image2.jpg', 'alt': 'Image 2', 'title': 'Repairs & Alternations'},
        {'type': 'video', 'src': '/static/images/video1.mp4', 'thumbnail': '/static/images/image3.jpg', 'alt': 'Video 1', 'title': 'Cushions Making'},
        {'type': 'video', 'src': '/static/images/video2.mp4', 'thumbnail': '/static/images/image4.jpg', 'alt': 'Video 2', 'title': 'Toy Before Repair'}
    ]
    return render_template('gallery.html', media_items=media_items)

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml', mimetype='application/xml')

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

 


    # Sending the message via email (simple example using SMTP)
    try:
        send_email(name, email, message)
        return jsonify({"status": "success", "name": name})
    except:
        return jsonify({"status": "error", "message": "Error sending message."}), 500


def send_email(name, email, message):
    # Set up your email server here (Gmail SMTP, etc.)
    sender = 'manorlane.drycleaners176@gmail.com'
    receiver = 'manorlane.drycleaners176@gmail.com'
    password = 'jeco ycgn mleu bgiz'

    msg = MIMEText(f'From: {name} ({email})\n\nMessage:\n{message}')
    msg['Subject'] = 'New Contact Message'
    msg['From'] = sender
    msg['To'] = receiver

    # Using Gmail as an example (use your own SMTP provider details)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())


if __name__ == '__main__':
    app.run(debug=True)

