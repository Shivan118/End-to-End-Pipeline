# End_to_End_Pipeline
This is Machine Leanrirng Project

#### Software Requirement:

1. [Github Account](https://github.com/)
2. [Heroku Account](https://dashboard.heroku.com/)
3. [VS Code IDE](https://code.visualstudio.com/Download)
4. [GIT CLI](https://git-scm.com/downloads)

Creating Conda Envronment
```
conda create -p venv python==3.7 -y

```

Activate Conda Envronment
```
conda activate venv/

```

OR 

```
conda activate venv

```

```
pip install -r requirements.txt

```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To Check the git status
```
git status
```

To check all version maintained by git
```
git log
```
To Create version/Commit all changes by git
```
git commit -m " Messaage "
```

To Send version / chnages to Github
```
git push origin main
```
To check remote url
```
git remote -v
```

To setup Ci/CD in Heroku we need 3 information

1. HEROKU_EMAIL = shivan@ineuron.ai
2. HEROKU_AIP_KEY = 523239b2-5b0a-447e-bc61-bdd7f88da5da
3. HEROKU_APP_NAME = starter-project-first

BUILD DOCKER IMAGE

```
docker build -t <image_name>:<tagname> .
```
Note: Image Name for Docker must be lowercase

To List Docker Image
```
docker images
```
Run Docker Image
```
docker run -p 5000:5000 -e PORT=5000 <Docker_Image>
```

To check running container in docker
```
docker ps
```
To Stop Docker container
```
docker stop <container_id>
```
