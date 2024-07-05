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
        sh 'docker inspect cicd-tutorial_default'
      }
    }
    stage('test') {
      steps {
        sh '''
        docker logs cicd-tutorial-db-1
        docker logs cicd-tutorial-server-1
        docker logs cicd-tutorial-vite-ts-1
        '''
        echo 'check server'
        script {
          def count = 0
          while (count < 5) {
              sh 'docker logs server'
              count++
              sleep 5
          }
        }
      }
    }
  }
  post {
    always {
      sh 'docker compose down --remove-orphans -v'
      sh 'docker compose ps'
    }
  }
}
