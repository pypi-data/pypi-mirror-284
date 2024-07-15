# -*- coding: utf-8 -*-
import os
import requests
import requests.auth
from typing import List
from scrapy.commands import ScrapyCommand


class ReportCommand(ScrapyCommand):

    def short_desc(self) -> str:
        return "report all spider by api"

    def callback(self, spider_name_list: List[str]):
        settings = self.crawler_process.settings
        api: str =  os.environ.get("REPORT_API") or settings.get('REPORT_API')
        user: str = os.environ.get("REPORT_USER") or settings.get('REPORT_USER')
        passwd: str = os.environ.get("REPORT_PASSWD") or settings.get('REPORT_PASSWD')

        DRONE_TAG: str = os.environ['DRONE_TAG']
        CMS_IMAGE: str = os.environ['CMS_IMAGE']
        DRONE_GIT_SSH_URL = os.environ['DRONE_GIT_SSH_URL']
        data = {
            "spider_name_list": spider_name_list,
            "git_ssh_url": DRONE_GIT_SSH_URL,
            "git_tag": DRONE_TAG,
            "image": CMS_IMAGE,
            "status": True
        }
        print(f"[*] url {api}")
        print(f"[*] json {str(data)}")
        print(f"[*] auth {user} {passwd}")
        with requests.post(
            url=api,
            json=data,
            auth=requests.auth.HTTPBasicAuth(user, passwd)
        ) as response:
            print(f"response.text: {response.text}")
            print(f"response.status_code: {response.status_code}")

    def run(self, args, opts) -> None:
        spider_name_list = []
        for s in sorted(self.crawler_process.spider_loader.list()):
            spider_name_list.append(s)

        for _ in range(3):
            try:
                self.callback(spider_name_list)
            except Exception as e:
                print(f"call error {str(e)}")
            else:
                break
