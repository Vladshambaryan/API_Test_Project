
FROM jenkins/jenkins:lts-jdk17
USER root
RUN apt-get update && apt-get install -y python3 python3-pip wget python3-venv
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable
USER jenkins

#  docker build -t jenkins_docker_test .  # obraz

#  docker run -p 8080:8080 -p 50000:50000 --restart=on-failure -v C:\Users\PC\PycharmProjects\sep_23\dockers\jenkins_home:/var/jenkins_home jenkins_docker_test

#  http://localhost:8080/

# docker ps ===spicok conteynerov !!!!!!!!!!!!!!!!

# docker stop e26f55494395  conteynera !!!!!!!!!!!!!!!!

# docker rmi -f 7a7add0bf3da принудительное

# docker rmi <image id>   Удаление образа