# django web application

This is a web application built using python django framework. 
This app uses django version 2.0.3 in the backend and 
postgres sql at the database side. This app has a basic front end 
developed using bootstrap css and js. This application is built 
and tested for python version 3.6.

## Installation Steps


1. Install python 3.6 if not done already 
2. Download and extract application tar ball
3. Import the project to an IDE of your choice (I use PyCharm)
4. Setup project interpreter (setup python venv) and project structure.
   - In PyCharm follow below steps
     - PyCharm -> Preferences -> Project -> Project Interpreter
     ![Alt text](scrrenshots/PyCharm1.png?raw=true "Setup Project Interpreter PyCharm")
     - PyCharm -> Preferences -> Project -> Project Structure
     ![Alt text](scrrenshots/PyCharm2.png?raw=true "Setup Project Structure PyCharm")
5. Configure your database details in settings.py file.
6. Execute following commands to setup your database with necessary tables.
   ```
   <venv>/python manage.py makemigrations music
   <venv>/python manage.py migrate
   ```
7. Create admin user for your application
   ```
   <venv>/python manage.py createsuperuser
   ```   
   create admin credentials when prompted 
8. Now run the application
   ```
   <venv>/python manage.py runserver
   ```
   now [application](http://localhost:8000/music) would be started in 8000 port. 
9. In PyCharm you can also setup the debug environment for the project by
   setting the run time configuration for manage.py
   ![Alt text](scrrenshots/PyCharm3.png?raw=true "Setup debug environment in PyCharm")
10. Browse through the app and enjoy... Happy coding
    ![Alt text](scrrenshots/app.png?raw=true "Application Detail View")

   
   
   
    
