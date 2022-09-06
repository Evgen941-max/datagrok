When you run command "docker-compose up --build", you need create docker network. Run command "docker network create --driver=bridge my_project_network"

Test application:
    After successfully launching the application, use command "curl 0.0.0.0:8080". 

The application will return the value in the forman JSON. Its for GitHub