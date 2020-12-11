pipeline {
  agent any
  stages {
    stage('One_11') {
      steps {
        bat 'dir'
      }
    }

    stage('Step_22') {
      steps {
        bat 'py -3 -m venv venv_enviroment'
      }
    }

    stage('Step_33') {
      steps {
        bat 'call venv_enviroment\\\\Scripts\\\\activate'
      }
    }

  }
}