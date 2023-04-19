pipeline {
    agent {
        docker {
            image 'python:3'
        }
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    reuseNode true
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
                    reuseNode true
                }
            }
            steps {
                sh 'python manage.py test'
            }
        }
    }
}
