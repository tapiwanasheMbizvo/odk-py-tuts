from odk_methods import ODKMETHODS


odk = ODKMETHODS()

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