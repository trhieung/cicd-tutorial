pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'Building ...'
        sh 'docker compose build --no-cache'
      }
    }

    stage('test') {
      steps {
        echo 'Testing ...'
        echo 'Not having test available yet'
      }
    }

    stage('deploy') {
      steps {
        echo 'Deploying ...'
        sh 'docker compose up -d'
      }
    }

  }
}