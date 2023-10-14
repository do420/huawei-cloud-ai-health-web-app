import json
import requests


def save_api_url(type, url):

    new_data = {type: url}

    config_file = open("./api_urls.json", "r")
    # load json data into a dictionary
    all_config = json.loads(config_file.read())
    # parse into tracked coins
    api_urls = all_config["urls"]
    config_file.close()
    # turn api urls into list
    configs_list = list(api_urls)

    config_file = open("./api_urls.json", "w")
    configs_list.append(new_data)

    # save into all json
    all_config["urls"] = configs_list
    # turn all_config into dictionary über saving
    all_config = dict(all_config)

    # dump json object
    json_object = json.dumps(all_config, indent=4)

    # write config file
    config_file.write(json_object)

    # close the file
    config_file.close()


def get_api_urls():

    config_file = open("./api_urls.json", "r")
    # load json data into a dictionary
    all_config = json.loads(config_file.read())
    # parse into tracked coins
    api_urls = all_config["urls"]
    config_file.close()

    return api_urls


def check_err(a_json):

    try:
        loaded_json = json.loads(a_json)
        predicted = loaded_json['predicted_label']
        return True

    except:
        return False


def get_xauth():

    url = "https://iam.myhuaweicloud.com/v3/auth/tokens?nocatalog=true"

    payload = "{\r\n    \"auth\": {\r\n        \"identity\": {\r\n            \"methods\": [\r\n                \"password\"\r\n            ],\r\n            \"password\": {\r\n                \"user\": {\r\n                    \"domain\": {\r\n                        \"name\": \"<YOUR_MAIN_USERNAME>\"    // CHANGE IT    \r\n                    },\r\n                    \"name\": \"<YOUR_IAM_USER>\",             // IAM user name. CHANEG IT\r\n                    \"password\": \"<YOUR_SUB_USER_PASSWD>\"      // IAM user password.  CHANGE IT\r\n                }\r\n            }\r\n        },\r\n        \"scope\": {\r\n            \"project\": {\r\n                \"name\": \"ap-southeast-1\"               //PROJECT NAME IS BASED ON YOUR CHOICE\r\n            }\r\n        }\r\n    }\r\n}"
    headers = {
        'Content-Type': 'text/plain',
        'Cookie': 'HWWAFSESID=4791a7624d3150f269; HWWAFSESTIME=1697018827053'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(type(response.headers['X-Subject-Token']))

    return response.headers['X-Subject-Token']


# print(get_xauth())
