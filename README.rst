======================
Django Youknowwho Gui
======================

Django Youknowwho Gui is a Django app to give gui for rule-engine app.

Quick start
-----------

1. Add "youknowwhogui" to your INSTALLED_APPS like this::

    ```
    INSTALLED_APPS = (
        ...
        'youknowwhogui',
    )
    ```

2. To create models, run migrate like::

    ```
    python manage.py migrate
    ```

3. Include the urls of the app in your root url by ::

    ```
    url(r'^youknowwhogui/', include('youknowwhogui.urls', namespace='youknowwhogui')),
    ```

4. To get the list of all rules, in json format, use `/rules` api.