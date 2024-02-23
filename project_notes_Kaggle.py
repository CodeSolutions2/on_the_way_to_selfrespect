# -------------------------------------------------
# Generating images for on_the_way_to_selfrespect
# -------------------------------------------------

import os

import matplotlib.pyplot as plt
import PIL
from PIL import Image

from PIL import ImageFont
from PIL import ImageDraw 

# -------------------------------------------------

# Download fonts
!git clone https://github.com/CodeSolutions2/fonts_2_download

# -------------------------------------------------

!ls -al

# -------------------------------------------------

# -------------------------------------------------
# Subfunctions
# -------------------------------------------------
def create_a_background(rgb_value, save_img_name, phrase, dict_font):
    width = 256
    height = width
    
    fontsize = dict_font['fontsize']
    font_startfromleft = dict_font['startfromleft']
    font_startfromtop = dict_font['startfromtop']

    # Create image object which is of specific color background
    # https://rgbcolorpicker.com/
    img = PIL.Image.new(mode = "RGB", size = (width, height), color = (rgb_value))
    img.show()
    img.save(f"/kaggle/working/{save_img_name}.png")

    # Add text to the image
    img = Image.open(f"/kaggle/working/{save_img_name}.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('/kaggle/working/fonts_2_download/FreeMono.ttf', fontsize)

    draw.text((font_startfromleft, font_startfromtop), phrase, font=font, fill=(0,0,0))

    img.show()
    img.save(f"/kaggle/working/{save_img_name}.png")
    
    # --------------------------------------
    
    # View image
    rgb_image = Image.open(f"/kaggle/working/{save_img_name}.png")

    # View a sample image
    fig, ax0 = plt.subplots(nrows=1, ncols=1, figsize=(4,4))

    ax0.imshow(rgb_image)
    ax0.axis('off')
    ax0.set_title("", size=20)
    plt.show()

# -------------------------------------------------

dignity, self-respect, self-esteem, responsibility, respect for others, esteem for others, respectability
self-confidence, self-worth

# -------------------------------------------------

# Self-respect messages: participation and belief

# Participation
To know 'the value of your things' is to maximize one's resources to accomplish a goal.
Having self-respect means to know the values of your things.

When one uses their resources in the best possiible way without complaining of lack to realize a goal,
one is often more responsible to manage more resources (ie: money, opportunity, work, etc).
Having self-respect means to realize a goal without complaining.

People/society/'the system' reinforce 'states of being and doing'. People who have
success and those who do not have suceess have experiences that reinforce their state of suceess and non-success.
Having self-respect means to change your actions daily so that you reinforce success in your life.

Following age, gender, race, and religion paradigms could lead to discrimination, violence,
poor decision making, self-disrespect, disrespect to others, lonliness, and gossiping.
Having self-respect means to not pay attention to age, gender, race, and religion paradigms, but focus on 
associations created by education, skill, and practice because they allow for societal success.

Some people who have low self-respect practice lying due to fear of not being able to 
obtain the things that they need in life, and they even lie when they do not need to lie because it becomes an engraned response mechanism. 
Having self-respect means to be aware that lying is an excuse to not be present; 
liers do not want to participate and are less couragous versions of their real selves.

Having self-respect means to not blindly follow people or connect yourself to others such that 
your life and their lives are directly influenced by the other person's actions. 
One does not have control over other people's lives, one can only control their own life. 
Having self-respect and respect for others means to make boundaries (ie: an understanding of how
one wants to be treated, or an intermediate that prevents direct interaction) such that other people's actions/lives
do not directly influence your life, and similarly your life actions should not directly influence other people's lives.


# Belief
One believes that they are suffering because they only look at the problem from one way. When 
you look at the problem from multiple persectives you can see that you are not suffering.
Having self-respect means to stay active, and take small actions and steps to change the situation.

People who participate in illegal, irresponsible activities, and lying participate because they believe that they can not 
obtain societal success without these behaviors. They lack self-respect because there are different ways to behave that are 
accepted by society to obtain success, taking unnecessary risk to loose one's freedom, money, job, home, or life is a form of self-disrespect.
Having self-respect means to not take unnecessary risks, such that one's dignity of one's character is not lost.


# -------------------------------------------------


# -------------------------------------------------
# Create different backgrounds
# -------------------------------------------------

# --------------------------------

phrase = 'dignity'
dict_font = {'fontsize': 36, 'startfromleft': 30, 'startfromtop': 100}

save_img_name = "red_dark"
rgb_value = 140, 0, 0 
create_a_background(rgb_value, save_img_name, phrase, dict_font)

save_img_name = "red"
rgb_value = 255, 0, 0
create_a_background(rgb_value, save_img_name, phrase, dict_font)

save_img_name = "red_light"
rgb_value = 255, 175, 175
create_a_background(rgb_value, save_img_name, phrase, dict_font)

# --------------------------------

phrase = 'self-respect'
dict_font = {'fontsize': 30, 'startfromleft': 30, 'startfromtop': 100}

save_img_name = "green_dark"
rgb_value = 0, 140, 0
create_a_background(rgb_value, save_img_name, phrase, dict_font)

save_img_name = "green"
rgb_value = 0, 255, 0
create_a_background(rgb_value, save_img_name, phrase, dict_font)

save_img_name = "green_light"
rgb_value = 175, 255, 175
create_a_background(rgb_value, save_img_name, phrase, dict_font)

# --------------------------------

phrase = 'self-esteem'
dict_font = {'fontsize': 30, 'startfromleft': 30, 'startfromtop': 100}

save_img_name = "blue_dark"
rgb_value = 0, 0, 170
create_a_background(rgb_value, save_img_name, phrase, dict_font)

save_img_name = "blue"
rgb_value = 0, 0, 255
create_a_background(rgb_value, save_img_name, phrase, dict_font)

save_img_name = "blue_light"
rgb_value = 175, 175, 255
create_a_background(rgb_value, save_img_name, phrase, dict_font)

# --------------------------------

phrase = 'responsibility'
dict_font = {'fontsize': 20, 'startfromleft': 30, 'startfromtop': 100}

save_img_name = "cyan_dark"
rgb_value = 0, 170, 170
create_a_background(rgb_value, save_img_name, phrase, dict_font)

save_img_name = "cyan"
rgb_value = 0, 255, 255
create_a_background(rgb_value, save_img_name, phrase, dict_font)

save_img_name = "cyan_light"
rgb_value = 175, 255, 255
create_a_background(rgb_value, save_img_name, phrase, dict_font)

# --------------------------------

phrase = 'respect for others'
dict_font = {'fontsize': 20, 'startfromleft': 5, 'startfromtop': 100}

save_img_name = "yellow_dark"
rgb_value = 210, 200, 0
create_a_background(rgb_value, save_img_name, phrase, dict_font)

save_img_name = "yellow"
rgb_value = 255, 245, 0
create_a_background(rgb_value, save_img_name, phrase, dict_font)

save_img_name = "yellow_light"
rgb_value = 255, 250, 175
create_a_background(rgb_value, save_img_name, phrase, dict_font)

# --------------------------------

phrase = 'esteem for others'
dict_font = {'fontsize': 22, 'startfromleft': 10, 'startfromtop': 100}

save_img_name = "magenta_dark"
rgb_value = 180, 0, 150
create_a_background(rgb_value, save_img_name, phrase, dict_font)

save_img_name = "magenta"
rgb_value = 255, 0, 212
create_a_background(rgb_value, save_img_name, phrase, dict_font)

save_img_name = "magenta_light"
rgb_value = 255, 175, 239
create_a_background(rgb_value, save_img_name, phrase, dict_font)

# --------------------------------

phrase = 'respectability'
dict_font = {'fontsize': 25, 'startfromleft': 30, 'startfromtop': 150}

save_img_name = "orange_dark"
rgb_value = 215, 100, 0
create_a_background(rgb_value, save_img_name, phrase, dict_font)

save_img_name = "orange"
rgb_value = 255, 119, 0
create_a_background(rgb_value, save_img_name, phrase, dict_font)

save_img_name = "orange_light"
rgb_value = 255, 216, 175
create_a_background(rgb_value, save_img_name, phrase, dict_font)

# --------------------------------
# -------------------------------------------------


# -------------------------------------------------


# -------------------------------------------------



# -------------------------------------------------


# -------------------------------------------------


# -------------------------------------------------
