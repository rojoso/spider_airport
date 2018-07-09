# -*- conding UTF-8 -*-

import conf_dev

import conf_test
import platform

#configure Multi-confronment

platform_os = platform.system()

config = conf_dev

if platform_od == 'Linux':
	config = conf_test

#path

data_root_path = config.data_root_path

def read(resources_file_path,encode = 'utf-8'):
	file_path = data_root_path + resources_file_path
	outputs = []

	for line in open(file_path,encoding = encode):
		if not line.startwith("//"):
			outputs.append(line.strip('\n').split(',')[-1])

	return outputs

def append(resources_file_path,data,encode = 'utf-8'):
	file_path = data_root_path+resources_file_path
	with open(file_path,'w',encoding = encode) as f:

		f.write(data)


