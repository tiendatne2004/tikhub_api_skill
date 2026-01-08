import json

# Load the openapi.json file
with open('D:/tikhub_api_skill/openapi.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

paths = data.get('paths', {})

print("=== Sample API Endpoints ===\n")
count = 0
for path, methods in list(paths.items())[:40]:
    for method, details in methods.items():
        tags = details.get('tags', [''])
        summary = details.get('summary', '')[:80]
        operation_id = details.get('operationId', '')
        print(f"{method.upper():6} {path[:55]:55} | {tags[0]:35}")
        print(f"       └─ {summary}")
        count += 1
        if count >= 30:
            break
    if count >= 30:
        break

print("\n\n=== API Categories by Tag ===\n")
tag_counts = {}
for path, methods in paths.items():
    for method, details in methods.items():
        for tag in details.get('tags', []):
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

for tag, count in sorted(tag_counts.items()):
    print(f"{count:4d} endpoints | {tag}")

print(f"\nTotal: {sum(tag_counts.values())} endpoints")
