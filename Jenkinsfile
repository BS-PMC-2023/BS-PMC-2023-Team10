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
               pip install -r requirements.txt --user
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
