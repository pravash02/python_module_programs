# NOTE:
# run this py file with arguments
# you can add arguments in the Edit Configuration option for this .py file.
# for example -
# -a upload -s file_system

import optparse
import json

dict_config = {}
config_file_path = "config.json"

with open(config_file_path) as f:
  data = json.load(f)
  dict_config.update(data)

parser = optparse.OptionParser(usage="usage: %prog [option values]", version="%prog 0.1")
parser.add_option('-a', '--action', help='[upload,download]', dest='action')
parser.add_option('-s', '--system', help='[aws|file_system]', dest='system')
parser.add_option('-f', '--filename', help='[filename]', dest='filename')
parser.add_option('-k', '--key', help='[key]', dest='key')
parser.add_option('-p', '--path', help='[hdfs_path]', dest='hdfs_path',
                  default=dict_config['default_hdfs_path'])
parser.add_option('-o', '--operation', help='[s3,hdfs,both]', dest='operation')
parser.add_option('-d', '--delete_flag', help='[Y, N]', dest='delete_flag', default='N')

(opts, args) = parser.parse_args()
print(opts)

if opts.action is None:
    action = None
else:
    action = opts.action

if opts.system is None:
    system = None
else:
    system = opts.system

if action in ['upload', 'download'] and system in ['file_system']:
    print('Y')
