#regular packages
import logging
import configparser
import argparse
from time import sleep
from tqdm import tqdm
import models



logging.getLogger().setLevel(logging.INFO)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    argparser = argparse.ArgumentParser()
    argparser.add_argument('zipfile', help="ZIP file of submissions.")
    argparser.add_argument('wikiid', help="Wiki ID on Moodle.")
    args = argparser.parse_args()
    print(args.wikiid)

    assignment = models.PeerGradeAssignment(args.zipfile)
    learnit = models.LearnIT(config['lms']['endpoint'] ,config['lms']['token'])

    for s in tqdm(assignment.submissions[:5]): 
        logging.info(s)
        learnit.create_page(args.wikiid, s)
        sleep(1)
    learnit.create_index_page(args.wikiid)
