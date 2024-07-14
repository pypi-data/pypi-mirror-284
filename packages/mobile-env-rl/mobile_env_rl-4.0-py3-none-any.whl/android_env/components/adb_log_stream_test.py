# coding=utf-8
# Copyright 2021 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for adb_log_stream."""

import subprocess

from absl.testing import absltest
from android_env.components import adb_log_stream
import mock


class FakeAdbSubprocess():

  @property
  def stdout(self):
    return [f'line_{i}' for i in range(100)]

  def kill(self):
    pass


class AdbLogStreamTest(absltest.TestCase):

  @mock.patch.object(subprocess, 'Popen', return_value=FakeAdbSubprocess())
  def test_get_stream_output(self, mock_popen):
    stream = adb_log_stream.AdbLogStream(adb_command_prefix=['foo'])
    stream.set_log_filters(['bar'])
    stream_output = stream.get_stream_output()

    for i, line in enumerate(stream_output):
      self.assertEqual(line, f'line_{i}')

    mock_popen.assert_called_with(
        ['foo', 'logcat', '-v', 'epoch', 'bar', '*:S'],
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE,
        bufsize=1,
        universal_newlines=True)


if __name__ == '__main__':
  absltest.main()
