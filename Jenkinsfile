pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3'
                }
            }
            steps {
               export HOME=/var/jenkins_home/jobs/Team-10/jobs/Team10/branches/main/workspace pip install -r requirements.txt --user
            }
        }
        stage('Test') {
            }
            steps {
                 sh 'python manage.py test'
            }
        }
    }
}
