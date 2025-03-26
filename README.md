# Morpheus Terminal: Positioning Matrix Experience

This repository contains a Matrix-inspired Morpheus terminal experience that introduces audiences to positioning expertise through an immersive, mind-bending interface. The experience uses terminal-style text, glitching effects, and visual moments to create open loops and transform how people think about positioning.

## Deployment Instructions

### Option 1: Deploy on Replit

1. Create a new Replit project
2. Choose "Python" as the template
3. Upload all files from this repository to your Replit project
4. In the Replit shell, run:
   ```
   pip install -r requirements.txt
   ```
5. Click the "Run" button or type `python app.py` in the shell
6. Replit will provide a URL where your application is hosted

### Option 2: Deploy on Cursor

1. Open Cursor and create a new project
2. Import all files from this repository
3. Open a terminal in Cursor and run:
   ```
   pip install -r requirements.txt
   python app.py
   ```
4. The application will run on `http://localhost:5000`

## Project Structure

```
morpheus_terminal/
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html              # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css           # CSS styling
│   └── js/
│       ├── matrix.js           # Matrix code rain effect
│       ├── terminal.js         # Terminal typing and interaction
│       ├── effects.js          # Visual effects
│       └── script.js           # Main script coordination
└── README.md                   # This file
```

## Positioning Matrix Framework

The experience is built around the "Positioning Matrix" framework, which includes:

### Core Positioning Dimensions
- **Perception Axis**: How the market views your brand vs. reality
- **Differentiation Axis**: How distinct your offering is from competitors
- **Resonance Axis**: How deeply your positioning connects with target audiences

### The Four Positioning Quadrants
1. **Commodity Zone** (Low Differentiation, Low Resonance)
   - Where most businesses exist
   - Price-driven competition
   - Interchangeable in customer minds

2. **Confusion Zone** (High Differentiation, Low Resonance)
   - Unique but irrelevant
   - "So what?" response from market
   - Innovation without purpose

3. **Compromise Zone** (Low Differentiation, High Resonance)
   - Connects emotionally but lacks distinction
   - Initial success followed by commoditization
   - Vulnerable to competitive copying

4. **Command Zone** (High Differentiation, High Resonance)
   - The positioning sweet spot
   - Market leadership position
   - Premium pricing power

## Customization

### Modifying the Script

The script content is defined in `app.py` in the `script_content` dictionary. Each scene has:
- `title`: The scene title
- `content`: Array of text lines to display
- `visual_effects`: Array of visual effects to trigger

### Customizing Visual Effects

Visual effects are implemented in `effects.js`. You can modify existing effects or add new ones by:
1. Adding a new method to the `VisualEffects` class
2. Adding a case for your effect in the `triggerEffect` function in `script.js`

### Changing Positioning Concepts

The positioning framework is defined in `app.py` in the `positioning_matrix` dictionary. You can modify:
- Dimensions
- Quadrants
- Methodologies

## Technical Requirements

- Python 3.6+
- Flask 2.0+
- Modern web browser (Chrome, Firefox, Safari, Edge)
- JavaScript enabled

## Credits

This experience was created by Manus for positioning expertise presentation. It draws inspiration from the Matrix film franchise while creating a unique framework for understanding market positioning.

## License

This project is proprietary and confidential. Unauthorized copying, distribution, or use is strictly prohibited.
