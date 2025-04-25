import os
from flask import Blueprint, request, send_from_directory, abort, render_template_string, render_template
from utils import parse_gns3_yaml

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

    # This route is static for now (only serves the generated png file from drawthe.net website)
    yaml_output = parse_gns3_yaml.parse_gns3_json(os.path.join(UPLOAD_FOLDER, filename))
    file_path = os.path.join(UPLOAD_FOLDER, filename.split('.')[0] + '.yaml')

    print(file_path)
    with open(file_path, 'w') as file:
        file.write(yaml_output)
    print('YAML file written successfully!')

    # Instead of reading the file, just render a template
    image_path = f"assets/{filename.split('.')[0]}.svg"
    with open(os.path.join("static", image_path)) as f:
        svg_content = f.read()
    return render_template("topology_view.html", svg_content=svg_content)

