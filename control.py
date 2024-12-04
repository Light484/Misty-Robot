from mistyPy import Robot
import time
import random

# Connect to Misty
misty_ip = "10.5.9.252"
misty = Robot(misty_ip)

###################################################
# Mock Robot class for testing without Misty
# class MockRobot:
#     def changeLED(self, red, green, blue):
#         print(f"Simulated LED color set to RGB({red}, {green}, {blue})")

#     def moveArm(self, arm, position, velocity):
#         print(f"Simulated moving {arm} arm to position {position} with velocity {velocity}")
    
#     def moveArms(self, LeftArmPosition, RightArmPosition, LeftArmVelocity, RightArmVelocity):
#         print(f"move both arms")
    
#     def changeImage(self, image_name):
#         print(f"Simulated changing face to {image_name}")

#     def say(self, phrase):
#         print(f"Misty says: {phrase}")

# misty = MockRobot()
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

def set_led_blue():
    misty.changeLED(0, 0, 255)
    print("LED set to red")

#####################################################
#Move Arms# 
#################################################


# Function to raise the right arm
def raise_right_arm():
    misty.moveArm("right", -90, velocity=5)
    print("Raised right arm")

# Function to lower the right arm
def lower_right_arm():
    misty.moveArm("right", 90, velocity=5)
    print("Lowered right arm")

# Function to raise the left arm
def raise_left_arm():
    misty.moveArm("left", -90, velocity=5)
    print("Raised left arm")

# Function to lower the left arm
def lower_left_arm():
    misty.moveArm("left", 90, velocity=5)
    print("Lowered left arm")

# Function to raise both arms 
def raise_both_arms():
    misty.moveArms(-90, -90, 15, 15)
    print("Raised both arms")

# Function to lower both arms 
def lower_both_arms():
    misty.moveArms(89, 89, 15, 15)
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
   misty.speak("Hello, world!")




######
# Test Functions # 
print("\nTesting led light:")
# set_led_green()

# print("\nTesting arm movements:")
# raise_right_arm()
# time.sleep(5)
# lower_right_arm()
# time.sleep(5)
# set_led_red()
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



