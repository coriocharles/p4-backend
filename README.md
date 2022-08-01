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

## Wireframes
![p3wireframe](https://user-images.githubusercontent.com/97096664/171978202-4a32b6bf-d62a-481d-8402-e337e3174db5.png)


## Links
[GitHub Repository, Front-end](https://github.com/coriocharles/P3-frontend)

[GitHub Repository, Back-end](https://github.com/danianise/p3-backend)


## Screen Captures
### Home Page w/ Recommended Album
<img width="1440" alt="Screen Shot 2022-06-03 at 11 27 09 PM" src="https://i.imgur.com/ipUGHqu.png">

### Stock Info
<img width="1439" alt="Screen Shot 2022-06-03 at 11 29 20 PM" src="https://user-images.githubusercontent.com/97096664/171979015-934333d6-0f2c-4bcc-9de6-7c21534cd5ee.png">

### Watchlist
![Recording 2022-06-04 at 14 42 43](https://user-images.githubusercontent.com/97096664/172021295-14a63925-e59c-4119-a39b-637552edb8a8.gif)


### Search by Stock Symbol
![Recording 2022-06-04 at 00 07 30](https://user-images.githubusercontent.com/97096664/171981804-74136122-34f0-431f-b820-0e09065ad41f.gif)

### Buy/Sell Stock
![Recording 2022-06-04 at 00 05 13](https://user-images.githubusercontent.com/97096664/171981764-315380d2-faba-49fe-9901-ebee220844de.gif)

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