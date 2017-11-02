#!/bin/bash

function printResult()
{
 if [ $2 -ne 0 ]; then
    echo -e "\033[31m ################ [ $1 install Faild ]\033[0m"
 else
    echo -e "\033[32m ################ [ $1 install Success ] \033[0m"
 fi
}
declare -A dic

cd /opt/commondj2/commondj2_envInstall/
tar zxvf sqlite-3.5.6.tar.gz
cd sqlite-3.5.6
./configure --disable-tcl && make && make install 
dic["sqlite-3.5.6"]=$?
cd ../;rm sqlite-3.5.6 -rf

cd /opt/commondj2/commondj2_envInstall/
tar xvf Python-2.7.9.tar.xz
cd Python-2.7.9
./configure --prefix=/opt/python27 ;make ;make install
dic["Python-2.7.9"]=$?
cd ../;rm Python-2.7.9 -rf

cd /opt/commondj2/commondj2_envInstall/
tar zxvf setuptools-0.6c11.tar.gz
cd setuptools-0.6c11
/opt/python27/bin/python setup.py install
dic["setuptools-0.6c11"]=$?
cd ../;rm setuptools-0.6c11 -rf

cd /opt/commondj2/commondj2_envInstall/
tar zxvf Django-1.9.5.tar.gz
cd Django-1.9.5
/opt/python27/bin/python setup.py install
dic["Django-1.9.5"]=$?
cd ../;rm Django-1.9.5 -rf



cd /opt/commondj2/commondj2_envInstall/
tar zxvf simplejson-3.5.2.tar.gz
cd simplejson-3.5.2
/opt/python27/bin/python setup.py install
dic["simplejson-3.5.2"]=$?
cd ../;rm simplejson-3.5.2 -rf

cd /opt/commondj2/commondj2_envInstall/
tar zxvf requests-2.13.0.tar.gz
cd requests-2.13.0
/opt/python27/bin/python setup.py install
dic["requests-2.13.0"]=$?
cd ../;rm requests-2.13.0 -rf

cd /opt/commondj2/commondj2_envInstall/
unzip pytz-2017.3.zip
cd pytz-2017.3
/opt/python27/bin/python setup.py install
dic["pytz-2017.3"]=$?
cd ../;rm pytz-2017.3 -rf

for key in $(echo ${!dic[*]})
do
        #echo "$key : ${dic[$key]}"
        printResult $key ${dic[$key]}
done
