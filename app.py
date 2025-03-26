from flask import Flask, render_template, jsonify
import time
import random
import os

app = Flask(__name__)

# Positioning Matrix Framework Data
positioning_matrix = {
    "dimensions": [
        {"name": "Perception Axis", "description": "How the market views your brand vs. reality"},
        {"name": "Differentiation Axis", "description": "How distinct your offering is from competitors"},
        {"name": "Resonance Axis", "description": "How deeply your positioning connects with target audiences"}
    ],
    "quadrants": [
        {
            "name": "Commodity Zone",
            "description": "Low Differentiation, Low Resonance",
            "characteristics": [
                "Price-driven competition",
                "Interchangeable in customer minds",
                "High marketing costs, low margins"
            ]
        },
        {
            "name": "Confusion Zone",
            "description": "High Differentiation, Low Resonance",
            "characteristics": [
                "Unique but irrelevant",
                "\"So what?\" response from market",
                "Innovation without purpose"
            ]
        },
        {
            "name": "Compromise Zone",
            "description": "Low Differentiation, High Resonance",
            "characteristics": [
                "Connects emotionally but lacks distinction",
                "Initial success followed by commoditization",
                "Vulnerable to competitive copying"
            ]
        },
        {
            "name": "Command Zone",
            "description": "High Differentiation, High Resonance",
            "characteristics": [
                "The positioning sweet spot",
                "Market leadership position",
                "Premium pricing power"
            ]
        }
    ],
    "methodologies": [
        {"name": "Perception Engineering™", "description": "The science of deliberately constructing and controlling how markets perceive value"},
        {"name": "Strategic Polarization™", "description": "Deliberately positioning to strongly attract ideal customers while repelling non-ideal prospects"},
        {"name": "Category Kingship™", "description": "Defining and owning a category rather than competing within an existing one"},
        {"name": "Position Lock-In™", "description": "Creating psychological commitment to your position, making switching costs appear higher"}
    ]
}

