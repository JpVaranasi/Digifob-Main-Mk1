# Digifob-Main-Mk1
Main version of digifob.

DigiFob is a software solution designed to eliminate the everyday hassle with physical keyfobs taking advantage of the urge in use of phones and iPads (especially within my school). 

It allows students to check their balance, make payments, reserve in advance to skip large queue times and take a look at the school menu from within the app. 

Parents can also view the menu, their child's balance , manage their accounts and top up their child's account all from the app.

Schools can also effectively do the same as parents but with additional features such as taking in payments through qr codes and view key statistics. 

## Setting up
To set up this project, I highly reccommend using a python virtual environment which can be created by the command 
''' python.exe -m venv venv '''
followed by 
''' .\venv\Scripts\Activete '''

To install the required libraries I have added a requirements.txt file, to use the file use the command 
''' pip install -r requirements. txt '''

After this you should be ready to start the server.
First you would have locate manage.py, to do this use the command
''' cd .\digifob_main\ '''
followed by
''' python.exe manage.py runserver '''

This would take a minute and load up the server for you to use, within the cmd/terminal it will aso give you the link to the home page.

Visiting the hyperlink will take you to the index page, which ask for login username and password.

The preloaded usernames and passwords are listed below.

Students : 

Alex : alex@stcyres.org , pwd : Alex123
Ron : ron@stcyres.org , pwd : Ron123
Clyde : clyde@stcyres.org, pwd : Clyde123
Trial : trial@stcyres.org , pwd : Trial

Teachers : 

Jack : jack@stcyres.org , pwd : SnottyJack

Parents :

Alex's parents:
Parent 1 : Alexparent@gmail.com , pwd : AlexParent1
Parent 2 : Alexparent2@gmail.com , pwd : AlexParent2

Admin :
Username : admin
Email : admin@admin.com
Password : root

If the admin causes issues , feel free to create an admin account using 
''' python.exe manage.py createsuperuser '''

For any other issues, feel free to contact 2010jpvaranasi@stcyres.org