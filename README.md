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
2. cd into directory
3. Open IDE
4. `touch .env` in vendomatic directory containing:
```
SECRET_KEY=<Contact_Repository_Owner>
DEBUG=<desired_debug_bool>
```
5. In CLI run: `docker compose up`
6. If web container fails on first compose, please wait for db container to initialize
7. Run: `docker compose down` && `docker compose up`
8. Attach shell to web container or run: `docker exec -it <web_container_id> bash`
9. In web container CLI run: `python manage.py showmigrations` && `python manage.py migrate`
10. In web container CLI run: `python manage.py createsuperuser` && fill out information
11. Close web container CLI
12. Navigate to localhost:8000/admin && log into admin console
13. Create 1 Currency named "coin" with the default quantity
14. Create 3 Items with default values
15. Click `View Site` on top right navbar
16. Enjoy!
