import os

def generate():
    assets_dir = 'assets'
    # Find all images starting with shubham_stationery__
    images = sorted([f for f in os.listdir(assets_dir) if f.startswith('shubham_stationery__') and (f.endswith('.jpg') or f.endswith('.webp') or f.endswith('.png'))])
    
    # Generate the cards
    cards_html = ""
    for idx, img in enumerate(images):
        # We can categorise them alternatingly for filter demonstration
        category = "store" if idx % 2 == 0 else "products"
        label = "Store Interior & Display" if idx % 2 == 0 else "Quality Stationery Stock"
        
        cards_html += f"""
                <div class="product-item-card" data-category="{category}">
                    <div class="product-image-box" style="height: 250px; background: #f1f5f9;">
                        <img src="assets/{img}" alt="Shubham Stationery Salem Store Photo {idx+1}" style="width: 100%; height: 100%; object-fit: cover;" loading="lazy">
                    </div>
                    <div class="product-info-box" style="padding: 16px; flex-grow: 0;">
                        <span class="product-cat-label">{label}</span>
                        <h3 class="product-item-title" style="font-size: 15px; margin-bottom: 0;">Shubham Stationery - Image {idx+1}</h3>
                    </div>
                </div>"""

    # Complete HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Take a visual tour of Shubham Stationery near Salem New Bus Stand. Browse real photos of our extensive school, office, and creative stock.">
    <meta name="keywords" content="Shubham Stationery photos, stationery store gallery Salem, stationery stock photos Salem, Nirmal Jain store Salem">
    <meta name="author" content="Nirmal Jayantilal Jain">
    <meta name="robots" content="index, follow">

    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="assets/favicon.svg">

    <title>Photo Gallery | Real Store Tour | Shubham Stationery Salem</title>
    
    <!-- Stylesheet -->
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

    <!-- Header / Sticky Navigation -->
    <header class="header">
        <div class="container">
            <a href="index.html" class="logo">
                <div class="logo-icon">S</div>
                <span>Shubham <span style="color: var(--color-secondary);">Stationery</span></span>
            </a>
            
            <nav class="nav">
                <a href="index.html" class="nav-link">Home</a>
                <a href="about.html" class="nav-link">About Us</a>
                <a href="products.html" class="nav-link">Products</a>
                <a href="gallery.html" class="nav-link">Gallery</a>
                <a href="gst-compliance.html" class="nav-link">GST Details</a>
                <a href="contact.html" class="nav-link">Contact Us</a>
                <a href="contact.html" class="nav-cta">Get Quote</a>
            </nav>
            
            <button class="menu-btn" aria-label="Toggle Navigation Menu">
                <span class="menu-btn-bar"></span>
                <span class="menu-btn-bar"></span>
                <span class="menu-btn-bar"></span>
            </button>
        </div>
    </header>

    <!-- Subpage Hero -->
    <section class="section-padding" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: white; padding: 100px 0 60px 0; margin-top: var(--header-height);">
        <div class="container">
            <span class="section-subtitle" style="color: var(--color-secondary);">Visual Tour</span>
            <h1 style="color: white; font-size: 48px; margin-bottom: 16px;">Our Shop & Stock Gallery</h1>
            <p style="color: #94a3b8; font-size: 18px; max-width: 700px;">Explore real photographs of Shubham Stationery. See our actual inventory, organized display shelves, and wholesale sections.</p>
        </div>
    </section>

    <!-- Gallery Section -->
    <section class="section-padding" style="background-color: var(--color-bg-base);">
        <div class="container">
            <!-- Filter Bar -->
            <div class="products-filter-container">
                <button class="filter-btn active" data-filter="all">All Photos ({len(images)})</button>
                <button class="filter-btn" data-filter="store">Store Interior</button>
                <button class="filter-btn" data-filter="products">Product Displays</button>
            </div>
            
            <!-- Grid -->
            <div class="products-catalog-grid">
                {cards_html}
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <!-- Info Column -->
                <div>
                    <div class="footer-info-logo">
                        <div class="logo-icon">S</div>
                        <span>Shubham Stationery</span>
                    </div>
                    <p class="footer-desc">Premium stationary supply shop near New Bus Stand, Salem. Over 15 years of serving academic and commercial sectors with high quality stationery.</p>
                    <div style="font-size: 13px; color: #64748b;">
                        Proprietor: <strong>Nirmal Jayantilal Jain</strong>
                    </div>
                </div>
                
                <!-- Quick links -->
                <div>
                    <h3 class="footer-links-title">Quick Links</h3>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html">About Our Shop</a></li>
                        <li><a href="products.html">Product Catalogue</a></li>
                        <li><a href="gallery.html">Photo Gallery</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                    </ul>
                </div>
                
                <!-- Trust & Compliance links -->
                <div>
                    <h3 class="footer-links-title">Trust & Legal</h3>
                    <ul class="footer-links">
                        <li><a href="gst-compliance.html">GST Registration Details</a></li>
                        <li><a href="gst-compliance.html">Form GST REG-06 Certificate</a></li>
                        <li><a href="about.html">15 Years Timeline</a></li>
                    </ul>
                </div>
                
                <!-- Contact info -->
                <div>
                    <h3 class="footer-links-title">Get in Touch</h3>
                    <ul class="footer-contact-list">
                        <li class="footer-contact-item">
                            <span class="footer-contact-icon">📍</span>
                            <span>20/2, Veerapandiyar Nagar, Near New Bus Stand, Salem, Tamil Nadu, 636004</span>
                        </li>
                        <li class="footer-contact-item">
                            <span class="footer-contact-icon">📞</span>
                            <span>
                                <a href="tel:+919025544624" style="color: white; font-weight:700;">9025544624</a><br>
                                <a href="tel:+919566449025" style="color: white; font-weight:700;">9566449025</a>
                            </span>
                        </li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; <span id="current-year"></span> Shubham Stationery. All rights reserved. Managed by Nirmal Jayantilal Jain.</p>
                <div class="footer-legal-links">
                    <a href="gst-compliance.html">GSTIN: 33AGWPJ3473C1ZC</a>
                    <span>|</span>
                    <a href="gst-compliance.html">Proprietorship Verified</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Client Script -->
    <script src="js/main.js"></script>
</body>
</html>
"""
    with open('gallery.html', 'w') as f:
        f.write(html_content)
    print("gallery.html generated successfully with", len(images), "images!")

if __name__ == '__main__':
    generate()
