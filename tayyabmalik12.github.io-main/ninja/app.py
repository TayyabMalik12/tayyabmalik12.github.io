from flask import Flask, render_template, request, abort, redirect, flash, send_from_directory, jsonify
import smtplib  # Use this for sending emails
from email.mime.text import MIMEText
import mimetypes
mimetypes.add_type('image/webp', '.webp')

app = Flask(__name__)
app.secret_key = 'tayyab12'
areas = {
    "blackheath": {
        "name": "Blackheath",
        "services": [
            "Dry Cleaners Blackheath",
            "Wedding Dress Cleaning & Alteration",
            "Curtain Cleaning & Alterations",
            "Clothing Repairs Blackheath",
            "Tailors",
            "Laundry"
        ],
        "description": """
        Manor Lane Dry Cleaners has been serving the residents
        of Lewisham for many years. Whether you live in SE3,
        SE12, SE13 or the surrounding areas, you can benefit
        from our FREE contactless collection and delivery.

        You can also visit us on Manor Lane. Free parking is
        available before 10:00 am and after 12:00 pm,
        Monday to Friday, and all day on Saturday across the road.

        We also offer an expert home fitting service for wedding
        dresses and other garments. Book an appointment and our
        expert will visit your home to professionally pin your
        wedding dress or garments for the perfect fit.

        Whatever you need, give us a call to discuss your
        requirements.
        """,
        "offer_title": "15% OFF DRY CLEANING",
        "offer_description": (
            "Special discount for Blackheath residents. "
            "Sign up for your Blackheath Residents 15% OFF "
            "Dry Cleaning Voucher."
        )
    },

"lee": {
    "name": "Lee",
    "services": [
        "Dry Cleaners Lee",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs Lee",
        "Tailors",
        "Laundry"
    ],
    "description": """
Manor Lane Dry Cleaners has been serving the residents of Lee for many years now. Whether you live in the SE12 or SE13 area, or the surrounding areas, you no longer need to search for 'Dry Cleaners near me'. We offer FREE Contactless Collection & Delivery, or you can visit us on Manor Lane.

Free parking is available before 10:00 am and after 12:00 pm, Monday to Friday, and free all day on Saturday across the road.

We also offer an Expert Home Fitting Service for wedding dresses and all garments. We bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit for your exact requirements.

Whatever you need, give us a call to discuss your requirements.

Don't forget to sign up for your Lee Residents 15% OFF Dry Cleaning Voucher.
""",
    "offer_title": "15% OFF DRY CLEANING",
    "offer_description": (
        "Special offer for Lee residents! "
        "Sign up for your Lee Residents 15% OFF "
        "Dry Cleaning Voucher."
    )
},

"manor-lane": {
    "name": "Manor Lane",
    "services": [
        "Dry Cleaners Manor Lane",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs Manor Lane",
        "Tailors",
        "Laundry"
    ],
    "description": """
Manor Lane Dry Cleaners has been serving the residents of Manor Lane for many years now. Whether you live in the SE12 or SE13 area, or the surrounding areas, you no longer need to search for 'Dry Cleaners near me'. We offer FREE Contactless Collection & Delivery, or you can simply visit us on Manor Lane.

Free parking is available before 10:00 am and after 12:00 pm, Monday to Friday, and free all day on Saturday across the road.

We also offer an Expert Home Fitting Service for wedding dresses and all garments. We bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit for your exact requirements.

Whatever you need, give us a call to discuss your requirements.

Don't forget to sign up for your Manor Lane Residents 15% OFF Dry Cleaning Voucher.
""",
    "offer_title": "15% OFF DRY CLEANING",
    "offer_description": (
        "Special offer for Manor Lane residents! "
        "Sign up for your Manor Lane Residents "
        "15% OFF Dry Cleaning Voucher."
    )
},

"south-west-london": {
    "name": "South West London",
    "services": [
        "Dry Cleaners South West London",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs South West London",
        "Tailors",
        "Laundry"
    ],
    "description": """
Manor Lane Dry Cleaners has been serving the residents of South West London for many years now. Whether you live in South West London or the surrounding areas, you no longer need to search for 'Dry Cleaners near me'. We offer FREE Contactless Collection & Delivery, or you can simply visit us on Manor Lane.

Free parking is available before 10:00 am and after 12:00 pm, Monday to Friday, and free all day on Saturday across the road.

We also offer an Expert Home Fitting Service for wedding dresses and all garments. We bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit for your exact requirements.

Whatever you need, give us a call to discuss your requirements.

Don't forget to sign up for your South West London Residents 15% OFF Dry Cleaning Voucher.
""",
    "offer_title": "15% OFF DRY CLEANING",
    "offer_description": (
        "Special offer for South West London residents! "
        "Sign up for your South West London Residents "
        "15% OFF Dry Cleaning Voucher."
    )
},

"south-east-london": {
    "name": "South East London",
    "services": [
        "Dry Cleaners South East London",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs South East London",
        "Tailors",
        "Laundry"
    ],
    "description": """
Manor Lane Dry Cleaners has been serving the residents of South East London for many years now. Whether you live in South East London or the surrounding areas, you no longer need to search for 'Dry Cleaners near me'. We offer FREE Contactless Collection & Delivery, or you can simply visit us on Manor Lane.

Free parking is available before 10:00 am and after 12:00 pm, Monday to Friday, and free all day on Saturday across the road.

We also offer an Expert Home Fitting Service for wedding dresses and all garments. We bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit for your exact requirements.

Whatever you need, give us a call to discuss your requirements.

Don't forget to sign up for your South East London Residents 15% OFF Dry Cleaning Voucher.
""",
    "offer_title": "15% OFF DRY CLEANING",
    "offer_description": (
        "Special offer for South East London residents! "
        "Sign up for your South East London Residents "
        "15% OFF Dry Cleaning Voucher."
    )
},

"south-london": {
    "name": "South London",
    "services": [
        "Dry Cleaners South London",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs South London",
        "Tailors",
        "Laundry"
    ],
    "description": """
Manor Lane Dry Cleaners has been serving the residents of South London for many years now. Whether you live in South London or the surrounding areas, you no longer need to search for 'Dry Cleaners near me'. We offer FREE Contactless Collection & Delivery, or you can simply visit us on Manor Lane.

Free parking is available before 10:00 am and after 12:00 pm, Monday to Friday, and free all day on Saturday across the road.

We also offer an Expert Home Fitting Service for wedding dresses and all garments. We bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit for your exact requirements.

Whatever you need, give us a call to discuss your requirements.

Don't forget to sign up for your South London Residents 15% OFF Dry Cleaning Voucher.
""",
    "offer_title": "15% OFF DRY CLEANING",
    "offer_description": (
        "Special offer for South London residents! "
        "Sign up for your South London Residents "
        "15% OFF Dry Cleaning Voucher."
    )
},

"eltham": {
    "name": "Eltham",
    "services": [
        "Dry Cleaners Eltham",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs Eltham",
        "Tailors",
        "Laundry"
    ],
    "description": """
Manor Lane Dry Cleaners has been serving the residents of Eltham for many years now. Whether you live in the SE12 or SE9 area, or the surrounding areas, you no longer need to search for 'Dry Cleaners near me'. We offer FREE Contactless Collection & Delivery, or you can simply visit us on Manor Lane.

Free parking is available before 10:00 am and after 12:00 pm, Monday to Friday, and free all day on Saturday across the road.

We also offer an Expert Home Fitting Service for wedding dresses and all garments. We bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit for your exact requirements.

Whatever you need, give us a call to discuss your requirements.

Don't forget to sign up for your Eltham Residents 15% OFF Dry Cleaning Voucher.
""",
    "offer_title": "15% OFF DRY CLEANING",
    "offer_description": (
        "Special offer for Eltham residents! "
        "Sign up for your Eltham Residents "
        "15% OFF Dry Cleaning Voucher."
    )
},

"greenwich": {
    "name": "Greenwich",
    "services": [
        "Dry Cleaners Greenwich",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs Greenwich",
        "Tailors",
        "Laundry"
    ],
    "description": """
Manor Lane Dry Cleaners has been serving the residents of Greenwich for many years now. Whether you live in the SE12 or SE10 area, or the surrounding areas, you no longer need to search for 'Dry Cleaners near me'. We offer FREE Contactless Collection & Delivery, or you can simply visit us on Manor Lane.

Free parking is available before 10:00 am and after 12:00 pm, Monday to Friday, and free all day on Saturday across the road.

We also offer an Expert Home Fitting Service for wedding dresses and all garments. We bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit for your exact requirements.

Whatever you need, give us a call to discuss your requirements.

Don't forget to sign up for your Greenwich Residents 15% OFF Dry Cleaning Voucher.
""",
    "offer_title": "15% OFF DRY CLEANING",
    "offer_description": (
        "Special offer for Greenwich residents! "
        "Sign up for your Greenwich Residents "
        "15% OFF Dry Cleaning Voucher."
    )
},

"sydenham": {
    "name": "Sydenham",
    "services": [
        "Dry Cleaners Sydenham",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs Sydenham",
        "Tailors",
        "Laundry"
    ],
    "description": """
Manor Lane Dry Cleaners has been serving the residents of Sydenham for many years now. Whether you live in the SE12 or SE26 area, or the surrounding areas, you no longer need to search for 'Dry Cleaners near me'. We offer FREE Contactless Collection & Delivery, or you can simply visit us on Manor Lane.

Free parking is available before 10:00 am and after 12:00 pm, Monday to Friday, and free all day on Saturday across the road.

We also offer an Expert Home Fitting Service for wedding dresses and all garments. We bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit for your exact requirements.

Whatever you need, give us a call to discuss your requirements.

Don't forget to sign up for your Sydenham Residents 15% OFF Dry Cleaning Voucher.
""",
    "offer_title": "15% OFF DRY CLEANING",
    "offer_description": (
        "Special offer for Sydenham residents! "
        "Sign up for your Sydenham Residents "
        "15% OFF Dry Cleaning Voucher."
    )
},
"forest-hill": {
    "name": "Forest Hill",
    "services": [
        "Dry Cleaners Forest Hill",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs Forest Hill",
        "Tailors",
        "Laundry"
    ],
    "description": """Manor Lane Dry Cleaners has been serving the residents of Forest Hill for many years now. So whether you are living in the SE12 or SE23 area, or the surrounding areas, you no longer need to search for 'Dry Cleaners near me' as we have come even closer by offering FREE Contactless Collection & Delivery. Alternatively, you can simply visit us on Manor Lane. There is FREE parking before 10:00 am and after 12:00 pm (Monday–Friday), and free all-day parking on Saturday across the road.

We also offer an Expert Home Fitting Service for your wedding dress and all garments. We now bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit to your exact requirements.

Whatever you decide, why not give us a call to discuss anything you need doing?""",
    "offer_title": "15% OFF DRY CLEANING FOR FOREST HILL RESIDENTS",
    "offer_description": "Don't forget to sign up for your Forest Hill Residents 15% OFF Dry Cleaning Voucher."
},
"new-cross": {
    "name": "New Cross",
    "services": [
        "Dry Cleaners New Cross",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs New Cross",
        "Tailors",
        "Laundry"
    ],
    "description": """Manor Lane Dry Cleaners has been serving the residents of New Cross for many years now. So whether you are living in the SE12 or SE14 area, or the surrounding areas, you no longer need to search for 'Dry Cleaners near me' as we have come even closer by offering FREE Contactless Collection & Delivery. Alternatively, you can simply visit us on Manor Lane. There is FREE parking before 10:00 am and after 12:00 pm (Monday–Friday), and free all-day parking on Saturday across the road.

We also offer an Expert Home Fitting Service for your wedding dress and all garments. We now bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit to your exact requirements.

Whatever you decide, why not give us a call to discuss anything you need doing?""",
    "offer_title": "15% OFF DRY CLEANING FOR NEW CROSS RESIDENTS",
    "offer_description": "Don't forget to sign up for your New Cross Residents 15% OFF Dry Cleaning Voucher."
},
"deptford": {
    "name": "Deptford",
    "services": [
        "Dry Cleaners Deptford",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs Deptford",
        "Tailors",
        "Laundry"
    ],
    "description": """Manor Lane Dry Cleaners has been serving the residents of Deptford for many years now. So whether you are living in the SE12 or SE8 area, or the surrounding areas, you no longer need to search for 'Dry Cleaners near me' as we have come even closer by offering FREE Contactless Collection & Delivery. Alternatively, you can simply visit us on Manor Lane. There is FREE parking before 10:00 am and after 12:00 pm (Monday–Friday), and free all-day parking on Saturday across the road.

We also offer an Expert Home Fitting Service for your wedding dress and all garments. We now bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit to your exact requirements.

Whatever you decide, why not give us a call to discuss anything you need doing?""",
    "offer_title": "15% OFF DRY CLEANING FOR DEPTFORD RESIDENTS",
    "offer_description": "Don't forget to sign up for your Deptford Residents 15% OFF Dry Cleaning Voucher."
},
"catford": {
    "name": "Catford",
    "services": [
        "Dry Cleaners Catford",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs Catford",
        "Tailors",
        "Laundry"
    ],
    "description": """Manor Lane Dry Cleaners has been serving the residents of Catford for many years now. So whether you are living in the SE12 or SE6 area, or the surrounding areas, you no longer need to search for 'Dry Cleaners near me' as we have come even closer by offering FREE Contactless Collection & Delivery. Alternatively, you can simply visit us on Manor Lane. There is FREE parking before 10:00 am and after 12:00 pm (Monday–Friday), and free all-day parking on Saturday across the road.

We also offer an Expert Home Fitting Service for your wedding dress and all garments. We now bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit to your exact requirements.

Whatever you decide, why not give us a call to discuss anything you need doing?""",
    "offer_title": "15% OFF DRY CLEANING FOR CATFORD RESIDENTS",
    "offer_description": "Don't forget to sign up for your Catford Residents 15% OFF Dry Cleaning Voucher."
},
"brockley": {
    "name": "Brockley",
    "services": [
        "Dry Cleaners Brockley",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs Brockley",
        "Tailors",
        "Laundry"
    ],
    "description": """Manor Lane Dry Cleaners has been serving the residents of Brockley for many years now. So whether you are living in the SE12 or SE4 area, or the surrounding areas, you no longer need to search for 'Dry Cleaners near me' as we have come even closer by offering FREE Contactless Collection & Delivery. Alternatively, you can simply visit us on Manor Lane. There is FREE parking before 10:00 am and after 12:00 pm (Monday–Friday), and free all-day parking on Saturday across the road.

We also offer an Expert Home Fitting Service for your wedding dress and all garments. We now bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit to your exact requirements.

Whatever you decide, why not give us a call to discuss anything you need doing?""",
    "offer_title": "15% OFF DRY CLEANING FOR BROCKLEY RESIDENTS",
    "offer_description": "Don't forget to sign up for your Brockley Residents 15% OFF Dry Cleaning Voucher."
},
"grove-park": {
    "name": "Grove Park",
    "services": [
        "Dry Cleaners Grove Park",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs Grove Park",
        "Tailors",
        "Laundry"
    ],
    "description": """Manor Lane Dry Cleaners has been serving the residents of Grove Park for many years now. So whether you are living in the SE12 or SE9 area, or the surrounding areas, you no longer need to search for 'Dry Cleaners near me' as we have come even closer by offering FREE Contactless Collection & Delivery. Alternatively, you can simply visit us on Manor Lane. There is FREE parking before 10:00 am and after 12:00 pm (Monday–Friday), and free all-day parking on Saturday across the road.

We also offer an Expert Home Fitting Service for your wedding dress and all garments. We now bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit to your exact requirements.

Whatever you decide, why not give us a call to discuss anything you need doing?""",
    "offer_title": "15% OFF DRY CLEANING FOR GROVE PARK RESIDENTS",
    "offer_description": "Don't forget to sign up for your Grove Park Residents 15% OFF Dry Cleaning Voucher."
},
"ladywell": {
    "name": "Ladywell",
    "services": [
        "Dry Cleaners Ladywell",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs Ladywell",
        "Tailors",
        "Laundry"
    ],
    "description": """Manor Lane Dry Cleaners has been serving the residents of Ladywell for many years now. So whether you are living in the SE12 or SE13 area, or the surrounding areas, you no longer need to search for 'Dry Cleaners near me' as we have come even closer by offering FREE Contactless Collection & Delivery. Alternatively, you can simply visit us on Manor Lane. There is FREE parking before 10:00 am and after 12:00 pm (Monday–Friday), and free all-day parking on Saturday across the road.

We also offer an Expert Home Fitting Service for your wedding dress and all garments. We now bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit to your exact requirements.

Whatever you decide, why not give us a call to discuss anything you need doing?""",
    "offer_title": "15% OFF DRY CLEANING FOR LADYWELL RESIDENTS",
    "offer_description": "Don't forget to sign up for your Ladywell Residents 15% OFF Dry Cleaning Voucher."
},
"hither-green": {
    "name": "Hither Green",
    "services": [
        "Dry Cleaners Hither Green",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs Hither Green",
        "Tailors",
        "Laundry"
    ],
    "description": """Manor Lane Dry Cleaners has been serving the residents of Hither Green for many years now. So whether you are living in the SE12 or SE13 area, or the surrounding areas, you no longer need to search for 'Dry Cleaners near me' as we have come even closer by offering FREE Contactless Collection & Delivery. Alternatively, you can simply visit us on Manor Lane. There is FREE parking before 10:00 am and after 12:00 pm (Monday–Friday), and free all-day parking on Saturday across the road.

We also offer an Expert Home Fitting Service for your wedding dress and all garments. We now bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit to your exact requirements.

Whatever you decide, why not give us a call to discuss anything you need doing?""",
    "offer_title": "15% OFF DRY CLEANING FOR HITHER GREEN RESIDENTS",
    "offer_description": "Don't forget to sign up for your Hither Green Residents 15% OFF Dry Cleaning Voucher."
},
"lewisham": {
    "name": "Lewisham",
    "services": [
        "Dry Cleaners Lewisham",
        "Wedding Dress Cleaning & Alteration",
        "Curtain Cleaning & Alterations",
        "Clothing Repairs Lewisham",
        "Tailors",
        "Laundry"
    ],
    "description": """Manor Lane Dry Cleaners has been serving the residents of Lewisham for many years now. So whether you are living in the SE12 or SE13 area, or the surrounding areas, you no longer need to search for 'Dry Cleaners near me' as we have come even closer by offering FREE Contactless Collection & Delivery. Alternatively, you can simply visit us on Manor Lane. There is FREE parking before 10:00 am and after 12:00 pm (Monday–Friday), and free all-day parking on Saturday across the road.

We also offer an Expert Home Fitting Service for your wedding dress and all garments. We now bring the tailor to you. Book an appointment, and our expert will visit your home to professionally pin your wedding dress or garments, ensuring the perfect fit to your exact requirements.

Whatever you decide, why not give us a call to discuss anything you need doing?""",
    "offer_title": "15% OFF DRY CLEANING FOR LEWISHAM RESIDENTS",
    "offer_description": "Don't forget to sign up for your Lewisham Residents 15% OFF Dry Cleaning Voucher."
},
}
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
    return render_template('index.html', services=services, price_list=price_list, slides=slides, media_items=media_items, areas=areas)

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


@app.route("/area-content/<slug>")
def area_content(slug):
    area = areas.get(slug)

    if area is None:
        abort(404)

    return render_template("_area_details.html", area=area)
if __name__ == '__main__':
    app.run(debug=True)

