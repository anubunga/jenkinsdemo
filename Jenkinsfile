pipeline {
    agent {
        label 'generic'
    } //agent
    stages {
        stage("Setup script") {
            steps {
                sh """
                    pip install --upgrade pip
                    pip install pytest
                """
            } //steps
        } //stage
        stage("Run unit tests") {
            steps {
                sh """
                    python -m pytest
                """
            } //steps
        } //stage
        stage("Echo") {
            steps {
                sh """
                    echo Hello world, we can't do it without HelloWorld
                """
            } //steps
        } //stage
    } //stages
    post {
        always {
            sh """
                pip uninstall pytest -y
            """
        } //always
    } //post
} //pipeline