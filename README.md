# django-twitter
Implement twitter backend system by Django, MySQL, Redis.
Used push model to fanout news feeds.
Used Redis to cache all tweets and feeds.
Used Redis as Message Queue Broker to deliver asynchronized tasks like email delivery and feeds fanout.
