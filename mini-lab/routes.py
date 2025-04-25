import os
import json
from flask import Blueprint, request, send_from_directory, abort, render_template_string, render_template, redirect, url_for, flash

from utils.parse_gns3_yaml import parse_gns3_yaml
from utils.extract_console_info import extract_console_info

upload_bp = Blueprint("upload_bp", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@upload_bp.route("/upload", methods=["POST"])
def upload():
    file = request.files["gns3file"]

    if file and file.filename.endswith(".gns3"):
        # Save the file with its original name
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Generate an HTML response with an anchor link to view the file
        return render_template_string("""
            <html>
                <body>
                    <h2>File uploaded successfully!</h2>
                    <p>You can view the file by clicking the link below:</p>
                    <a href="{{ url_for('upload_bp.view_file', filename=file.filename) }}">View File</a>
                </body>
            </html>
        """, file=file)

    else:
        return "Invalid file type. Only .gns3 files are allowed.", 400


@upload_bp.route("/view/<filename>")
def view_file(filename):
    if not filename.endswith(".gns3"):
        abort(404)

    file_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(file_path, 'r') as file:
        data = json.load(file)

    yaml_output = parse_gns3_yaml(data)
    yaml_path = os.path.join(UPLOAD_FOLDER, filename.split('.')[0] + '.yaml')
    with open(yaml_path, 'w') as file:
        file.write(yaml_output)

    console_info = extract_console_info(data)

    config_options = ["configure_ip.py", "rip.py", "vpn.py"]

    form_html = '''
    <h2>Configuration Options</h2>
    <form method="POST" action="/apply-config" enctype="multipart/form-data">
        <table>
            <thead>
                <tr>
                    <th>Device</th>
                    <th>Host</th>
                    <th>Port</th>
                    <th>Protocol</th>
                    <th>Select Configuration</th>
                    <th>Upload Config File</th>
                </tr>
            </thead>
            <tbody>
    '''
    for device in console_info:
        form_html += f'''
            <tr>
                <td>{device['name']}</td>
                <td>{device['host']}</td>
                <td>{device['port']}</td>
                <td>{device['type']}</td>
                <td>
                    <select name="{device['name']}:{device['port']}">
                        <option value="testingpurposesonly.py">-- Select --</option>'''
        for option in config_options:
            form_html += f'<option value="{option}">{option}</option>'
        form_html += f'''</select>
                </td>
                <td>
                    <input type="file" name="config_{device['name']}" />
                </td>
            </tr>
        '''
    form_html += '''
            </tbody>
        </table>
        <button type="submit">Apply Configurations</button>
    </form>
    '''

    image_path = f"assets/{filename.split('.')[0]}.svg"
    with open(os.path.join("static", image_path)) as f:
        svg_content = f.read()

    return render_template("topology_view.html", svg_content=svg_content, form_html=form_html)


@upload_bp.route("/apply-config", methods=["POST"])
def apply_config():
    for config_name, script in request.form.items():
        print(f"{config_name} = {script}")
    # for file_devicename, blob in request.files.items():
    #     content = blob.read().decode("utf-8") # works for text based content only
    #     print(f"{file_devicename} = {content}")
    #     break

    for (hostname_port, script), (_, blob) in zip(request.form.items(), request.files.items()):
        config_data = blob.read().decode("utf-8") # works for text based content only
        splt = hostname_port.split(':')
        hostname, port = splt[0], splt[1]

        # Pass those info to the automation tool with the automation script name
        # TODO: ensure the script name is safe (not for now)
        try:
            config_obj = json.loads(config_data)  # config must be JSON
        except json.JSONDecodeError:
            return "Invalid JSON", 400

        if script == "configure_ip":
            run_configure_ip(port, config_obj)

        elif script == "rip":
            # expect a list of router configs
            run_rip(config_obj)

        elif script == "vpn":
            # expect dict with 'acl' and 'peers'
            run_vpn(config_obj['acl'], config_obj['peers'])

        else:
            return f"Unknown script: {script}", 400

        break
    return "Configuration applied.", 200
