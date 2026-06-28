import json

with open("experiment.json", 'r') as f:
    data = json.load(f)

print(f"Experiment: {data['experiment_id']}")
print(f"Model: {data['model']}")
print(f"Test accuracy: {data['metrics']['test_accuracy']}")
print()

data['status'] = "completed"

with open("experiment_updated.json", "w") as f:
    json.dump(data, f, indent=2, sort_keys=True)

with open("experiment_updated.json", 'r') as f:
    for _ in range(5):
        print(f.readline(), end="")