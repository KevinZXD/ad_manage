import time

from django.conf import settings
from elasticsearch import Elasticsearch


class ESHelper:
    def __init__(self, **kwargs):
        """
        self.start = "2019-10-17" or "2019-10-17 10:10:10"
        example: ESHelper()
        """
        self.es = Elasticsearch([{'host': settings.ES_ADDR, 'port': settings.ES_PORT, "timeout": 360000}],
                                http_auth=(str(settings.ELK_USERNAME), str(settings.ELK_PWD)))
        self.query_str = kwargs.get('query_str', '')
        self.query_body = kwargs.get('query_body', '')
        self.area = kwargs.get('area', '')
        self.index = kwargs.get('index', 'py-operator-log')
        self.type = kwargs.get('type', 'doc')
        self.other_condition = kwargs.get('other_condition', dict())
        self.start = kwargs.get('start', '')
        self.end = kwargs.get('end', '')
        self.size = kwargs.get('size', 0)
        self.search_dict = dict()

    # 设置查询时间范围
    def set_time_ranges(self) -> str:
        if not any([self.start, self.end]):
            return ''
        strat_time = int(time.mktime(time.strptime(self.format_time(self.start), '%Y-%m-%d %H:%M:%S')) * 1000)
        end_time = int(time.mktime(time.strptime(self.format_time(self.end, 'end'), '%Y-%m-%d %H:%M:%S')) * 1000)
        return self.query_str + 'timestamp:[%s TO %s]' % (strat_time, end_time)

    @staticmethod
    def format_time(time_str: str, time_type: str = 'start'):
        if len(time_str.strip()) > 10:
            return time_str
        suffix = ' 00:00:00' if time_type == 'start' else ' 23:59:59'
        return time_str + suffix

    # 查询ES
    def search(self):
        self.set_time_ranges()
        self.set_other_condition()
        if not self.index:
            return None
        if self.query_str.strip():
            self.search_dict['q'] = self.query_str
        if self.query_body:
            self.search_dict['body'] = self.query_body
        self.search_dict['size'] = self.size
        search_result = self.es.search(index=self.index, doc_type=self.type, **self.search_dict)
        if search_result:
            return search_result
        return None

    # 设置查询条件
    def set_other_condition(self):
        other_query_str = ''
        for key, value in self.other_condition.items():
            other_query_str += 'and ' + key + f': {value} '
        if not self.query_str:
            other_query_str = other_query_str[3:].strip()
        self.query_str += ' ' + other_query_str
