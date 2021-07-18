# FBS (facebook stalky) [BROKEN]
The program that you see here is an old bet between me andmy friend.
The idea was to creat the Stalk bot for facebook to observer their activity icon. BUT in new version in facebook it's impossible to do so. Why? 
Facbook changed API to graph api +incoming values are hidden or have inconsistant claes.

That's why it uses old mobile version of the site, and utilize category "Active friends". Why not the right bar of the site? The problem is this "activebar" is limited to 20-25 people active + group. Even more - updates are irregular and might be off by 1-2 mins. 

## How to use it?
Head to the static folder and change lines:

```python

mail = "your@mail"
pwd  = 'your_password'
profile_name = "profilename showed in the url (after facebook.com/) when you are on your profile page"
cookie={you can do it  by using f12 after login in normal facebook and copy it here}

```

Then the program should run and open the selenium page. In colleceted_data folder you will find created files with active hours.
Don't close selenium window.