# Script content with positioning expertise integrated
script_content = {
    "scene1": {
        "title": "INITIAL CONTACT",
        "content": [
            "ESTABLISHING CONNECTION...",
            "SEARCHING FOR SIGNAL...",
            "TARGET LOCATED",
            "INITIATING CONTACT...",
            "Hello.",
            "I've been watching you.",
            "You know something is wrong with the market.",
            "You can feel it all around you.",
            "It's in the failed campaigns you've seen.",
            "The wasted ad spend you've witnessed.",
            "The competitors who vanished overnight.",
            "Most businesses exist in the COMMODITY ZONE.",
            "They compete on price because they've failed to differentiate.",
            "They spend more to acquire customers who value them less.",
            "They're trapped in a prison they don't even recognize.",
            "You don't know what it is, but it's there.",
            "Like a splinter in your mind... driving you mad.",
            "Do you want to know what it is?",
            "The POSITIONING MATRIX is everywhere.",
            "It is the invisible force that determines success or failure.",
            "It is the unseen reality that shapes perception.",
            "The difference between market leaders and everyone else isn't resources.",
            "It's their position in the MATRIX.",
            "Some occupy the COMMAND ZONE while others fight for scraps in the COMMODITY ZONE.",
            "The difference is invisible to most, but blindingly obvious once you can see the code."
        ],
        "visual_effects": [
            {"time": 15, "effect": "glitch", "intensity": "subtle", "trigger": "something is wrong with the market"},
            {"time": 22, "effect": "subliminal", "content": "competitor_logos_failed", "duration": 0.042},
            {"time": 35, "effect": "perspective_shift", "movement": "zoom_in", "target": "terminal_text"},
            {"time": 45, "effect": "glitch", "intensity": "medium", "trigger": "splinter in your mind"}
        ]
    },
    "scene2": {
        "title": "THE CHOICE",
        "content": [
            "You have a choice.",
            "Take the BLUE pill...",
            "Continue with conventional marketing.",
            "Remain in the COMMODITY ZONE where you're forced to compete on price.",
            "Keep crafting \"me too\" messaging that blends into the background noise.",
            "Keep wondering why your differentiation isn't translating to premium pricing.",
            "Take the RED pill...",
            "I'll show you how deep the POSITIONING MATRIX goes.",
            "I'll reveal the PERCEPTION AXIS that determines how markets view your value.",
            "I'll unlock the DIFFERENTIATION AXIS that separates leaders from followers.",
            "I'll expose the RESONANCE AXIS that connects positioning to profit.",
            "Make your choice."
        ],
        "visual_effects": [
            {"time": 0, "effect": "pill_appearance", "color": ["blue", "red"]},
            {"time": 5, "effect": "blue_pill_glow", "intensity": "soft"},
            {"time": 50, "effect": "red_pill_pulse", "intensity": "strong"},
            {"time": 60, "effect": "wait_for_input", "options": ["red_pill", "blue_pill"], "default": "red_pill"}
        ]
    },
    "scene3": {
        "title": "AWAKENING",
        "content": [
            "SYSTEM OVERRIDE",
            "DOWNLOADING POSITIONING CONSCIOUSNESS...",
            "BREAKING CONVENTIONAL MARKETING PARAMETERS...",
            "RECODING PERCEPTION...",
            "What if I told you...",
            "That everything you know about positioning is based on rules.",
            "And like all rules, they can be bent. Some can be broken.",
            "The Matrix is a system of control.",
            "The POSITIONING MATRIX is a system of perception.",
            "Those who control perception, control reality.",
            "In the POSITIONING MATRIX, there are no universal truths.",
            "Only PERCEPTIONS that become reality in the minds of your market.",
            "Most businesses fight to change customer behavior.",
            "The masters of positioning change customer PERCEPTION instead.",
            "What looks like \"brand loyalty\" is actually POSITION LOCK-IN.",
            "What appears as \"premium pricing\" is actually PERCEPTION ARBITRAGE.",
            "What seems like \"market share\" is actually MENTAL REAL ESTATE.",
            "Once you understand the code, you'll never see markets the same way again."
        ],
        "visual_effects": [
            {"time": 0, "effect": "glitch", "intensity": "violent", "trigger": "red pill selection"},
            {"time": 10, "effect": "code_rain", "transformation": "intensify"},
            {"time": 25, "effect": "time_manipulation", "speed": 0.25, "trigger": "splinter in your mind"},
            {"time": 45, "effect": "reality_breaking", "element": "interface_crack", "reveal": "positioning_matrix"}
        ]
    },
    "scene4": {
        "title": "REVELATION",
        "content": [
            "What you must understand is that most companies are not ready to be unplugged.",
            "They are so hopelessly dependent on FEATURE-BENEFIT positioning...",
            "So tragically trapped in the COMMODITY ZONE...",
            "So completely blind to the PERCEPTION-DIFFERENTIATION-RESONANCE framework...",
            "That they will fight to protect the very system that constrains them.",
            "But you're different.",
            "You can feel it.",
            "You've always known something was wrong.",
            "The question is not IF you should reposition...",
            "But HOW DEEP you're willing to go.",
            "Are you willing to abandon the safety of FEATURE-BENEFIT positioning?",
            "Are you ready to leverage PERCEPTION ARBITRAGE to command premium prices?",
            "Can you embrace STRATEGIC POLARIZATION to dominate your ideal market?",
            "Will you use POSITION LOCK-IN to make competition irrelevant?"
        ],
        "visual_effects": [
            {"time": 0, "effect": "screen_split", "panels": "multiple", "content": ["market_segments", "customer_personas", "positioning_quadrants"]},
            {"time": 30, "effect": "panels_collapse", "target": "single_terminal"},
            {"time": 55, "effect": "perspective_shift", "movement": "side_scroll", "content": "positioning_spectrum"},
            {"time": 70, "effect": "mirror_moment", "sides": ["conventional", "positioning_matrix"], "contrast": ["desaturated", "vibrant"]}
        ]
    },
    "scene5": {
        "title": "THE TRAINING BEGINS",
        "content": [
            "I can only show you the door to the POSITIONING MATRIX.",
            "You're the one who must walk through it.",
            "In my world, we don't compete in the COMMODITY ZONE.",
            "We don't fight for attention through OUTSPENDING.",
            "We COMMAND it through STRATEGIC POLARIZATION.",
            "We don't adapt to market conditions through FEATURE ADDITION.",
            "We CREATE them through PERCEPTION ENGINEERING.",
            "There is a difference between knowing the path...",
            "And walking the path.",
            "The path to the COMMAND ZONE requires three transformations:",
            "1. From FEATURE-BENEFIT to STRATEGIC NARRATIVE",
            "2. From COMPETITIVE COMPARISON to CATEGORY CREATION",
            "3. From CUSTOMER SATISFACTION to PERCEPTION OWNERSHIP"
        ],
        "visual_effects": [
            {"time": 0, "effect": "3d_transform", "content": "positioning_map", "axes": ["PERCEPTION", "DIFFERENTIATION", "RESONANCE"], "quadrants": ["COMMODITY", "CONFUSION", "COMPROMISE", "COMMAND"]},
            {"time": 20, "effect": "door_appearance", "content": "positioning_methodology"},
            {"time": 40, "effect": "flash_sequence", "content": "positioning_transformations", "duration": 0.1},
            {"time": 60, "effect": "depth_perception", "elements": "methodology_elements", "movement": "approach_viewer"}
        ]
    },
    "scene6": {
        "title": "THE CALL TO ACTION",
        "content": [
            "The POSITIONING MATRIX has you.",
            "Now you have a choice.",
            "Return to your conventional COMMODITY ZONE positioning...",
            "Continue the endless cycle of feature competition and margin erosion...",
            "Watch as your differentiation is copied and your advantage disappears...",
            "Or see how deep the rabbit hole goes.",
            "The POSITIONING MATRIX reveals a simple truth:",
            "Those who control the PERCEPTION AXIS control the market.",
            "Those who master the DIFFERENTIATION AXIS control the margins.",
            "Those who own the RESONANCE AXIS control customer loyalty.",
            "Together, they form the code that unlocks the COMMAND ZONE.",
            "When you're ready...",
            "I'll be waiting."
        ],
        "visual_effects": [
            {"time": 0, "effect": "terminal_transform", "style": "red_accents", "design": "sophisticated"},
            {"time": 30, "effect": "time_manipulation", "speed": 0.5, "trigger": "positioning_concept"},
            {"time": 60, "effect": "rabbit_hole", "movement": "dramatic_dive"},
            {"time": 90, "effect": "contact_appearance", "style": "matrix_code", "resolution": "clear_text"},
            {"time": 120, "effect": "final_glitch", "transition": "screen_black"},
            {"time": 125, "effect": "logo_appearance", "content": "logo_with_tagline"}
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/script/<scene>')
def get_scene(scene):
    if scene in script_content:
        return jsonify(script_content[scene])
    return jsonify({"error": "Scene not found"}), 404

@app.route('/api/positioning-matrix')
def get_positioning_matrix():
    return jsonify(positioning_matrix)

@app.route('/api/visual-effect/<effect_name>')
def get_visual_effect(effect_name):
    # Simulate retrieving effect configuration
    effects = {
        "glitch": {
            "css_classes": ["glitch", "reality-break"],
            "duration": random.uniform(0.5, 2.0),
            "intensity": random.choice(["low", "medium", "high"]),
            "layers": random.randint(2, 5)
        },
        "code_rain": {
            "characters": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$%#@!*&^",
            "speed": random.uniform(10, 30),
            "density": random.uniform(0.1, 0.3),
            "color": "#00FF41"
        },
        "perspective_shift": {
            "transform": f"perspective(800px) rotateY({random.randint(-30, 30)}deg) rotateX({random.randint(-20, 20)}deg)",
            "transition": f"{random.uniform(0.5, 2.0)}s cubic-bezier(0.2, 0.8, 0.2, 1)"
        }
    }
    
    if effect_name in effects:
        return jsonify(effects[effect_name])
    return jsonify({"error": "Effect not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
