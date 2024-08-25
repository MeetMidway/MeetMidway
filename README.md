# MeetMidway Setup

Welcome to meetmidways beautiful repository, current techstack: flask and React JS

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Node.js**: [Download Node.js](https://nodejs.org/en/download/)
- **npm**: This comes with Node.js, but you can update it with `npm install -g npm`

## Installation and Setup

### Setting up backend (Flask)

1. Navigate to the `backend` directory and create virtal environment
   ```bash
   python -m venv venv
   ```
2. Activate venv according to OS

   unix
   ```bash
   source venv/bin/activate
   ```

   windows
      ```bash
   venv\Scripts\activate
   ```
3. Install required packaged
   ```bash
   pip install -r requirements.txt
   ```
4. Create a .env file and refer to discord for api keys
   
5. Start the flask server (ensure this is running in a separate terminal)
   ```
   export FLASK_APP=app.py
   export FLASK_ENV=development
   flask run
   ```

### Setting up frontend (React)
1. in another terminal cd into frontend and install packages
   ```
   npm i
   ```
2. Navigate to /src/contexts/MapsContext.js and input API key
   
3. Navigate to /Firebase/Firebase.js and input the firebase context
   
4. Start the React server
   ```
   npm start
   ```

## PR etiquette
Ensure all PRs are directed to development branch, squash all commits before making PR and ensure to provide a summary of your changes and perform the required tests to ensure everything works properly

### squashing commits
Why squash? This keeps our git log clean, and if we ever have to roll back there aren't separate commits we have to filter through from one PR to find the break in the link

once you've made a commit and pushed it to your branch:
   ```
   git rebase -i development
   ```

press "i" to start editing

you should see something like this:

pick <commit 1>
pick <commit 2>

change the keyword pick to "s" for commits after the first commit

pick <commit 1>
s <commmit 2>

to close and save the editor:

:x

Changing the first commit message of the new editor that pops up now will change the commit message of the squashed commits, if you don't need to change it or have, then same exit:

:x

to push the squashed commits:

git push --force






   
   
