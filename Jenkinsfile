pipeline {
    agent {
        docker {
            image 'python:3.11' // Docker image to use
            args '-v /var/run/docker.sock:/var/run/docker.sock -u root' // Add -u root option for elevated permissions
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install pipenv') {
            steps {
                sh 'apt-get update' // Update package lists
                sh 'apt-get install -y python3-dev python3-pip' // Install Python and pip
                sh 'pip install pipenv' // Install pipenv
            }
        }

        stage('Build') {
            steps {
                sh 'pipenv install --skip-lock' // Create and activate virtual environment, install dependencies (skip lock)
                sh 'pipenv install -r requirements.txt' // Install dependencies from requirements.txt
            }
        }

        stage('Test') {
            steps {
                sh 'pipenv run python manage.py test' 
            }
        }

        stage('Deploy') {
            steps {
                sh 'pipenv run python manage.py migrate' 
                sh 'nohup pipenv run python manage.py runserver & sleep 5' 

            }
        }
        stage('Coverage Report') {
            steps {
                sh 'pipenv run coverage report'
            }
        }
        stage('Customer Satisfaction Metrics') {
                steps {
                    script {
                        sh 'pipenv run python customer_satisfaction.py'
                        sh 'pipenv run python customer_interviews.py'
                }
            }
        }
        
        stage('Count Lines of Code') {
            steps {
                script {
                      sh 'pipenv run pygount --format=summary'
                }
            }
        }
    }

    post {


        success {
            echo 'Build successful!' // Display success message
        }

        failure {
            echo 'Build failed!' // Display failure message
        }
    }
}