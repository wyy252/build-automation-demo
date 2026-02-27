pipeline {
    agent { label 'docker-agent' }

    environment {
        IMAGE_NAME = "build-automation-demo"
        CONTAINER_NAME = "build-automation-demo-container"
        APP_PORT = "5000"
    }

    options {
        timestamps()
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 --version
                python3 -m venv .venv
                . .venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                . .venv/bin/activate
                pytest -q
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                  docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                  docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Run Container (Smoke Test)') {
            steps {
                sh '''
                set -e

                docker rm -f build-automation-demo-container || true

                docker run -d \
                    --name build-automation-demo-container \
                    --network jenkins-net \
                    build-automation-demo:latest

                sleep 2

                curl -fsS http://build-automation-demo-container:5000/health
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline finished (success or failure)."
            sh 'docker rm -f ${CONTAINER_NAME} || true'
        }
        failure {
            echo "Build blocked due to failure (e.g., tests failed)."
        }
        success {
            echo "Build + test + docker run succeeded."
        }
    }
}