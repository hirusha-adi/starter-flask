# built a new image
echo "Running: docker build -t flaskapp_image ."
docker build -t flaskapp_image .

# run the new container as deamon
echo "Running: docker run -d -p 5000:5000 --name flaskapp flaskapp_image"
docker run -d -p 5000:5000 --name flaskapp flaskapp_image

# list the running containers
echo "Running: docker ps"
docker ps