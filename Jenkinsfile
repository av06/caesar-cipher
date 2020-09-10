pipeline {
    agent any
    /*parameters {
	choice (
		name: 'Proceed_Permission',
		choices: ['Proceed' , 'Stop'],
		description: ''
		)
	}*/
    stages {
	stage('Clean WS'){
	    steps {
		cleanWs()
		sh 'ls'
	    }
	}
	stage('SCM'){
	    steps {
		checkout scm
		sh 'ls'
	    }
	}
	stage('build') {
	    steps {
		//withEnv(["HOME=${env.WORKSPACE}"]) {
		    echo '#####-Beginnig Build-#####'
		    sh 'python3 -m virtualenv venv'   // Setting Up Python Virtual Environment
		    sh '. venv/bin/activate'   // Activating Python Virtual Environment
		    sh 'sudo pip3 install --user -r requirements.txt'   // Installing Required Python Modules
		    echo '#####-Build Complete-#####'
		//}
	    }
	}
	stage('test') {
	    /*when{
		expression {
		    params.Proceed_Permission == 'Proceed'
		}
	    }*/
	    steps {
		//withEnv(["HOME=${env.WORKSPACE}"]) {
		    echo '#####-Beginnig Test-#####'
		    sh 'pylint --const-rgx="[a-z_][a-z0-9_]{2,30}$" sample.py'   // Checking the code quality by linting
		    sh 'python3 -m unittest test1.py'   // Testing the Functions
		    echo '#####-Test Complete-#####'
		//}
		}
	}
    }
}
