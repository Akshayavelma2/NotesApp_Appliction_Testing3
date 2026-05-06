pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests in Parallel') {
            steps {
                bat 'pytest -n 2 --html=report.html --alluredir=allure-results'
            }
        }

        stage('Publish Artifacts') {
            steps {
                archiveArtifacts artifacts: 'report.html, screenshots/*, logs/*, allure-results/*', allowEmptyArchive: true
            }
        }
    }
}