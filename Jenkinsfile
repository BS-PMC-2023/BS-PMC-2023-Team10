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
            steps {
                 sh 'python manage.py test'
            }
        }
    }
}
