# Quick Start Guide

## Installation & Setup

### Step 1: Install Python
Make sure you have Python 3.7 or higher installed:
```bash
python --version
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install pandas numpy matplotlib
```

## Running the Analysis

### Basic Usage (Default Q400 Profile)
Simply run the script with your CSV file:
```bash
python flight_phase_detector.py your_flight_data.csv
```

Or use the sample data:
```bash
python flight_phase_detector.py 5Y_TBX_Q400.csv
```

### Aircraft-Specific Analysis
Specify the aircraft type for optimized detection:
```bash
# Regional turboprops
python flight_phase_detector.py flight.csv Q400
python flight_phase_detector.py flight.csv ATR72

# Narrow-body jets
python flight_phase_detector.py flight.csv B737
python flight_phase_detector.py flight.csv A320

# Wide-body jets
python flight_phase_detector.py flight.csv B777

# Generic profiles (when aircraft type unknown)
python flight_phase_detector.py flight.csv GENERIC_TURBOPROP
python flight_phase_detector.py flight.csv GENERIC_JET
```

### Available Aircraft Types
| Code | Aircraft | Category |
|------|----------|----------|
| `Q400` | Bombardier Q400 | Regional Turboprop (default) |
| `ATR72` | ATR 72 | Regional Turboprop |
| `B737` | Boeing 737 | Narrow-Body Jet |
| `A320` | Airbus A320 | Narrow-Body Jet |
| `B777` | Boeing 777 | Wide-Body Jet |
| `GENERIC_TURBOPROP` | Generic Turboprop | Generic |
| `GENERIC_JET` | Generic Jet | Generic |

**See [AIRCRAFT_CONFIGURATIONS.md](AIRCRAFT_CONFIGURATIONS.md) for detailed threshold configurations**

### What You Get
The script will automatically generate:

1. **5Y_TBX_Q400_phases.csv** - Your original data with a new "PHASE" column
2. **5Y_TBX_Q400_phases_summary.csv** - Summary table of all flight phases
3. **5Y_TBX_Q400_phase_report.txt** - Detailed text report
4. **5Y_TBX_Q400_phase_analysis.png** - Visualization plots

## Understanding the Output

### Console Output
You'll see a summary like this:
```
================================================================================
FLIGHT PHASE SUMMARY
================================================================================

1. GROUND
   Samples: 1 - 166
   Duration: 1.38 minutes (83.0 seconds)
   Altitude: 129 ft → 129 ft (range: 96 - 129 ft)
   Airspeed: 0 kts → 0 kts (max: 0 kts)
   ...

2. TAXI-OUT
   ...
```

### Visual Output
The PNG file shows 4 plots:
- Altitude profile with color-coded phases
- Airspeed vs time
- Vertical speed vs time
- Engine torque vs time

## Using as a Python Module

```python
from flight_phase_detector import FlightPhaseDetector

# Create detector with aircraft type
detector = FlightPhaseDetector('5Y_TBX_Q400.csv', aircraft_type='Q400')

# Load and analyze
detector.load_data()
phases = detector.detect_phases()

# View summary
detector.print_summary()

# Export results
detector.export_to_csv()
detector.generate_report()
detector.plot_phases()

# Access phase data
for phase in phases:
    print(f"{phase['phase']}: {phase['duration_minutes']:.2f} minutes")
```

### Using Different Aircraft Profiles

```python
# Boeing 737
detector = FlightPhaseDetector('737_flight.csv', aircraft_type='B737')

# Airbus A320
detector = FlightPhaseDetector('a320_flight.csv', aircraft_type='A320')

# Generic jet (when exact type unknown)
detector = FlightPhaseDetector('unknown_jet.csv', aircraft_type='GENERIC_JET')
```

## Customizing Detection

### Method 1: Use Appropriate Aircraft Profile
The easiest way - just select the right aircraft type:
```python
detector = FlightPhaseDetector('flight.csv', aircraft_type='B737')
```

### Method 2: Custom Thresholds
Start with a base profile and override specific thresholds:
```python
custom_thresholds = {
    'takeoff_speed': 90,           # Adjust for different weights
    'cruise_vs_threshold': 150,    # Stricter cruise definition
    'approach_altitude': 2500,     # Different procedures
}

detector = FlightPhaseDetector('flight.csv', 'B737', custom_thresholds)
detector.load_data()
detector.detect_phases()
```

### Method 3: Modify After Initialization
```python
detector = FlightPhaseDetector('your_data.csv', 'Q400')

# Customize for specific conditions
detector.THRESHOLDS['takeoff_speed'] = 85  # knots
detector.THRESHOLDS['cruise_vs_threshold'] = 150  # fpm

detector.load_data()
detector.detect_phases()
```

### Aircraft Profile Thresholds
Each aircraft type has optimized thresholds:
- **Speeds**: `taxi_speed`, `takeoff_speed`, `rotation_speed`
- **Rates**: `climb_rate`, `descent_rate`, `cruise_vs_threshold`
- **Altitudes**: `approach_altitude`, `initial_climb_alt`, `landing_altitude`

**See [AIRCRAFT_CONFIGURATIONS.md](AIRCRAFT_CONFIGURATIONS.md) for complete threshold tables**

## CSV File Format

Your CSV should have these columns (minimum):
- `AIRSPEED L` / `AIRSPEED R` - Left/right airspeed (knots)
- `ALTITUDE L` / `ALTITUDE R` - Left/right altitude (feet)
- `TQ 1` / `TQ 2` - Engine torque (%)
- `AP ENGAGED` - Autopilot status
- `ACCN NORM` / `ACCN LONG` / `ACCN LAT` - Accelerations (g)

See `5Y_TBX_Q400.csv` for example format.

## Common Issues

### Issue: File not found
```
Error: File 'your_file.csv' not found!
```
**Solution**: Check file path is correct and file exists

### Issue: Column name errors
```
KeyError: 'AIRSPEED L'
```
**Solution**: Ensure CSV has required columns with correct names

### Issue: Poor phase detection
**Solution**: 
1. Try a different aircraft profile (Q400, B737, A320, etc.)
2. Use GENERIC_TURBOPROP or GENERIC_JET if exact type unknown
3. Adjust thresholds using custom_thresholds parameter
4. See [AIRCRAFT_CONFIGURATIONS.md](AIRCRAFT_CONFIGURATIONS.md) for tuning guidance

## Next Steps

1. **Choose your aircraft profile**: See available types above or in [AIRCRAFT_CONFIGURATIONS.md](AIRCRAFT_CONFIGURATIONS.md)
2. **Read the full documentation**: See `README.md` for detailed information
3. **Research flight phases**: See `FLIGHT_PHASES_RESEARCH.md` for aviation background
4. **Try examples**: Run `python example_usage.py` for more usage examples
5. **Customize**: Modify thresholds and detection logic for your needs

## Support

For questions or issues:
1. Check the README.md for detailed documentation
2. Review FLIGHT_PHASES_RESEARCH.md for aviation concepts
3. Open an issue on the repository

## License

MIT License - Free to use and modify
