pipeline {
  agent any
  stages {
    stage('One_11') {
      steps {
        retry(count: 1) {
          sh 'py -3 -m venv venv_enviroment'
        }

        sh 'py -3 -m venv venv_enviroment'
      }
    }

  }
}