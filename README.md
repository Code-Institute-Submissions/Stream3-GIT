##############======== TastyTimes ======###########
Title: TastyTimes
Navbar: links to differnt Apps

Website tree:
   ** This project uses Django framework which helps you to create your own website base on MVC (Model/View/Controller) and you can create a basis for any templates to main features (all the structure that will support any new templates from your site like static styles, nav bar, etc).
   * On this project the basic template is 'base.html' and the website tree is represented as below:

ebjango project origins the follow Apps:
   	  |___
   	      |
	   	  |__Account
	   	  |
	   	  |__About
	   	  |
	   	  |__Blog
	   	  |
	   	  |__Forum
	   	  |
	   	  |__Contact
	   	  |
	   	  |__Products
	   	  |
	   	  |__Login
	   	  |		|
	   	  |		|__Logout
	   	  |		|
	   	  |		|__Profile
	   	  |
	   	  |__Register/Profile
test
** This is a project based on Python with the followed templates and separated apps:
@pp >> Account app and User Authentication: this app is responsible for User Authentication using email and password.
	- Views contains login, logout, register and Profile page.
		-> Login area presents unique pages that just users logged in can view: profile page, posts and possibility to new posts with polls and logout option.
	- backends.py: this file is responsible to allow/disallow login and will hold our code to check if the email and password are correct.
	- The AbstractUser brings user attributes
	- The User Manager controls registration
	- The django_forms_bootstrap renders the form on the register page. 
	- After the Register page suceeded the Profile Page is shown.
@pp >> Blog app: a separated app designed to the Blog's owner be able to publish many articles and receive comments from anyone at the end of each article. It was provided by Disqus (source: disqus.com, a publisher tool that creates a comment area for readers).
As all the other apps on this project, it is using the base.html template. 

@pp >> Forum app: a new app created to allow discussions about any threads published by users. The users publish new threads and do new posts in any threads if they are logged.
Plugins activated on this Forum app:
    * arrow: a Python library that offers a sensible approach to converting timestamps in human-friendly approaches. Highly recommended reading: http://arrow.readthedocs.io/en/latest/

    * emoticons: this application allows the use of emoticons on any templates (source:https://pypi.python.org/pypi/django-emoticons/1.1.2)

    * django-tinymce: which great features, it is an advanced WYSWIYG HTML editor designed to simplify website content creation. The user's textarea field is much better with this text editor and they can enjoy it while they are writing their posts and threads on Forum App.

@pp >> Contact: its design permits a form to get in touch with the blog's owner. The button 

@pp >> Products: it was designed to allow the purchase of products by users logged in. The Products table shows an image of the product, its name, price, description and a button to PayPal purchase.
The PayPal button is obviously linked just with Sandbox because it is just to illustrate PayPal integration. More info about how to use PayPal Integration to production environment can be seen on http://django-paypal.readthedocs.io/en/stable/standard/ipn.html

@pp >> Login/Logout: those templates are designed to distinct the users that are logged in to permit purchases, new threads and posts. The Profile template appears only when the user is logged in. Logout just appears when the user are logged in and the contrary happens to Login.

@pp >> Register: this template allows the registration of a new user. Stripe: 
Note: Using Python3 where the command "xrange" has became "range".

@pp >> Main: this app contains special functions to the project as it is responsible to important views to render as the views: get_about, get_index, get_thanks and get_contact.

##PayPal
	* The Sandbox was used as a solution to offer products do buy. A button was created but it is just valid when the user are already logged in (requires authentication). After that, the webpage redirects to the PayPal environment with details of the purchase.

## Tests ##
	* The test is necessary to check if a url resolves to the correct view function and that the view shows the right information. The main app contains in tests.py example of testing using django TestCase when a copy is just temporarily made and destroyed to check if the url is resolving the correct page.

##Database
	* The database used to this project locally and hosted to Heroku was SQLite3.
	
##Version Control on GitHub: https://github.com/alinechribeiro/Stream3-GIT.git

## Deployment ##
	* This app was deployed on heroku: https://ebdjango-test2.herokuapp.com/
		>Instructions: Login on Heroku, then follow the commands to push the project on heroku and on GitHub (just used Linux command lines):
			* git add . && git commit -am "make it better" && git push heroku master
			* anytime you need to check your error logs you can use: #heroku logs

** Obviously attention about my Production Sample**
This code was only intended to be used for illustration of how Python, Django framework and Paypal can be integrated. It is not ready for use and is not meant to be used in a production environment by real chocolate trufles lovers. This is the esquelethon to be used for real site in future so PLEASE don't try to buy chocolate truffles through here, it can cause indigestion. :P
