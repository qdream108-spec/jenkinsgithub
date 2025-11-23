pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/qdream108-spec/jenkinsgithub.git', branch: 'main'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat """
                python -m venv venv
                venv\\Scripts\\activate
                pip install --upgrade pip
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                venv\\Scripts\\activate
                pip install -r requirements.txt || echo "No packages to install"
                """
            }
        }

        stage('Run Python Script') {
            steps {
                bat """
                venv\\Scripts\\activate
                python jn.py
                """
            }
        }
    }
}
