pipeline {
    agent any

    environment {
        BASE_URL = "http://127.0.0.1:5000"
        RECIPIENTS = 'sebastianvelozac@hotmail.com'
    }

    stages {
        stage('Start Application') {
            steps {
                bat 'start /B python -m app.api'
                // Espera unos segundos para que la app arranque
                bat 'timeout /T 5'
            }
        }
        stage('Run Unit Tests') {
            steps {
                bat 'set BASE_URL=%BASE_URL% && pytest test/unit --junitxml=report_unit.xml'
            }
        }
        stage('Run API Tests') {
            steps {
                bat 'pytest test/rest --junitxml=report_api.xml'
            }
        }
    }

    post {
        always {
            // Intenta cerrar la aplicación (ajusta el nombre si es diferente)
            bat 'taskkill /IM python.exe /F'
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