from io import BytesIO
from zipfile import ZipFile

from odk_methods import ODKMETHODS
import pandas as pd

odk = ODKMETHODS()

"""
projects = odk.getProjects()
for project in projects:
    project_name = project['name']
    project_id = project['id']
    print(f"Project: {project_name}\t ID: {project_id}")

one_project = odk.getProject(str(6))
print(one_project)

forms = odk.getForms(str(6))
for form in forms:
    print(f"Form: {form['name']}\t State: {form['state']}")

#  project_id, form_name, startdate, enddate):
#  odk.getFormData(str(6), 'Form_1', '2019-01-01', '2019-01-31')
"""
response = odk.getSubmissions(project_id=str(6), form_name="TASQC COA's Diary of Daily Services v2",
                              startdate="2022-01-01", enddate="2022-03-01")

if response.content:
    print("HEY HEY ")
    df = pd.DataFrame()
    result = pd.DataFrame()

    zip_file = ZipFile(BytesIO(response.content))
    files = zip_file.namelist()
    if len(files) == 1:
        file = files[0]
        print(file)
        df = pd.read_csv(zip_file.open(file))
        print(df.head())
        result = df.groupby('SubmissionDate').agg({'SubmitterName': 'count'})
        print(result.head())
        result.to_csv('submission_count.csv')
