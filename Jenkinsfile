pipeline {
  agent any
  stages {
    stage('Prepare Environment') {
      steps {
        echo "Prepare environment"
        sh 'docker network list'
      }
    }
    stage('Verify Tooling') {
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
    stage('Start Container') {
      steps {
        sh 'docker compose up -d --no-color --wait'
        sh 'docker compose ps'
        sh 'docker network list'
        sh 'docker inspect cicd_tutorial_network'
      }
    }
    stage('test') {
      steps {
        sh '''
        docker logs cicd-pipeline-db-1
        docker logs cicd-pipeline-server-1
        docker logs cicd-pipeline-vite-ts-1
        docker compose down
        '''
      }
    }
  }
}
