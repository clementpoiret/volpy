import hydra
import requests
from bs4 import BeautifulSoup
from hydra import compose, initialize
from omegaconf import DictConfig

from volpy.login import login
from volpy.volbrain import get_upload_form

initialize(config_path="volpy/conf")
cfg = compose(config_name="config")


@hydra.main(config_path="conf", config_name="config")
def main(cfg: DictConfig):
    content = login(cfg.volbrain.base_url + cfg.volbrain.login, cfg.credentials)

    soup = BeautifulSoup(content, "lxml")
    form = get_upload_form(soup)
