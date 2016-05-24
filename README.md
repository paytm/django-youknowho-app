# django-youknowho-app

Django Youknowwho Gui is a Django app to give gui for rule-engine app. It also exposes an api
where rules can be get in json format.

## Installation

* Download and install manually

    ```
    git clone https://github.com/paytm/django-youknowho-app.git
    cd django-youknowho-app
    python setup.py install
    ```

## Use

1. Add "youknowwhogui" to your INSTALLED_APPS like this

    ```
    INSTALLED_APPS = (
        ...
        'youknowwhogui',
    )
    ```

2. To create models, run migrate like

    ```
    python manage.py migrate
    ```

3. Include the urls of the app in your root url by

    ```
    url(r'^youknowwhogui/', include('youknowwhogui.urls', namespace='youknowwhogui')),
    ```

4. To get the list of all rules, in json format, use `/rules` api. Assuming that your app is running
    at port 8000, curl call can be 

    ```
    curl 'http://localhost:8000/youknowwhogui/rules'
    ```
