<h1> Introduction </h1>
<br>
Hamrobazaar on Steroids is a platform for all individuals to get rid of their unwanted functioning items. This application concentrates on providing aid to needy ones while also focusing on sustainability. The saying “One man’s trash is another man’s treasure” goes way back in the day. The application helps to achieve this motive by making people able to list the goods they no longer used on this platform which are later attainable for other people using the platform. This web application uses the Django framework for its backend and HTML, CSS, and Javascript for the frontend embedded with a web3 payment option if the user wants to send tip. 
<br>
<h1>Aim</h1>
<br>

	The primary aim of the platform is to directly impact the environment and sustainability, as the program can achieve eight out of seventeen goals of sustainability of the domain.
<br>


<h1>Objectives </h1>
<br>
•	To promote reusability before recycling.
<br>
•	To manage waste products from the base level.
<br>
•	To uplift people living under the poverty line.
<br>
•	For responsible consumption and production.
<br>
•	To reduce inequalities that remain in the modern era.
<br>
•	To have the slightest impact on the overall economic growth.
<br>


<br>
<h1>Features and functionalities</h1>

<br>
<h2>Feature </h2>
•	List user’s unwanted item in the open market with its category.
<br>
•	Register and log in 
<br>
•	Find what you want and reserve the item at a limit of one item per day, which suits the pickup location.
<br>
•	An option to tip users anonymously using the Web-3 gateway.
<br>

<br>
<h2>Functional Requirements </h2>
<br>
•	A single email can be used to register only one account
<br>
•	Once a user reserves an item, it cannot be reserved by another user.
<br>
•	The receiving customer can initiate an optional tip.
<br>
•	Users can reserve utmost one item each day.  
<br>

<br>
<h2>Non-functional Requirements </h2>
<br>
•	The server should be able to handle more than one user registration at any given time.
<br>
•	The super user of the application can remove the listings if any seem inappropriate for the site.
<br>
•	The passwords are stored in the database using the sha256 hashing mechanism, which is next to impossible to decrypt.
<br>


<h2> How to run this project </h2>
<br>
Step-1 : Install requirements.txt from commnand below <br>
        pip install -r requirements.txt 
        <br>
Step-2 :  Create database <br>
Step-3 : Run this commands <br> python manage.py makemigrations <br>
Step-4 : python manage.py migrate <br>
Step-5 : python manage.py runserver <br>
