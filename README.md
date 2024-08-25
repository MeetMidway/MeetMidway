# MeetMidway Setup

Welcome to meetmidways beautiful repository, current techstack: flask and React JS

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Node.js**: [Download Node.js](https://nodejs.org/en/download/)
- **npm**: This comes with Node.js, but you can update it with `npm install -g npm`

### Installation and Setup

#### Setting up backend (Flask)

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

#### Setting up frontend (React)
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

   
   
