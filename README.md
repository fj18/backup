## 简单文件备份脚本
### 主要功能：
- 压缩一个文件夹，并加密
- 在备份文件名后加上日期

### 原理：
- 调用[7zip](https://www.7-zip.org/)的压缩命令
- 根据配置文件和当前日期生成不同的命令参数，方便配合系统的定时任务使用

### 使用场景:
- 定时备份某个文件夹
- 定时加密备份后，配合[syncthing](https://syncthing.net/)更安全的同步到其他设备

### 开始使用

#### 运行环境
> Windows操作系统 <br/>
> [python3.9](https://www.python.org/) <br/>
> [7zip](https://www.7-zip.org/) <br/>
> [syncthing](https://syncthing.net/)(可选)<br/>


1. 修改[配置文件](#配置文件说明)`config.ini`
2. 运行 `main.py`
3. (可选) 运行`schedule.py`,添加定时任务
4. (可选) 运行`cancel.py`,取消定时任务
4. (可选) 新建忽略文件或者文件夹的列表ignore.txt
6. (可选) 用[syncthing](https://syncthing.net/)把备份文件同步到其他设备



#### 配置文件说明

> 配置文件中如果有中文（包括中文注释），读取配置文件可能因为编码问题出错

~~~ini
[DEFAULT]
### 要备份的文件夹，末尾带'/'
source=D:/test/data/

### 备份文件存放的文件夹，末尾带'/'
destination=D:/test/backup/

### 备份文件的文件名，最后会被命名为[文件名]_[年]_[月]_[日].7z
fileName=data

[zip7Exe]
### 7zip 安装路径，如果目录有空格，需要用双引号引起来
zip7Exe=C:/"Program Files"/7-Zip/7z.exe

#[optional]
### 密码
#password=123456

### 忽略文件或者文件夹的列表
#ignore=D:/abc/code/ignore.txt

~~~


