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
# https://console.cloud.google.com/

# Determine what project to put the files
gcloud projects list

PROJECT_ID="webapps-codesolutions2"

# Create a new project
gcloud projects create $PROJECT_ID

# Set the project
gcloud config set project $PROJECT_ID

# -------------------------------------------------

# List project billing ACCOUNT_ID
gcloud alpha billing accounts list

ACCOUNT_ID=""
clear

# Enable project billing
gcloud alpha billing accounts projects link $PROJECT_ID --billing-account=$ACCOUNT_ID

# -------------------------------------------------

# Create storage bucket parameters
BUCKET_NAME="on-the-way2selfrespect"
LOCATION="europe-west9"

# Create a storage bucket
gcloud storage buckets create gs://$BUCKET_NAME --project=$PROJECT_ID --default-storage-class=STANDARD --location=$LOCATION --uniform-bucket-level-access

gcloud storage ls

# -------------------------------------------------

export SERVICE_ACCOUNT_ID=$(echo "sendData2bucket")
export SERVICE_ACCOUNT_EMAIL=$(echo "j622amilah@gmail.com")
export SERVICE_ACCOUNT=$SERVICE_ACCOUNT_ID@$PROJECT_ID.iam.gserviceaccount.com 

# -------------------------------------------------

# [0] Create a custom service account (ONLY HAVE TO DO ONCE)
gcloud iam service-accounts create $SERVICE_ACCOUNT_ID --description="SVC" --display-name="sendData2bucket"

# -------------------------------------------------

# Add roles to serviceaccount

# storage.objectAdmin - serviceaccount
gcloud projects add-iam-policy-binding $PROJECT_ID --member=serviceAccount:$SERVICE_ACCOUNT --role="roles/storage.objectAdmin"

# -------------------------------------------------

# Create a service account key
gcloud iam service-accounts keys create key.json --iam-account=$SERVICE_ACCOUNT

# -------------------------------------------------

# List existing service account keys
gcloud iam service-accounts keys list --iam-account=$SERVICE_ACCOUNT

# -------------------------------------------------

cat key.json

# -------------------------------------------------

