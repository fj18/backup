import os

deleteSchedule = 'schtasks /delete /tn myBackupTask /f'

#取消定时任务
os.system(deleteSchedule)