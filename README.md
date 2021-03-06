# Mark McClean

## Milestone Project 4 – Full Stack Frameworks

## Route Share – Django application

### Table of Contents
* [Why make Route Share?](#Why-make-Route-Share)
* [How the website works](#How-the-website-works)
* [UX: Strategy](#UX-Strategy)
* [Scope](#Scope)
* [Structure](#Structure)
* [Defensive Design](#Defensive-design-features)
* [Surface](#Surface)
* [Skeleton](#Skeleton)
* [Database Design](#Database-design)
* [Technologies Used](#Technologies-Used)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Credits](#Credits)

### View the live project
The live website hosted by Heroku can be viewed [here](https://bicycle-route-share.herokuapp.com/).

### Note to Assessors:
If you wish to test out the checkout form and payment please use the following test card details:
* Card No: 4242 4242 4242 4242
* Expiry Date: Any future Date
* CVC & ZIP: Any numbers
If you wish to view the database you login [here](https://bicycle-route-share.herokuapp.com/admin/login/?next=/admin/) and the following read-only credentials can be used to view the data:
* Username: GuestAdmin
* Password: routeshare2020

### Why make Route Share?

For the fourth milestone project I decided to build an application where users can find new bicycle routes as well as adding and sharing their own favourite routes, therefore building up a community of users that expand the database of routes. 

Due to a recent foot injury which restricts my ability to exercise on foot, I bought a road bike and for the past few months have been enjoying a new lease of life with a new form of exercise that has no effect on my foot injury. 

During this time I have found myself trying to come up with all different routes in and around the area where I live using Google Maps. That’s when I thought it would be a good idea to create an application where cyclists can share and view each other’s favourite routes. 

### How the website works

Users will initially arrive at the home page which will consist of an extensive menu at the top with options to search for, view and filter routes along with login/sign up options and a link to view the users profile. 

Below the menu will be a callout section consisting of 2 large buttons to get the users attention. A ‘View Routes’ button and a ‘Sign in/Sign Up’ button. 

There will be limited functionality for users who are not yet signed up. They will be able to look through the routes, using the search, sort and filter options but will be unable to see full details of the routes or the route itself unless they have signed up and paid for some form of membership. 

There will be 3 layers of membership: 

- A free trial membership allowing members to view one full route detail and map before being restricted again. The user will also have unlimited uploading of routes 

- A limited membership that costs €4.99/month and allows the user to view 5 routes/month. The user will also have unlimited uploading of routes 

- An unlimited membership for €9.99/month that allows full unlimited access to all routes on the site. The user will also have unlimited uploading of routes 

The routes will be displayed in a grid with enough information to enable the user to choose a route that is useful for them. For example they can view the country and area of the route, the length and bicycle type, and a description of the route. Users will also have the ability to upload a photo with their route to enhance the appeal to other users although this will not be required. 

When a user wants to get a route, they first need to click on that route in the grid which links to a new page with further details of the route and in that page there will be a ‘Reveal Route’ button that will enable the user to see the Google Map link where they can open the route. This will be dependent on the current conditions of the users membership. 

For uploading routes there will be some instructions on the site about how users can do that but basically they will have to first create their route in Google maps and copy the URL from Google maps into the upload route form so it can be stored in the database. 

### Technical Details

The application was built using Django 3 and follows a good practise architecture pattern of model-template-view. The application also uses ‘Separation of Concern’ for the apps created within the project to utilise the Django framework effectively. 

Within the development environment sqlite is the default database used along with Django. For the deployment of the site Heroku was used and I switched to a Postgres database which is easily set up through the Heroku dashboard. All data from the sqlite database is then transferred to the Postgres database so the deployed version enjoys all the benefits of the development version. 

There is also an Admin side to this application where the site owner will be able to have CRUD (Create, Read, Update and Delete) functionality through a built in Django admin interface. For the site owner a superuser account is created during the development process so only they can access this interface. This user interface is also customisable to the owner’s needs and allows the owner to adjust records outside of the main user interface ie. the website itself. 

Git and Github are used for version control and Heroku for the full deployment of the site. All project secret keys are stored in the Gitpod Environmental Variables in the settings menu. For deployment these are then stored in the Config. Variables of the Heroku dashboard. This is to keep them hidden to protect the integrity and security of the application.

[↥ Back to top](#Mark-McClean)


## UX: Strategy

### Primary Target Audience

The target audience is for cyclists of all kinds. Regardless of what type of bike you have, there will be routes to enjoy for everyone from leisure bikes, road bikes and mountain bikes. This will be particularly useful for people new to the cycling world, who otherwise have little knowledge of available cycle routes where they live. 

### Appropriate Content

I think it would be appropriate to have many beautiful images of cyclists on the website to give off a feel of excitement and adventure to the potential users. I plan to have a home page with several images below each other separated by some small paragraphs about the website’s content. Some of the other pages will also have striking images to help maintain the theme and feel of the website overall. The users who upload routes also have the opportunity to attach a photo to the route which also adds to the visual aspect of the site and the display of the routes. There will also be a dark theme to the navbar, footer and several buttons along with an orange aspect for the primary buttons. 

Appropriate content also includes giving the users clear instructions on how to use and manage all aspects of the site and ensuring a seamless use of all functions like instructions on how to create the route and paste into the route upload form.

### Why this website?

As I briefly mentioned earlier I have recently taken up cycling with a road bike and am very much enjoying it but I’m always looking for new routes. I thought that a website where people can share and views other people favourite routes would be a good idea.

I have also recently read that, especially since the Covid-19 crisis, cycling has become very popular in many countries. It is a great form of exercise which can be done alone or in small (socially distanced) groups. With this growing popularity people will always be looking for more resources to find routes and this could be a very useful application for many cyclists.

[↥ Back to top](#Mark-McClean)


## Scope

### User Stories

|     Story #    |     User Type            |     Activity                        |     Goal                                                 |     Reason                                                                              |
|----------------|--------------------------|-------------------------------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------|
|     1          |     Member/non-member    |     Viewing & Navigation            |     View a list of routes                                |     To find a suitable cycle route                                                      |
|     2          |     Member/non-member    |     Viewing & Navigation            |     View route details                                   |     To get more information on the route                                                |
|     3          |     Non-member           |     Viewing & Navigation            |     View membership options                              |     To choose the correct membership for myself                                         |
|     4          |     Non-member           |     Viewing & Navigation            |     To see I’ve selected a membership to purchase        |     Incase I forget to follow the purchase procedure                                    |
|     5          |     Member               |     Viewing & Navigation            |     Instructions on how to upload my favourite route     |     To share my favourite route with fellow users                                       |
|                |                          |                                     |                                                          |                                                                                         |
|     6          |     Member/Non-member    |     Sorting & Searching             |     Sort the list of routes                              |     To find the best rated or closest routes to the user                                |
|     7          |     Member/Non-member    |     Sorting & Searching             |     Sort a specific category of route                    |     To find the best rated or closest routes in a specific bike type or route length    |
|     8          |     Member/Non-member    |     Sorting & Searching             |     Search for a route by name or description            |     Find a specific route with a keyword search of the name or description              |
|     9          |     Member/Non-member    |     Sorting & Searching             |     See what I’ve searched for and number of results     |     Quickly find if there’s a route with the keywords I’m looking for.                  |
|                |                          |                                     |                                                          |                                                                                         |
|     10         |     Non-Member           |     Registration/User Accounts      |     Register for an account                              |     To have an account to access full details of all routes                             |
|     11         |     Member               |     Registration/User Accounts      |     Log in and out                                       |     To access my personal information and full route details                            |
|     12         |     Member               |     Registration/User Accounts      |     Recover my lost password                             |     To regain access to my account if I forget password                                 |
|     13         |     Member               |     Registration/User Accounts      |     Receive email notification on registration           |     To confirm that my registration was successful                                      |
|     14         |     Member               |     Registration/User Accounts      |     Have a personalised user profile                     |     To view or update personal details and view membership restrictions                 |
|                |                          |                                     |                                                          |                                                                                         |
|     15         |     Member               |     Purchasing and checkout         |     View membership type in my basket to be purchased    |     To identify the membership type and cost                                            |
|     16         |     Member               |     Purchasing and checkout         |     Enter my payment details                             |     To easily purchase membership type required                                         |
|     17         |     Member               |     Purchasing and checkout         |     View an order confirmation after payment             |     To ensure I have received the product that I have ordered                           |
|     18         |     Member               |     Purchasing and checkout         |     Receive an email confirmation after checkout         |     To have a separate confirmation of what I’ve purchased                              |
|                |                          |                                     |                                                          |                                                                                         |
|     19         |     Member               |     Admin & Route Management        |     Add a route                                          |     Add a route for other members to view                                               |
|     20         |     Member               |     Admin & Route Management        |     Edit or update a route                               |     To change the route details of route I uploaded                                     |
|     21         |     Member               |     Admin & Route Management        |     Delete a route                                       |     To delete a route that is no longer correct                                         |
|     22         |     Member               |     Admin & Route Management        |     Rate and review a route                              |     To have a rating and review of a route posted on the website                        |
|     23         |     Member               |     Admin & Route Management        |     Create a forum post                                  |     Create a post on the site about a subject I’d like to discuss                       |
|     24         |     Member               |     Admin & Route Management        |     Reply to a forum post                                |     Reply to post by another user                                                       |
|     25         |     Member               |     Admin & Route Management        |     Save Routes to my profile                            |     To save a route based on your membership conditions                                 |
|     26         |     Member               |     Admin & Route Management        |     View saved routes                                    |     To view your saved routes separately for quick access                               |

[↥ Back to top](#Mark-McClean)

## Structure

### Features
1. Site Name and logo in the top left corner. This then disappears on medium and small screens but the callout remains with a welcome message so users still know where they have arrived.
2. A collapsible navbar element has been implemented for medium and smaller screens. The menu is hidden inside the 'burger' icon and the navbar sweeps down when clicked. When the collapsed menu is open on smaller screens the ‘burger’ icon toggles to an ‘X’ to signify to the user that this button will close the menu, then it toggles back to the ‘burger’ icon.
3. A search bar is visible on larger screens and hidden on smaller screens with a button to toggle the search bar’s visibility on smaller screens. This search bar can be used to search for key words from the routes titles, descriptions, bike types, route types and countries so there are many ways for the users to find the routes they want.
4. A profile icon appears in the top right of the navbar. This provides a dropdown menu giving the users links to sign in, register and access their own profile page if already logged in.
5. A shopping basket icon also appears in the top right corner of the navbar beside the profile icon. When a user adds a membership type to their basket, the icon will change colour to alert the user and display a number ‘1’ underneath, to indicate to the user that there is 1 item in their shopping basket.
6. The bottom section of the navbar is a sorting and filtering menu. Each link is a dropdown menu with filtering and sorting choices the user can make depending on their needs. The routes dropdown will continue to display all routes available but sort them according to your choice, for example length. The routes will then be displayed with the longest first to the shortest route last. The other menu choices are all filtering options so the user will only see routes that correspond with the choice they made, for example if they choose ‘Bike Type’ and ‘Race Bike’ from the dropdown they will only see routes that have a bike type of ‘Race Bike’.
7. Within all the route displays under the navbar is a separate sorting selector. This dropdown selector will give the user further sorting options even within a filter. If a user has selected for example a filter of countries and ‘United Kingdom’, they can sort these routes by length, from longest to shortest and also in reverse order or by bike type A-Z or Z-A.
8. Each route displayed is a link that will take the user to a details page about that particular route. This page will have a few extra details about the route and a button to get the route. This will then reveal the Google Maps URL for this route that the user uploaded when they created this route. The revelation of the Google Maps URL will be dependent on the current state of the users membership. If they have reached their current monthly routes limit, there will be an error message to let the user know they have reached their limit for this month.
9. On the main navigation is a ‘Membership’ option to take the users to the membership choices that they can purchase. The user will be required to have an account and be logged in before they can add a membership option to the basket. If they try to add a membership to the basket without being logged in, an error message will appear to alert them and they will be redirected to the log in page.
10. After a user adds a membership type to the basket, a message will appear to alert them to this and specify what has been added and a link to view the basket. Unlike all other messages on the site which appear for 5 seconds, this one has the alternative functionality of an exit button that the user will have to use to close the message. This is because this particular message has a lot more information than most so it gives the user more time to think about what they want to do.
11. When a user wants to purchase the chosen membership they can navigate to the checkout page through the basket page. This will then display a further order summary and a form to fill out basic user details and payment card details. Within in the payment card element is a hidden card error section where potential card errors will alert the user in real time to prevent them submitting the wrong card details.
12. When the user submits the checkout form, animated loading screen will appear for a few seconds while the payment is being processed. If there is a problem with the form for example they will be redirected back to the checkout page and a message will alert them to the problem. If the checkout was successful they will be directed to a success page where a further summary of their order will be available for them to see.
13. On successful checkout a user profile will be created for the user to view their current details and membership information including how many routes they have currently saved. This will automatically update when a user saves a route so the user can keep up to date with the current status of the membership.
14. In the route details page of any route there will be a button to get the route map and directions. There will first be a check if the user has a profile and which membership type they have and a further check to see how many routes they currently have saved and if all the conditions are met the map will be revealed and the route added to the users saved routes. If the conditions are not met the user will receive a message informing them of the reason.
15. The user's saved routes can all be viewed on a seperate page which is accessable from the user profile or the profile icon dropdown menu.
16. There is a forum page on the site which gives users the chance to create a post about something cycling related. Other users can browse through the posts and toggle the full post text to reveal it or hide it again. If the user clicks on the 'View Comments' link they will be brought to a new page for that post where they can comment on the post. All posts are editable and deletable only by the user who created them.
17. A 'Contact Us' section is also available if users, registered or not, wish to contact the Route Share owner to make a query. There is an option for the user to get a copy of the mail that is created, sent to them so they can receive the same mail that the Route Share team will receive. This mail will also contain all the details they filled in on the form.

[↥ Back to top](#Mark-McClean)

### Features left to implement
1. Pagination for the routes and forum pages. Over time more and more routes and forum posts/comments will be added to the site and it may get quuite unruly scrolling all the way down to the bottom of a very a very long page to view them. It would be better to set limit per page and then take a new page when the amount of routes/posts exceeds that amount.
2. The ability to edit/delete a forum comment. There is currently functionality to edit/delete a forum post but not yet for forum comments. This functionality would be useful in the future.
3. On the main forum page an indication of how many comments there currenly are per post. This would be useful instead of clicking the 'View Comments' link each time to see if there are comments.
4. Rating the routes. A function to give users the ability to rate each route out of 5 and count up and average all ratings to dynamically update and display the rating for each route.

### Overall Structure
On the homepage I wanted to use several large full screen cycling images in conjunction with small snippets of information about the site. The overall design I tried to implement was fixed positioned images, seperated by a cycling graphic which scrolls up over the image to hide the image above and reveal the image below. The information snippets also scroll up over the fixed images. I think this gives a nice vsual effect to welcome the user to the site.

The navigation panel along the top of the site is split into 2 sections. Theres the head section which is always visible on all screens but changes slightly depending on device size. It incorporates a site name/logo, a search bar, a profile icon and a basket icon. On smaller screens the site logo toggles to become the menu button for the main page navigation below. Inside this dropdown menu in a seperate link to the homepage. The search bar also toggles to a button on smaller screens which reveals the search bar below to save some space on smaller devices.

For the lower part of the navigation panel I went with centrally alligned links to the routes, membership and forum pages. Several of these links have their own dropdown menus to choose filtering options when browsing for routes. On smaller devices this navigation panel disappears and transfers to inside the menu button, which will reveal the list of links when clicked.

The footer section is a fairly standard but modern responsive information panel with links on the left to other parts of the site and on the right for social links, which all open in a new tab so the user is not permanently directed away from the site. The 3 footer sections trnasform into a centrally aligned single column on smaller screens.

For the overall styles within the site I wanted to use coloured background sections with white text. These coloured background sections were all styled with rounded edges and often with an orange horizontal dividers to seperate information. I think this gave an attractive, soft and fun feel to the overall appearance ot the site. All existing allauth templates were also updated to reflect the sites main styles to provide consistency throughout the website.

[↥ Back to top](#Mark-McClean)

## Defensive design features
A number a defensive design practises and tools were used throughout the site to prevent certain actions or errors occuring. They are outlined below.
1. Before a user can add a membership plan to the basket, they need to have an account and be logged in to add the membership. If they are not, they will be redirected to the login page with an error message alerting them to the problem.
2. Before a user can add a route to the database, they will also require an account and be logged in. Of course this is not a full prevention but more of a deterrant for any one not serious about adding quanity routes to the database. The link to add a route is not available unless the user is logged in and attempting to access the URL manually will redirect the user to the login page.
3. Attempting to access the checkout manually by typing in the URL will result in a redirect to the membership page and an error message that there is nothing in your basket at the moment.
4. Viewing posts and post comments in the forum section is open to view for all users. However only logged in users will be able to post or comment. Redirects to the login page and messages have been added to aid the user.
5. Only users who have added a particular route or forum post can edit or delete that route or forum post. The links are only available for them to see and any users tryin to type in the urls manually will be redirected and receive a warning message that they don't have authorisation to edit or delete that particular route or post.
6. Custom 404 and 500 pages have been created for the site where users will land if they type in a url that doesn't exist or experience an error. They will see the custom 404 page if they navigate to a page that doesn't exist and if there is an error in the site they will arrive at the custom 500 page. Both pages are displayed within the base template so all navbar and footer links will still be available to the users to find their way back to the flow of the site and additional links are provided within the main page display.
7. Modals are used for route and post deletion to give the user a confirmation option in the event that they accidently clicked delete route/post. This action can then be cancelled and the user will return to the route/post.

[↥ Back to top](#Mark-McClean)

## Surface

### Colours and icons
* **Background Colours** - From the beginning I wanted to go with a darker theme throughout the site with regards to the navbar, footer and all the elements that render on the main body of each page with a white background to separate all the elements. Initially I just went the colour of black for all these elements along with an orange trim in the form of a horizontal divider to break up the black elements. This horizontal divider was also used to separate the header section of an element from the main body of the element. For example on the routes page, it separates the name or title of the route form the other details of the route.
* **Colour Adjustments** - I continued to build my site using this combination of black, white and orange which I thought was a good combination, especially when rendered with some of the images I have throughout the site. However when it came to building the forum section of the site, because there were no images and potentially a lot of just black, white and orange, the black started to look a little harsh on the eye so at that point I decided to soften it up a little and played around with a number of dark greys before finally settling on rgb(80,82,81). I think this still works great with the white and orange. As I had a background class of black set up in the CSS I was easily and quickly able to change the colour of all elements on the site to this new dark grey.
* **Text Colours** - For the text on the site I went with white as most of the text was on top of the grey elements so this was the natural choice. There are a few exceptions throughout the site, for example on the navbar, the site name, profile and basket icons are all in the same orange trim colour. The basket icon changes to white, when a user adds a membership to the basket.
* **Button Colours** - For the primary buttons on the site to proceed and go forward with various functions I used the same orange as the orange trim from the elements with white text and a lighter orange colour when hovered over. For the secondary buttons, ie to go back to different pages or cancel various functionality I used an inversion of the primary button with a thin orange outline, a white background and orange text. This again inverted to appear as a primary button when hovered over.
* **Text Links** - Throughout the site there are also some text links, for example on the footer and in the forum pages, which are either in white with an orange hover or orange with a white hover. I did this to try to keep a consistent colour theme throughout the site.
* **Icons** - I also used many Font Awesome icons on the site. I think they really improve the appearance of the site and are also excellent visual indicators for the users to quickly understand what they are looking at.

[↥ Back to top](#Mark-McClean)

## Skeleton

### Wireframes
I used the Balsamiq program for the wireframes and attached them to the directory. The original idea is still recognizable from the finished application. There have obviously been some design changes along the way but the wireframe is useful to have to put the idea in your head down on paper before you start coding. The wireframes can also be viewed her below.<br/>
<details>
    <summary>
        Home Page - Desktop
    </summary>
    <img alt="Homepage-Desktop" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/f7cfa39737d6d1df96308ac81758efe50cc54ce9/static/wireframes/Homepage-Desktop.png">
</details>

<details>
    <summary>
        Home Page - Mobile
    </summary>
    <img alt="Homepage-Mobile" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Homepage-Mobile.png">
</details>

<details>
    <summary>
        Routes - Desktop
    </summary>
    <img alt="Routes-Desktop" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Routes-Desktop.png">
</details>

<details>
    <summary>
        Routes - Mobile
    </summary>
    <img alt="Routes-Mobile" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Routes-Mobile.png">
</details>

<details>
    <summary>
        Route Details - Desktop
    </summary>
    <img alt="RouteDetails-Desktop" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/RouteDetails-Desktop.png">
</details>

<details>
    <summary>
        Route Details - Mobile
    </summary>
    <img alt="RouteDetails-Mobile" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/RouteDetails-Mobile.png">
</details>

<details>
    <summary>
        Membership - Desktop
    </summary>
    <img alt="Membership-Desktop" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Membership-Desktop.png">
</details>

<details>
    <summary>
        Membership - Mobile
    </summary>
    <img alt="Memebership-Mobile" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Membership-Mobile.png">
</details>

<details>
    <summary>
        Checkout - Desktop
    </summary>
    <img alt="Checkout-Desktop" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Checkout-Desktop.png">
</details>

<details>
    <summary>
        Checkout - Mobile
    </summary>
    <img alt="Checkout-Mobile" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Checkout-Mobile.png">
</details>

<details>
    <summary>
        Profile - Desktop
    </summary>
    <img alt="Profile-Desktop" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Profile-Desktop.png">
</details>

<details>
    <summary>
        Profile - Mobile
    </summary>
    <img alt="Profile-Mobile" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Profile-Mobile.png">
</details>

<details>
    <summary>
        Upload Route - Desktop
    </summary>
    <img alt="UploadRoute-Desktop" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/UploadRoute-Desktop.png">
</details>

<details>
    <summary>
        Upload Route - Mobile
    </summary>
    <img alt="UploadRoute-Mobile" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/UploadRoute-Mobile.png">
</details>

[↥ Back to top](#Mark-McClean)

## Database design

### Database Schema
Despite a lot of advice to thoroughly plan my database schema I still found it difficult to fully realise my database setup until I was already developing the project and many instances the models I had created were adapted and changed to reflect my evolving vision of how I wanted my site to function.

This is something I can put down to inexperience but the knowledge I have gained from this process has been invaluable in developing my own skills in planning the project before hand.

In the development environment I used the built-in mySQLite3 as the database frovided for by Django. As I was changing models frequently I held back on deploying the project to Heroku to save on double migrations. This is also something I can avoid by better planning of the database schema from the beginning.

For the deployed version of the project, the database used is Prosgres provided for by Heroku and set up during the deployment of the project. Some pre-writen data created by myself at the start of the project did have to be transferred over to the new database but that was done with the loaddata function in the command line during deployment.

See below the database relationships
* One User/User Profile can have one:
    1. Order at a time
    2. Membership at a time
* One user can have many:
    1. Forum posts
    2. Forum comments
* Many Users can have many:
    1. Saved Routes
* One Order can have one:
    1. Memerbship
* One Route can have one:
    1. Bike type
    2. Route Type

<details>
    <summary>
        Database - Schema
    </summary>
    <img alt="Database Schema" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/media/Database.PNG">
</details>

The membership type is the most important piece of information in the database schema as it needs to be saved on to the User Profile to set the conditions under which the user can save routes or not.

Not surprisingly this was challenging as the membership type has to pass from the membership model to the basket when added by the user. It then needs to transfer from the basket to the order during checkout. Finally when the order is fully processed, the membership type has to be transferred to the User Profile.

This was not fully successful in the beginning and several alterations had to be made to the model and views in which the membership type was been passed through on each step.

The membership type is not fully passed through to the User Profile and can also be updated if the user decides to change their membership by buying a different membership after the initial purchase.

I decided against an order line item model as each order can only have 1 membership type and I thought it would be simpler and more efficient to pass through all the order details directly in the main order model.

To give the users the ability to save routes depending on their membership conditions, I went for a ManyToMany relationship between the user and the route. I was advised against going for a ManyToMany relationship but found it difficult to find an alternative method to achieve the desired functionality.

[↥ Back to top](#Mark-McClean)

## Technologies Used
* [Gitpod]( https://www.gitpod.io/) – Used as my IDE for the development of the website. 
* HTML – Used to write the code for the structure and layout of all templates in the site.
* CSS – Used for custom styling of many HTML elements and some animations.
* Python – The core backend language used to create the logic for the views.
* [Django](https://www.djangoproject.com/) – This is a Python based framework which uses a model-template-view approach as the architectural engine. 
* Jinja - This templating language was used to project some of the Python functionality and template variables onto the frontend to create a dynamic site which automatically updates when user data is submitted.
* Javascript – Used to provide some interactive features of the website and to handle the checkout form submission
* jQuery – Used for several post-load JS scripts on the templates, the delete route modal and also to initialize some Bootstrap components.
* Popper.JS – Used to aid the responsiveness of the website.
* [Bootstrap]( https://getbootstrap.com/) – Bootstrap was used to provide the navbar, footer and the use of a grid system. Many bootstrap classes were also used throughout the site to add pre-existing colours, padding and margins to elements. 
* [Font Awesome]( https://fontawesome.com/) - for all site icons
* [Google Font](https://fonts.google.com/) - 1 Font was imported from Google Fonts and the URL can be found in the core css block of the base template.
* sqlite3 – Was used as the backend development database and provided for by the Django framework
* Postgtres – Was used as the deployed database, provided for through Heroku
* [Heroku]( https://www.heroku.com/) – Used to deploy the website and hosted on Heroku’s cloud platform
* Git – Used for version control on the CLI (Command Line Interface) within Gitpod.
* [Github](https://github.com/Sparkplug84/route_share_MS4) – Used to store the repository of all committed versions of the code. Also linked to Heroku to enable automatic deployment simultaneously. 
* Balsamiq - This was used to build the wireframes that were then uploaded to the Gitpod IDE.
* [Tables Generator](https://www.tablesgenerator.com/) - Used to create the tables inserted here in the README file.
* [Codacy](https://www.codacy.com/) – Used to validate all code on the entire site instead of copying and pasting many files one at a time into the various HTML, CSS, JS and Python code validators.
* Google Chrome Developer Tools – Used frequently to check and examine all elements and styles throughout the development. Even adjusting live in the browser before updating the corresponding code in Gitpod.
* [Google Maps](https://www.google.com/maps/) – Used to generate the html <iframe> element of the users route so it can pasted it in to the add route form.

[↥ Back to top](#Mark-McClean)

## Testing

### General Testing
All testing was carried out manually by checking the browser frequently throughout development. How I achieved this was after almost every line of code that I wrote, I refreshed up the browser to check the updated code. Viewing it in Google Chrome I am then able to right click on the website and select inspect from the menu. Chrome Developer tools opens up which allows me to view the elements, styles and console log to see JavaScript errors.

On the previous project I had used Materialize as the CSS framework but decided to go back to Bootstrap as I felt more comfortable using it instead. Throughout the project I was often cheking the Bootstrap documentation to use as many utility classes as possible to style my site. This was to cut down on the amount of custom CSS being used as I think in previous projects I was writing too much CSS.

I tried to work with small tasks in the beginning, setting up the navbar, creating some links. During this process I would view the website in the browser many times, select elements to see what default styles had been attached to them and change if necessary. Chrome Developer tools also allows you to add styles to elements and change the website as you view it. I would then add Bootstrap utility classes in the developer tools to see the instant result. This would then be copied into the project if it was the desired outcome. Within the Chrome developer tools there is also the console, which I monitored to find bugs in the JavaScript functions.

After spending some time on the HTML, Bootstrap and CSS to set up the look, styles and responsiveness of the website, I moved on to writing the Python code. I used the same manual tests as above using Chrome Developer tools. I would often print statements in the python code and check in the command line to see if the statements were printed. This helps to see if the program reaches parts of your function and if there are any bugs, at which point it is going wrong.

When the basic functionality of the site was in place, I shared by the website with friends and family to get their feeback of usablity and first impressions of the game and functionality.

Through continual monitoring and with the feedback of friends and family, I have fixed a few design faults throughout the project duration.

### Testing in different browsers
I used Google Chrome as my main browser test as I was constantly using the Chrome developer tools to view and adjust my code. I also regularly tested the website on my phone, also using Google Chrome. I occasionally checked Firefox on the laptop. I sent the URL to friends and family to test on ipads(5th generation or younger) and iphones(8 or younger) along with Samsung Galaxy(S9 or younger) and Saumsung Galaxy Tab(S3 or younger). Any issues I found have been documented below in the section: [Issues still to be resolved](#Issues-still-to-be-resolved).

### User Story Testing

| Story # | Activity                   | Goal                                              | Outcome                                                                                                                  |
|---------|----------------------------|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| 1       | Viewing & Navigation       | View a list of routes                             | Success - Routes can be accessed from several links.                                                                     |
| 2       | Viewing & Navigation       | View route details                                | Success - Clicking on a route photo will show more route details.                                                        |
| 3       | Viewing & Navigation       | View membership options                           | Success - There are several links to the membership options.                                                             |
| 4       | Viewing & Navigation       | To see I’ve selected a membership to purchase     | Success - A messages to alert you and basket icon changes colour.                                                        |
| 5       | Viewing & Navigation       | Instructions on how to upload my favourite route  | Success - A separate dedicated instruction page                                                                          |
|         |                            |                                                   |                                                                                                                          |
| 6       | Sorting & Searching        | Sort the list of routes                           | Success - Routes can be sorted on a number of different ways through the sort selector                                   |
| 7       | Sorting & Searching        | Sort a specific category of route                 | Success - In the navbar users can choose different categories of routes                                                  |
| 8       | Sorting & Searching        | Search for a route by name or description         | Success - word/number searches will return words from the title, description, length, country, bike type and route type. |
| 9       | Sorting & Searching        | See what I’ve searched for and number of results  | Success - Resulting search shows number to records and search words/numbers                                              |
|         |                            |                                                   |                                                                                                                          |
| 10      | Registration/User Accounts | Register for an account                           | Success - Registration will create a new account                                                                         |
| 11      | Registration/User Accounts | Log in and out                                    | Success - Logging in and out works and user receives messages of confirmation                                            |
| 12      | Registration/User Accounts | Recover my lost password                          | Success - Password reset sends an email to the user.                                                                     |
| 13      | Registration/User Accounts | Receive email notification on registration        | Success - Users receive email after registration with a link to confirm email address.                                   |
| 14      | Registration/User Accounts | Have a personalised user profile                  | Success - After purchase of a membership, a user profile is created for the user to view                                 |
|         |                            |                                                   |                                                                                                                          |
| 15      | Purchasing and checkout    | View membership type in my basket to be purchased | Success - clicking on the basket will display the membership type added by the user                                      |
| 16      | Purchasing and checkout    | Enter my payment details                          | Success - Payment details can be entered.                                                                                |
| 17      | Purchasing and checkout    | View an order confirmation after payment          | Success - An order summary appears after a successful checkout.                                                          |
| 18      | Purchasing and checkout    | Receive an email confirmation after checkout      | Success - the user receives the order confirmation by email                                                              |
|         |                            |                                                   |                                                                                                                          |
| 19      | Admin & Route Management   | Add a route                                       | Success - Users ca add routes                                                                                            |
| 20      | Admin & Route Management   | Edit or update a route                            | Success - Edit a route is possible but only by the user who uploaded it                                                  |
| 21      | Admin & Route Management   | Delete a route                                    | Success - Delete a route is possible but only by the user who uploaded it                                                |
| 22      | Admin & Route Management   | Rate and review a route                           | Unsuccessful - Future feature, ran out of time                                                                           |
| 23      | Admin & Route Management   | Create a forum post                               | Success - Only authenticated users can add posts                                                                         |
| 24      | Admin & Route Management   | Reply to a forum post                             | Success - Only authenticated users can reply to posts.                                                                   |
| 25      | Admin & Route Management   | Save Routes to my profile                         | Success - Routes can be saved depending on membership conditions                                                         |
| 26      | Admin & Route Management   | View saved routes                                 | Success - Saved routes per user can be viewed on a separate page.                                                        |

[↥ Back to top](#Mark-McClean)

### Issued found and solved throughout the development

Below is a overview of the more major issues I faced during development. This these issues I needed the help of the Code Istitute tudors or my mentor.

There were many other smaller issues I came accross during development but I think a whole new README file would be needed to document them all. I was able to figure most of them out by myself so I don't think its necessary to document them all. Escpecially since a lot of them were design based anyway.

1.	* **Issue** – The membership is a vital part of the website so I needed to pass it from the basket to the order but kept getting an 'Order has no membershp' error during checkout.
    * **Fix** – I was using a for loop to loop through the basket items to get the membership type and tried saving that to the order after I had saved the form data. This resulted in only the membership being saved to the order. I needed to loop through the basket items first and get the membership type, then save the form data with a `commit=False` which doesn't add it to the database yet. Then I set the membership on the order with `order.membership` and then again `order.save()` to commit the save.
    * **Result** – The order was then saved in the database with both the form data and the membership type.

2.	* **Issue** – Attaching a user to the add and edit route functions.
    * **Fix** – To attach the user to the route model I initially used a custom save override method inside the model but this seemed to be blocking the entire add and edit route functions from working. I removed the save function from the route model entirely and that seemed to fix the problem for editing the routes but not for adding a new route as there was still no user set on the route. I was able to resolve this by again getting the user in the view with `user = request.user` and saving it like the issue above with `route.user = user` and then saving the route.
    * **Result** – New routes can be created and existing ones edited with the user attached.

3.	* **Issue** – Couldn't add a comment to a post in the forum.
    * **Fix** – When trying to add a comment to a forum post, I getting an `*arg` error regarding the field whcich was named 'reply'. I was originally setting the `__init__` method of the form whcih takes in the `*args` as a parameter but it was blocking the comment from being created. Im not completely sure what the issue was in the end but I tried removing the `__init__` method completely and setting the field manually with `reply = forms.CharField` and setting the required, label and placeholder conditions inside this as parameters.
    * **Result** – Comments on forum posts are now rendering

4.	* **Issue** – Regitration error
    * **Fix** – The application was throwing a Internal server error when users tried to register for an account. The problem seemed to be coming from the user profile model which has a relationship with the user, even if through no user profile has been created yet. On the User Profile model I had the membership field set to `null=False` which meant that a membership had to be set during the registration but this is only possible during the checkout. The simple fix was to change the membership field on the user profile to `null=True` so it was no longer required.
    * **Result** – New users were able to register for a new account

5.	* **Issue** – Membership not being attached to user profile
    * **Fix** – The fix for the previous error caused this error. Because the membership was no longer required on the user profile, it was no longer saving on to the profile during the checkout. To solve this I set the membership like before but this time within the checkout success view. I set it to `profile.membership=order.memberhsip` as the order was being passed into this view then saved it with `profile.save()`. This ensured that the membership was being added or updated for existing users during ever checkout process.
    * **Result** – Membership types are added to user profiles or updsted to the new membership type if user purchases a different membership.

6.	* **Issue** – Registration error again
    * **Fix** – While trying to fix the previous issue I added in a `default=1` to the membership field of the User Profile in order to attach a membership type but since I eneded creating a new save of the profile during the checkout success view, the `default=1` was not really required any more as I was overriding it but I forgot to remove it. This was causing an issue only on the deployed version of the project. While setting up my memberships on the deployed version I had deleted several and created new ones so a membership with an id=1 no longer existed in the deployed version. The simple fix here was to remove the `default=1` from the membership field as is was no longer necessary.
    * **Result** – Registration was again possible for new users.

### Issues still to be resolved

There are a few issues that I was unfortunately unable to overcome before submission. Theses issue are documented as follows.

1.  * **Issue** - Homepage images zooming slightly on mobile screens
    * **Info** - I am using 4 fixed images on my homepage that are stacked on top of each other and seprated by a scrolling cycling graphic to reveal the next image and hide the previous one. I think this looks really good but on mobile devices it causes a slight zoom of the image while scrolling up and down the page. It is not visibale in the Google Chrome Developer tools but it was visible on my own phone.
    * **Possible Fix** - I think the `background position: cover` may be causing the problem so I may need to fix the image to the top or bottom of the parent element to stop the zooming

2.  * **Issue** - Security issue using Google Maps `<iframe>`
    * **Info** - I had come up with a nice plan to reveal the actual Google map of each route on the site. This required the users to first mke their route in Google Maps, get the `<iframe>` html element provided by Google and paste it into the form. The whole thing works nicely and looks good but it provides an obvious security risk to my site that people may post malicious content or even cause the site to crash.
    * **Possible Fix** - Adding some form of validation to the form field to make sure it comes from a Google Maps source.

3.  * **Issue** - Webhook not working completely
    * **Info** - When completing an order the webhook should check if the order has been saved in the database. If the order is not in the database after 5 seconds the order information that was captured during submission, is then passed into the database automatically by the webhook. This is in the event that the order submission fails after clicking the submit button. This way the user will still have their order processed. When I tested the form submission failing to see if the webhook worked, everything appeared to work. In the stripe webhook events the `payment_intent.succeeded` showed a 200 response and the with the statement `Order created in the webhook` as opposed to `Order already eists in database` under normal checkouts. However when I checked the admin panel of my application, the order was not there. While trying to fix the issue I may have caused another a further problem as the `payment_intent.succeeded` in the stripe dashboard is now showing a 500 error.
    * **Possible Fix** - I did go through this with the tudors a couple of times but we couldn't figure out what the problem was. I think the best thing to do would be to put several print statements throughout the webhook handler file and see which ones print and see at which point the code breaks out of the sequence. Unfortunately I ran out of time to fully dive into this. Ordering normally without the use of the webhook works perfectly but it is bug that remains to be fixed.

[↥ Back to top](#Mark-McClean)

### Code Validation
Since this was a much bigger project than I had done before, I used an online code validator called [Codacy](https://www.codacy.com/). This was recomended by my mentor and it links to my Github account and analyses my code everytime I push it to Github. Ireceive an email with a list of new or previously resolved code issues.

Below is an outline of the problems I encountered ad fixed per code language:
* **HTML** - Fortunately there were no errors in all my HTML templates throughout the whole project.
* **CSS** - I had used several pseudo elements where I had forgot the double colon `::after`. Other problems included trailing white space and missing semi-colons. I was able to quickly fix these issues. There were also a lot of issues regrding '2 space indentation'. I just used the automatic indention when you hit the enter button so I ignored this issue as I don't think it's a problem. There were also many warnings for the use of `!important`. I also ignored these as it is sometimes necessary to override bootstrap stlyes to accomplish what you are looking for.
* **JavaScript** - In my Javascript files a had a lot of errors regarding the use of double quotes instead of single quotes. I decided to ignore these as the single quotes were used in the course content and I don't think this is a problem. Other problems were missing semi-colons, and using == instead of ===. I was able to fix most issues withour any problems.
* **Python** - For my Python files I mainly used the built in flake8 function in Gitpod. This would instantly tell me if the code was invalid and I mainly fixed all issues immediately during development. Near the end I ran a `python3 -m flake8` command in the terminal which would list all issue throughout all Python files saved so I'm able to see all issues in one place. I was quickly able to go through each file an validate the code. The ones I ignored were automatically generated files like migrations and some preinstalled code in the settings file. I also ignored warning to Avoid using `null=True` on string-based fields as in my project it is sometimes fine if the user wants to leave this field empty.

## Deployment
The code environment was taken from a code institute [Gitpod template](https://github.com/Code-Institute-Org/gitpod-full-template) that is stored on Github. 

This is then cloned and saved onto my own Github account as a new repository. From there I use the built in 'Gitpod' button to open up the new repository on my own Gitpod account. 

The template then opens with a boiler plate to start coding including links for Bootstrap, jQuery, Popper and Font Awesome so I didn’t need to look for the CDN’s myself. 

After every session of coding I committed my work using the Git terminal in Gitpod. Every commit has a message attached to clearly explain the changes that were made since the last commit. After the commit, the code is also then pushed to my Github account, also using the Git terminal.

### Heroku Deployment
* Create a requirements.txt file using the terminal command `pip freeze > requirements.txt`
* Create a Procfile with the terminal command `echo web: python app.py > Procfile`
* git add and git commit the new requirements and Procfile and then git push the project to GitHub.
* Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.
* From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
* Confirm the linking of the heroku app to the correct GitHub repository.
* In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

<details>
    <summary>
        Set the following config vars
    </summary>
    <img alt="Database Schema" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/media/config-vars.png">
</details>

* In the heroku dashboard, click "Deploy"
* In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch"
* The site should now be successfully deployed.

### Media and static file storage
All media and static files are stored in [AWS](https://aws.amazon.com/console/) and linked to my heroku account throught config variables.

[↥ Back to top](#Mark-McClean)

## Credits
* All content was written by myself
* All images on the site were talken from various google image results
* For the contact app I used a stack overflow article to help with the sending of the main functionality, the article can be found [here](https://stackoverflow.com/questions/48023948/handling-contact-form-in-django-email-not-sent)
* For the set up of the 'Save Routes' functionality for users with a membership I found a handy video turorial outlining the steps I could roughly apply to my application to achieve something similar. The tutorial can be viewed [here](https://www.youtube.com/watch?v=1XiJvIuvqhs)
* For the forum app on my site I mostly used code I already knew and had implemented similarly on the adding routes section however I did read through and take some tip form this forum app example [here](https://data-flair.training/blogs/discussion-forum-python-django/)
* Code institute tudors helped me throughout the project, for example with passing the membership type through different apps so it would appear in the User Profile. Also with sign up issues and attempting to resolve my webhook issue.
* Stack overflow was used to find articles on similar issues I had throughout development and the credits for that can also be found in comments within the code itself especially in the CSS file.
* CSS Tricks and codepen were also useful for finding creative style solutions for creating triangles and implementing an underline hover for the navbar links.

### Special thanks
* Special thanks to my mentor [Anthony Ngene](https://github.com/tonymontaro) who talked me through several pieces of code, for example the `key:lambda` function used to alphbetically sort the coutries by `country.name` instead of the standard 2 letter country code as it's not the same alphbetical order. He also helps me withh other issues such as membership and registration errors.
* Many thanks to the Code Institute tudors, who also helped me out with some small and larger issues I had during the development process
* Thanks to all the friends and family who tested the application on various devides and gave me feedback to improve the game

Disclaimer:
The content of the website is for educational purposes only.

[↥ Back to top](#Mark-McClean)