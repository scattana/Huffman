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
	print('\n\n\t' + "USAGE: python huff.py [OPTIONS]")
	print('\t' + ''.join('=' for i in range(90)))
	print("\t{: <20} {: <40}".format("-h", "Display usage instructions"))
	print("\t{: <20} {: <40}".format("-c [file]", "Compress/encode usage mode (-c or -d is required)"))
	print("\t{: <20} {: <40}".format("-d [file]", "Decompress/decode usage mode (-c or -d is required)"))
	print("\t{: <20} {: <40}".format("-g", "Use global encoding (default). Specify -o to use optimized encoding"))
	print("\t{: <20} {: <40}".format("-o", "Optimize compression with file-specific character encoding"))
	print("\t{: <20} {: <40}".format("-e [encoding]", "Specify input text file encoding. Default is utf-8"))
	print("\t{: <20} {: <40}".format("-v", "Verbose program output"))
	print('\n')
	print("\tThanks for using the Huffman text compressor! We currently support the following character encodings:")
	with open("supported_encoding_types.txt", "r") as f:
		print('\n'.join(['\t>> ' + line for line in f.readlines()]))
	print()


# main execution
def main():
	# read command line arguments
	if len(sys.argv) < 2 or (len(sys.argv) >= 2 and '-h' in sys.argv):
		display_usage()

# main function handler
if __name__ == "__main__":
	main()
