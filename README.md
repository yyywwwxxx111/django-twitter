# django_twitter
Implement twitter backend system by Django, MySQL, Redis. <br>
Used push model to fanout news feeds.<br>
Used Redis to cache all tweets and feeds.<br>
Used Redis as Message Queue Broker to deliver asynchronized tasks like email delivery and feeds fanout.<br>
