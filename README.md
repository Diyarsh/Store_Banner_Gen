# Printify Prompt Engineer Test Task

### Task Prompt

Create a concise and intriguing store banner text using the following inputs: Store Name: [STORE_NAME] Store Concept: [STORE_CONCEPT]. The banner text should be a single phrase no longer than 50 characters. It must be original and must not include any copyright-infringing elements. The output should be only the phrase, with no preface or additional text.

### Explanation

#### Introduction

The task involves generating a concise and original banner text for a new merchant setting up their first store. The goal is to create a banner text that is no longer than 50 characters, is free of copyright-infringing elements, and consists of a single phrase without any preface or additional text.

#### Prompt Details

The prompt is designed with the following components:

- **Store Name**: Placeholder for the store's name.
- **Store Concept**: Placeholder for a brief description of the store.
- **Instructions**: Clear guidelines on the length and originality of the output, emphasizing that the output should be a single phrase with no preface or additional text.

#### How the Prompt Meets Requirements

- **Length Constraint**: The prompt specifies that the banner text should be no longer than 50 characters, ensuring conciseness.
- **Originality and Copyright**: The prompt instructs that the text must be original and free from copyright-infringing elements.
- **Single Phrase Output**: The prompt explicitly states that the output should be a single phrase, with no additional or prefatory text.

### Use Case

An example of how the prompt would be used:

- **Store Name**: "TechGadgets"
- **Store Concept**: "Innovative electronics and gadgets"
- **Generated Banner**: "Innovative Gadgets for a Smarter Life"

### Technical Implementation

The solution was implemented using the Hugging Face API to generate the banner text. The following steps were taken:

- **Input Handling**: The user inputs the store name and concept.
- **API Request**: A request is made to the Hugging Face API with the inputs.
- **Validation**: The generated text is validated to ensure it meets the length and format requirements. Any text that does not meet the criteria is discarded and a new request is made.

### Testing and Validation

The prompt was tested with various store names and concepts to ensure consistent and valid outputs. For instance:

- **Store Name**: "EcoTrends"
- **Store Concept**: "Sustainable home decor"
- **Generated Banner**: "Eco-Friendly Decor for Modern Living"

### Issues Encountered

During testing, issues such as the generated text exceeding 50 characters or not being concise enough were encountered. These were resolved by adjusting the prompt and refining the API request parameters to produce more accurate results.

## How to Run the Application

### Prerequisites

- Python 3.x installed
- Flask installed (`pip install flask`)
- Requests library installed (`pip install requests`)
- A Hugging Face API key

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Update the Hugging Face API key in `app.py`:

   ```python
   HUGGING_FACE_API_KEY = "YOUR_HUGGING_FACE_API_KEY"
   ```

5. Run the Flask application:

   ```bash
   python app.py
   ```

6. Open your web browser and go to `http://127.0.0.1:5000`

### File Structure

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the web interface.
- `static/style.css`: The CSS file for styling (if any).
- `README.md`: This file.

## Contact

If you have any questions, please feel free to contact me at [your-email@example.com].
