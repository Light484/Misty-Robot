from control import * 
import time

# Function to simulate Misty's gaze towards the participant
def gaze_at_participant():
    # Add code here to physically make Misty gaze at the participant
    print("Simulated gaze at participant.")
    pitch = 5    # Vertical movement (tilting the head up or down)
    roll = 5     # Side tilt (rotating the head along the axis going through the nose)
    yaw = 10     # Horizontal movement (turning the head left or right)
    misty.moveHead(pitch=pitch, roll=roll, yaw=yaw)

def run_experiment():
    num_trials = 1  # Number of trials

    for trial in range(num_trials):
        # Gaze towards participant
        # gaze_at_participant()
        

        # LED green (follow)
        set_led_green()
        time.sleep(1)

        raise_right_arm()
        time.sleep(1)

        raise_left_arm()
        time.sleep(1)

        lower_both_arms()
        time.sleep(1)

        set_led_blue()
        time.sleep(1)

        raise_both_arms()
        time.sleep(1)

        raise_left_arm()
        time.sleep(1)


        set_led_red()
        time.sleep(1)

        raise_right_arm()
        time.sleep(1)

        set_led_green()
        time.sleep(1)

        lower_left_arm()
        time.sleep(1)

        raise_both_arms()
        time.sleep(1)

        # Wait before next trial
        time.sleep(1)

    # End of experiment
    print("Experiment complete!")

if __name__ == "__main__":
    run_experiment()
