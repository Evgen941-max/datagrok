When you run command "docker-compose up --scale flask_cpu=2 -d", you need create docker network. Run command "docker network create --driver=bridge my_project_network"

In this task, will need create two backend containers. In this task I used docker-compose scale:
    docker-compose up --scale flask_cpu=2 -d
After that, docker up two backend containers, and one frontent.

Test application:
    After successfully launching the application, use command "curl 0.0.0.0:8080".
    You can see information about cpu in format JSON.
    For example, in this repository you can see work two backend containers and one frontent. (test.jpeg)

 Its for GitHub