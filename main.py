from logging import Filter, getLogger, Logger
from logging.config import dictConfig
from pathlib import Path
from yaml import safe_load


def configure_logging() -> None:
    with open('logging.yaml', 'r') as yaml:
        log_cfg: dict = safe_load(yaml.read())

    for key, value in log_cfg.get('handlers').items():
        file_path: str = value.get('filename')
        if not file_path:
            continue
        log_file: Path = Path(file_path)
        log_file.parent.mkdir(exist_ok=True, parents=True)
    dictConfig(log_cfg)
    logger: Logger = getLogger(__name__)
    logger.info(f'logging initialized')


def main() -> None:
    configure_logging()
    log_name: str = 'vehicle'
    logger: Logger = getLogger(log_name)
    veh_filter: Filter = Filter(log_name)
    logger.addFilter(veh_filter)
    logger.info(f'should appear in vehicle.log only')


if __name__ == '__main__':
    main()
