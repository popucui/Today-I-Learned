'''The config file for Clash will be updated once in a while, yet the clash for linux version is a CUI tool which do not have an option to fetch the config periodically, so here comes this small script. 
It get the clash config from agentNeo website and make some changes for my own usage. The comments will be discarded(not my intention), and this script depends on python3.

Clash binary file can be found at: https://github.com/Dreamacro/clash/releases
'''
import sys
import yaml
import requests

key = 'ScrRetword'
config_file_name = 'config.yaml'
url_prefix = 'https://api.example.com'

with requests.get(f'{url_prefix}/{key}/clash.yml') as r, open (config_file_name, 'w') as new_config_fh:
    if r.status_code != 200:
        sys.exit(f'Somthing wrong when accessing the yml url, code is: {r.status_code}')
    config = yaml.safe_load(r.text)
    ## change the config
    config['allow-lan'] = True
    config['Proxy Group'][0]['type'] = 'url-test'
    config['Proxy Group'][0]['url'] = "http://www.gstatic.com/generate_204"
    config['Proxy Group'][0]['interval'] = 300

    ## save the new config
    yaml.dump(config, new_config_fh, encoding='utf-8', allow_unicode=True, sort_keys=False)
    print(f'New config has been saved in {config_file_name}')
