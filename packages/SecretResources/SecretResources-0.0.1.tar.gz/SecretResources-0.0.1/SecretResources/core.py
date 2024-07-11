#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import requests


def get_secret_msg(_id, url='http://127.0.0.1:8062/api/secret/'):
    """获取万象平台参数模块、密码库子模块中相关配置信息
    :param _id: 任务ID 
    :param url: 自定义平台接口，
    :return: dict
    """
    url = f"{url}{_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()