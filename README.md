# Spider-WebDev-Task_4
Spider Web Dev Task 4 - User Authentication

GENERAL OVERVIEW  
  
#####  
SPIDER BACKEND TASK 2 


 This is the second task for Spider WebDev Inductions (Backend). Authentication and authorization are important concepts towards securing your websites and applications.
Authentication is used to verify that a particular user is exactly who he/she claims to be. Authorization is the process of allowing an authenticated user to perform certain operations which may be restricted to other users.
 ------------------------------------------------------------------------------------------------------

 MODULES USED AND BUILD INSTRUCTIONS :-  

Python Version used = 2.7.10    
Django version used = 1.9.4    
Get it by using the command :-  
pip install django  
  
Database used = MySQL 5.7.12  
Download from :- http://dev.mysql.com/downloads/mysql/    

You also need some python modules for working with the MySQL database.  
Get it on Windows :-  
pip install mysqlclient  
pip install MySQL-python  
    
Get it on Linux :-   
sudo apt-get install libmysqlclient-dev  
sudo pip install MySQL-python    
   
    
Database Name :- spider2   


If you have the above requisites, you may follow the given steps :-  
1) Clone the repository on a local folder.  
2) For setting up your database connections, open 'bulletin_board\settings.py'. In the 'DATABASES' section, 
   set the NAME as your database name (make sure that it already exists), set the USER and PASSWORD as you username and
   password for setting up the connection with the database, and similarly set the HOST and PORT for the MySQL server.   
     The default values are :-   
	      'NAME': 'spider2',  
        'USER' : 'root',   
        'PASSWORD' : 'password',   
        'HOST' : 'localhost',  
        'PORT':'3306',   

3) In your local directory, run the command :-  
		 python manage.py makemigrations    
4) In the same directory, run another command :-  
		 python manage.py migrate      
5) To create an admin user, run this command in the local directory :-   
         python manage.py createsuperuser    
   Enter the details for the admin user.     
6) If the above commands are successful, then you are ready to run your server.  
   Run the command :-  
		 python manage.py runserver  
   (OR)   
    Run the script runserver.bat (if you are on Windows)      
     
If this executes without errors, then your server is up and running on port 8000. You can view it by opening 'localhost:8000' in your browser. 
