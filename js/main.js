/**
 * Shubham Stationery - Client-Side Interactivity
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Toggling
    const menuBtn = document.querySelector('.menu-btn');
    const nav = document.querySelector('.nav');

    if (menuBtn && nav) {
        menuBtn.addEventListener('click', () => {
            menuBtn.classList.toggle('active');
            nav.classList.toggle('active');
        });

        // Close menu when clicking navigation links
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                menuBtn.classList.remove('active');
                nav.classList.remove('active');
            });
        });
    }

    // 2. Header Scroll Transition
    const header = document.querySelector('.header');
    const handleScroll = () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    };
    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Initial run

    // 3. Dynamic Copyright Year
    const yearSpan = document.getElementById('current-year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // 4. Product Catalog Filtering (Only executes if filter controls exist)
    const filterButtons = document.querySelectorAll('.filter-btn');
    const productCards = document.querySelectorAll('.product-item-card');

    if (filterButtons.length > 0 && productCards.length > 0) {
        filterButtons.forEach(button => {
            button.addEventListener('click', () => {
                // Remove active class from all buttons and apply to current
                filterButtons.forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');

                const filterValue = button.getAttribute('data-filter');

                productCards.forEach(card => {
                    const category = card.getAttribute('data-category');
                    if (filterValue === 'all' || category === filterValue) {
                        card.style.display = 'flex';
                        // Small animation delay for smooth fade in
                        card.style.opacity = '0';
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transition = 'opacity 0.4s ease';
                        }, 50);
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }

    // 5. Quote and Contact Form Submission (Mock)
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Basic fields validation
            const name = document.getElementById('name').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const message = document.getElementById('message').value.trim();

            if (!name || !phone || !message) {
                alert('Please fill out all required fields.');
                return;
            }

            // Custom modern UI success response
            const formContainer = contactForm.parentElement;
            formContainer.innerHTML = `
                <div style="text-align: center; padding: 40px 20px;">
                    <div style="width: 70px; height: 70px; background-color: #d1fae5; color: #10b981; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 36px; margin: 0 auto 24px auto;">
                        ✓
                    </div>
                    <h3 style="font-family: 'Outfit', sans-serif; font-size: 24px; color: #0f172a; margin-bottom: 12px;">Quote Request Received!</h3>
                    <p style="font-family: 'Plus Jakarta Sans', sans-serif; color: #64748b; font-size: 15px; margin-bottom: 24px; max-width: 380px; margin-left: auto; margin-right: auto;">
                        Thank you, <strong>${name}</strong>. Nirmal Jain and team will get back to you shortly. For immediate response, call us directly or click the WhatsApp button.
                    </p>
                    <a href="tel:+919025544624" class="btn btn-primary" style="display: inline-flex; align-items: center; gap: 8px;">
                        Call Shop Now
                    </a>
                </div>
            `;
        });
    }

    // 6. Highlight active navbar link matching current page pathname
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        // Check if path ends with href or if at root folder index
        if (currentPath.endsWith(href) || (currentPath.endsWith('/') && href === 'index.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});
