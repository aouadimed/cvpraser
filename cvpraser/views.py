from django.http import HttpResponse
from pyresparser import ResumeParser
import json

def say_hello(request):
    # Provide the path to your resume file
    resume_file_path = 'C:\\Users\\21692\\Desktop\\124-modele-cv-canadien.docx'

    # Parse the resume
    data = ResumeParser(resume_file_path).get_extracted_data()
    print(data)
    # Convert the extracted data to JSON format
    json_data = json.dumps(data, indent=4)

    # Set the content type of the HTTP response to application/json
    response = HttpResponse(json_data, content_type='application/json')

    return response
