pipeline{
	agent any
	DOCKER_TAG = getDockerTag()
	stages{
		stage("build"){
			when { branch 'develop' }
			steps{
                		sh "docker build ./be -t 98ashish/mybeapp:${DOCKER_TAG}"
				sh "docker build ./fe -t 98ashish/myfeapp:${DOCKER_TAG}"
				sh "docker build ./api -t 98ashish/myapiapp:${DOCKER_TAG}"
            		}
		}
		stage("push"){
			when { branch 'develop' }
			steps{
				withCredentials([string(credentialsId: 'dockercred', variable: 'dockerHubPwd')]) {
                 			sh "docker login -u 98ashish -p ${dockerHubPwd}"
                    			sh "docker push 98ashish/mybeapp:${DOCKER_TAG}"
					sh "docker push 98ashish/myfeapp:${DOCKER_TAG}"
					sh "docker push 98ashish/myapiapp:${DOCKER_TAG}"


                		}
			}
		}
		stage("deploy"){
		}
	}
}
def getDockerTag(){
    def tag  = sh script: 'git rev-parse HEAD', returnStdout: true
    return tag
}
