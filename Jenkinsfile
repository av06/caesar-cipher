Jenkinsfile
pipeline {
    agent any

    stages {
        stage('CleanWorkspace') {
            steps {
                deleteDir()
            }
        }

        stage('CheckOutSCM') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'sudo apt-get update'
                sh 'sudo apt install virtualenv'
                sh 'python3 -m virtualenv venv'
                sh 'source venv/bin/activate'
                sh 'pip3 install -r requirements.txt'
                sh 'pylint --const-rgx='[a-z_][a-z0-9_]{2,30}$' sample.py'
            }

        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest test1.py'

            }
        }

    }
}