import sys
import os


#获得当前目录
currentDirectoryPath = os.path.dirname(sys.argv[0])
backupPyPath = '/'.join([currentDirectoryPath,"main.py"])

#填写python.exe的路径
pythonExePath = 'C:/Python39/python.exe'

#构造定时任务要执行的命令
cmd = pythonExePath + ' ' + backupPyPath


time = '21:30:00'
createSchedule = 'schtasks /create /tn myBackupTask /tr \"' + cmd +'\" /sc DAILY /st ' + time
deleteSchedule = 'schtasks /delete /tn myBackupTask /f'

#创建定时任务
print(createSchedule)
os.system(createSchedule)
