# -*- encoding:utf-8 -*-

import os
import time
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_html = now + '.html'

project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

test_report_path = os.path.join(project_path,'test_result','html_report',''+report_html)

print project_path