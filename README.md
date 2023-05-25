# Air Insight  
Install the following dependencies:

    pip install flask flask_cors oracledb

Set your Oracle username and password on the main.py file from database directory:

    connection = oracledb.connect(
    user="username",
    password="password",
    dsn="localhost/xe")

Execute the main.py file from backend directory:

    python main.py

If Python doesn't find the dependencies modules.
Create a virtual environment, make sure that you in the 'backend' directory and run the following command:

    python -m venv myenv
    myenv/Scripts/Activate

If you want to desactivate the environment:

    deactivate

Run again:

    pip install flask flask_cors oracledb

Execute main.py file:

    python main.py