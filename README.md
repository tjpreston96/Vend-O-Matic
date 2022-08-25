# Vend-O-Matic
## Links

### [Deployed Site](https://vend-o-matic-service.herokuapp.com/)
### [Trello](https://trello.com/b/wlLE03H0/vend-o-matic)

## Docker
| Image                              | Image ID    |  Tag        |  Size       |
| -----------                        | ----------- | ----------- | ----------- |
| tpreston96/emma-assessment_web     | 92be66af5a90| latest      |  1.01 GB    |


## Instructions

1. Open [deployed site](https://vend-o-matic-service.herokuapp.com/)
2. Navigate to '/routes' to view all possible actions
3. Use Vend-O-Matic
4. Restore database by navigating to '/restore' and sending a PUT request

## Local Instructions

1. git clone https://github.com/tjpreston96/Vend-O-Matic.git <preferred_dir_name>
2. cd into directory and open IDE
3. `touch .env` in vendomatic directory containing:
```
SECRET_KEY=<Contact_Repository_Owner>
DEBUG=<desired_debug_bool>
```
4. In CLI run: `docker compose up`
> If web container fails on first compose, please wait for db container to initialize
5. Run: `docker compose down` and `docker compose up`
6. Attach shell to web container or run: `docker exec -it <web_container_id> bash`
7. In web container CLI run: 
    1. `python manage.py showmigrations`
    2. `python manage.py migrate`
    3. `python manage.py createsuperuser` and fill out information
8. Close web container CLI
9. Navigate to localhost:8000/admin
10. Log in and create:
    1. 1 Currency named 'coin' with default quantity
    2. 3 Items with default values
11. Click `View Site` on top right navbar
12. Enjoy!
