# BS-PMC-2023-Team10
BS-PMC-2023-Team10


=========================================
Django Project README
=========================================

This README provides instructions on how to set up and run the Django project. Before getting started, make sure you have Python and pip installed on your system.

-----------------------------------------
Setting Up the Virtual Environment
-----------------------------------------

To ensure a clean and isolated environment for running the project, it is recommended to create a virtual environment. Follow the steps below to set it up:

1. Open a terminal or command prompt.
2. Navigate to the project directory using the 'cd' command.
3. Create a new virtual environment by running the following command:
   
   python -m venv env

4. Activate the virtual environment:

   - For Windows:

     env\Scripts\activate

   - For macOS/Linux:

     source env/bin/activate

-----------------------------------------
Installing Project Dependencies
-----------------------------------------

The project's dependencies are listed in the 'requirements.txt' file. To install them, follow the steps below:

1. Ensure that your virtual environment is activated.
2. Run the following command to install the required packages:

   pip install -r requirements.txt

   This command will install all the necessary packages and their dependencies.

-----------------------------------------
Running the Django Project
-----------------------------------------

Once the virtual environment is set up and the project dependencies are installed, you can run the Django project using the following steps:

1. Ensure that your virtual environment is activated.
2. Navigate to the project directory if you're not already there.
3. Run the following command to start the Django development server:

   python manage.py runserver

   The development server should start, and you'll see output indicating that the project is running.

4. Open your web browser and visit 'http://localhost:8000/' to view the project.

-----------------------------------------
Additional Configuration
-----------------------------------------

The Django project may require additional configuration depending on its specific requirements. Please refer to the project documentation or consult with the project developer for any additional steps needed.

-----------------------------------------
Conclusion
-----------------------------------------

Congratulations! You have successfully set up and run the Django project. Feel free to explore the code and customize it to fit your needs. If you encounter any issues or have questions, please refer to the project documentation or seek assistance from the project developer.
