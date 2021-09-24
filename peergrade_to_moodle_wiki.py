import logging
import configparser
from time import sleep
from tqdm import tqdm

import models

logging.getLogger().setLevel(logging.INFO)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    assignment = models.PeerGradeAssignment(config['assignment']['zipfile'])
    learnit = models.LearnIT(config['lms']['endpoint'], config['lms']['token'])

    for s in tqdm(assignment.submissions):
        logging.info(s)
        learnit.create_page(config['wid'], s)
        sleep(1)
    learnit.create_index_page(config['wid'])
