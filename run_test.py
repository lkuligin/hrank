#!/Users/lkuligin/anaconda2/bin/python
# coding: utf8

import argparse
import os
import unittest
import subprocess

TEST_RELPATH = './tests/'


def execute_test(filename, testname, expected):
  cmd = "cat {0} | python {1}".format(testname, filename)
  p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize = 1, stderr=subprocess.PIPE, shell = True)
  res = ''
  with p.stdout:
    for line in iter(p.stdout.readline, b''):
        res = ''.join([res, line.strip()])
  p.wait() 
  output = ''
  if res  == expected:
    output = "OK"
  else:
    output = "ERROR: {1} instead of {0}".format(expected, res)
  print ': '.join((output, testname))
    
def parse_args():
  parser = argparse.ArgumentParser(description='Run tests for /.../xxx.py. Tests should be in /.../test folder')
  parser.add_argument('filename', nargs = 1, help='path to program to be tested')
  parser.add_argument('-t', nargs = 1, help='name of the test file to be tested')
  parser.add_argument('-e', nargs = 1, help='expected value')
  args = parser.parse_args()
  filename = os.path.abspath(args.filename[0])
  testname = None
  if args.t:
    testname = os.path.abspath(args.t[0])
  expected = None
  if args.e:
    expected = args.e[0]
  return filename, testname, expected

def get_ans_filename(testname):
  return '.'.join((os.path.splitext(testname)[0],'ans'))

def get_ans_fromfile(testname):
  res = None
  ansname = get_ans_filename(testname)
  with open(ansname, 'r') as f:
    res = f.readline()
  return res

def get_test_list(filename):
  testdir = os.path.normpath(os.path.join(os.path.dirname(filename), TEST_RELPATH))
  testcases = {}
  for file in os.listdir(testdir):
    if file.endswith('.tst'):
        testcase = os.path.abspath(os.path.join(testdir, file))
        testcases[testcase] = get_ans_fromfile(testcase)
  return testcases

def main():
  filename, testname, expected = parse_args()
  filedir = os.path.dirname(filename)
  testcases = {}
  if testname:
    testcases[testname] = get_ans_fromfile(testname)
  else:
    testcases = get_test_list(filename)
  for case, ans in testcases.iteritems():
    execute_test(filename, case, ans)


if __name__ == "__main__":
  main()
  