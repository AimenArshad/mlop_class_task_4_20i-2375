build:
    docker build -t app .

run:
    docker run -p 5000:5000 app

push:
    git add .
    git commit -m "Initial commit"
    git push origin master
