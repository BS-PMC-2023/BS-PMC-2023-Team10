pipeline {
    agent any
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3'
                }
            }
            steps {
                sh """
                    pwd
                    id
                    env | sort
                    
                    ls -la
                """
                sh """
                    export HOME=${WORKSPACE}
                    pip install -r requirements.txt --user
                """
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'python:3'
                    reuseNode true
                }
            }
            steps {
                sh 'python manage.py test'
            }
        }
    }
}
