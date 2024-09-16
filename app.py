from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv
import logging
from fpdf import FPDF  # For PDF generation
import tempfile
import shutil

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Enable CORS for specific domains
CORS(app, resources={r"/generate-letter": {"origins": "shopify page address"}})

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    logger.error('OPENAI_API_KEY is not set in the environment variables.')
else:
    logger.info(f"Loaded API Key: {api_key}")

# Set OpenAI API key from the .env file
openai.api_key = api_key

# Function to generate the love letter
def generate_love_letter(recipient, tone, characteristics, moments, sender):
    prompt = f"Write a love letter in German for {recipient}. Mention these characteristics: {characteristics}, and the love letter should be written in a {tone} tone. Describe these special moments: {moments} and at the end of the letter, the sender's name should appear as a signature: {sender}."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative love letter writer who writes in German"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        logger.error(f"Error generating letter: {e}")
        raise

# Function to save the letter to a PDF
def save_as_pdf(letter, recipient, sender):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, letter)
    
    pdf_file_path = os.path.join(tempfile.gettempdir(), f"love_letter_{recipient}_{sender}.pdf")
    pdf.output(pdf_file_path)
    return pdf_file_path

# API endpoint to handle form data and return the generated letter
@app.route('/generate-letter', methods=['POST'])
def generate_letter():
    try:
        data = request.get_json()
        recipient = data.get('recipient')
        tone = data.get('tone')
        characteristics = data.get('characteristics')
        moments = data.get('moments')
        sender = data.get('sender')

        if not all([recipient, tone, characteristics, moments, sender]):
            return jsonify({'error': 'Missing required fields'}), 400

        letter = generate_love_letter(recipient, tone, characteristics, moments, sender)
        
        # Save the letter to a PDF
        pdf_path = save_as_pdf(letter, recipient, sender)

        # Save letter as a preview for front-end live preview
        return jsonify({'letter': letter, 'pdf_path': pdf_path}), 200
    except Exception as e:
        logger.error(f"API endpoint error: {e}")
        return jsonify({'error': 'An error occurred while generating the letter'}), 500


'''# API endpoint to download the generated PDF
@app.route('/download-pdf', methods=['GET'])
def download_pdf():
    try:
        pdf_path = request.args.get('pdf_path')
        if not pdf_path or not os.path.exists(pdf_path):
            return jsonify({'error': 'File not found'}), 404
        
        return send_file(pdf_path, as_attachment=True, download_name=os.path.basename(pdf_path))
    except Exception as e:
        logger.error(f"Error downloading PDF: {e}")
        return jsonify({'error': 'An error occurred during file download'}), 500'''

# Route to test the API and its flow
@app.route('/test', methods=['GET'])
def test_workflow():
    return jsonify({
        'message': 'API is live, and the workflow is functional.',
        'status': 'OK'
    }), 200

@app.route('/')
def home():
    return "Love Letter Generator API is running!"

'''# Clean up temporary files to prevent space overflow
@app.route('/cleanup-temp', methods=['POST'])
def cleanup_temp_files():
    try:
        temp_dir = tempfile.gettempdir()
        shutil.rmtree(temp_dir, ignore_errors=True)
        return jsonify({'message': 'Temporary files cleaned up'}), 200
    except Exception as e:
        logger.error(f"Error cleaning up temporary files: {e}")
        return jsonify({'error': 'An error occurred during cleanup'}), 500'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
