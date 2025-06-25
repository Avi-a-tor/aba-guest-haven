Flask web app version of Asaba Guest Haven

from flask import Flask, render_template_string

app = Flask(name)

Sample HTML template using Jinja2 templating (simplified version of original HTML)

template = '''

<!DOCTYPE html><html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Asaba Guest Haven</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
    header, footer { background-color: #1e1e1e; color: white; padding: 1em; text-align: center; }
    nav { background-color: #f4f4f4; display: flex; justify-content: center; gap: 20px; padding: 1em; }
    nav a { text-decoration: none; color: #333; font-weight: bold; }
    section { padding: 2em; }
    .listings { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5em; }
    .property { border: 1px solid #ccc; padding: 1em; border-radius: 8px; }
    .property img { width: 100%; height: 180px; object-fit: cover; border-radius: 4px; }
  </style>
</head>
<body>
  <header>
    <h1>Asaba Guest Haven</h1>
    <p>Your perfect stay in the heart of Asaba</p>
  </header>  <nav>
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#services">Services</a>
    <a href="#blog">Blog</a>
    <a href="#shop">Shop</a>
    <a href="#contact">Contact</a>
  </nav>  <section id="home">
    <h2>Featured Listings</h2>
    <div class="listings">
      {% for property in properties %}
      <div class="property">
        <img src="{{ property.image }}" alt="{{ property.title }}">
        <h3>{{ property.title }}</h3>
        <p>{{ property.description }}</p>
        <p><strong>{{ property.price }}</strong></p>
      </div>
      {% endfor %}
    </div>
  </section>  <section id="about">
    <h2>About Us</h2>
    <p>Asaba Guest Haven is your go-to destination for premium stays in Asaba.</p>
  </section>  <section id="services">
    <h2>Our Services</h2>
    <ul>
      <li>24/7 Concierge Service</li>
      <li>Airport Pickup & Drop-off</li>
      <li>Fully Furnished Apartments</li>
      <li>Free Wi-Fi and Cable TV</li>
      <li>Daily Housekeeping</li>
    </ul>
  </section>  <section id="blog">
    <h2>From the Blog</h2>
    <p><strong>Coming Soon:</strong> Local guides and guest tips.</p>
  </section>  <section id="shop">
    <h2>Shop</h2>
    <p>Coming soon! Local souvenirs and guest amenities.</p>
  </section>  <section id="contact">
    <h2>Contact Us</h2>
    <p>Email: info@asabaguesthaven.com</p>
    <p>Phone: +234 800 000 0000</p>
    <p>Location: Asaba, Delta State, Nigeria</p>
  </section>  <footer>
    <p>&copy; 2025 Asaba Guest Haven. All rights reserved.</p>
  </footer>
</body>
</html>
'''@app.route('/') def home(): # Sample property data properties = [ { 'title': '2-Bedroom Apartment', 'description': 'Cozy and modern, perfect for weekend getaways. Located in GRA Asaba.', 'price': '₦35,000/night', 'image': 'https://via.placeholder.com/400x300' }, { 'title': 'Luxury Guest House', 'description': 'Fully furnished, with premium amenities and serene environment.', 'price': '₦60,000/night', 'image': 'https://via.placeholder.com/400x300' } ] return render_template_string(template, properties=properties)

if name == 'main': app.run(debug=True)
flask
render.yaml
