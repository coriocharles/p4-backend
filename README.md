# Tune
## Overview

An app that will allow users to log-in using JWT, have a custom user profile, and be able to use the music review platform.  Users can add artists, albums, genres, and reviews on albums with full CRUD.  A recommended page exists that reads the logged-in user's preferences and serves an album up as a recommendation.  This is accomplished utilizing django querying in the views and serializers.  This app has a robust back-end with a reg-ex search feature, many-to-many relationships, and data refinement to send only as much data as necessary.


## Technologies used:
- Python
- Django
- React
- JavaScript
- Fetch & Axios
- React MUI

## Links
[GitHub Repository, Front-end](https://github.com/coriocharles/p4-frontend)

[GitHub Repository, Back-end](https://github.com/coriocharles/p4-backend)


## Screen Captures
### Home Page w/ Recommended Album
<img width="1440" alt="Screen Shot 2022-06-03 at 11 27 09 PM" src="https://i.imgur.com/ipUGHqu.png">

### Artist Page
<img width="1439" alt="Screen Shot 2022-06-03 at 11 29 20 PM" src="https://i.imgur.com/CakrnHi.png">

### Album Page
<img width="1439" alt="Screen Shot 2022-06-03 at 11 29 20 PM" src="https://i.imgur.com/DbhzoVv.png">

### User Profile
<img width="1439" alt="Screen Shot 2022-06-03 at 11 29 20 PM" src="https://i.imgur.com/EQFKe7v.png">


### Logging In
![Recording 2022-06-04 at 14 42 43](https://media.giphy.com/media/qV3ZnRanFKDDPtlq65/giphy.gif)


### Viewing Artist, adding Review, liking a Review
![Recording 2022-06-04 at 00 07 30](https://media.giphy.com/media/LLhp8lY2JkwZxp8nID/giphy.gif)


## User Stories
### MVP Goals
- As a user, I would like add albums, artists, genres and reviews.
- As a user, I would like to be able to register / log in with JWT.
- As a user, I want to be able to search for all objects.

### Stretch Goals
- As a user, I would like albums to be recommended to me.
- As a user, I would like to 'like' other peoples posts and have it update live.  
- As a user, I would like to be able to upload a profile picture.
 
## Hurdles
- MUI dependencies (styling will always be my downfall)