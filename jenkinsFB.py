#-*- encoding = utf-8 -*-
import jenkins
jenkins_server_url = "http://jenkins.dev.com/"
user_id = "spring"
api_token = "123456"
server=jenkins.Jenkins(url=jenkins_server_url,username=user_id,password=api_token)
# jobs=server.get_all_jobs()

params= {'branch': 'release-20200810'}
server.build_job("user",params)