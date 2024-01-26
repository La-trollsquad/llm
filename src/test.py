from trollsquadAI import TrollsquadAI

instance = TrollsquadAI()
prompt = "Faire un récit pour enfant, mettant en scène une petite fille prénomée Agathe, qui prend le trône de la Reine des Neiges."
styles = ["Realistic"]
print("PROMPT INITIAL: " + prompt)
#STYLES: "DSLR photography", "sharp focus", "Unreal Engine 5", "Octane Render", "Redshift", "f/1.4", "ISO 200", "1/160s", "8K", "RAW", "unedited", "symmetrical balance", "in-frame" 

for style in styles: 
    prompt += " "+style 
output = instance.prompt_to_text(prompt)

print("LLAMA : " + output)

payload = {
    "prompt" : prompt,
    "steps" : 100,
    "negative_prompt": "",
}

result = instance.text_to_image(payload)