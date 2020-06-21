# -*- coding: utf-8 -*-
# @Time : 2020/4/6 20:53
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : class_11_01.py
# @Project : xuxiaobingclass
import requests

url = "http://v6-gw.m.163.com/gentie-web/api/v2/products/a2869674571f77b5a0867c3d71db5856/threads/F9HOLR3U05129QAF" \
      "/wordGeng?ibc=newsappandriod "
res_get = requests.get(url)
print("文章详情页结果", res_get)
# print("get请求的状态码",res_get.status_code)
# print("get请求的响应报文json格式",res_get.json())
print("get请求的响应报文text格式", res_get.text)
# print("get请求的响应头",res_get.headers)
print("get请求的请求头", res_get.request.headers)
