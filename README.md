# Github and Twitter Connections
This is a simple Django app for the exploring GitHub and Twitter API.

REST API which will return whether two “developers” are fully connected or not. Given a pair of developer IDs,
they are considered connected if:
* They follow each other on Twitter.
* They have at least a Github organization in common.
Assume that people having the same handle both in Twitter and Github are actually the same
person.

## Real-time Endpoint
An example of a request to this endpoint for the handles @dev1 and @dev2 would be like:
```
GET /connected/realtime/dev1/dev2
```
The response is in JSON format with the following structure:
- Case the devs are not connected:

```
{
    "connected" : false
}
```
- Case the devs are connected:
```
{
    "connected" : true,
    "organisations": ["org1", "org2", "org3"]
}
```
In case there are some errors the API should respond with a JSON describing the issue/s, for
instance in case one or both handles does not exist in any of the services we return a
JSON like:
```
{
    "errors": [
        "dev1 is no a valid user in github",
        "dev1 is no a valid user in twitter",
        "dev2 is no a valid user in twitter"
    ]
}
```

## Register Endpoint
This endpoint should be invoked with:
```
GET /connected/register/dev1/dev2
```
And it returns all the related information from previous requests to the real-time endpoint.
The response is a list of found records in JSON format (or an empty list if no records are
in the database). As in this example:
```
[
    {
        "registered_at" : "2019-09-13T09:30:00Z",
        "connected" : false
    },
    {
        "registered_at" : "2019-09-15T10:30:00Z",
        "connected" : true,
        "organisations": ["org1", "org2", "org3"]
    },
    {
        "registered_at" : "2019-09-27T12:34:00Z",
        "connected" : true,
        "organisations": ["org1", "org2", "org3", "org4"]
    }
    ...
]
```
This implementation to query the official Twitter and Github APIs.

## HOWTO run the application
This is a simple Django app, so the steps are the following:
1. Install Python 3 interpreter with pip.
2. Run `pip install -r requirements.txt` from the root of the project.
3. Provide necessary environment variables, such as:
   1. SECRET_KEY
   2. TWITTER_CONSUMER_KEY
   3. TWITTER_CONSUMER_SECRET
   4. GITHUB_TOKEN
   5. DJANGO_SETTINGS_MODULE
4. Run `python manage.py runserver` to run the dev server.

There is also Docker files which can be used to start app in the container.