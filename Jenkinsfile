pipeline {
  agent any
  stages {
    stage('verify tooling') {
      steps {
        sh '''
          docker info
          docker version
          docker compose version
          curl --version
          git --version
        '''
      }
    }
    stage('Start container'){
      steps{
        sh 'docker compose up -d --no-color --wait'
        sh 'docker compose ps'
      }
    }
    stage('Run test against the container'){
      steps {
        echo 'Testing...'
        sh 'curl http://0.0.0.0:8000/users/'
      }
    }
  }
}