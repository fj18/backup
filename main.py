import time
import os
import sys
import configparser

def getConf(configPath):
    if(configPath == ''):
        #读取默认配置文件

        #获取当前目录路径
        currentDirectoryPath = os.path.dirname(sys.argv[0])

        #获取当前配置文件路径
        configPath = '/'.join([currentDirectoryPath,"conf.ini"])

    

    #读取配置文件
    config = configparser.ConfigParser()
    config.read(configPath)


    #解析配置文件
    source=config['DEFAULT']['source']
    destination=config['DEFAULT']['destination']
    fileName=config['DEFAULT']['fileName']

    zip7Exe=config['zip7Exe']['zip7Exe']

    password=''
    ignore=''
    if(config.has_section('optional')):
        if(config.has_option('optional','password')):
            password=config['optional']['password']
        if(config.has_option('optional','ignore')):
            ignore=config['optional']['ignore']
    
    return source,destination,fileName,zip7Exe,password,ignore

def backup(source,destination,fileName,zip7Exe,password,ignore):
    # 格式化日期
    date = time.strftime('%Y_%m_%d',time.localtime(time.time()))
    
    #构造压缩文件全名
    backupFilePrefix = '_'.join([fileName,date])
    backupFileSuffix = '.7z'
    backupFileName = destination +  ''.join([backupFilePrefix,backupFileSuffix])
    
    #构造7zip压缩命令
    if(password != ''):
        optional1 = '-p"'+ password +'"' + ' -mhe'
    else:
        optional1 = ''

    if(ignore != ''):
        optional2 = '-xr@'+ignore
    else:
        optional2 = ''

    cmd = ' '.join([zip7Exe,'a',backupFileName,source,optional1,optional2])
    
    #执行7zip命令
    os.system(cmd)


if(__name__ == '__main__'):
    #读取默认配置文件

    #获取当前目录路径
    currentDirectoryPath = os.path.dirname(sys.argv[0])

    #获取当前配置文件路径
    configPath = '/'.join([currentDirectoryPath,"config.ini"])
    # configPath = ''

    source,destination,fileName,zip7Exe,password,ignore = getConf(configPath)
    backup(source,destination,fileName,zip7Exe,password,ignore)

    