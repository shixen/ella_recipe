# Recipe

This is a recipe website i built for my partner who loves to bake pastery and cook food.
its a simple and clean site to brows for recipes to try out , read information about "Ella" herself or 
to mabye place and order of some pastery.

![Skärmbild 2024-06-08 114109](https://github.com/shixen/ella_recipe/assets/150827343/9a2a5a4a-63a3-4bae-8ed9-181367b6a6d0)
[link to live page](https://ella-recipe-cb81f80dd053.herokuapp.com/)

### key information
* information and description of how to cook and bake
* inspiration of food
* learning experience on food and baking
* ordering food or pastery

### User stories
* Site visitor should be able to determine the purpose of the site immediately
* Site user should find the content of the page easy to understand
* Site user should be able to navigate the site easy
* Site user should be comfortable contacting the business for more information or ordering

### Visitor goals
* To be able to visit the site on any device size
* To find recipes to cook or bake
* Take contact for ordering

### Returning visitor goals
* To find more recipes to bake or cook
* To take contact for more ordering of food or pastery
* To get answers to any questions


### Design

I went with a simple brighter and a smooth color scheme to keep it clean and simple.

![Skärmbild 2024-06-08 115516](https://github.com/shixen/ella_recipe/assets/150827343/b110d6ef-fa51-4366-8342-4c5e2157e2d7)

language of the page is supposed to be in swedish but keeping it in english for now but will change later.

## Wireframes

* homepage 

![Skärmbild 2024-06-08 180423](https://github.com/shixen/ella_recipe/assets/150827343/8677cc09-2438-4d51-97ad-c4ce8ca6fec8)

* About page

![Skärmbild 2024-06-08 180709](https://github.com/shixen/ella_recipe/assets/150827343/84d4e083-5d29-40a0-b540-fbca79e4f385)

* Contact page

![Skärmbild 2024-06-08 181207](https://github.com/shixen/ella_recipe/assets/150827343/af5e8891-b96b-4672-8bff-1f44b20810aa)

* Register account page

![Skärmbild 2024-06-08 182116](https://github.com/shixen/ella_recipe/assets/150827343/0d5261c1-11b2-472d-947a-8731b16f797d)

* Login page

![Skärmbild 2024-06-08 182413](https://github.com/shixen/ella_recipe/assets/150827343/1b56d1a8-8013-48fa-9c12-c491f113bd38)



## Features
* List of displayed recipes

![Skärmbild 2024-06-08 120004](https://github.com/shixen/ella_recipe/assets/150827343/a168663b-5ad1-49e4-b146-5656f7749784)

* Link to social media

![Skärmbild 2024-06-08 120008](https://github.com/shixen/ella_recipe/assets/150827343/86ab0af4-6ffd-4957-aaf0-750eee057b6f)

* Navigation bar to navigate around the page
  
![Skärmbild 2024-06-08 120016](https://github.com/shixen/ella_recipe/assets/150827343/278b9500-9e6d-41e9-8526-7ba2a8ce5a39)

* Sign-up page to create an account on the page
  
![Skärmbild 2024-06-08 120023](https://github.com/shixen/ella_recipe/assets/150827343/04d7e3a5-2657-410c-a4c3-0306d35e30aa)

* Page to sign in when user have an account
  
![Skärmbild 2024-06-08 120027](https://github.com/shixen/ella_recipe/assets/150827343/20fdc3aa-323d-4de8-af57-e92cb468a922)

* Information page about the site owner
  
![Skärmbild 2024-06-08 120034](https://github.com/shixen/ella_recipe/assets/150827343/a9c4e2a9-9d70-4372-813f-bdae276bfb42)

* Contact page to contact site owner for questions or ordering

![Skärmbild 2024-06-08 120040](https://github.com/shixen/ella_recipe/assets/150827343/8c419485-21e9-46a4-a6bc-ddd7b9101e77)

# Future features

* search bar to search for categories on recipes

# Technologies used 

### Programming Languages and frameworks
HTML, CSS, PYTHON, javaScript, DJANGO

### Programs used

Github to store files 

Google Devtools to control and test code functionality

Gitpod used to code the site

Heroku used to host the page

Cloudinary to store images 

# Deployment

This site was deployed using heroku

To deploy on heroku.

* 1 go to https://www.heroku.com
* 2 Create and account or login.
* 3 Go to dashboard and click New and Create new app
* 4 Go to settings in your new app and connect your heroku app to your github repository
* 5 Go to Deploy page in your app
* 6 Scroll down to Deploy a GitHub branch
* 7 On Choose a branch to deploy select main
* 8 Click on Deploy Branch


# Database design

![Skärmbild 2024-06-08 191433](https://github.com/shixen/ella_recipe/assets/150827343/fd659645-fd4b-4fd3-87b8-18829b73d038)



# Testing 

[CSS validator](https://validator.w3.org/)

[Python validation](https://pep8ci.herokuapp.com/#)

[JavaScript validator](https://www.site24x7.com/sv/tools/javascript-validator.html)

* Lighthouse google devtools

![Skärmbild 2024-06-08 142117](https://github.com/shixen/ella_recipe/assets/150827343/6b55b9d7-d836-445a-9b62-e097bf312333)

Manual testing is done by the people themself that actually build the project that needs testing and people are more adaptable to changes that may come during testing.
And manual testing does not require any specific programs or tools to execute , i just requiers the page or program that needs to be tested.

Automated testing is done by testscripts or testframeworks such as Jest or pytest and gets done automaticly by the program itself.
And automated testing is better for saving time , lesser risk for human errors. automated testing automates the process and makes it faster and more consistent

* Link to manual tesing [TESTING.md](https://github.com/shixen/ella_recipe/blob/main/TESTING.md)

# Security

* keeping the website secure by changing the secret key from the initial commit and keeping everying in a file thats not getting commited to visable eyes

* Django has built-in support for CSRF protection. This prevents attacks where an unauthorized user can send a request from another website to perform unwanted actions on a logged-in user's account.

* Django protects the application against SQL Injection attacks by using parameterized queries and sanitizing user data used in SQL queries.



# Credits and Acknowledgements

[Stackoverflow](https://stackoverflow.co/teams/features/?upgrade=true&utm_source=adwords&utm_medium=ppc&utm_campaign=kb_teams_search_nb_dsa_targeted_audiences_emea-dach&_bt=646019453180&_bk=&_bm=&_bn=g&gad_source=1&gclid=CjwKCAjwgpCzBhBhEiwAOSQWQS-IB-nTczz7ooMoToXuLeYv6wqeenTgHnfqwc_EDTWMPtOE92VPcRoCrXsQAvD_BwE)

[Google](https://www.google.com/)

code institute for support and information [code institute](https://codeinstitute.net/se/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI+-+SWE+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14660337051&hsa_grp=134087657984&hsa_ad=635849372549&hsa_src=g&hsa_tgt=aud-594467886660:kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=CjwKCAjwgpCzBhBhEiwAOSQWQclKyriDZuUK3ZXMSusGgtQ4284TD7Hno9jb8x9WrQxwZREj9xUpURoCk5wQAvD_BwE)

my code institute menter Rory Patrick Sheridan for great mentoring and support during the build of this project


