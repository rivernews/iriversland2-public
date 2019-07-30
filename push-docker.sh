docker login
docker build . -t shaungc/iriversland2-django:w-cred01 -f prod.Dockerfile
docker push shaungc/iriversland2-django:w-cred01