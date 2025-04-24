import os
from flask import Blueprint, request, send_from_directory, abort, render_template_string, render_template

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

@upload_bp.route("/view")
def view_file():
    # if not filename.endswith(".gns3"):
    #     abort(404)

    # This route is static for now (only serves the generated png file from drawthe.net website)
    # Instead of reading the file, just render a template
    return render_template("topology_view.html", image_path="assets/demo.png")

