pipeline {
    agent {
        docker {
            image 'python:3'
        }
    }
    stages {
        stage('Build') {
            steps {
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
