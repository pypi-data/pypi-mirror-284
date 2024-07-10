# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from .._functions.cookies import set_tab_cookies, set_session_cookies, set_browser_cookies


class BrowserCookiesSetter(object):
    def __init__(self, owner):
        """
        :param owner: Chromium对象
        """
        self._owner = owner

    def __call__(self, cookies):
        """设置一个或多个cookie
        :param cookies: cookies信息
        :return: None
        """
        set_browser_cookies(self._owner, cookies)

    def clear(self):
        """清除cookies"""
        self._owner._run_cdp('Storage.clearCookies')


class CookiesSetter(BrowserCookiesSetter):

    def __call__(self, cookies):
        """设置一个或多个cookie
        :param cookies: cookies信息
        :return: None
        """
        set_tab_cookies(self._owner, cookies)

    def clear(self):
        """清除cookies"""
        self._owner._run_cdp('Network.clearBrowserCookies')

    def remove(self, name, url=None, domain=None, path=None):
        """删除一个cookie
        :param name: cookie的name字段
        :param url: cookie的url字段，可选
        :param domain: cookie的domain字段，可选
        :param path: cookie的path字段，可选
        :return: None
        """
        d = {'name': name}
        if url is not None:
            d['url'] = url
        if domain is not None:
            d['domain'] = domain
        if not url and not domain:
            d['url'] = self._owner.url
            if not d['url'].startswith('http'):
                raise ValueError('需设置domain或url值。如设置url值，需以http开头。')
        if path is not None:
            d['path'] = path
        self._owner._run_cdp('Network.deleteCookies', **d)


class SessionCookiesSetter(object):
    def __init__(self, owner):
        self._owner = owner

    def __call__(self, cookies):
        """设置多个cookie，注意不要传入单个
        :param cookies: cookies信息
        :return: None
        """
        set_session_cookies(self._owner.session, cookies)

    def remove(self, name):
        """删除一个cookie
        :param name: cookie的name字段
        :return: None
        """
        self._owner.session.cookies.set(name, None)

    def clear(self):
        """清除cookies"""
        self._owner.session.cookies.clear()


class MixPageCookiesSetter(CookiesSetter, SessionCookiesSetter):

    def __call__(self, cookies):
        """设置多个cookie，注意不要传入单个
        :param cookies: cookies信息
        :return: None
        """
        if self._owner.mode == 'd' and self._owner._has_driver:
            super().__call__(cookies)
        elif self._owner.mode == 's' and self._owner._has_session:
            super(CookiesSetter, self).__call__(cookies)

    def remove(self, name, url=None, domain=None, path=None):
        """删除一个cookie
        :param name: cookie的name字段
        :param url: cookie的url字段，可选，d模式时才有效
        :param domain: cookie的domain字段，可选，d模式时才有效
        :param path: cookie的path字段，可选，d模式时才有效
        :return: None
        """
        if self._owner.mode == 'd' and self._owner._has_driver:
            super().remove(name, url, domain, path)
        elif self._owner.mode == 's' and self._owner._has_session:
            if url or domain or path:
                raise AttributeError('url、domain、path参数只有d模式下有效。')
            super(CookiesSetter, self).remove(name)

    def clear(self):
        """清除cookies"""
        if self._owner.mode == 'd' and self._owner._has_driver:
            super().clear()
        elif self._owner.mode == 's' and self._owner._has_session:
            super(CookiesSetter, self).clear()
