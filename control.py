from mistyPy import Robot
import time
import random

# Connect to Misty
# misty_ip = "Misty Ip here"
# misty = Robot(misty_ip)

###################################################
# Mock Robot class for testing without Misty
class MockRobot:
    def changeLED(self, red, green, blue):
        print(f"Simulated LED color set to RGB({red}, {green}, {blue})")

    def moveArm(self, arm, position, velocity):
        print(f"Simulated moving {arm} arm to position {position} with velocity {velocity}")
    
    def changeImage(self, image_name):
        print(f"Simulated changing face to {image_name}")

    def say(self, phrase):
        print(f"Misty says: {phrase}")

misty = MockRobot()
#####################################################
##LED colors##
###################################################
# Function to set the LED to green (follow command)
def set_led_green():
    misty.changeLED(0,255,0)
    print("LED set to green")

# Function to set the LED to red (invert command)
def set_led_red():
    misty.changeLED(255, 0, 0)
    print("LED set to red")

#####################################################
#Move Arms# 
#################################################
# Function to raise the right arm
def raise_right_arm():
    misty.moveArm("right", 5, velocity=5)
    print("Raised right arm")

# Function to lower the right arm
def lower_right_arm():
    misty.moveArm("right", 0, velocity=5)
    print("Lowered right arm")

# Function to raise the left arm
def raise_left_arm():
    misty.moveArm("left", 5, velocity=5)
    print("Raised left arm")

# Function to lower the left arm
def lower_left_arm():
    misty.moveArm("left", 0, velocity=5)
    print("Lowered left arm")

# Function to raise both arms 
def raise_both_arms():
    misty.moveArm("left", 5, velocity=5)
    misty.moveArm("right", 5, velocity=5)
    print("Raised both arms")

# Function to lower both arms 
def lower_both_arms():
    misty.moveArm("left", 0, velocity=5)
    misty.moveArm("right", 0, velocity=5)
    print("Lowered both arms")
    
############################################
#Change face# 
############################################
# Function to set Misty's face to a smile
def set_smile():
    misty.changeImage("Happy.png")  # will need the proper name 
    print("Set face to smile")

# Function to set Misty's face to a frown
def set_frown():
    misty.changeImage("Sad.png")  # will need the proper name
    print("Set face to frown")

############################################
#Speech#
############################################
def misty_speak(phrase):
    misty.say(phrase)




######
# Test Functions # 
# print("\nTesting led light:")
# set_led_green()
# set_led_red()
# print("\nTesting arm movements:")
# raise_right_arm()
# raise_left_arm()
# lower_right_arm()
# lower_left_arm()
# raise_both_arms()
# lower_both_arms()
# print("\nTesting facial expressions:")
# set_smile()
# set_frown()
# print("\nTesting speech:")
# misty_speak("Simon Says")


