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
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            agent {
                docker {
                  image 'python:3'
                }
            }
            steps {
                 sh 'python manage.py test'
            }
        }
    }
}
