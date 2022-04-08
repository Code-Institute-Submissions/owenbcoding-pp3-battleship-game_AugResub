![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome eoghankb,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
# ------BATTLESHIP-GAME-------
  - Pre-reqs: Loops, Strings, Arrays, 2D Arrays, Global Variables, Methods
  - You will have 10 bullets to take down the 2 ships that are placed down
  - You can choose one column such as A3 to indicate where to shoot,
  - A ship cannot be placed diagonally, so if a shot hits the rest of the ship is one of 4 directions, left, right, up, and down

# User Stories
 - The user will be given 2 ships
 - The user will have 10 bullets to try to hit the ships
 - The user will be able to input where on the grid to hit the target
 - The user can only hit the ship if its in a column 