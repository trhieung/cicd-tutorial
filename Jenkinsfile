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
    stage('Wait for service'){
      steps {
        script {
          def retries = 5
          while (retries > 0) {
            if (sh(script: 'curl -s -o /dev/null -w "%{http_code}" http://server:8000/users/', returnStatus: true) == 0) {
              echo "Service is up and running!"
              break
            } else {
              echo "Service not available yet. Retrying..."
              sleep 5
              retries--
            }
          }
          if (retries == 0) {
            error "Service did not become available in time"
          }
        }
      }
    }
    stage('Run test against the container'){
      steps {
        echo 'Testing...'
        sh 'curl http://0.0.0.0:8000/users/'
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
