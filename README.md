# ☁️ Word Cloud Maker ☀️

This Python-powered app helps you create stunning word clouds with customizable settings, including the ability to use a custom shape for the word cloud.

## Features

- **Customizable Word Clouds**: Adjust word limits, dimensions, and background color
- **Mask Image Upload**: Option to create word clouds in custom shapes
- **Real-Time Visualization**: See the word cloud as soon as you generate it

## Documentation

Learn more about word clouds:

- [Understanding Word Clouds](https://github.com/ashleysally00/word-cloud-maker-app/blob/main/undertstanding-word-clouds.md) - Detailed explanation of how word clouds work, including frequency, placement, and customization options.
- [Adding Sentiment Analysis to Word Clouds](https://github.com/ashleysally00/word-cloud-maker-app/blob/main/add-sentiment-analysis.MD) - Learn how to incorporate sentiment analysis in your word clouds using VADER and TextBlob libraries.

## Installation

1. **Clone the Repository**:

```bash
git clone <repository-url>
cd word-cloud-maker
```

2. **Set Up a Virtual Environment** (recommended):

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

## How to Run the App

1. Launch the app with:

```bash
streamlit run word_cloud_app.py
```

2. Open your browser and go to the provided URL (e.g., `http://localhost:8501`)

## How to Use the App

### Input Text

- Enter the text you want to include in the word cloud in the **Text Input** box on the sidebar

### Adjust Word Cloud Settings

- Use sliders to customize:
  - Maximum number of words
  - Width and height of the word cloud
  - Background color with the color picker

### Optional: Upload a Mask Image

The **Upload Mask Image** feature lets you create word clouds in custom shapes.

#### Supported File Types

- **File Types**: PNG, JPG, or JPEG
- **File Requirements**:
  - The shape (where words appear) should be **darker** than the background
  - The background (where no words appear) should be **lighter** or transparent

#### What It Does

- When you upload a mask, the app uses it to determine the shape of the word cloud
- Words will fill the darker areas of the image, leaving the lighter or transparent parts empty

#### Do You Need to Use This Feature?

- **No**: The app works perfectly without an uploaded mask and will default to a **rectangular word cloud**
- However, uploading a mask adds a fun, creative element by letting you create shapes like hearts, stars, or logos

### Generate the Word Cloud

- Click the **Generate Word Cloud** button to create your word cloud
- View the generated word cloud directly in the app

### Example Mask Image

You can use a mask like a **heart shape** or **star shape**. Here's how:

1. Prepare or download a black-and-white or high-contrast image where the shape is darker and the background is lighter or transparent
2. Upload it using the **Upload Mask Image** button

## Troubleshooting

- If the app doesn't start, make sure all dependencies are installed by running:

```bash
pip install -r requirements.txt
```

- For issues with mask uploads, ensure the image meets the **file requirements** mentioned above

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
📚 ✏️ ❤️
