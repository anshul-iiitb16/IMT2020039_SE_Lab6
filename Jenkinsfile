pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/anshul-iiitb16/IMT2020039_SE_Lab6.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Sum_Nat_Nums.py"
                sh "./Sum_Nat_Nums.py"
            }
        }
        stage('Passing Test Code') {
            steps {
                sh "chmod u+x Pass_Unit_Test.py"
                sh "./Pass_Unit_Test.py"
            }
        }
        stage('Failing Test Code') {
            steps {
                sh "chmod u+x Fail_Unit_Test.py"
                sh "./Fail_Unit_Test.py"
            }
        }
    } 
}
