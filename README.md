# Hausmans
Application to serve static site for Hausmans

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

```
cp packaging/environment/example.env.prod .env
# fill in values in .env
cp docker-compose-prod.yml docker-compose.yml
docker-compose up --build -d
```

To set up SSL certificates with certbot, edit the `init-letsencrypt.sh` file and all nginx files in the nginx directory to have the correct domain name.

Then run `./init-letsencrypt.sh` to generate the certificates.

Once the certs have been generated, the application can be started with 
```
docker-compose up --build -d
```


###Loading portfolio project data

The images for the portfolio projects that were on the legacy version of hausmans.com can be found in the src/hausmans/public_app/media_fixtures directory.

To load them into the media directory so Django can recognize them and serve them in the front end, run the following command:
```shell script
docker-compose exec web python manage.py collectmedia
```

In addition, the database records for these projects are stored in the fixtures directory. To load these records, run:
```shell script
docker-compose exec web python manage.py loaddata fixtures/portfolio_projects.json
```

After these two commands have been ran, the database will be seeded with the portfolio projects from legacy hausmans.com 


### Deploying changes to the application server
1. Make your changes to the application locally, then commit them and push them to the Github repo
2. SSH into the application server, and cd into the project directory (should be ~/hausmans)
3. The application server has a deploy key registered with Github, so you should be able to pull from the repository as usual (e.g. `git pull origin main`)
    a. No changes have been made on the server that are not checked into git, so you can pull freely without worry
4. Restart the application containers to pick up the changes:
    a. `docker-compose down && docker-compose up -d`
    
 
