# Just Cupcakes - Testing Details

[Main README.md file](README.md)

[Deployed site](https://just-cupcakes.herokuapp.com/)

The following validators were used to check the validity of the website code:

[W3C Makup Validation Service](https://validator.w3.org/)

[W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/)

[JSHint](https://jshint.com/)

[PEP8online](http://pep8online.com/)

No errors are returned for HTML, JavaScript and CSS. 

For Python, there are 5 errors for "line too long" in the settings.py file, which I did not correct in order not to break the code (errors are for AUTH_PASSWORD_VALIDATORS and STATICFILES_STORAGE). 

## User Stories Testing 

User stories can be found in the UX section in the [README.md file](README.md)

Home and about pages

- As a Site User I want to be presented with a well displayed home page, the information is laid out clearly so that I can navigate the website easily and find what I am looking for.

        i. The home page has a simple but effective layout, there are clear calls to action and the user is not presented with too much information that could be confusing and cause lack of interest. 

        ii. There is a clear navigation menu at the top of the page that allows the users to easily navigate thought the website and find what they are searching for. 

- As a Site User I want to be able to view the bakery information, including address and contact details so that I can visit or contact the bakery if I need to. 

        i. By clicking on the "About us" link from the "About" dropdown menu in the main navigation bar, the user is redirected to the About page, where the bakery information is displayed. 

Products

- As a Site User I want to be able to easily identify the different cupcake categories so that I can chose the one I am intersted in. 

        i. Site users can identify the different cupcakes categories by clicking on the "Shop" dropdown in the main navigation menu, they are then presented with the 3 available categories and an option so see all products for all categories. 

- As a Site User I want to be able to view a list of the available cupcakes for a specified category so that I can select the ones I want to purchase. 

        i. By clicking on one of the categories on the "Shop" dropdown in the main navigation bar, users are redirected to the products page where they can view the available products for the selected category.

        ii. At the top left corner of the page, users will also see how many products are avilable for that category and the category name itself.

- As a Site User I want to be able to select a specific cupcake so that I can view the details on that cupcake such as price, description, image.

        i. By clicking on the picture of any of the products shown in the products page, the user is redirected to the product details page. 

        ii. On the product details page the user is presented with all the information on the selected cupcake, such as name, category, price, description, sku and the cupcake picture. The text "popular" will be displayed next to the cupcke name if the store owners have turned that option. 

Authentication and account 

- As a Site User I want to be able to easily register for an account so that I can have access to a personal profile with information on my past purchases.

        i. The website has an authentication process and users have the possibility to create an account and have access to a personalised profile page. 

- As a Site user I want to receive a confirmation email when I register for an account so that I can verify that the registration was successful. 

        i. Users who register for an account will receive a verification email to their email address. 

        ii. Users are required to complete the verification process in order for them to be able to access the website with their credentials.

- As a registered Site User I want to be able to update my address and contact information stored in my profile so that they can be used for future orders. 

        i. Registered users have access to a personalised profile page that they can access by clicking on "Profile" from the "Account" dropdown in the main navigation menu. 

        ii. In the profile page, users can view their current address and contact information and have the possibility to update them if needed. 

- As a Site User I want to be able to login and logout easily so that I can access my personal account information when I need it. 

        i. Users cn easily login and logout by clicking on the options in the "Account" dropdown in the main navigation menu. 

        ii. Users who logout are presented with a message asking them to confirm that they would like to logout. 

Search and Sort

- As a Site User I want to be able to sort the list of available cupcakes so that I can view the results ordered by price, date, name and category.

        i. On the products page, users will find a sort dropdown menu on the top right corner of the page. 

        ii. In th dropdown, users will see the options to sort the available results by price, date, name and category, in both descending or ascending order.

- As a Site User I want to be able to search the available cupcakes by name and description so that I can find the ones I am interested in. 

        i. There is a seach bar in the main navigtion menu that allows users to search for products. 

        ii. The results returned will have the term the user has searched for in either the name of the cupcake or in the description. 

- As a Site User I want to be able to easily see what I have searched for and the number of results so that I can quickly decide if what I am looking for is available. 

        i. The results of the search will be displayed in the products page, along with the number of results found and the term that the user has searched for. 

Order and checkout

- As a Site User I want to be able to select the quantity of an item when making the purchase so that I can order the quantity I need. 

        i. On the product details page, users have the possibility to select the quantity for the selected products. Default quantity is 1. 

        ii. Users can either enter the quantity manually or click on the plus and minus signs. 

- As a Site User I want to be able to view the items I selected in my bag so that I can see the total price and I can make sure I have selected the correct items and related quantity.

        i. On the top right corner of every page (except for the authentication pages), there is a button that displays the total amount for the items in the bag. By clicking on the button, users are redirected to the bag page.

        ii. In the bag page, users will see a table listing all the items currently in the bag. 

        iii. For each item, users will see the picture of the product, the name, the price, the quantity and the subtotal. 

- As a Site User I want to be able to adjust the quantity of the items in my bag so that I can make the required changes before proceeding with the payment. 

        i. Users have the possibility to update the product quantity in the bag page. They can enter the quantity manually or by clicking on the plus and minus signs. 

        ii. Once the desired quantity has been selected, the user can click on the "Update" link just under the quantity selector and the quantity and related price will be updated. 

- As a Site User I want to easily enter my payment information so that I can checkout quickly. 

        i. When clicking on the "Checkout" button in the bag page, users are redirected to the checkout page. 

        ii. In the checkout page, users are presented with a form where they can enter their shipping information and payment information. 

- As a registered Site Use I want to be able to save my delivery information when creating an order so that they can be used for a future purchase. 

        i. Authenticated users will see a checkbox in the checkout page that will allow to save their delivery information to their profile so that it can be used for future orders. 

- As a Site User I want to view an order summary and confirmation after checkout so that I can verify there are no mistakes in my purchase. 

        i. By clicking on the "Place order" button on the checkout page, an order will be created (if the form is valid) and the user is redirected to the success checkout page. 

        ii. On the success checkout page, users will see a summary of the items purchased, the order details (order number and date) and the delivery information.  

- As a Site User I want to receive a confirmation email after placing the order so that I can verify that the order was successful and I can keep a written record of my purchase. 

        i. A confirmation email will be sent to the customer when an order is created. 

Careers

- As a Site User I want to be able to view current job openings so that I can apply for a position I am interested in.

        i. By clicking on the "Careers" link in the "About" dropdown in the main navigation menu, users will be redirected to the job openings page. 

        ii. On the job openings page, users will see a list of the available job positions that they can apply for. 

- As a Site User I want to be able to apply for a job position so that I might get an interview for a job I am interested in. 

        i. By clicking on the "Apply" button in the job posting, users will be redirected to the application page. 

        ii. On the application page users are presented with a form that they can use to enter their information and submit their application. 

Admin 

- As a Site Owner I want to be able to add a new product so that it will be available for customers to purchase. 

        i. Admin users have an additional option in the main navigation menu, "Management", by clickin on this link they are redirected to the add product page. 

        ii. On the add product page, Admin users will see a form that will allow them to create a new product to be added to the store. 

- As a Site Owner I want to be able to edit an existing product so that I can modify the product's details (description, price, image etc.).

        i. Admin users have the ability to edit an existing product by clicking on the "edit" links that are displayed in both the product cards in the product page or in the product details page for a specific product. 

        ii. By clicking on the "edit" link, Admin users are redirected to the edit product page where they are presented with a form that will allow them to update the existing details for a product. 

- As a Site Owner I want to be able to delete a product so that it is no longer available for sale. 

        i. Admin users have the ability to delete an existing product by clicking on the "delete" links that are displayed in both the product cards in the product page or in the product details page for a specific product. 

        ii. By clicking on the "delete" link, Admin users are redirected to the delete product page where they are presented with a message asking them if they are sure they want to delete the product. By clicking on "Delete product" the selected product will be permanently deleted. 

## Manual Testing 

### Authentication

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
