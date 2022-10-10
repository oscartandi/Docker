# Docker Commands

1. docker –version

   This command is used to get the currently installed version of docker
   
   ![docker version](https://user-images.githubusercontent.com/98871819/194724145-62b29e3d-f32e-42e9-ad3f-34e37db0e86e.png)

2. docker pull
  Usage: docker pull <image name>
  This command is used to pull images from the docker repository(hub.docker.com)
  ![docker pull](https://user-images.githubusercontent.com/98871819/194724214-708aad19-81cf-48d1-bba0-939d2b32b244.png)


3. docker run
  Usage: docker run -it -d <image name>
  This command is used to create a container from an image
  ![docker run](https://user-images.githubusercontent.com/98871819/194724287-711b4288-1f9b-4234-bc74-6ebe60ab2fef.png)

4. docker ps
  This command is used to list the running containers
  ![docker run ps](https://user-images.githubusercontent.com/98871819/194724355-95193da1-19e8-48b9-9134-5f10419efa68.png)

5. docker ps -a
   This command is used to show all the running and exited containers
   ![docker run ps -a](https://user-images.githubusercontent.com/98871819/194724423-e94a5f38-5eba-4d88-9965-41e46fcd110e.png)
  
6. docker exec
   Usage: docker exec -it <container id> bash
   This command is used to access the running container
   ![exec -it](https://user-images.githubusercontent.com/98871819/194724524-4dd78e00-99f1-45bf-9a33-1507779979d1.png)

7. docker stop
   Usage: docker stop <container id>
   This command stops a running container
   ![image](https://user-images.githubusercontent.com/98871819/194724640-8dc05941-6c69-4a0a-b3e5-66f4f0ce7424.png)

8. docker kill

   Usage: docker kill <container id>

   This command kills the container by stopping its execution immediately. The difference between ‘docker kill’ and ‘docker stop’ is that ‘docker stop’ gives the      container time to shutdown gracefully, in situations when it is taking too much time for getting the container to stop, one can opt to kill it
   ![image](https://user-images.githubusercontent.com/98871819/194725556-5c956277-3867-4151-ba43-9fc9f4e5f67e.png)

9. docker commit

   Usage: docker commit <conatainer id> <username/imagename
   This command creates a new image of an edited container on the local system
   ![image](https://user-images.githubusercontent.com/98871819/194725670-521eae4e-cf7e-4a3d-a264-ca8b0cbf9e70.png)
                                      
10. docker login
   ![image](https://user-images.githubusercontent.com/98871819/194725775-df660491-6d27-470b-9481-694d0f42e2cc.png)


   
   
   
