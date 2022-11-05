
def userResToDic(user):
    Id, username, _, profile_pic, fullName, roleName = user
    return {"id": Id, "username":username, "profile_pic": profile_pic, "fullName": fullName, "role": roleName}

def projectResToDic(project):
    Id, project_images, project_desc, project_name, project_active = project
    return {"id": Id, "project_images":project_images, "project_desc": project_desc,"project_name": project_name, "project_active": project_active}
