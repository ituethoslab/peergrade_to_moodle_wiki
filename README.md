# Peergrade to Moodle wiki

A little contraption to push Peergrade assignment into a Moodle wiki.

## Pre-requisites
The script is semi-automated. This means that you need to do a few things before it can begin to do its magic. Specifically, you'll need the following:

### 1. A Moodle token. 
   At the time of writing, LearnIT doesn't allow for creation of token/key without admin authorization. Our work around is to re-use the mobile key that is automatically created when a user signs into LearnIT from the Moodle mobile App. It's not the most straight forward but it's easier and faster than asking the IT department ¯\_(ツ)_/¯

   Once you've downloaded and then logged in using the mobile app. Go into your Personal Settings -> Security Keys
   There you can find the key assigned to your mobile app. The key is a long combination of number and letters that kinda looks like this bfcsefd44545a25dd82wc08ddf602980

### 2. A Moodle Wiki ID. 
   First one has to create a Moodle Wiki in the in the specific module that you wish to upload to. Make sure to name them pertinently :)
   This can be made by anyone with LearnIT editing capacity. Once a wiki has been created you have to run the following API call on your browser:

   `https://learnit.itu.dk/webservice/rest/server.php?wstoken=TOKENHERE&wsfunction=mod_wiki_get_wikis_by_courses&moodlewsrestformat=json`

   Replace 'TOKENHERE' in the URL with the token you have been assigned after the first pre-requisite. The query will result in a JSON file with all of the wikis in the course. Each wiki will be presented with their "id" and their name. Make sure you have the id for the module you want!


## How to use
The scripts takes two positional arguments:
- A **zipfile** containing exported PeerGrade submissions
- A **WikiID** corresponding to the wiki for the desired module

The **zipfile** must be obtained by the person that has admin access to PeerGrade and is able to use the export function. Make sure the file is located in the same directory as the python files

The **WikiID**  that you got earlier. Just remember to use the right ID and you're set.

Enjoy!