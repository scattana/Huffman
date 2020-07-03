# ---------------------------------------------------------------------------
# huff.py
# 
# A Python implementation of a text compression utility
# 	that employs the Huffman Encoding algorithm
# 
# Supports compression and decompression. For usage and 
#	instructions, run "huff.py --help" or "huff.py -h"
#
# Seth Cattanach, scattanach1@gmail.com
# LAST UPDATED: 25 June 2020
# ---------------------------------------------------------------------------

# import statements
import sys
import os


# ---------------------------------------------------------------------------
# "encode" function employs the Huffman Encoding algorithm to compress
#	a text file. File location & permissions should be validated before
#	file is passed to this function. 
# 
#	Returns: TODO
# ---------------------------------------------------------------------------
def encode(f, custom=False):
	return True		# TODO

# display_usage function displays usage instructions for command-line use
def display_usage():
	print('\n\t' + "USAGE: python huff.py [OPTIONS]")
	print('\t' + ''.join('=' for i in range(90)))
	print("\t{: <20} {: <40}".format("-h", "Display usage instructions"))
	print("\t{: <20} {: <40}".format("-c [file]", "Compress/encode usage mode (-c or -d is required)"))
	print("\t{: <20} {: <40}".format("-d [file]", "Decompress/decode usage mode (-c or -d is required)"))
	print("\t{: <20} {: <40}".format("-g", "Use global encoding (default). Specify -o to use optimized encoding"))
	print("\t{: <20} {: <40}".format("-o", "Optimize compression with file-specific character encoding"))
	print("\t{: <20} {: <40}".format("-e [encoding]", "Specify input text file encoding. Default is utf-8"))
	print("\t{: <20} {: <40}".format("-v", "Verbose program output"))
	print('\n')
	print("\tThanks for using the Huffman text compressor!\n\tWe currently support the following character encodings:")
	print('\t' + ''.join('=' for i in range(60)))
	with open("supported_encoding_types.txt", "r") as f:
		print('\n'.join(['\t>> ' + line for line in f.readlines()]))
	print()


# main execution
def main():
	# initialize default program parameters
	input_encoding = "utf-8"
	optimize = False
	verbose = False



	# read command line arguments
	if len(sys.argv) < 2 or (len(sys.argv) >= 2 and '-h' in sys.argv):
		display_usage()
		exit(1)
	if '-c' not in sys.argv and '-d' not in sys.argv:
		print("\n\t!! USAGE ERROR: please specify mode (compression or decompression)")
		display_usage()
		exit(1)
	if '-o' in sys.argv:
		optimize = True
	if '-v' in sys.argv:
		verbose = True

	# loop through remaining options, skipping binary flags, and set parameters or display errors appropriately
	for i in range(len(sys.argv)):
		if sys.argv[i] in ['-o', '-v', '-g'] or sys.argv[i][0] != '-':
			continue
		if sys.argv[i] == '-c':
			if i+1 >= len(sys.argv):
				print("\n\t!! USAGE ERROR: please provide a text file for compression")
				display_usage()
				exit(1)
			elif sys.argv[i+1][0] == '-':
				print("\n\t!! USAGE ERROR: please provide a text file for compression")
				display_usage()
				exit(1)
			else:
				input_file = sys.argv[i+1]
				mode = "c"
		if sys.argv[i] == '-d':
			if i+1 >= len(sys.argv):
				print("\n\t!! USAGE ERROR: please provide a text file for decompression")
				display_usage()
				exit(1)
			elif sys.argv[i+1][0] == '-':
				print("\n\t!! USAGE ERROR: please provide a text file for decompression")
				display_usage()
				exit(1)
			else:
				input_file = sys.argv[i+1]
				mode = "d"
		if sys.argv[i] == '-e':
			if i+1 >= len(sys.argv):
				print("\n\t!! USAGE ERROR: -e flag specified, but no encoding provided")
				display_usage()
				exit(1)
			elif sys.argv[i+1][0] == '-':
				print("\n\t!! USAGE ERROR: -e flag specified, but no encoding provided")
				display_usage()
				exit(1)
			elif sys.argv[i+1] not in [item.strip() for item in open("supported_encoding_types.txt", "r").readlines()]:
				print("\n\t!! USAGE ERROR: specified encoding is not currently supported")
				display_usage()
				exit(1)
			else:
				input_encoding = sys.argv[i+1]


	# debug print program parameters
	print("usage params:")
	print("encoding: " + input_encoding)
	print("optimize:", optimize)
	print("verbose:", verbose)
	print("file: " + input_file)


# main function handler
if __name__ == "__main__":
	main()
