pipeline {
    agent { docker { image 'python:3.6' } }
    stages {
        stage('build') {
            steps {
                python 't.py'
            }
        }
    }
}
