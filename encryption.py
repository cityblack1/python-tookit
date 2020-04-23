# -*- coding: utf-8 -*-


def simple_encrypt_integer(n):
    salt = 20180126 + 20191201
    n_salted = n + salt
    s_salted = '%.10d' % n_salted
    s_salted = '%s%s%s' % (s_salted[0:6], s_salted[6:8][::-1], s_salted[8:10])
    s_salted = s_salted[::-1]
    s_salted = '%s%s%s' % (s_salted[0:6], s_salted[6:8][::-1], s_salted[8:10])
    return s_salted


def simple_decrypt_integer(s_salted):
    s_salted = '%s%s%s' % (s_salted[0:6], s_salted[6:8][::-1], s_salted[8:10])
    s_salted = s_salted[::-1]
    s_salted = '%s%s%s' % (s_salted[0:6], s_salted[6:8][::-1], s_salted[8:10])
    n_salted = int(s_salted, 10)
    salt = 20180126 + 20191201
    n = n_salted - salt
    return n
