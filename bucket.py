#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from functools import wraps
from threading import RLock


class TokenBucket(object):
    """令牌桶算法"""

    def __init__(self, capacity, fill_rate, is_lock=False):
        self._capacity = float(capacity)
        self._tokens = 0
        self._fill_rate = float(fill_rate)
        self._last_time = time.time()
        self._is_lock = is_lock
        self._lock = RLock()

    def _get_cur_tokens(self):
        if self._tokens < self._capacity:
            now = time.time()
            delta = self._fill_rate * (now - self._last_time)
            self._tokens = min(self._capacity, self._tokens + delta)
            self._last_time = now
        return self._tokens

    def get_cur_tokens(self):
        if self._is_lock:
            with self._lock:
                return self._get_cur_tokens()
        else:
            return self._get_cur_tokens()

    def _consume(self, tokens):
        if tokens <= self.get_cur_tokens():
            self._tokens -= tokens
            return True
        return False

    def consume(self, tokens):
        if self._is_lock:
            with self._lock:
                return self._consume(tokens)
        else:
            return self._consume(tokens)


def rate_limit(fill_rate, capacity, cost=1):
    token_bucket = TokenBucket(capacity * cost, fill_rate * cost)

    def outer(func):
        @wraps(func)
        def wrapper(*arg, **kwargs):
            while 1:
                if token_bucket.consume(cost):
                    res = func(*arg, **kwargs)
                    return res
                continue

        return wrapper

    return outer
