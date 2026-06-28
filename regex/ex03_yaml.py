import yaml

with open("config.yaml", 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

print(f"Model: {config['model']['name']}")
print(f"Learning rate: {config['training']['learning_rate']}") 

config["training"]["learning_rate"] = 0.01
config["experiment_id"] = "run_007"

with open("config_updated.yaml", 'w', encoding='utf-8') as f:
    yaml.dump(config, f, default_flow_style=False)

with open("config_updated.yaml", "r", encoding="utf-8") as f_check:
    print(f_check.read())   
    