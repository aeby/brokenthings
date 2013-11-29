# -*- coding: utf-8 -*-
# Copyright (c) Reto Aebersold.
# See LICENSE for details.


def first_value(value, default='Undefined'):
    return value[0] if len(value) else default