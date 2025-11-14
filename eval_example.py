from pogema_toolbox.evaluator import evaluation
from pogema import BatchAStarAgent


from pathlib import Path

import yaml

from pogema_toolbox.create_env import create_env_base, Environment
from pogema_toolbox.registry import ToolboxRegistry

PROJECT_NAME = 'pogema-toolbox'
BASE_PATH = Path('config_examples')


def main():
    ToolboxRegistry.setup_logger(level='INFO')
    ToolboxRegistry.register_env('Pogema-v0', create_env_base, Environment)
    ToolboxRegistry.register_algorithm('A*', BatchAStarAgent)

    folder_names = [
        'logo',
    ]

    for folder in folder_names:
        config_path = BASE_PATH / folder / f"{Path(folder).name}.yaml"
        eval_dir = BASE_PATH / folder

        ToolboxRegistry.info(f'Starting: {folder}')

        with open(config_path) as f:
            evaluation_config = yaml.safe_load(f)

        evaluation(evaluation_config, eval_dir=eval_dir)



if __name__ == '__main__':
    main()
