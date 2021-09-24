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

    assignment = models.PeerGradeAssignment(args.zipfile)
    learnit = models.LearnIT(args.wikiid)

    for s in tqdm(assignment.submissions):
        logging.info(s)
        learnit.create_page(config['wid'], s)
        sleep(1)
    learnit.create_index_page(config['wid'])
