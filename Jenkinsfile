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
                sh 'virtualenv venv'
                sh 'source venv/bin/activate'
            }

        }

        stage('Test') {
            steps {
                sh 'pip3 install pylint'
                sh 'pip3 install unittest'
                sh 'pylint --const-rgx='[a-z_][a-z0-9_]{2,30}$' sample.py'
                sh 'python3 -m unittest test1.py'

            }
        }

    }
}