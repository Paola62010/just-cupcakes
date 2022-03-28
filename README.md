# Just Cupcakes

![Mockups](readme-testing-images/multidevice-mockup.png)

[View deployed site here](https://just-cupcakes.herokuapp.com/)

Just Cupcakes is a well established bakery based in Dublin. The bakery specializes in high quality cupcakes and offers deliveries everywhere in Ireland. Customers can place orders online, register for an account to have access to a personalised profile page where they can review past orders and save their shipping information for future orders. Store employees can manage product creation, update and cancellation via the website. 

## UX
---

### The ideal client for this website: 

- Is based in Ireland.
- Businesses or individuals who are looking for cupcakes deliveries.

### Visitors to this website are searching for: 

- A bakery located in Dublin.
- A bakery that offers online purchases and deliveries in Ireland. 
- A bakery that specializes in cupcakes.  

### User stories

Home and about pages

- As a Site User I want to be presented with a well displayed home page, the information is laid out clearly so that I can navigate the website easily and find what I am looking for. 
- As a Site User I want to be able to view the bakery information, including address and contact details so that I can visit or contact the bakery if I need to. 

Products

- As a Site User I want to be able to easily identify the different cupcake categories so that I can chose the one I am intersted in. 
- As a Site User I want to be able to view a list of the available cupcakes for a specified category so that I can select the ones I want to purchase. 
- As a Site User I want to be able to select a specific cupcake so that I can view the details on that cupcake such as price, description, image.

Authentication and account 

- As a Site User I want to be able to easily register for an account so that I can have access to a personal profile with information on my past purchases.
- As a Site user I want to receive a confirmation email when I register for an account so that I can verify that the registration was successful. 
- As a registered Site User I want to be able to update my address and contact information stored in my profile. 
- As a Site User I want to be able to login and logout easily so that I can access my personal account information when I need it. 

Search and Sort

- As a Site User I want to be able to sort the list of available cupcakes so that I can view the results ordered by price, popularity, date (able to see newest items).
- As a Site User I want to be able to search the available cupcakes by name and description so that I can find the ones I am interested in. 
- As a Site User I want to be able to easily see what I have searched for and the number of results so that I can quickly decide if what I am looking for is available. 

Order and checkout

- As a Site User I want to be able to select the quantity of an item when making the purchase so that I can order the quantity I need. 
- As a Site User I want to be able to view the items I selected in my bag so that I can see the total price and I can make sure I have selected the correct items and related quantity. 
- As a Site User I want to be able to adjust the quantity of the items in my bag so that I can make the required changes before proceeding with the payment. 
- As a Site User I want to easily enter my payment information so that I can checkout quickly. 
- As a registered Site Use I want to be able to save my payment information so that they can be used for a future purchase. 
- As a Site User I want to view an order summary and confirmation after checkout so that I can verify there are no mistakes in my purchase. 
- As a Site User I want to receive a confirmation email after placing the order so that I can verify that the order was successful and I can keep a written record of my purchase. 

Careers

- As a Site User I want to be able to view current job openings so that I can apply for a position I am interested in.
- As a Site User I want to be able to apply for a job position so that I might get an interview for a job I am interested in. 

Admin 

- As a Site Owner I want to be able to add a new product so that it will be available for customers to purchase. 
- As a Site Owner I want to be able to edit an existing product so that I can modify the product's details (description, price, image etc.).
- As a Site Owner I want to be able to delete a product so that it is no longer available for sale. 

### Wireframe mockups

[Desktop Mockups](readme-testing-images/desktop-wireframes)

[Tablet Mockups](readme-testing-images/tablet-wireframes)

[Mobile Mockups](readme-testing-images/mobile-wireframes)

### Faceboob page mockup

[Facebook page](readme-testing-images/facebook-page.pdf)

## Features
---

The header of each page features the website logo and the navigation menu. By clicking on the logo the user is redirected to the home page as it would be expected. The navigation menu is responsive and collapses into a burger menu in smaller screens. The navigation menu shows additional option "Profile" for all authenticated users and additional option "Management" for authenticated Admin users.
The footer on each page features links to social media pages, a link to the privacy policy for the company and the copyright info.

### Home Page



### About Page

### Products Page

### Product Details Pages

### Add Product Page

### Edit Product Page 

### Delete Product Page

### Bag page 

### Checkout Page 

### Success Checkout Page 

### Profile Page 

### Edit Profile 

### Job Postings Page

### Job Aplication Page

### Features to Implement in future

## Technologies Used

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

### Database

- [Heroku Postgres](https://www.heroku.com/postgres) - I have used Postgres both during development and for production.

A detailed diagram for the database can be found [here](readme-testing-images/JustCupcakes-database.pdf).

### Storage

- [Cloudinary](https://cloudinary.com/) - I have used Cloudinary to store media and static files.

### Frameworks

- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - I have used Bootstrap 5.0.2 which helped me design and build a responsive website.
- [Django](https://www.djangoproject.com/) - I have used Django to build the project. 

### Libraries, tools and online resources used

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used extensively during development to check responsiveness.
- [Dj-database-url](https://pypi.org/project/dj-database-url/) - A utility to help you load your database into your dictionary from the DATABASE_URL environment variable. 
- [Pyscopg2](https://pypi.org/project/psycopg2/) - this was used as a PostgreSQL database adapter for Python.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/overview.html) - Used to handle authentication process.
- [Google Fonts](https://fonts.google.com/) - Used for the website fonts.
- [Gunicorn](https://gunicorn.org/) - Used to deploy the project to Heroku.
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - Jinja templating language was used to display backend data in the templates. This has been used both in the HTML and JavaScript.
- [Django-countries](https://pypi.org/project/django-countries/) - A Django application that provides country choices for use with forms, flag icons static files, and a country field for models.
- [Django-autoslug](https://django-autoslug.readthedocs.io/en/latest/) - a Django library that provides an improved slug field which can automatically populate itself from another field. 
- [Stripe](https://stripe.com/) - Used to handle payments for the online purchases. 
- [JQuery](https://jquery.com/) - JavaScript library, used throughout the project to write JavaScript.
- [Pillow](https://pillow.readthedocs.io/en/stable/) - a Python Imaging Library, it was used to help processing image files to store in the database.
- [favicon.io](https://favicon.io/) - Favicon generator.
- [TechSini](http://techsini.com/multi-mockup/) - multidevice mockup generator. I have used this to generate the preview image of the website.
- [Visual Studio Code](https://code.visualstudio.com/) - IDE used for code editing.
- [Heroku](https://www.heroku.com/home) - Used to deploy the app.
- [Adobe XD](https://www.adobe.com/products/xd.html) - Used to create the wireframes. 

## Testing

Testing information can be found in [TESTING.md](TESTING.md) file.

## Deployment

### Cloning the repository

To clone the repository, follow these steps: 

1. Log into Github and locate the repository for this project: [Paola62010/just-cupcakes](https://github.com/Paola62010/just-cupcakes)
2. Above the list of files, click on _Code_, a dropdown menu is presented with different options.
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open the terminal.
5. Change the current working directory to the location where you want the cloned directory to be. 
6. Type _git clone_, and then paste the URL copied earlier (step 3).
7. Press Enter to create your local clone.

Additional information on how to clone a Github repository can be found [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

### Environment variables and ALLOWED_HOSTS

Create an <span>env.py</span> file. The following variables are required for this project:
- SECRET_KEY: any randomly generated key.
- CLOUDINARY_URL: Copy your CLOUDINARY_URL e.g. API Environment Variable from Cloudinary Dashboard (a free account with [Cloudinary](https://cloudinary.com/) is needed for this).
- DATABASE_URL: This is the value of DATABASE_URL in Heroku (step 5 of the next section), located in the Settings Tab, in Config Vars.
- STRIPE_PUBLIC_KEY: your Stripe Publishable key, you will find this in your Stripe dashboard. A free account with [Stripe](https://stripe.com/) is needed for this. 
- STRIPE_SECRET_KEY: your Stripe Secret key, you will find this in your Stripe dashboard. A free account with [Stripe](https://stripe.com/) is needed for this.
- STRIPE_WH_SECRET: your Stripe Webhook secret, you will receive this when you setup an endpoint for webhooks on Stripe. A free account with [Stripe](https://stripe.com/) is needed for this.
- EMAIL_HOST_USER: your email host user. 
- EMAIL_HOST_PASS: your email host password.

In <span>settings.py</span> make sure to correct the ALLOWED_HOSTS values to use your localhost and Heroku app name.

### Deploying to Heroku

To deploy to Heroku follow these steps: 

1. Log into [Heroku](https://dashboard.heroku.com/apps) and locate the "New" button, on the top right end side of your dashboard page. 
2. Click on "Create new app", select your region and pick a name for your project. 
3. On top of the next page there is a navigation bar, select "Settings". 
4. In "Settings" add buildpack Python.
5. Add Database to App Resources. This is located in the Resources Tab, Add-ons, search and add e.g. "Heroku Postgres". 
6. In the Settings Tab, in Config Vars, make sure you have the DATABASE_URL added with the previous step and to add the other variables. Make sure you have the same variables here and in your <span>env.py</span>.
7. On the navigation bar on top of the page, select now "Deploy".
8. Select deployment method "Github" and seach for your repository. 
9. Proceed to link the Heroku app to the repository by clicking on "Connect". 
10. Click on Deploy.

## Credits

### Code

The following articles helped me with my code:

- [How to add favicon to Django in 4 steps](https://simpleit.rocks/python/django/django-favicon-adding/)

### Content

Cupcakes descriptions were taken from [Sally's Baking Recipes](https://sallysbakingaddiction.com/)

### Media

All images for the website have been taken from [Unsplash](https://unsplash.com/)

### Acknowledgements

Thank you to Code Institute, the tutors and my mentor for putting up with my questions and pointing me in the right direction.
