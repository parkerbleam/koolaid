#!/usr/bin/python

################# IMPORTS #####################
import sys, getopt

################# FUNCTIONS ###################
def getMACDict(DICT_FILE):
        with open(DICT_FILE, 'r') as df:
            df_lines = df.readlines()

        # Create dictionary of MAC Addresses to People
        mac_to_person = [(x.rstrip().split(')')[1], x.lstrip('(').split(')')[0]) for x in df_lines]
        mac_dict = dict(mac_to_person)
        return mac_dict


def getScrapedMACs(SCRAPED_FILE):
        # Get the most recent list of scraped MAC Addresses
        with open(SCRAPED_FILE, 'r') as sf:
                sf_lines = sf.readlines()

        scraped_macs = [x.split(' ')[2] for x in sf_lines][:-1]
        return scraped_macs

################## MAIN RUN ###################
def main(argv):

        try:
                opts, args = getopt.getopt(argv, "hd:s:", ["dictfile=","scrapedfile="])
        except getopt.GetoptError:
                print("file-reader.py -d <dictfile> -s <scrapedfile>")
                sys.exit(2)

        for opt, arg in opts:
                if opt =='-h':
                        print("file-reader.py -d <dictfile> -s <scrapedfile>")
                        sys.exit()
                elif opt in ("-d", "--dictfile"):
                        DICT_FILE = arg
                elif opt in ("-s", "--scrapedfile"):
                        SCRAPED_FILE = arg
        print("DICT_FILE is: ", DICT_FILE)
        print("SCRAPED_FILE is: ", SCRAPED_FILE)
                
        #DICT_FILE = '/Users/parker.bleam/koolaid/txt/known-MAC-addresses.txt'
        #SCRAPED_FILE = '/Users/parker.bleam/koolaid/txt/MAC-scrape.txt'

        mac_dict = getMACDict(DICT_FILE)
        scraped_macs = getScrapedMACs(SCRAPED_FILE)

        present_macs = [mac_dict[x] for x in scraped_macs if x in mac_dict.keys()]

        if present_macs:
                print(present_macs)
        else:
                print("No one's home")

if __name__ == "__main__":
        main(sys.argv[1:])
