# 将pfx转换为key和crt文件

    openssl pkcs12 -in $1 -clcerts -nokeys -out out.crt
    openssl pkcs12 -in $1 -nocerts -nodes -out out.rsa