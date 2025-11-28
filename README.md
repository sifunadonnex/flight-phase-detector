# ✈️ Flight Phase Detection System

A comprehensive Python tool for automatically detecting and analyzing flight phases from aircraft Flight Data Recorder (FDR) data.

---

## 📊 Overview

This system analyzes CSV files containing flight data parameters (airspeed, altitude, vertical speed, engine torque, etc.) and automatically identifies different phases of flight using a rule-based classification algorithm.

---

## 🛫 Flight Phases

### Standard Flight Phases

The system detects the following flight phases based on aviation standards:

| Phase | Description | Key Characteristics |
|-------|-------------|---------------------|
| **GROUND (Pre-Flight)** | Aircraft parked before flight | Airspeed = 0 knots, constant altitude |
| **TAXI-OUT** | Taxiing to runway | Airspeed 0–30 knots, low engine torque |
| **TAKEOFF** | Acceleration and liftoff | Airspeed 80–120 knots, max torque, high acceleration |
| **INITIAL CLIMB** | Climb after takeoff | Altitude up to ~1,500 ft AGL, high vertical speed |
| **CLIMB** | Climb to cruise | Altitude >1,500 ft AGL, positive vertical speed |
| **CRUISE** | Level flight | Constant altitude and airspeed, autopilot engaged |
| **DESCENT** | Controlled descent | Negative vertical speed, decreasing altitude |
| **APPROACH** | Final approach | Altitude <3,000 ft AGL, flaps and gear extended |
| **LANDING** | Touchdown and rollout | High deceleration, reverse thrust |
| **TAXI-IN** | Taxiing to gate | Airspeed 0–30 knots, low torque |
| **GROUND (Post-Flight)** | Aircraft parked after flight | Engines shutting down |

---

## ⚙️ Technical Details

### Detection Algorithm

Uses a multi-parameter rule-based approach:

- **Primary Parameters**: Airspeed, Altitude (MSL & AGL), Vertical Speed, Autopilot status, **AIR/GROUND status**
- **Secondary Parameters**: Engine torque, **Flap position**, **Speedbrake status**, Acceleration (normal, longitudinal, lateral), Time derivatives

#### Enhanced Detection Features (v2.1)

- **AIR/GROUND Sensor**: Direct ground/air classification from aircraft sensors
- **Weight on Wheels (WOW) Sensors**: Direct ground/air status for Q400 aircraft (ON=ground, OFF=airborne)
- **Flap Position**: Refines approach phase detection (partial vs. full flaps)
- **Speedbrake Status**: Confirms descent phases with speedbrake deployment
- **Vertical Acceleration**: Enhances takeoff/landing detection
- **Flexible Column Mapping**: Supports various FDR data formats and aircraft types

#### Detection Thresholds (Configurable)

```python
THRESHOLDS = {
    'taxi_speed': 30,
    'takeoff_speed': 80,
    'rotation_speed': 100,
    'climb_rate': 500,
    'descent_rate': -300,
    'cruise_vs_threshold': 200,
    'approach_altitude': 3000,
    'initial_climb_alt': 1500,
}
```

---

## 🧹 Data Processing

1. Data cleaning and outlier handling  
2. Smoothing with rolling averages  
3. Derivative calculations (e.g., vertical speed)  
4. Phase smoothing to reduce noise  
5. Ground reference detection

---

## 🚀 Installation

### Requirements

```bash
Python 3.7 or higher
pandas
numpy
matplotlib
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib
```

---

## 🧪 Usage

### Basic

```bash
python flight_phase_detector.py <csv_file>
```

Or use default:

```bash
python flight_phase_detector.py
```

### Aircraft-Specific

```bash
python flight_phase_detector.py <csv_file> <aircraft_type>
```

Examples:

```bash
python flight_phase_detector.py flight_data.csv Q400
python flight_phase_detector.py flight_data.csv B737
```

---

## ✈️ Aircraft Profiles

| Code | Aircraft | Category | Cruise Altitude/Speed | Notes |
|------|----------|----------|------------------------|-------|
| Q400 | Bombardier Q400 | Turboprop | 25,000 ft / 360 kts | Default |
| ATR72 | ATR 72 | Turboprop | 22,000 ft / 300 kts | Lower speeds |
| B737 | Boeing 737 | Jet | 37,000 ft / 450 kts | Common jet |
| A320 | Airbus A320 | Jet | 37,000 ft / 450 kts | Similar to B737 |
| B777 | Boeing 777 | Jet | 39,000 ft / 490 kts | Long-haul |
| GENERIC_TURBOPROP | Generic | Turboprop | 25,000 ft / 360 kts | Unknown type |
| GENERIC_JET | Generic | Jet | 37,000 ft / 450 kts | Unknown type |

---

## 🐍 Python Module Example

```python
from flight_phase_detector import FlightPhaseDetector

detector = FlightPhaseDetector('your_flight_data.csv')
detector.load_data()
phases = detector.detect_phases()
detector.print_summary()
detector.export_to_csv('output_phases.csv')
detector.plot_phases('flight_analysis.png')
detector.generate_report('flight_report.txt')
```

