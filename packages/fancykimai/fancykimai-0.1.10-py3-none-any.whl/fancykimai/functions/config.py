import os
import json

def get_config(key) -> str:
    config_file = os.path.expanduser(f"~/.config/fancykimai/config.json")
    if os.path.exists(config_file):
        try:
            with open(config_file, "r") as f:
                configuration = json.loads(f.read())
            # Get the selected context
            context = configuration.get("selected_context", "default")
            context_config = next((c for c in configuration["contexts"] if c["name"] == context), None)
            if context_config:
                return context_config.get(key, None)
            else:
                return None
        except KeyError:
            # Create a new config file
            config_dir = os.path.dirname(config_file)
            if not os.path.exists(config_dir):
                os.makedirs(config_dir)
            configuration = {
                "selected_context": "default",
                "contexts": [{"name": "default", key: None}]
            }
            with open(config_file, "w") as f:
                f.write(json.dumps(configuration, indent=4))
            return None
    else:
        return None

def set_config(key: str, value: str, context: str = None, debug=False):
    if debug:
        print(f"Setting {key} to {value}")
    config_file = os.path.expanduser(f"~/.config/fancykimai/config.json")
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            configuration = json.loads(f.read())
        if not context:
            context = configuration.get("selected_context", "default")
        if debug:
            print(f"Selected context: {context}")
        context_config = next((c for c in configuration["contexts"] if c["name"] == context), None)
        if debug:
            print(f"Context config: {context_config}")
        if context_config:
            context_config[key] = value
            if debug:
                print(f"Setting {key} to {value} in context {context}")
        else:
            if debug:
                print(f"Context not found, creating new context")
            configuration["contexts"].append({"name": context, key: value})
        with open(config_file, "w") as f:
            if debug:
                print(f"Writing configuration to {config_file}")
            f.write(json.dumps(configuration, indent=4))
    else:
        if debug:
            print(f"Configuration file not found, creating new configuration")
        config_dir = os.path.dirname(config_file)
        if not os.path.exists(config_dir):
            if debug:
                print(f"Creating directory {config_dir}")
            os.makedirs(config_dir)
        configuration = {
            "selected_context": "default",
            "contexts": [{"name": "default", key: value}]
        }
        if debug:
            print(f"Writing configuration to {config_file}")
        with open(config_file, "w") as f:
            f.write(json.dumps(configuration, indent=4))

def unset_config(key: str, context: str = None):
    config_file = os.path.expanduser(f"~/.config/fancykimai/config.json")
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            configuration = json.loads(f.read())
        if not context:
            context = configuration.get("selected_context", "default")
        context_config = next((c for c in configuration["contexts"] if c["name"] == context), None)
        if context_config:
            context_config.pop(key, None)
            with open(config_file, "w") as f:
                f.write(json.dumps(configuration, indent=4))
        else:
            raise ValueError("Context not found")
    else:
        raise ValueError("Configuration file not found")