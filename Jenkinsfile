pipeline{
	agent any
	environment{
		DOCKER_TAG=getDockerTag()
	}
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
			 when { branch 'develop' }
			steps{
				sshagent(['ec2cred']) {
					def privateip = "172.31.17.11"
					def dockerrunfe= "docker run -d --rm -p 8989:4200 --name frontend 98ashish/myfeapp:${DOCKER_TAG}"
    					sh "ssh -o StrictHostKeyChecking=no ec2-user@${privateip} ${dockerrunfe}"
					def dockerrunbe= "docker run -d --rm -p 8990:27017 --name backend 98ashish/mybeapp:${DOCKER_TAG}"
                                        sh "ssh -o StrictHostKeyChecking=no ec2-user@${privateip} ${dockerrunbe}"
					def dockerrunapi= "docker run -d --rm -p 8991:5000 --name api 98ashish/myapiapp:${DOCKER_TAG}"
                                        sh "ssh -o StrictHostKeyChecking=no ec2-user@${privateip} ${dockerrunapi}"
				}
			}
		}
	}
}
def getDockerTag(){
    def tag  = sh script: 'git rev-parse HEAD', returnStdout: true
    return tag
}
