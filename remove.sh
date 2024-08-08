# stop the currently running container
echo "Running: docker stop flaskapp"
docker stop flaskapp

# remove the built image
echo "Running: docker rm flaskapp"
docker rm flaskapp