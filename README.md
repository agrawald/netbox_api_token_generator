=====
netbox-api-token-generator
=====
A Django Netbox plugin to expose API token generation API using basic authorization header

This Django Netbox plugin will expose a REST API 

> `GET /api/plugins/token/token`

with following required header parameters

- `Authorization: Basic <base64>` : The `Authorization` header will be base64 of `username:password` string
- `Z-Expires: yyyy-MM-dd`: The `X-Expires` is use to provide expiry for the token


## Installation and configuration
-----------

This instruction only describes how to install this plugin into [Docker-compose](https://github.com/netbox-community/netbox-docker) instance of NetBox.
>General installation steps and considerations follow the [official guidelines](https://netbox.readthedocs.io/en/stable/plugins/).
>The plugin is available as a Python package from [PyPi](https://pypi.org/project/netbox-api-token-generator/) or from [GitHub](https://github.com/agrawald/netbox-api-token-generator).

### 0. Pull NetBox docker-compose version from GitHub

```shell
mkdir ~/netbox && cd "$_"
git clone https://github.com/netbox-community/netbox-docker
```

### 1. Create new docker container based on latest netbox image

```shell
cd ~/netbox
git clone https://github.com/agrawald/netbox-api-token-generator
cd netbox-api-token-generator
sudo docker build -t netbox-myplugins .
```

>What's in the Dockerfile:
>
>```dockerfile
>FROM netboxcommunity/netbox:latest
>COPY ./netbox_api_token_generator /opt/netbox/netbox/netbox_api_token_generator
>```

### 2. Change **netbox** service in docker-compose.yml (do not delete, just add new lines and change image name)

```dockerfile
version: '3.4'
services:
  netbox: &netbox
    # Change image name to netbox-myplugins (old name is netboxcommunity/netbox:${VERSION-latest})
    image: netbox-myplugins
    ...
    ports:
    - 8080:8080
```

### 3. Update the *PLUGINS* parameter in the global Netbox **configuration.py** config file in *netbox-docker/configuration* directory

```python
PLUGINS = [
    "netbox_api_token_generator"
]
```

### 4. Start Docker-compose

```shell
$ cd ~/netbox/netbox-docker/
sudo docker-compose up -d
```

# Usage

You can use either postman or a simple curl as shown below to generate an API token

> curl --request GET 'http://NETBOX_IP:8080/api/plugins/token/token' --header 'Authorization: Basic BASE64' --header 'X-Expires: 2021-12-31'

Response will be a JSON as shown below

> {
>   "token": "adshkjhWJKHSDBCFlajksdhkjhkjahr214kjh234235kjasdkj123dhkj23h423kjk"
> }