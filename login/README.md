# Login app in Pynecone

#### Create your whole app in a single language. Don't worry about writing APIs to connect your frontend and backend

## Getting Started

+ Install pynecone using ```pip install pynecone```

+ Create directory for your project ```mkdir YOUR_DIR_NAME``` and ```cd YOUR_DIR_NAME```

+ Initiate pynecone to project directory ```pc init```

+ Run in development server ```pc run```

## Directory Structure Insights

#### .web
##### The Pynecone frontend compiles down to a NextJS app. The output is stored in the .web directory. You will never need to touch this directory, but it can be useful for debugging.

##### Each Pynecone page will compile to a corresponding .js file in the .web/pages directory.

#### Assets
##### The assets directory is where you can store any static assets you want to be publicly available. This includes images, fonts, and other files.

#### Main Project
##### Initializing your project creates a directory with the same name as your app. This is where you will write your app's logic.

##### Pynecone generates a default app within the hello/hello.py file. You can modify this file to customize your app.

#### Config
##### The pcconfig.py file contains configuration for your app.

<a href="pynecone.io">Visit Pynecone Here </a>