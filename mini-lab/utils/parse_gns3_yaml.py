import json

def parse_gns3_yaml(data):
    nodes = data.get('topology', {}).get('nodes', [])
    # drawings = data.get('topology', {}).get('drawings', [])
    # from pprint import pprint
    # pprint(drawings)
    # exit()
    links = data.get('topology', {}).get('links', [])

    yaml_output = []

    yaml_output.append("diagram:")
    yaml_output.append("  fill: none")
    yaml_output.append("title:")
    yaml_output.append('  text: "Minimalistic Demo"')
    yaml_output.append("  fill: none")
    yaml_output.append("  logoFill: none")
    yaml_output.append("  author: hxuu")
    yaml_output.append("iconsDefaults: &iconsDefaults")
    yaml_output.append("  icon: router")
    yaml_output.append("  iconFamily: cisco")
    yaml_output.append("  fill: none")
    yaml_output.append("icons:")

    node_name_map = {}

    for index, node in enumerate(nodes):
        name = node.get("name")
        node_id = node.get("node_id")
        node_name_map[node_id] = name

        image = node.get("properties", {}).get("image", "")

        if "vEOS" in image:
            gns3_template = "Arista vEOS"
        elif "IOSv" in image or "c2691" in image:
            gns3_template = "Cisco IOSv L3"
        else:
            gns3_template = "Unknown"

        x = (index % 4) * 3  # Spread across 0, 3, 6, 9
        y = (index // 4) * 3  # Next row every 4 devices

        yaml_output.append(
            f"  {name}: {{ <<: *iconsDefaults, gns3_template: \"{gns3_template}\", x: {x}, y: {y} }}"
        )


    yaml_output.append("connections:")

    for link in links:
        node_ends = link.get("nodes", [])
        if len(node_ends) != 2:
            continue
        ep1 = node_ends[0]
        ep2 = node_ends[1]

        n1 = node_name_map.get(ep1.get("node_id"), "unknown")
        n2 = node_name_map.get(ep2.get("node_id"), "unknown")

        p1 = ep1.get("label", {}).get("text", "Gi0/0")
        p2 = ep2.get("label", {}).get("text", "Gi0/0")

        yaml_output.append(f"  - {{ endpoints: [{n1}:{p1}, {n2}:{p2}] }}")

    return "\n".join(yaml_output)


# Example usage
if __name__ == '__main__':
    yaml_output = parse_gns3_yaml('mpls.gns3')
    with open('mpls.yaml', 'w') as file:
        file.write(yaml_output)
    print('YAML file written successfully!')
