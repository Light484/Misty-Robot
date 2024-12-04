import mistyPy
from control import * 

mia = mistyPy.Robot("10.5.11.234")

reply = mia.populateImages()
print("Reply from robot:", reply)  # Debugging line

# Function to simulate Misty's gaze towards the participant
def gaze_at_participant():
    # Add code here to physically make Misty gaze at the participant
    print("Simulated gaze at participant.")
    pitch = 5    # Vertical movement (tilting the head up or down)
    roll = 5     # Side tilt (rotating the head along the axis going through the nose)
    yaw = 10     # Horizontal movement (turning the head left or right)
    misty.moveHead(pitch=pitch, roll=roll, yaw=yaw)

def run_experiment():
    num_trials = 2  # Number of trials

    for trial in range(num_trials):
        # Gaze towards participant
        # gaze_at_participant()
        

        # LED green (follow)
        set_led_green()
        time.sleep(1)

        # Perform actions with and without "Simon says"
        misty_speak("Simon says, raise your right arm.")
        raise_right_arm()

        misty_speak("Raise your left arm.")  # No "Simon says"
        raise_left_arm()

        misty_speak("Simon says, raise both arms.")
        raise_both_arms()

        misty_speak(" Simon says, Lower your right arm.")  # No "Simon says"
        lower_right_arm()

        misty_speak("Simon says, lower your left arm.")
        lower_left_arm()

        misty_speak("Lower both arms.")  # No "Simon says"
        lower_both_arms()

        misty_speak("Simon says, smile.")
        set_smile()

        misty_speak("Frown.")  # No "Simon says"
        set_frown()

        # LED red (invert)
        set_led_red()
        misty_speak("Invert my command!")

        # Perform inverted actions with and without "Simon says"
        misty_speak("Simon says, lower your right arm.")
        lower_right_arm()

        misty_speak("Lower your left arm.")  # No "Simon says"
        lower_left_arm()

        misty_speak("Simon says, lower both arms.")
        lower_both_arms()

        misty_speak(" Simon says, Raise your right arm.")
        raise_right_arm()

        misty_speak("Simon says, raise your left arm.")
        raise_left_arm()

        misty_speak("Raise both arms.")  # No "Simon says"
        raise_both_arms()

        # Wait before next trial
        time.sleep(3)

    # End of experiment
    misty_speak("Experiment complete. Thank you!")
    print("Experiment complete!")

if __name__ == "__main__":
    run_experiment()
