import logging
import logging.config
from pathlib import Path
from yaml import safe_load


def configure_logging() -> None:
    with open('logging.yaml', 'r') as yaml:
        log_cfg = safe_load(yaml.read())

    for key, value in log_cfg.get('handlers').items():
        file_path = value.get('filename')
        if not file_path:
            continue
        log_file = Path(file_path)
        log_file.parent.mkdir(exist_ok=True, parents=True)
    logging.config.dictConfig(log_cfg)
    logger = logging.getLogger(__name__)
    logger.info(f'logging initialized')


def main():
    configure_logging()
    log_name: str = 'vehicle'
    logger = logging.getLogger(log_name)
    veh_filter: logging.Filter = logging.Filter(log_name)
    logger.addFilter(veh_filter)
    logger.info(f'should appear in vehicle.log only')


if __name__ == '__main__':
    main()