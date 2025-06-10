pipeline {
    agent any

    environment {
        BASE_URL = "http://127.0.0.1:5000"
        RECIPIENTS = 'sebastianvelozac@hotmail.com'
    }

  stages {
     stage('Error') {
        steps {
            sh 'python3 -m app. &'
            // Espera uque app arranque
            sh 'sleep 5'
        
    }
    stage('Start Application') {
        steps {
            sh 'python3 -m app.api &'
            // Espera uque app arranque
            sh 'sleep 5'
        }
    }
    stage('Run Unit Tests') {
        steps {
            sh 'BASE_URL=$BASE_URL pytest test/unit --junitxml=report_unit.xml'
        }
    }
    stage('Run API Tests') {
        steps {
            sh 'pytest test/rest --junitxml=report_api.xml'
        }
    }
}

post {
    always {
        // Intenta cerrar la aplicación (ajusta el comando si es necesario)
        sh 'pkill -f "python3 -m app.api"'
        }
        success {
            emailext (
                subject: "Jenkins Pipeline Exitoso: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Las pruebas se ejecutaron correctamente. Se adjuntan los reportes.",
                to: "${env.RECIPIENTS}",
                attachmentsPattern: 'report_unit.xml,report_api.xml'
            )
        }
        failure {
            emailext (
                subject: "Jenkins Pipeline Fallido: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "La ejecución del pipeline falló. Por favor, revisa los logs.",
                to: "${env.RECIPIENTS}"
            )
        }
    }
}