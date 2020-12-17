# Hubbard Research
Application to manage testing of Hubbard Research students

## Running the app locally

```
cp packaging/environment/example.env.dev .env
cp docker-compose-dev.yml docker-compose.yml
docker-compose up --build
```

View the application at localhost:8000

### Loading test data
To load dummy data for testing, run:
```shell script
docker-compose exec web python manage.py loaddata fixtures/test_data.json
```

Loading this test data also creates a superuser with the following login information:

**username:** superuser<br>
**password:** superuser

## Deployment Notes
This app uses nginx running in a docker container.

Use the docker-compose-prod.yml file when running on a server.

To set up SSL certificates with certbot, edit the `init-letsencrypt.sh` file and all nginx files in the nginx directory to have the correct domain name.

Then run `./init-letsencrypt.sh` to generate the certificates.

Once the certs have been generated, the application can be started with 
```
cp packaging/environment/example.env.prod .env
# fill in values in .env
cp docker-compose-prod.yml docker-compose.yml
docker-compose up --build -d
```
