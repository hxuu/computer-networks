import json

def parse_gns3_json(json_file_path):
    """
    Parses a GNS3 JSON schema file to extract network topology and SVG information.

    Args:
        json_file_path (str): The path to the GNS3 JSON file.

    Returns:
        dict: A dictionary containing the parsed data, with keys like:
              - 'project_info':  Project-level information (name, version, etc.).
              - 'nodes':         List of network nodes with their properties.
              - 'links':         List of connections between nodes.
              - 'drawings':      List of drawing elements (SVGs, text, etc.).
    """

    with open(json_file_path, 'r') as f:
        data = json.load(f)

    parsed_data = {
        'project_info': {
            'name': data.get('name'),
            'version': data.get('version'),
            'project_id': data.get('project_id'),
            # Add other relevant project info as needed
        },
        'nodes': data.get('topology', {}).get('nodes', []),
        'links': data.get('topology', {}).get('links', []),
        'drawings': data.get('topology', {}).get('drawings', [])
    }

    return parsed_data


# Example Usage (assuming the json file is in the same directory):
json_file = "mpls.gns3"  # Replace with the actual path to your JSON file
parsed_data = parse_gns3_json(json_file)

# Now you can access the parsed data:
print("Project Name:", parsed_data['project_info']['name'])
print("Number of Nodes:", len(parsed_data['nodes']))
print("Number of Links:", len(parsed_data['links']))
print("Number of Drawings:", len(parsed_data['drawings']))

# Example: Print the SVG of the first drawing element
if parsed_data['drawings']:
    print("\nFirst Drawing SVG:", parsed_data['drawings'][0]['svg'])

# Example:  Iterate through nodes and print names
print("\nNode Names:")
for node in parsed_data['nodes']:
    print(node['name'])

#Example: Iterate through links and print node connections
print("\nLinks:")
for link in parsed_data['links']:
  node1_name = ""
  node2_name = ""
  for node in parsed_data['nodes']:
    if node['node_id'] == link['nodes'][0]['node_id']:
      node1_name = node['name']
    if node['node_id'] == link['nodes'][1]['node_id']:
      node2_name = node['name']
  print(f"Link between {node1_name} and {node2_name}")
