import requests
import json
import config
#submission_response = requests.get(FORMSERVER_URL+'/projects/'+project_id+'/forms/'+form_name+'/submissions.csv.zip?attachments=false?media=true&%24filter=__system%2FsubmissionDate%20gt%20'+startdate+'%20and%20__system%2FsubmissionDate%20lt%202'+enddate,auth=HTTPBasicAuth(FORMSERVER_USER, FORMSERVER_PASSWORD))
class ODKMETHODS():
    BASE_URL = config.BASE_URL
    SERVER_USER = config.SERVER_USER
    SERVER_PASSWORD = config.SERVER_PASSWORD



    def getProjects(self):
        """
        Get all users from the server.
        """

        # Set the URL
        url = self.BASE_URL + "/projects"

        # Set the headers
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        # Set the auth
        auth = (self.SERVER_USER, self.SERVER_PASSWORD)

        # Make the request
        response = requests.get(url, headers=headers, auth=(self.SERVER_USER, self.SERVER_PASSWORD))

        # Check the status code
        if response.status_code == 200:
            # Return the users
            return response.json()

        else:
            # Return an empty list
            return []

    def getProject(self, project_id):
        """ get project using project_id
        """
        url = self.BASE_URL + "/projects/" + project_id
        response = requests.get(url, auth=(self.SERVER_USER, self.SERVER_PASSWORD))
        if response.status_code == 200:
            return response.json()
        else:
            return "{'message':'project not found'}"

    def getForms(self, project_id):
        """
        Get all forms from the server.
        """

        # Set the URL
        url = self.BASE_URL + "/projects/" + project_id + "/forms"

        # Set the headers
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        # Set the auth
        auth = (self.SERVER_USER, self.SERVER_PASSWORD)

        # Make the request
        response = requests.get(url, headers=headers, auth=(self.SERVER_USER, self.SERVER_PASSWORD))

        # Check the status code
        if response.status_code == 200:
            # Return the users
            return response.json()

        else:
            # Return an empty list
            return []

    def getSubmissionsFromFrom(self, project_id, form_name):
        pass