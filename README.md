# user_activity
user_activity

1.install virtual environment

 sudo apt-get install python3-venv

2. activate virtual environment

python3 -m venv virt_env && source virt_env/bin/activate

3. install requirements

pip3 install -r requirements.txt

4. do the migrations

python3 manage.py makemigrations testapp

5. do the migrate

python3 manage.py migrate

6. dump the data using fixture

python3 manage.py loaddata data.json

7. run server

python3 manage.py runserver


