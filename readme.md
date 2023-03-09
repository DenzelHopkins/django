# Django web api

## Version
python 3.10.4
pip 23.0.1
django 4.1.7
django-admin 4.1.7

## Docker
### Build docker image
> docker build -t django_web_api .

### Run docker container
> docker run -p 8000:8000 django_web_api

### Login to docker registry
<strong>Important</strong>: Saved environment variable is needed.

> echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin

### Tag docker image
> docker tag django_web_api ghcr.io/denzelhopkins/django_web_api:latest

### Push docker image
> docker push ghcr.io/denzelhopkins/django_web_api:latest