from pogema import pogema_v0

from pogema_toolbox.registry import ToolboxRegistry
import shutil
import tempfile
import yaml

from pathlib import Path


def seeded_configs_to_scenarios_converter(env_configs):
    scenarios = {}

    for idx, cfg in enumerate(env_configs):
        env: pogema_v0 = ToolboxRegistry.create_env(env_name=cfg['name'], **cfg)
        env.reset()
        if env.grid_config.on_target == 'restart':
            targets_xy = env.get_lifelong_targets_xy(ignore_borders=True)
        else:
            targets_xy = env.get_targets_xy(ignore_borders=True)
        agents_xy = env.get_agents_xy(ignore_borders=True)
        if hasattr(agents_xy, 'tolist'):
            agents_xy = agents_xy.tolist()
        else:
            agents_xy = [[int(x), int(y)] for x, y in agents_xy]

        if hasattr(targets_xy, 'tolist'):
            targets_xy = targets_xy.tolist()
        elif env.grid_config.on_target == 'restart':
            targets_xy = [[[int(x), int(y)] for x, y in agent_targets] for agent_targets in targets_xy]
        else:
            targets_xy = [[int(x), int(y)] for x, y in targets_xy]

        scenario = {'agents_xy': agents_xy,
                    'targets_xy': targets_xy,
                    'map_name': env.grid_config.map_name,
                    'seed': cfg.get('seed', env.grid_config.seed)}
        scenario_name = f'Scenario-{str(idx).zfill(len(str(len(env_configs))))}'

        scenarios[scenario_name] = scenario

    return scenarios


def scenarios_to_yaml(scenarios):
    class FlowStyleDumper(yaml.Dumper):
        def represent_sequence(self, tag, sequence, flow_style=None):
            if isinstance(sequence, list) and all(isinstance(i, list) for i in sequence):
                flow_style = True  # Use flow style for lists of lists
            return super().represent_sequence(tag, sequence, flow_style)

    yaml_str = yaml.dump(scenarios, Dumper=FlowStyleDumper, default_flow_style=None, width=256)
    return yaml_str
