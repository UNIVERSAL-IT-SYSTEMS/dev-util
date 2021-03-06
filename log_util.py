# Copyright (c) 2012 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Logging via CherryPy."""

import re

import cherrypy


class Loggable(object):
  """Provides a log method, with automatic log tag generation."""
  _CAMELCASE_RE = re.compile('(?<=.)([A-Z])')

  def _Log(self, message, *args):
    return LogWithTag(
        self._CAMELCASE_RE.sub(r'_\1', self.__class__.__name__).upper(),
        message, *args)


def LogWithTag(tag, message, *args):
  # CherryPy log doesn't seem to take any optional args, so we just handle
  # args by formatting them into message.
  return cherrypy.log(message % args, context=tag)
