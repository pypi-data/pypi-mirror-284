# -*- coding: utf-8 -*-
import os
import json
import logging
from typing import Optional
from scrapy.exceptions import UsageError
from scrapy.commands.crawl import Command

logger = logging.getLogger(__name__)


class CrawlWithSettingsCommand(Command):

    def run(self, args, opts):
        if len(args) < 1:
            raise UsageError()
        elif len(args) > 1:
            raise UsageError(
                "running 'scrapy crawl' with more than one spider is not supported"
            )
        spname: str = args[0]

        cms_spider_settings_str: Optional[str] = os.environ.get('CMS_SPIDER_SETTINGS')
        if cms_spider_settings_str:
            cms_spider_settings: dict = json.loads(cms_spider_settings_str) or {}
            self.crawler_process.settings.setdict(cms_spider_settings, priority="cmdline")

        crawl_defer = self.crawler_process.crawl(spname, **opts.spargs)

        if getattr(crawl_defer, "result", None) is not None and issubclass(
            crawl_defer.result.type, Exception
        ):
            self.exitcode = 1
        else:
            self.crawler_process.start()

            if (
                self.crawler_process.bootstrap_failed
                or hasattr(self.crawler_process, "has_exception")
                and self.crawler_process.has_exception
            ):
                self.exitcode = 1