# ---------------------------
# On Kaggle run three cells
# ---------------------------
%%bash --err null
cat > key.json <<EOF
{
  "type": "service_account",
  "project_id": "webapps-codesolutions2",
  "private_key_id": "e9decbe52d4441d6577fddb6f0192bfd540f142d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCO61nnEYYuHFF8\nLWPaUaumSr9ePi3YdzJHu8j1OoVRaWlxLM061w0oDdvk3d/5c60oZMXiSQNTA4O0\ns+2Hy6jQThv5kKwMXzwrvRvnOaUVM6VdiPkwm8J1i43HUSJ6xJEhWKGhZ/kL6OO9\n3w3W2jOzThv4SksLTHONFKnQ4ni9JsdMAaZ4El740/UElBiDojlGin1q6uDdW5nT\n5750l/ddbUW999TUq+IBRLDSJkzhW8nfOf7hcdUVy2sm/Vy3CRRVCWTgZgR2mS6R\nXeOc8fPJgoQ+A0ySzYqp2tpy5hthDUM0nPxUNkZD2rUErufFq0kaMPFXmwFCcLJa\nrlBiPpdFAgMBAAECggEACEmQ78N2IKffOMBoDSGVvsGQWb5oyafVyE+VDlVLpEYk\nyV2D9BDC0EsHcHzGL1CcHp7DU8UQloh6Y2jYkfqHCjcxS5YuR9Rg6JdhbhXLYxCY\n2vTloEIz8z15pfBoO664zLJ3QuUEzcI+LIUp6AbEnzXdDNeABQJ0o95qH3T2c99c\n2YQktYJr3LZkHrp/NjZGxe6FeYQEW+HZN3fT8ptTZddoCTbEi5ANma1g9ccPyTrR\nln8s1iUUgx7MuUjt2nRdLob7lWHLcjw1WNDXre8SY6hgoShTVAHIshwCxJxT6KYM\no3XLwP7316pqlZhXeHfBKO6UHbuCNqJd7G30wjTxoQKBgQDA0tO2lnWBceTU70ka\nFVrAHlq6UKJI+nm5ka1AxAhhBqn7oVQEtRftFETowe+KGbdw3KvhTpbHdJ/wM3xh\nr28M9N10FY83hHVHvzctPHkflU4MxVcbYMHd7Qu6weoIuNB8okWatxOSpTYeKakM\nCHwvzUifs1aiNaIyd6/Xs1jQJQKBgQC9vsij3hneLMRk536Qpac3IFGea6Sap6wY\nllz0DXiZV5nrX4dZ4JYEZ2ryx0YqhIG30gS85tBMUKpr32+XY6xxlRMxlrlxAkN0\nxaR25r7DwGwFytN3YhotlA6J1Pv4dETXCp/Ifh3HMl8ewvqaqVAzGuhIMJPuiuPI\nXgI/eu3woQKBgGnBN6ykyL2+IatHsehEXgmQnGIjZ15vQeOtKkCjQ5Uzencv/Ey4\npe65dzHRa/dqM1oLLZnc6IVsSWwMUOOivF12zx6j1HC2jTxUe4ar7CKOWMhYU3YI\nk0uMfypmwF0YQACbX2GDl5COXCge4UBgRvxQsswkKBe/Ir5bNm4vRz6hAoGAUtvc\nbErSCwaLoPDCgVIFinovijnBgNPVwErxPpYfYv8xNOrbhXEgsb2jo29IAcsphmdN\nMFyu+5SCR2ckKP0a0eLipdYHFwWBBZ5FarLq/TqrMYBYBhsuCVdNXf1HJ0FGyo1W\nJ0yDnngtt5Y3r5BeeGK4qsWj5Bh8zgPXgXciLuECgYEAqX4geM4DovXsEufOb/k2\n0APvz0mzTj1kAJNZO2AaHPaZeSXwUuTQLawF3ysaa2/1djA4wH9XRh2rPcWczjYG\nMJbaq4JZkUcqDIFqA/wzQNmESFYgXi+a/XBj9tNdOu5tSZreoLjvkmFnEFD2HBhG\nNBtQdFu4nzkaNbF8vGcG/ac=\n-----END PRIVATE KEY-----\n",
  "client_email": "sendData2bucket@webapps-codesolutions2.iam.gserviceaccount.com",
  "client_id": "115611473637861486610",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/sendData2bucket%40webapps-codesolutions2.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

# -------------------------------------------------

# Log into GCP
!gcloud auth login --quiet --cred-file=key.json --force

# -------------------------------------------------

# Remove the credential key
!rm -rf key.json

# -------------------------------------------------

# Upload an object to a bucket: an error will be created but it still runs
%%bash --err null
declare -a files=('red_dark.png' 'red.png' 'red_light.png' 'green_dark.png' 'green.png' 'green_light.png' 'blue_dark.png' 'blue.png' 'blue_light.png' 'cyan_dark.png' 'cyan.png' 'cyan_light.png' 'yellow_dark.png' 'yellow.png' 'yellow_light.png' 'magenta_dark.png' 'magenta.png' 'magenta_light.png' 'orange_dark.png' 'orange.png' 'orange_light.png');

# Get the length of the array
export N=$(echo ${#files[@]})

echo 'N'
echo $N

for r in $( seq 0 $N )
do
    echo ${files[$r]}
    gcloud storage cp ${files[$r]} gs://on-the-way2selfrespect/
    
done

# -------------------------------------------------

# List the contents of a storage buckets GCP to see that the images arrived
gcloud storage ls --recursive gs://$BUCKET_NAME/**

# -------------------------------------------------



# -------------------------------------------------
# Go back to GCP
# -------------------------------------------------

# https://cloud.google.com/storage/docs/access-control/making-data-public#permissions-cli

# Make individual objects publicly readable
gcloud storage objects update gs://$BUCKET_NAME/image2.png --add-acl-grant=entity=AllUsers,role=READER

# Make all objects in a bucket publicly readable 
gcloud storage buckets add-iam-policy-binding gs://$BUCKET_NAME --member=allUsers --role=roles/storage.objectViewer

# -------------------------------------------------

# Check if the image can be viewed in the browser
https://storage.googleapis.com/on-the-way2selfrespect/red.png

# -------------------------------------------------

# Use storage path to refer to image
gs://on-the-way2selfrespect/red.png

# -------------------------------------------------

# -------------------------------------------------


touch cors.json

echo '[{"origin": ["https://yourdomain.com"],"responseHeader": ["Content-Type"],"method": ["GET", "HEAD"],"maxAgeSeconds": 3600}]' > cors.json

# OR

%%bash --err null
cat > cors.json <<EOF
[
    {
      "origin": ["https://CodeSolutions2.github.io"],
      "responseHeader": ["Content-Type"],
      "method": ["GET", "HEAD"],
      "maxAgeSeconds": 3600
    }
]
EOF

# Set CORS settings
gsutil cors set cors.json gs://$BUCKET_NAME

# ---------------------------------------------

# View saved CORS settings
gsutil cors get gs://$BUCKET_NAME


# -------------------------------------------------

