This **Docker compose** is used to create a Wordpress enviroment. It creates an image for Docker with version **3.9** and then configures the services for MySQL and WordPress with the login info, ports and volumes.

Finally, a volume is configured to hold the data so that it is not deleted when Docker is shut down. 

When port 85:80 is opened, an image will be displayed.