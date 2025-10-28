# interactive_logic_riddles_10.py

def print_riddle(number, title, story, current_state, options, diagram, formula):
    print(f"\n{'='*100}")
    print(f"{number}️⃣ {title}\n")
    print(f"Story: {story}\n")
    print(f"Current State: {current_state}\n")
    print(f"Options: {options}\n")
    print("Logic Gate Diagram:")
    print(diagram)
    print("\nLogic Formula (LaTeX style):")
    print(formula)
    print(f"{'='*100}\n")


def main():
    riddles = []

    # ----- RIDDLE 1 -----
    riddles.append({
        "number": "1",
        "title": "Lab Entrance Door",
        "story": "The entrance door opens only if the master key is inserted and the code entered, "
                 "or if the emergency override is active and the maintenance hatch is closed, "
                 "or if the backup battery is active, main power functional, and sensors detect no tampering. "
                 "Additionally, the biometric scan must match an authorized user or override must be on.",
        "current_state": "Master key missing, code not entered, override dark, backup battery active, main power on, sensors normal, biometric mismatch.",
        "options": "A. Door can open (Q)  B. Door cannot open (L) ✅  C. Cannot be determined (Z)",
        "diagram": """\
MasterKey ----\\
                AND ----\\
Code ---------/          \\
                           OR ----\\
Override ----\\             \\
              AND ----\\    \\
HatchClosed -/          OR ---- DoorOpen
BackupBattery --\\     /
Power --------- AND --/
Sensors ------/
Biometric -- OR
Override ---/
""",
        "formula": r"DoorOpen = (MasterKey \land Code) \lor (Override \land HatchClosed) \lor (BackupBattery \land Power \land Sensors) \lor (BiometricMatch \lor Override)"
    })

    # ----- RIDDLE 2 -----
    riddles.append({
        "number": "2",
        "title": "Hallway Motion Sensors",
        "story": "The alarm triggers if motion is detected while the fire alarm is inactive, "
                 "or if windows are open and doors unlocked while the override is off, "
                 "or if pressure sensors alert and the emergency lockdown is not active. "
                 "Also, if the temperature sensor reads extreme heat, the alarm triggers unless the system is in maintenance mode.",
        "current_state": "No motion, windows closed, doors locked, fire alarm active, override off, pressure normal, lockdown inactive, temperature normal, maintenance off.",
        "options": "A. Alarm triggers (K)  B. Alarm does not trigger (M) ✅  C. Cannot be determined (X)",
        "diagram": """\
MotionSensor ---\\
                 AND --\\
FireAlarmOff ---/       \\
                          OR ----\\
WindowOpen ----\\          \\
DoorUnlocked -- AND ---- OR ---- Alarm
OverrideOff ----/          /
PressureAlert ---\\       /
LockdownInactive - AND --/
TempExtreme -----\\
MaintenanceOff --- AND --/
""",
        "formula": r"Alarm = (MotionSensor \land FireAlarmOff) \lor (WindowOpen \land DoorUnlocked \land OverrideOff) \lor (PressureAlert \land LockdownInactive) \lor (TempExtreme \land MaintenanceOff)"
    })

    # ----- RIDDLE 3 -----
    riddles.append({
        "number": "3",
        "title": "Security Badge Scans",
        "story": "A person's presence is confirmed if badge scan is positive and camera evidence matches, "
                 "or if at least two witnesses report seeing them, "
                 "or if the access log shows entry and biometric matches or override is active. "
                 "Alibi is valid only if none of these conditions confirm presence.",
        "current_state": "Badge scan partial, CCTV blurry, witnesses conflicting, access log positive, biometric mismatch, override off.",
        "options": "A. Suspect was in lab (X) ✅  B. Suspect not in lab (W)  C. Cannot be determined (Z)",
        "diagram": """\
BadgeScan ---\\
             AND ---\\
CCTV --------/       \\
                        OR ----\\
Witness1 ---\\           \\
Witness2 --- AND ------ OR ---- Present
AccessLog --\\         /
Biometric --- AND ---/
Override ----/
AlibiValid = NOT(Present)
""",
        "formula": r"Present = (BadgeScan \land CCTV) \lor (Witness1 \land Witness2) \lor (AccessLog \land (BiometricMatch \lor Override))\nAlibiValid = \lnot(Present)"
    })

    # ----- RIDDLE 4 -----
    riddles.append({
        "number": "4",
        "title": "Server Room Access",
        "story": "Access is granted if the security badge is valid and the pin is correct, "
                 "or if a manager override exists and CCTV is functional, "
                 "or if the emergency lockdown is inactive and the backup generator is running. "
                 "Further, access is only allowed if the smoke sensor does not detect fire.",
        "current_state": "Badge valid, pin incorrect, manager override off, CCTV functional, lockdown inactive, generator active, smoke clear.",
        "options": "A. Access granted (A) ✅  B. Access denied (B)  C. Cannot be determined (C)",
        "diagram": """\
BadgeValid ---\\
              AND ----\\
PinCorrect ---/         \\
                          OR ----\\
ManagerOverride ---\\      \\
CCTVFunctional --- AND -- OR ---- Access
LockdownInactive ---\\    /
BackupGenActive ---- AND -/
SmokeClear --------- AND --/
""",
        "formula": r"Access = ((BadgeValid \land PinCorrect) \lor (ManagerOverride \land CCTVFunctional) \lor (LockdownInactive \land BackupGenActive)) \land SmokeClear"
    })

    # ----- RIDDLE 5 -----
    riddles.append({
        "number": "5",
        "title": "Laboratory Chemical Alarm",
        "story": "The chemical alarm sounds if a high temperature is detected or pressure exceeds limits, "
                 "unless the safety override is active. "
                 "Additionally, if the ventilation system fails and the door is locked, the alarm will trigger. "
                 "Finally, if a spill sensor detects leakage and the containment is breached, the alarm sounds.",
        "current_state": "Temperature normal, pressure normal, safety override off, ventilation functional, door locked, spill detected, containment intact.",
        "options": "A. Alarm sounds (H)  B. Alarm does not sound (I) ✅  C. Cannot be determined (J)",
        "diagram": """\
HighTemp ---\\
            OR ---\\
HighPressure -/       \\
                     AND ---- NOT ---- SafetyOverride
VentFail ---\\
DoorLocked - AND ---- OR ---- Alarm
SpillDetected ---\\
ContainBreached - AND -/
""",
        "formula": r"Alarm = ((HighTemp \lor HighPressure) \land \lnot SafetyOverride) \lor (VentFail \land DoorLocked) \lor (SpillDetected \land ContainBreached)"
    })

    # ----- RIDDLE 6 -----
    riddles.append({
        "number": "6",
        "title": "Data Center Cooling",
        "story": "Cooling activates if the temperature exceeds threshold and fans are operational, "
                 "or if emergency coolant is available and power is stable. "
                 "If both main and secondary sensors detect overheating, cooling is also triggered. "
                 "Additionally, if the server load is high, cooling activates unless maintenance mode is on.",
        "current_state": "Temp normal, fans operational, emergency coolant available, power stable, main sensor normal, secondary sensor normal, server load high, maintenance off.",
        "options": "A. Cooling activates (C) ✅  B. Cooling does not activate (D)  C. Cannot be determined (E)",
        "diagram": """\
TempHigh ---\\
            AND ----\\
FansOperational -/       \\
                         OR ----\\
EmergencyCoolant ---\\    \\
PowerStable ------- AND -- OR ---- Cooling
MainSensorHigh ---\\      /
SecondarySensorHigh - AND -/
ServerLoadHigh ---\\
MaintenanceOff ---- AND --/
""",
        "formula": r"Cooling = (TempHigh \land FansOperational) \lor (EmergencyCoolant \land PowerStable) \lor (MainSensorHigh \land SecondarySensorHigh) \lor (ServerLoadHigh \land \lnot Maintenance)"
    })

    # ----- RIDDLE 7 -----
    riddles.append({
        "number": "7",
        "title": "Rooftop Security",
        "story": "The alarm on the rooftop triggers if motion is detected and cameras are online, "
                 "or if pressure mats detect intruders while lights are off, "
                 "or if vibration sensors detect movement and access doors are unlocked. "
                 "Additionally, remote override can force alarm on regardless of other conditions.",
        "current_state": "Motion normal, cameras online, mats clear, lights on, vibration normal, doors locked, override off.",
        "options": "A. Alarm triggers (F)  B. Alarm does not trigger (G) ✅  C. Cannot be determined (H)",
        "diagram": """\
MotionDetected ---\\
                   AND ----\\
CamerasOnline ---/          \\
                             OR ----\\
PressureMat ---\\             \\
LightsOff ----- AND -------- OR ---- Alarm
VibrationDetected ---\\      /
DoorsUnlocked -------- AND -/
Override ----------- OR ----/
""",
        "formula": r"Alarm = (MotionDetected \land CamerasOnline) \lor (PressureMat \land LightsOff) \lor (VibrationDetected \land DoorsUnlocked) \lor Override"
    })

    # ----- RIDDLE 8 -----
    riddles.append({
        "number": "8",
        "title": "Server Authentication",
        "story": "Access is granted if username and password match, "
                 "or if two-factor authentication is valid and the IP address is whitelisted, "
                 "or if admin override is active. "
                 "Additionally, access fails if the account is locked unless override is present.",
        "current_state": "Username correct, password wrong, 2FA valid, IP whitelisted, admin override off, account unlocked.",
        "options": "A. Access granted (L) ✅  B. Access denied (M)  C. Cannot be determined (N)",
        "diagram": """\
Username ---\\
Password --- AND ----\\
                     OR ----\\
2FA ---\\               \\
IPWhitelisted - AND ---- OR ---- Access
AdminOverride ---------- OR ----/
AccountLocked --- NOT --- AND --/
""",
        "formula": r"Access = ((Username \land Password) \lor (2FA \land IPWhitelisted) \lor AdminOverride) \land (\lnot AccountLocked \lor AdminOverride)"
    })

    # ----- RIDDLE 9 -----
    riddles.append({
        "number": "9",
        "title": "Laboratory Containment",
        "story": "Containment is secure if doors are locked and sensors detect no breach, "
                 "or if override is active, "
                 "or if pressure valves are functional and backup locks engaged. "
                 "Additionally, containment fails if emergency vent is open unless override is on.",
        "current_state": "Doors locked, sensors normal, override off, pressure valves functional, backup locks engaged, vent closed.",
        "options": "A. Containment secure (P) ✅  B. Containment breached (Q)  C. Cannot be determined (R)",
        "diagram": """\
DoorsLocked ---\\
SensorsNormal - AND ----\\
                       OR ----\\
Override ----------- OR ---- Containment
PressureValves ---\\
BackupLocks ----- AND -/
EmergencyVent --- NOT --- AND ----/
Override ----------- OR ----/
""",
        "formula": r"Containment = ((DoorsLocked \land SensorsNormal) \lor Override \lor (PressureValves \land BackupLocks)) \land (\lnot EmergencyVent \lor Override)"
    })

    # ----- RIDDLE 10 -----
    riddles.append({
        "number": "10",
        "title": "Power Grid Safety",
        "story": "Safety is maintained if main breaker is closed and backup generator online, "
                 "or if all circuit sensors report normal, "
                 "or if remote override is active. "
                 "Additionally, if voltage spikes occur, safety depends on surge protectors or override being active.",
        "current_state": "Main breaker closed, backup generator online, all sensors normal, override off, voltage normal, surge protectors active.",
        "options": "A. Safety maintained (S) ✅  B. Safety compromised (T)  C. Cannot be determined (U)",
        "diagram": """\
MainBreaker ---\\
BackupGen --- AND ----\\
                       OR ----\\
SensorsNormal ---------- OR ---- Safety
RemoteOverride ---------- OR ----/
VoltageSpike --- AND ----\\
SurgeProtector --- OR ----/
RemoteOverride --- OR ----/
""",
        "formula": r"Safety = ((MainBreaker \land BackupGen) \lor SensorsNormal \lor RemoteOverride) \land ((\lnot VoltageSpike) \lor SurgeProtector \lor RemoteOverride)"
    })

    # ----- LOOP THROUGH RIDDLES -----
    for r in riddles:
        print_riddle(
            r["number"],
            r["title"],
            r["story"],
            r["current_state"],
            r["options"],
            r["diagram"],
            r["formula"]
        )

        while True:
            cont = input("Do you want to continue to the next riddle? (y/n): ").strip().lower()
            if cont in ("y", "n"):
                break
            print("Please enter 'y' or 'n'.")
        if cont == "n":
            print("Exiting the game. Goodbye!")
            break


if __name__ == "__main__":
    main()