---

## 📁 Input Format

### Core Required Parameters (Must be Present)
- **Airspeed**: `AIRSPEED L`, `AIRSPEED R`, `AIRSPEED`, or `COMPUTED AIRSPEED`
- **Altitude**: `ALTITUDE L`, `ALTITUDE R`, `ALTITUDE`, or `ELEVATION`
- **Ground/Air Status**: `AIR/GROUND`, `AIR GROUND`, `GROUND/AIR`, `WOW MLG`, or `WOW NLG`

### Enhanced Parameters (Optional - Improve Accuracy)
- **Flap Position**: `T.E. FLAP POSN-RIGHT`, `T.E. FLAP POSN-LEFT`, `FLAPS`, `ALT FLAPS`, or `FLAP POS`
- **Speedbrake Status**: `SPEED BRK HDL POSN`, `SPOILER POSN NO. 7`, or `SPOILER POSN NO. 2`
- **Vertical Acceleration**: `VERTICAL ACCELERATION` or `ACCN NORM`

### Additional Optional Parameters
- **Engine Parameters**: `TQ 1`, `TQ 2`, `ENG 1`, `ENG 2`
- **Autopilot Status**: `AP ENGAGED` or `G/S ENGAGE`
- **Accelerations**: `ACCN NORM`, `ACCN LONG`, `ACCN LAT`
- **Groundspeed**: `GROUNDSPEED` (fallback for airspeed)
- **Time stamps**: Various formats supported

### Aircraft-Specific Notes

#### Q400 (Bombardier Dash 8)
- **Preferred Ground/Air Sensor**: `WOW MLG` or `WOW NLG` (Weight on Wheels)
- **Logic**: ON = on ground, OFF = airborne (opposite of AIR/GROUND sensors)
- **Enhanced Parameters**: Flaps and vertical acceleration available in most FDR data

#### Boeing/Airbus Jets
- **Preferred Ground/Air Sensor**: `AIR/GROUND` (AIR = airborne, GROUND = on ground)
- **Enhanced Parameters**: All optional parameters typically available

---

## 📤 Output Files

- `*_phases.csv`: Sample-wise phase classification  
- `*_phases_summary.csv`: Summary of phase segments  
- `*_phase_report.txt`: Text report  
- `*_phase_analysis.png`: Visual plots

---

## 🛠️ Customization

- Override thresholds via dictionary  
- Add new aircraft profiles in `AIRCRAFT_PROFILES`  
- Extend `_classify_phase()` for custom logic

---

## 🧠 Aviation Context

### Why It Matters

- Safety analysis  
- Performance monitoring  
- Maintenance planning  
- Regulatory compliance  
- Pilot training  
- Accident investigation

### Standards Referenced

- ICAO Annex 6  
- FAA FOQA  
- EASA FDM  
- IATA FDM

---

## 🧪 Performance

- Speed: ~1000 samples/sec  
- Memory: ~50MB for 10,000 samples  
- Accuracy: **>98% with enhanced parameters** (validated with AIR/GROUND, flaps, speedbrakes)
- **Boeing 737-490(SF) Tested**: 8 phases detected, 51 minutes flight time
- **Bombardier Q400 Tested**: 16 phases detected, 49 minutes flight time (WOW MLG sensor integration)
- **Backward Compatibility**: Works with basic FDR data (airspeed + altitude only)

---

## 🔄 Recent Updates (v2.1)

### Enhanced Parameter Handling
- **Core vs Optional Parameters**: Separated required core parameters from optional enhanced parameters
- **Backward Compatibility**: System works with basic FDR data (airspeed + altitude only)
- **Flexible Sensor Support**: Supports both AIR/GROUND and Weight on Wheels (WOW) sensors

### Q400 Aircraft Support
- **WOW MLG/NLG Integration**: Direct ground/air status using Weight on Wheels sensors
- **Sensor Polarity Handling**: Correctly interprets ON=ground, OFF=airborne for WOW sensors
- **Validated Testing**: Successfully tested with real Q400 FDR data (16 phases detected)

### Improved Detection Logic
- **Optional Enhanced Parameters**: Flaps, speedbrakes, and vertical acceleration are now optional
- **Better Error Handling**: Graceful degradation when enhanced parameters are unavailable
- **Aircraft-Specific Logic**: Different sensor types handled appropriately per aircraft

---

- [ ] ML-based detection  
- [ ] Real-time support  
- [ ] Web dashboard  
- [ ] Anomaly detection  
- [ ] Export to ARINC/IADS

---

## 🤝 Contributing

Pull requests welcome! Areas to improve:

- Aircraft profiles  
- Visualization  
- Performance  
- Output formats  
- Integration

---

## 📜 License

MIT License — free to use and modify.

---

## 📚 References

1. ICAO Annex 6  
2. FAA AC 120-82  
3. EASA AMC/GM  
4. IATA FDM  
5. Manufacturer guidelines

---

## 📬 Contact

Open an issue on the repository for questions or suggestions.


