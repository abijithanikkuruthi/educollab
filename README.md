# The Social Web Assignment - EduCollab
EduCollab enables educators from all over the world to work together in designing and maintaining curricula with ease. It is also a platform to review each other’s course content in a discussion and feedback network. The collaboratively constructed curricula can be followed around the world, which should empower students and improve global education standards. Educators will be able to save time maintaining their curricula as the network can suggest the newest findings.

This project is done by Group 16 as a part of The Social Web course in Vrije University Amsterdam for the academic year 2019-20. The project is hosted and can be accessed at <a href="http://social.abijith.net">social.abijith.net</a>.

## Local Development

### Setup
Clone the repository and `cd` into the directory. Use the following commands to build the virtual environment. This is done to create an isolated environment and also to avoid Python module version mismatch.
```
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
### Database Migrations
This is done to propagate the changes of the model into the database schema.
```
python3 manage.py makemigrations
python3 manage.py migrate
```
### Collect Static Files
This allows you to gather static files from different modules for deployment.
```
python3 manage.py collectstatic
```
### Create Superuser
```
python3 manage.py createsuperuser
```
Create a super user to log into the admin panel. This enables you to edit the internal settings of the application which can be accessed using the url path `/admin/`.

### Start Server
```
python3 manage.py runserver
```
Debugging can be enabled by changing `DEBUG=True` in the file `educollab/settings.py`. The server should be accessible from http://localhost:8000

## Production Deployment

### Prerequisites
Apache2 and mod_wsgi module for Apache. The wsgi module can be installed by `sudo apt-get install libapache2-mod-wsgi-py3`.

### Setup
Follow the first four steps of local development and make sure that debugging is disabled in `educollab/settings.py`. Also, update the `SECRET_KEY` variable in the same file with corresponding production key to ensure privacy. Additonally, provide Apache with required read and write permissions for the directory as well as the database.

### Configuration
The configurations for static, dynamic file and application server is included below. Also, make sure that the static files and dynamic files url match the corresponding ones in `STATIC_URL` and `MEDIA_URL` in `educollab/settings.py`.
```
        ServerAdmin admin@webmaster
        DocumentRoot /var/www/educollab

        Alias /static /var/www/educollab/staticfiles
        <Directory /var/www/educollab/staticfiles>
                Options -Indexes
        </Directory>

        Alias /media /var/www/educollab/media
        <Directory /var/www/educollab/media>
                Options -Indexes
        </Directory>

        <Directory /var/www/educollab/educollab>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        WSGIDaemonProcess educollab python-path=/var/www/educollab python-home=/var/www/educollab/venv processes=4 threads=4
        WSGIProcessGroup educollab
        WSGIScriptAlias / /var/www/educollab/educollab/wsgi.py
```
Restart the server after adding the host using `a2ensite educollab`.