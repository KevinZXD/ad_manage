广告管理系统

1. 流量配置系统

负责流量降级开关和相关系统级别配置

2. 用户基础画像编辑查看

用户基础画像对于广告千人前面投放至关重要， 用户基础画像包含年例，区域，性别，地理位置，爱好标签等重要标记

3. 黑名单管理

广告黑名单涉及类别很多，包含流量黑名单，业务黑名单，产品黑名单以及广告主黑名单等等

4. 品牌在投广告位管理

品牌广告是指大品牌广告，广告预算很高，目的在于品牌宣传，需要大规模覆盖传播


环境安装注意事项

第一步
openresty  安装教程（linux）

确保yum周边工具已经安装

yum install yum-utils -y

# 添加仓库

yum-config-manager --add-repo https://openresty.org/package/centos/openresty.repo

# 安装openresty

yum install openresty -y
 
第二步 后台管理系统安装

Yum -y install python3(pip3)

django  redis  mysql


docker-compose up -d 安装依赖的数据库

yum -y install python3-devel（解决uwsgi无法编译问题）


pip3.6  install -r requirements.txt.  pymysql

python3 manage.py runscript scripts.db_migrate.create_const_crw_model

python3 manage.py collectstatic

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver 0.0.0.0:80

python3 manage.py runscript scripts.db_configure.consts_configure_data

第三 问题收集

ERROR: Couldn't connect to Docker daemon at http+docker://localunixsocket - is it running?

If it's at a non-standard location, specify the URL with the DOCKER_HOST environment variable.

 systemctl start docker


plugins/python/uwsgi_python.h:2:20: 致命错误：Python.h：没有那个文件或目录

yum -y install python3-devel 解决冲突






