report_filename = "report.html"

# After generating the report, copy it to a directory where it can be uploaded as an artifact
import shutil

shutil.copy(report_filename, "pr/reports")
