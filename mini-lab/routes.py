import os
from flask import Blueprint, request, send_from_directory, abort, render_template_string

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
    try:
        # Ensure only .gns3 files are served
        if not filename.endswith(".gns3"):
            abort(404)  # Return 404 if not a .gns3 file
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        # Read the file contents and display as text
        with open(filepath, "r") as f:
            file_contents = f.read()

        return render_template_string("""
            <html>
                <body>
                    <h2>Viewing {{ filename }}</h2>
                    <pre>{{ file_contents }}</pre>
                </body>
            </html>
        """, filename=filename, file_contents=file_contents)

    except FileNotFoundError:
        abort(404)  # Return 404 if file does not exist

