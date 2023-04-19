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
                export HOME=${WORKSPACE} sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                 sh 'python manage.py test'
            }
        }
    }
}
