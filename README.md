# Welcome to Run for It.

This web application is the source code for the Run for It a web app to track runs and thoughts of runs. It is powered by Python and Django.

This is what we inherited on starting the project.

1. User registration
1. User login
1. User logout

# Setting up
1. Clone down repo into a directory
1. Create a virtual environent as sibling of this repo
   - `virtualenv <name_of_virtualenv>`
1. Activate virtual environment
   - `source <name_of_virtualenv>/bin/activate`
1. CD into repo
1. Run `pip install -r requirements.txt`

## File naming conventions/File Structure

All directories and files should be named lower case with snake case for multi word names.

Similar files such as models/views will go in their respective directories. Name those files with the following template

For models - `<resource name>_model.py`
For views - `<resource name>_<view type>_view.py`

examples
```
employee_model.py
employee_edit_view.py
```
## Resources

The following resources are available through the application

### Navbar
A navbar that links to the resources below. More links can be added by adding buttons that follow the same formula and path of the newly linked item.

### Runner
1. Runner table holds infromation about a runner
    - user name(string) the user name of the runner
    - e-mail(string) the e-mail of the runner
    - date joined(string) the date the user joined
    - goal(string) the users goal


### Schedule
1. schedule(string) type of string
1. goal(integer) distance to run

### Day
1. id
1. distance (integer)



## Faker Data Setup
To populate DB, run: `django_data.sh employee_portal faker_factory` from terminal in the directory that contains django_data.sh

Use your models to create fake data in the employee_portal/manage/commands/faker_factory.py
you can view the documentation for seeder arguments here
https://github.com/Brobin/django-seed


## URLS and views

urls will follow the following conventions

rootdirectory/<resource name>/ for list view
rootdirectory/<resource name>/<pk:id> for detail views
rootdirectory/<resource name>/add for adding form
rootdirectory/<resource name>/<pk:id>/edit for editing a resource

## tests
make sure to create tests for each new resource and view to make sure they are sending the correct data/html/status code etc...

tests will live under the tests directory and are run from the root directory using
`python manage.py test`