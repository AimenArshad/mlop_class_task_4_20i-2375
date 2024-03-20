build:
    docker build -t my-flask-app .

run:
    docker run -p 5000:5000 my-flask-app

push:
    git add .
    git commit -m "Initial commit"
    git push origin master
