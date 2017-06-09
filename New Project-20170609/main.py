#encoding:utf=8  
import pymongo  

connection=pymongo.Connection('10.32.38.50',27017)  

#选择myblog库  s
db=connection.myblog  

# 使用users集合  
collection=db.users  

#添加命令如下：  

# 添加单条数据到集合中  
user = {"name":"xiaoxu","age":"23"}  
collection.insert(user)     #添加数据
collection.save(users)      #添加数据

#同时添加多条数据到集合中  
users=[{"name":"xiaoxu","age":"23"},{"name":"xiaoli","age":"20"}]  
collection.insert(users)    #添加数据
collection.save(users)      #添加数据