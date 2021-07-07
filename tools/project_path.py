# -*- encoding:utf-8 -*-

import os
import time
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_html = now + '.html'
log_txt = now + '.txt'
#根路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
#生成HTML报告路径
test_report_path = os.path.join(project_path,'test_result','html_report',''+report_html)
#cast路径
test_case_path = os.path.join(project_path,'testFile','data.xlsx')
#配置日志文件路径
test_logger_path= os.path.join(project_path,'test_result','log',''+ log_txt)
#配置文件路径
case_config_path = os.path.join(project_path,'conf','case.config')

print project_path