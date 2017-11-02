# commondj2

## Install

cd commondj2_envInstall
sh install.sh


## Config
commondj2/settings.py

#### allowed hosts
ALLOWED_HOSTS = ['192.168.150.120']

#### Database

default : sqlite

默认使用sqlite 轻量数据库，若数据库并发较大，请修改数据库配置 使用mysql数据库
linux 下需要安装 MySQL-python 即可支持 安装包在操作系统安装包中可以找到
然后打开如下配置就行了


## run Procect

/opt/python27/bin/python manage.py runserver 0.0.0.0:8088


## Django admin

admin/njitv1302


