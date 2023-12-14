Dream Garden Real Estate Company
---
1. Clone Project from github
2. Create virtualenv
      ```sh
    $ virtualenv venv
    ```
3. Activate Virtualenv
   ```sh
    $ source venv/Scripts/activate
    ```
4. Install Requirements
   ```sh
    $ pip install -r requirements.txt
    ```

5. Add project specific information in .env
6. Make migration
    ```sh
    $ python manage.py makemigrations
    ```
7. Migrate
    ```sh
    $ python manage.py migrate
    ```
8. Create Superuser
    ```sh
    $ python manage.py createsuperuser
    ```
9. Start Server
    ```sh
    $ python manage.py runserver
    ```

10. Run Celery for the background tasks
    ```sh
    $ celery -A real_estate_erp worker -l info -P threads  
    $ celery -A real_estate_erp beat -l info

    $ stripe listen --forward-to http://localhost:8000/api/v1/webhooks/stripe/
    ```

11. Stripe Webhook CLI Commands
    ```sh
    $ stripe login

    $ stripe listen --forward-to http://localhost:8000/api/v1/webhooks/stripe/
    ```