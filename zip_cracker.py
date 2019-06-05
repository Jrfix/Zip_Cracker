import zipfile


count=1

zip_filename = raw_input("zip path: ")
dictionary = raw_input("wordlist path: ")

def main():
	password = None
	zip_file = zipfile.ZipFile(zip_filename)
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			try:
				zip_file.extractall(pwd=password)

				data = zf.namelist()[0]

				data_size = zf.getinfo(data).file_size
				
				print('''######\n[+] Password found! ~ %s\n ~%s\n ~%s\n######''' % (password.decode('utf8'), data, data_size))
				    
				break

			except:
				number = count
			    	print('[%s] [-] Password failed! - %s' % (number,password.decode('utf8')))
			    	count += 1
				pass
	

if __name__ == '__main__':

	main()
