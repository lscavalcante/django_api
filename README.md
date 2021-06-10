## Project Description
1. System with login authentication in social media (google, facebook)

2. Confirm credencial login by email

3. Reset password by email

4. Token authentication

5. Blacklist token

6. Tests endpoints

## Installation steps
1. Ensure you have python3 installed

2. Clone the repository
3. create a virtual environment using `virtualenv venv`
4. Activate the virtual environment by running `source venv/bin/activate`

- On Windows use `source venv\Scripts\activate`

5. Install the dependencies using `pip install -r requirements.txt`

6. Migrate existing db tables by running `python manage.py migrate`

7. Run the django development server using `python manage.py runserver`

# **Git**
**Create pull request:** 

`git add .`

`git commit -m "string"`

`git push origin **branch**`

`correct request`

**Correct file:**

`git add . `

`git commit --amend --no-edit`

`git push origin **branch**`

# **Commands**
Debug:
`import pdb  pdb.set_trace()`