# Django

## Version
python 3.10.4
pip 23.0.1
django 4.1.7
django-admin 4.1.7

## Docker
### Build docker image
> docker build -t django .

### Run docker container
> docker run -p 8000:8000 django

### Login to docker registry
<strong>Important</strong>: Saved environment variable $CR_PAT is needed.

https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry

> echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin

### Tag docker image
> docker tag django ghcr.io/denzelhopkins/django:latest

### Push docker image
> docker push ghcr.io/denzelhopkins/django:latest