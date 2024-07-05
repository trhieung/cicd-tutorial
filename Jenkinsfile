pipeline {
  agent any
  stages {
    stage('Prepare Environment') {
      steps {
        script {
          // Ensure the Docker network exists
          def networkExists = sh(script: "docker network ls | grep -w jenkins", returnStatus: true) == 0
          if (!networkExists) {
            sh 'docker network create jenkins'
          }
        }
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
    stage('Prune Docker data'){
      steps {
        echo 'Prune all volume data'
        sh 'docker system prune -a --volumes -f'
      }
    }
    stage('Start Container') {
      steps {
        sh 'docker compose up -d --no-color --wait'
        sh 'docker compose ps'
      }
    }
    stage('Wait for Service') {
      steps {
        script {
          def retries = 10 // Increase retries
          def sleepTime = 10 // Increase sleep duration
          def success = false

          while (retries > 0) {
            def httpCode = sh(script: 'curl -s -o /dev/null -w "%{http_code}" http://server:8000/users/', returnStatus: true)
            if (httpCode == 200) {
              echo "Service is up and running!"
              success = true
              break
            } else {
              echo "Service not available yet. HTTP status: ${httpCode}. Retrying..."
              sleep sleepTime
              retries--
            }
          }

          if (!success) {
            sh 'docker compose logs server' // Print server logs for debugging
            error "Service did not become available in time"
          }
        }
      }
    }
    stage('Run Test Against the Container') {
      steps {
        echo 'Testing...'
        sh 'curl http://server:8000/users/'
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
