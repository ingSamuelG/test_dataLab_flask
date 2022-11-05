import sqlite3

class DbConection:
    
    def __init__(self,database) -> None:

        self.db_name= database
        self.connection = sqlite3.connect(database,  check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.projectTableName = "project"
        self.roleTableName = "role"
        self.userTableName = "user"
        self.roleUserAsocTableName = "user_role_association_table"

    def getProjects(self):
        getAllProjectsStaments = f'SELECT * FROM {self.projectTableName};'
        res = self.cursor.execute(getAllProjectsStaments)
        return res.fetchall()
    
    def getProjectByName(self, name):
        # sqlite no tiene un buen collate para escapar acentos esto deberia servir en otro sql server
        getProjectsByStaments = f'SELECT * FROM  {self.projectTableName} WHERE project_name COLLATE SQL_Latin1_General_Cp1_CI_AI like ?'
        res = self.cursor.execute(getProjectsByStaments,('%'+name+'%',))
        return res.fetchall()

    def getUsers(self):
        getUsersStaments = f'SELECT {self.userTableName}.*, {self.roleTableName}.name as \'role\' FROM user INNER JOIN {self.roleUserAsocTableName} ON {self.userTableName}.id={self.roleUserAsocTableName}.user_id INNER JOIN {self.roleTableName} ON	{self.roleUserAsocTableName}.role_id = {self.roleTableName}.id;'
        res = self.cursor.execute(getUsersStaments)
        return res.fetchall()
