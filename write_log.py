def write_log (log_text):

	log = open ('log.txt','a')
	log.write (log_text + '\n')
	log.close()