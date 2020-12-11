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

    stage('Step_44') {
      steps {
        bat 'python -m pip install --upgrade pip'
      }
    }

    stage('Step_55') {
      steps {
        bat 'python -m pip install -r requirements.txt'
      }
    }

    stage('Step_66') {
      steps {
        bat 'cd Tests'
      }
    }

    stage('Step_77') {
      steps {
        bat 'pytest -v --wdriver Chrome'
      }
    }

    stage('Step_88') {
      steps {
        bat 'venv_enviroment\\\\Scripts\\\\deactivate'
      }
    }

  }
}