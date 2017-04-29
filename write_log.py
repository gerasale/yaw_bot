def write_log (log_text):
	# coding: utf8
	log = open ('log.txt','a')

	log.write (log_text)
	log.write ('\n')
	log.close ()