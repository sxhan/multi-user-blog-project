# TFYT - Created for Udacity Full Stack Web Developer Nanodegree Project 3: Multi-User Blog
A Boostrap 3, jinja2 and webapp2 based Multi-User blog and Reddit clone created in fulfillment of Project 3 Requirements of Udacity's Full Stack Nano Degree Program.

A live demo is hosted on google cloud [here](https://hello-world-155208.appspot.com/)

This project can be viewed by either running the project locally or deploying it to the Google Cloud Platform. Instructions for deployments are below:

## Setup (Mac and Linux)
Follow the instructions found in [this pdf](http://blog2.thoughtforyourthoughts.com/udacity-fsnd-project-3/docs/InstallingAppEnginewithGCloudonMacOSandLinux.pdf) to set up Google Cloud SDK on your machine. Specific versions used at time of development:

- Google Cloud SDK 139.0.1
- app-engine-python 1.9.49
- bq 2.0.24
- bq-nix 2.0.24
- core 2017.01.12
- core-nix 2016.12.09
- gcloud
- gsutil 4.22
- gsutil-nix 4.22

The following instructions assume that you have adde the SDK's python commands to your PATH, so commands like `gcloud` and `dev_appserver.py` are available. See the [Google Cloud SDK setup instructions](http://blog2.thoughtforyourthoughts.com/udacity-fsnd-project-3/docs/InstallingAppEnginewithGCloudonMacOSandLinux.pdf) for more details.

### Running a local server
1. Checkout the project: `git clone git@github.com:sxhan/udacity-fsnd-project-3.git`
2. Navigate to project dir: `cd udacity-fsnd-project-3`
3. Start a local development server: `dev_appserver.py .` Note the dot at the end.
4. By default, the site should be available at `localhost:8080` in your browser. Alternatively, check the prompt in terminal. It display something similar to:
 > INFO     2017-01-23 17:05:53,720 admin_server.py:116] Starting admin server at: http://localhost:8000

5. Use ctrl-C to stop the development server.


### Deploying to the cloud
1. Checkout the project: `git clone git@github.com:sxhan/udacity-fsnd-project-3.git`
2. Navigate to project dir: `cd udacity-fsnd-project-3`
3. Follow instructions in the [Google Cloud SDK setup instructions](http://blog2.thoughtforyourthoughts.com/udacity-fsnd-project-3/docs/InstallingAppEnginewithGCloudonMacOSandLinux.pdf) to set up a blank project in the web console, and configure the `gcloud` command use that project.
4. Run the following to deploy to your pre-configured Google Cloud Project: `gcloud app deploy app.yaml index.yaml`. Answer yes to the prompt.
 > WARNING: if you had another project previously set up as your gcloud app,

5. If successful, the project should be deployed to Google Cloud Project's url, which should be in the format `https://{{project-name}}-{{some-numbers}}.appspot.com/`
