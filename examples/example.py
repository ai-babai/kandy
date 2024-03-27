from kandy import Kandy

kandy = Kandy(
    api_key="your_api_key", 
    secret_key="your_secret_key"
)

images = kandy.images.generate(
    pos_prompt="pet in hat",
    neg_prompt="dog"
)

if images:
    image = images[0].to_image()
    image.save("generated_image.png")
