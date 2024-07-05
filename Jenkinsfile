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
    stage('build'){
      steps {
        echo 'Building...'
        sh 'docker compose build --no-cache'
      }
    }
  }
}