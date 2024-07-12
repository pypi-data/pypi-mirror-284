# OpenLXP-Authentication

This is a Django package built on the social-auth-app-django package to allow additional authentication options for the OpenLXP project.

Currently this package adds support for storing SAML configurations in the database used by Django, to allow for site administrators to set SAML configurations through the admin app.


## Setup

To install this package install the dependencies from the requirements file (this should happen automatically if using pip) (make sure libxml2-dev libxmlsec1-dev are installed if running in Docker).

Add the required settings to the Django settings file, social_django settings may also be used.

Add the included URLs to Django (this will add the social_django URLs for you).

```python
urlpatterns = [
    ...
    url('', include('openlxp_authentication.urls')),
]
```

Access the `/saml/metadata/` endpoint to view the configuration XML and verify it is correct (if AssertionConsumerService Location is incorrect, there are optional settings to fix it).

Upload the XML to needed IDPs.

Login to the admin module to add IDP configurations (the name setting will be used to identify which configuration to use).

To test the login configuration: 

1. Logout if you are already logged in

1. Access `/login/samldb/?idp=nameFromConfig`

1. You should be redirected to your chosen IDP

1. Login with your IDP

1. You will be returned to the application and sent to the REDIRECT_URL if set


## Settings 


### Required Settings

#### JSONFIELD_ENABLED

The JSONFIELD_ENABLED setting is required as it allows storing the attribute mapping as JSON in the database.

```ini
JSONFIELD_ENABLED = True
```

#### USER_MODEL

The USER_MODEL setting sets what model should be used when authenticating a User.

```ini
USER_MODEL = 'core.XDSUser'
```

#### SP_ENTITY_ID

The SP_ENTITY_ID setting sets Entity ID that IDPs should use for identifying the service.  This settings should be unique to your service.

```ini
SP_ENTITY_ID = 'http://localhost:8000'
```

#### SP_PUBLIC_CERT

The SP_PUBLIC_CERT setting sets the public key to be used when authenticating users.

```ini
SP_PUBLIC_CERT = "******"
```

#### SP_PRIVATE_KEY

The SP_PRIVATE_KEY setting sets the private key to be used when authenticating users.

```ini
SP_PRIVATE_KEY = "******"
```

#### Contact Info

Contact information is set in three settings to provide to IDPs; ORG_INFO, TECHNICAL_CONTACT, and SUPPORT_CONTACT.

```ini
ORG_INFO = {
    "en-US": {
        "name": "example",
        "displayname": "Example Inc.",
        "url": "http://localhost",
    }
}
TECHNICAL_CONTACT = {
    "givenName": "Tech Gal",
    "emailAddress": "technical@localhost.com"
}
SUPPORT_CONTACT = {
    "givenName": "Support Guy",
    "emailAddress": "support@localhost.com",
}
```

#### USER_ATTRIBUTES

The USER_ATTRIBUTES setting list the attributes of the User model that should be retrieved from the IDP.

This setting is used to set the default value for the attribute map in the IDP configuration

```ini
USER_ATTRIBUTES = ["user_permanent_id",
        "first_name",
        "last_name",
        "email"]
```

#### AUTHENTICATION_BACKENDS

The AUTHENTICATION_BACKENDS setting sets what authentication services should be available.

This setting must include `'openlxp_authentication.models.SAMLDBAuth'`, but others can included as desired.

```ini
AUTHENTICATION_BACKENDS = (
    ...
    'django.contrib.auth.backends.ModelBackend',
    'openlxp_authentication.models.SAMLDBAuth',
)
```

#### INSTALLED_APPS

The INSTALLED_APPS setting sets what apps Django should load.

Both social_django and openlxp_authentication must be added for this package to work correctly.

```ini
INSTALLED_APPS = [
    ...
    'social_django',
    'openlxp_authentication',
]
```


### Optional Settings

#### SESSION_EXPIRATION

The SESSION_EXPIRATION setting has the Django session expiration match an expiration supplied by the IDP.

```ini
SESSION_EXPIRATION = True
```

#### LOGIN_REDIRECT_URL

The LOGIN_REDIRECT_URL setting is used by the application to redirect the user upon a successful login.

```ini
LOGIN_REDIRECT_URL = 'http://www.google.com'
```

#### OVERIDE_HOST

The OVERIDE_HOST setting is used when Django is not able to accurately determine the host and port being used (this can occur in certain reverse proxy configurations).  

The setting must follow the format `http://www.hostname.com:port`, `https://` may be used instead.

If this setting is supplied, SOCIAL_AUTH_STRATEGY and BAD_HOST should also be set.

```ini
OVERIDE_HOST = 'http://localhost:8000'
```

#### BAD_HOST

The BAD_HOST setting is used to remove part of the host and port string if the automatically detected configuration is incorrect.

Similar to OVERIDE_HOST, this setting should also start with either `http://` or `https://`.

The setting is required if using the OVERIDE_HOST setting.

```ini
BAD_HOST = 'http://localhost'
```

#### SOCIAL_AUTH_STRATEGY

The SOCIAL_AUTH_STRATEGY setting is required if using the OVERIDE_HOST setting.  OpenLXP-Authentication provides a strategy but custom solutions can be created and referenced in this setting.

```ini
SOCIAL_AUTH_STRATEGY = 'openlxp_authentication.models.SAMLDBStrategy'
```
