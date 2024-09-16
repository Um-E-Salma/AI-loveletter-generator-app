# AI-loveletter-generator-app
This project is a web application that integrates OpenAI's GPT-4 API with Shopify form to generate personalized love letters. The app is integrated within Shopify using a custom form and includes an editor powered by TinyMCE, allowing users to modify the generated love letters. Once edited, the changes are dynamically saved and displayed on the overlay

## Features
- **Generate Love Letters**: Using OpenAI's GPT-4 model, users can create custom love letters based on prompts like recipient name, characteristics, tone, and special moments.
- **Multi-language Support**: Support for generating love letters in German and English using GPT-4’s capabilities.
- **Text Editing**: After the letter is generated, users can make modifications using the **TinyMCE** rich text editor, which provides a user-friendly interface for editing.
- **Save Changes**: The application allows users to save their modified love letter, ensuring the updated text is retained after editing.
  
## Key Technologies
- **Heroku**: The app is hosted and deployed on Heroku, making it easily accessible online.
- **Shopify Embedded App**: The web app is embedded within Shopify, where the form for generating love letters is integrated.
- **OpenAI GPT-4**: GPT-4 is used to generate the love letters based on user input.
- **TinyMCE**: A rich text editor that allows users to easily modify the generated love letter before saving.
- **Flask (Backend)**: The app uses Python's Flask framework to handle backend processes like API calls and data handling.
  
## How It Works
1. **Form Submission on Shopify**: Users fill out a form embedded in Shopify with details like recipient name, characteristics, tone, and special moments.
2. **Love Letter Generation with GPT-4**: After form submission, the app sends a request to OpenAI's GPT-4 API, which generates a personalized love letter based on the provided inputs.
3. **TinyMCE Editing**: Once the letter is generated, the content is displayed in a TinyMCE editor with a popup window, allowing users to edit the letter as they wish.
4. **Save Changes**: After making edits, users can save the updated love letter, which is dynamically updated and retained on the page.

## Steps to Set Up the Project

### 1. Clone the Repository
To get started with the project, clone the repository:

```bash
git clone https://github.com/yourusername/loveletter-generator-app.git
```

2. **Install the Required Dependencies**  
   To install all necessary dependencies, run the following command:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**  
   To run the app locally, you’ll need to set your OpenAI API key and Shopify credentials in the environment variables.

   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   export SHOPIFY_API_KEY=your_shopify_api_key
   export SHOPIFY_SECRET_KEY=your_shopify_secret_key
   ```

4. **Run the Application**  
   To start the app locally, run the following command:

   ```bash
   python app.py
   ```

   The application should now be running on `http://localhost:3000`.

5. **Deploy to Heroku**  
   If you wish to deploy the app to Heroku, you can do so by following these steps:

   - Install the Heroku CLI and log in:

     ```bash
     heroku login
     ```

   - Create a new Heroku app:

     ```bash
     heroku create loveletter-generator-app
     ```

   - Push the code to Heroku:

     ```bash
     git push heroku master
     ```

   - Set environment variables on Heroku:

     ```bash
     heroku config:set OPENAI_API_KEY=your_openai_api_key
     heroku config:set SHOPIFY_API_KEY=your_shopify_api_key
     heroku config:set SHOPIFY_SECRET_KEY=your_shopify_secret_key
     ```

   Your app should now be live on Heroku.

## Functions of the Application

### Generating a Love Letter
1. **Go to the Shopify form**:  
   Users will fill out the following fields in the embedded Shopify form:
   - Recipient’s Name
   - Characteristics (e.g., kind, humorous)
   - Tone (e.g., romantic, playful)
   - Special moments (e.g., trips, memories)

2. **Submit the form**:  
   Once the form is submitted, the backend calls GPT-4 using OpenAI’s API to generate a love letter based on the input.

3. **Edit the Letter**:  
   The generated love letter is displayed in a popup window in a TinyMCE editor, where users can make changes to the text, formatting it to their liking.

4. **Save Changes**:  
   Once users are satisfied with their edits, they can save the changes, and the updated letter will be stored dynamically without refreshing the page.

## Screenshots

Below are some screenshots showing the flow of the application:

- **Shopify Form**:  
   ![Shopify Form image](https://github.com/Um-E-Salma/AI-loveletter-generator-app/blob/main/Response%20in%20german-TinyMCE%20popup.jpg)

- **Generated Love Letter in TinyMCE**:  
   (Add screenshot here)

- **Overlay with Saved Content**:  
   (Add screenshot here)

## APIs and Libraries Used

- **OpenAI API**: For generating personalized love letters using GPT-4.
- **TinyMCE**: For rich text editing of generated letters.
- **Flask**: Python web framework used for backend processes.
- **Heroku**: For hosting and deploying the application.

## Contact

If you have any questions or suggestions, feel free to contact me at [umesalma622@gmail.com](mailto:umesalma622@gmail.com).
```
