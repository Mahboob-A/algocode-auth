#!/bin/bash 

set -o errexit 

set -o nounset 

if [ -z "${AUTH_CODE_MANAGER_EC2_SERVER_IP_ADDRESS}" ]
then 
        echo "EC2 Server IP Address for Auth and Code Manager Service is not defined."
        echo "Please export the EC2 server IP address in host machine and try again."
        exit 0  
fi 

# git archive --format tar --output ./production_project.tar main 
tar --exclude='.git' --exclude='docker/production/ec2_deploy.sh' -cvf ./production_project.tar . 

echo "Uploading the Project to the server ... " 

# rsync -e "ssh -i ${AUTH_CODE_MANAGER_EC2_SERVER_PEM_PATH}" ./production_project.tar root@"${AUTH_CODE_MANAGER_EC2_SERVER_IP_ADDRESS}":/tmp/production_project.tar

rsync -e "ssh -i ${AUTH_CODE_MANAGER_EC2_SERVER_PEM_PATH}" ./production_project.tar ubuntu@"${AUTH_CODE_MANAGER_EC2_SERVER_IP_ADDRESS}":/tmp/production_project.tar

echo "Upload complete ... "

echo "Building the docker compose  ... "

ssh -i "${AUTH_CODE_MANAGER_EC2_SERVER_PEM_PATH}" -o StrictHostKeyChecking=no ubuntu@"${AUTH_CODE_MANAGER_EC2_SERVER_IP_ADDRESS}" << 'ENDSSH'
        mkdir -p /home/ubuntu/app 
        rm -rf /home/ubuntu/app/* && tar -xf /tmp/production_project.tar -C /home/ubuntu/app 
        sudo docker compose -p auth_cm_service -f /home/ubuntu/app/production.yml up --build -d --remove-orphans 
ENDSSH

echo "Build Success ... "
