import time
from zoomus import ZoomClient

# Zoom API constants
API_KEY = "YOUR_ZOOM_API_KEY"
API_SECRET = "YOUR_ZOOM_API_SECRET"
MEETING_ID = "YOUR_ZOOM_MEETING_ID"

# Initialize Zoom client
client = ZoomClient(API_KEY, API_SECRET)


# Function to grant multipin and lower hand
def grant_multipin_and_lower_hand(participant_id):
    response = client.meeting.participant_control(MEETING_ID, "unmute", participant_id)
    if response.get("status") == "success":
        print("Multipin granted successfully and hand lowered.")
    else:
        print("Failed to grant multipin and lower hand.")


# Main function
def main():
    while True:
        response = client.meeting.list(part_meeting_id=MEETING_ID)
        if response.get("status") == "success":
            participants = response.get("participants", [])
            for participant in participants:
                if participant.get("user_id") and participant.get("user_info").get(
                    "hand_raised"
                ):
                    grant_multipin_and_lower_hand(participant.get("user_id"))
        time.sleep(5)  # Check for raise hand status every 5 seconds


if __name__ == "__main__":
    main()
