2/12/2015:

This is a project I'm working on to compile and display information on US politicians.  The information will draw from a number of APIs including Wikipedia, Sunlight Foundation and Open Secrets.  Who knows where this will go.  Right now I have the following done(ish):
- Backend model for politicians
- Database populated with info drawn from wikipedia using population scripts
- Profile view and an individual politician's profile view
- Bootswatch theme (Yeti) installed
- Live search function for politician names that uses an AJAX request to populate a list client side then a jQuery/KEYUP initiated regex filter

Short-term goals:
- Pull in more information from relevant APIs client side
- Have information put into individual profile template
- Create user accounts/authentication
- 
- Create some sort of evaluation system of politicians (likes/dislikes/change over time period)

Long-term ideas:
- Add in a facebook-style news feed of recent events, filtered by registered user interest
- Create a comment/like system for these news entries
- Add in a "rabbit hole" widget so users can track where they're clicking -- three dimensional so you can "go back" pages in rabbit hole and follow different route. Basically an advanced, visual "back" button.

Why?
This project is meant to shine light on our government and how they operate. We need to know what exactly our politicians are doing so as to remove any ambiguity about how they do or do not work for us, "the taxpayers". 

We are what we do, not what we say we do.