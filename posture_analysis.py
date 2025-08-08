import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose

def analyze_posture(image):
    with mp_pose.Pose(static_image_mode=True) as pose:
        results = pose.process(image)

        if not results.pose_landmarks:
            return {"error": "No human detected."}

        landmarks = results.pose_landmarks.landmark

        left_ear = landmarks[mp_pose.PoseLandmark.LEFT_EAR]
        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
        left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP]

        head_forward = left_ear.x < left_shoulder.x - 0.03
        pelvis_angle = left_shoulder.y - left_hip.y
        anterior_pelvic_tilt = pelvis_angle < 0.1
        kyphosis = (left_ear.y - left_shoulder.y) > 0.1

        problems = []
        advice = {}

        if head_forward:
            problems.append("Forward Head Posture")
            advice["Forward Head Posture"] = "Consider chin tucks and reducing screen time to improve posture."

        if anterior_pelvic_tilt:
            problems.append("Anterior Pelvic Tilt")
            advice["Anterior Pelvic Tilt"] = "Stretch the hip flexors and strengthen glutes through bridges or lunges."

        if kyphosis:
            problems.append("Rounded Shoulders")
            advice["Rounded Shoulders"] = "Perform back extension exercises and strengthen scapular retractors."

        return {
            "postureProblems": problems,
            "advice": advice
        }
