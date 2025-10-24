# Aircraft Configurations and Thresholds

## Overview

The Flight Phase Detection System supports multiple aircraft types with predefined threshold configurations. Each configuration is optimized for the specific performance characteristics of that aircraft type.

## Using Aircraft Profiles

### Command Line

```bash
# Use specific aircraft type
python flight_phase_detector.py flight_data.csv B737
python flight_phase_detector.py flight_data.csv A320
python flight_phase_detector.py flight_data.csv Q400
```

### Python API

```python
from flight_phase_detector import FlightPhaseDetector

# Using predefined profile
detector = FlightPhaseDetector('flight.csv', aircraft_type='B737')

# Using custom thresholds
custom = {'takeoff_speed': 95, 'cruise_vs_threshold': 150}
detector = FlightPhaseDetector('flight.csv', 'A320', custom_thresholds=custom)
```

## Predefined Aircraft Profiles

### Regional Turboprops

#### Bombardier Q400
**Code**: `Q400`

| Parameter | Value | Unit | Description |
|-----------|-------|------|-------------|
| Taxi Speed | 30 | knots | Maximum speed for taxi phase |
| Takeoff Speed | 80 | knots | Speed indicating takeoff roll |
| Rotation Speed | 100 | knots | Typical rotation speed (Vr) |
| Climb Rate | 500 | fpm | Minimum vertical speed for climb |
| Descent Rate | -300 | fpm | Maximum vertical speed for descent |
| Cruise VS Threshold | 200 | fpm | Max vertical speed variation in cruise |
| Approach Altitude | 3000 | ft AGL | Altitude threshold for approach phase |
| Initial Climb Alt | 1500 | ft AGL | Threshold for initial climb phase |
| Landing Altitude | 500 | ft AGL | Altitude variation for landing |
| **Typical Cruise Alt** | 25,000 | ft | Reference cruise altitude |
| **Typical Cruise Speed** | 360 | knots | Reference cruise speed |

**Notes**:
- Twin turboprop regional aircraft
- High-frequency short-haul operations
- Excellent short-field performance
- Typical routes: 100-500 nm

#### ATR 72
**Code**: `ATR72`

| Parameter | Value | Unit | Description |
|-----------|-------|------|-------------|
| Taxi Speed | 25 | knots | Maximum speed for taxi phase |
| Takeoff Speed | 75 | knots | Speed indicating takeoff roll |
| Rotation Speed | 95 | knots | Typical rotation speed |
| Climb Rate | 500 | fpm | Minimum vertical speed for climb |
| Descent Rate | -300 | fpm | Maximum vertical speed for descent |
| Cruise VS Threshold | 200 | fpm | Max vertical speed variation in cruise |
| Approach Altitude | 3000 | ft AGL | Altitude threshold for approach |
| Initial Climb Alt | 1500 | ft AGL | Threshold for initial climb |
| Landing Altitude | 500 | ft AGL | Altitude variation for landing |
| **Typical Cruise Alt** | 22,000 | ft | Reference cruise altitude |
| **Typical Cruise Speed** | 300 | knots | Reference cruise speed |

**Notes**:
- Fuel-efficient turboprop
- Lower speeds than Q400
- Ideal for thin routes

---

### Narrow-Body Jets

#### Boeing 737
**Code**: `B737`

| Parameter | Value | Unit | Description |
|-----------|-------|------|-------------|
| Taxi Speed | 30 | knots | Maximum speed for taxi phase |
| Takeoff Speed | 100 | knots | Speed indicating takeoff roll |
| Rotation Speed | 140 | knots | Typical rotation speed |
| Climb Rate | 800 | fpm | Minimum vertical speed for climb |
| Descent Rate | -500 | fpm | Maximum vertical speed for descent |
| Cruise VS Threshold | 200 | fpm | Max vertical speed variation in cruise |
| Approach Altitude | 3000 | ft AGL | Altitude threshold for approach |
| Initial Climb Alt | 1500 | ft AGL | Threshold for initial climb |
| Landing Altitude | 500 | ft AGL | Altitude variation for landing |
| **Typical Cruise Alt** | 37,000 | ft | Reference cruise altitude |
| **Typical Cruise Speed** | 450 | knots | Reference cruise speed (M0.78) |

**Notes**:
- Most common commercial jet aircraft
- Variants: 737-700, 737-800, 737 MAX
- Short to medium-haul operations
- Typical routes: 200-3,000 nm

#### Airbus A320
**Code**: `A320`

| Parameter | Value | Unit | Description |
|-----------|-------|------|-------------|
| Taxi Speed | 30 | knots | Maximum speed for taxi phase |
| Takeoff Speed | 95 | knots | Speed indicating takeoff roll |
| Rotation Speed | 135 | knots | Typical rotation speed |
| Climb Rate | 800 | fpm | Minimum vertical speed for climb |
| Descent Rate | -500 | fpm | Maximum vertical speed for descent |
| Cruise VS Threshold | 200 | fpm | Max vertical speed variation in cruise |
| Approach Altitude | 3000 | ft AGL | Altitude threshold for approach |
| Initial Climb Alt | 1500 | ft AGL | Threshold for initial climb |
| Landing Altitude | 500 | ft AGL | Altitude variation for landing |
| **Typical Cruise Alt** | 37,000 | ft | Reference cruise altitude |
| **Typical Cruise Speed** | 450 | knots | Reference cruise speed (M0.78) |

**Notes**:
- Direct competitor to Boeing 737
- Family: A318, A319, A320, A321
- Fly-by-wire flight controls
- Similar performance to 737

---

### Wide-Body Jets

#### Boeing 777
**Code**: `B777`

| Parameter | Value | Unit | Description |
|-----------|-------|------|-------------|
| Taxi Speed | 35 | knots | Maximum speed for taxi phase |
| Takeoff Speed | 120 | knots | Speed indicating takeoff roll |
| Rotation Speed | 160 | knots | Typical rotation speed |
| Climb Rate | 1000 | fpm | Minimum vertical speed for climb |
| Descent Rate | -800 | fpm | Maximum vertical speed for descent |
| Cruise VS Threshold | 250 | fpm | Max vertical speed variation in cruise |
| Approach Altitude | 3000 | ft AGL | Altitude threshold for approach |
| Initial Climb Alt | 1500 | ft AGL | Threshold for initial climb |
| Landing Altitude | 500 | ft AGL | Altitude variation for landing |
| **Typical Cruise Alt** | 39,000 | ft | Reference cruise altitude |
| **Typical Cruise Speed** | 490 | knots | Reference cruise speed (M0.84) |

**Notes**:
- Long-haul wide-body aircraft
- Variants: 777-200, 777-300, 777X
- Higher speeds and climb rates
- Typical routes: 2,000-8,000 nm

---

### Generic Profiles

#### Generic Turboprop
**Code**: `GENERIC_TURBOPROP`

Use this profile when:
- Exact aircraft type is unknown
- Aircraft is a regional turboprop
- Similar to Q400/ATR/Dash 8

Configuration: Same as Q400 profile

#### Generic Jet
**Code**: `GENERIC_JET`

Use this profile when:
- Exact aircraft type is unknown
- Aircraft is a commercial jet
- Similar to B737/A320

Configuration: Same as B737 profile

---

## Regulatory Standards

### FAA (Federal Aviation Administration)
**Standard**: AC 120-82 - Flight Operational Quality Assurance

Key Criteria:
- **Approach Altitude**: 3,000 ft AGL - Begin approach phase
- **Stabilized Approach**: 1,000 ft AGL - Must be stabilized
- **Decision Altitude**: 500 ft AGL - Go-around decision point

### EASA (European Aviation Safety Agency)
**Standard**: AMC/GM to Part-ORO - Flight Data Monitoring

Key Criteria:
- **Approach Altitude**: 3,000 ft AGL
- **Stabilized Approach**: 1,000 ft AGL (500 ft in IMC)
- **Final Approach**: Below 1,000 ft AGL

### IATA (International Air Transport Association)
**Standard**: Flight Data Analysis Best Practices

Key Criteria:
- Standardized phase definitions
- Event exceedance monitoring
- Safety performance indicators

---

## Customizing Thresholds

### Method 1: Custom Thresholds in Code

```python
from flight_phase_detector import FlightPhaseDetector

# Start with a base profile and override specific values
custom_thresholds = {
    'takeoff_speed': 85,           # Adjust for different weights
    'rotation_speed': 105,
    'cruise_vs_threshold': 150,    # Stricter cruise definition
    'approach_altitude': 2500,     # Different airport procedures
}

detector = FlightPhaseDetector('flight.csv', 'Q400', custom_thresholds)
```

### Method 2: Modify Aircraft Profile

Edit `flight_phase_detector.py` and add your custom profile:

```python
AIRCRAFT_PROFILES = {
    # ... existing profiles ...
    
    'MY_CUSTOM': {
        'name': 'My Custom Aircraft Configuration',
        'taxi_speed': 30,
        'takeoff_speed': 80,
        # ... all other thresholds
    }
}
```

### Method 3: Runtime Configuration

```python
detector = FlightPhaseDetector('flight.csv', 'B737')

# Adjust after initialization
detector.THRESHOLDS['cruise_vs_threshold'] = 150
detector.THRESHOLDS['approach_altitude'] = 2500

# Then proceed with analysis
detector.load_data()
detector.detect_phases()
```

---

## Threshold Definitions

### Speed Thresholds

- **taxi_speed**: Maximum groundspeed for taxi phase (5-35 knots)
- **takeoff_speed**: Minimum speed indicating takeoff roll has begun (75-120 knots)
- **rotation_speed**: Speed at which aircraft rotates for takeoff (95-160 knots)

### Vertical Speed Thresholds

- **climb_rate**: Minimum vertical speed to classify as climb (500-1000 fpm)
- **descent_rate**: Maximum vertical speed to classify as descent (-300 to -800 fpm)
- **cruise_vs_threshold**: Maximum absolute vertical speed for level flight (150-250 fpm)

### Altitude Thresholds

- **approach_altitude**: Altitude below which approach phase begins (typically 3,000 ft AGL)
- **initial_climb_alt**: Altitude separating initial climb from climb (typically 1,500 ft AGL)
- **landing_altitude**: Altitude variation indicating landing phase (typically 500 ft AGL)
- **final_approach_alt**: Altitude for final approach phase (typically 1,000 ft AGL)

---

## Adding New Aircraft Types

To add a new aircraft type:

1. Research the aircraft's performance characteristics
2. Determine typical speeds (V1, VR, V2, cruise, approach)
3. Determine typical climb/descent rates
4. Add to `AIRCRAFT_PROFILES` dictionary:

```python
'NEW_AIRCRAFT': {
    'name': 'Aircraft Name (Category)',
    'taxi_speed': XX,
    'takeoff_speed': XX,
    'rotation_speed': XX,
    'climb_rate': XXX,
    'descent_rate': -XXX,
    'cruise_vs_threshold': XXX,
    'approach_altitude': XXXX,
    'initial_climb_alt': XXXX,
    'landing_altitude': XXX,
    'typical_cruise_alt': XXXXX,
    'typical_cruise_speed': XXX,
}
```

### Reference Sources

1. **Aircraft Flight Manual (AFM)**: Authoritative source for V-speeds
2. **Quick Reference Handbook (QRH)**: Typical operating speeds
3. **FCOM (Flight Crew Operating Manual)**: Normal procedures and speeds
4. **Type Certificate Data Sheet (TCDS)**: FAA/EASA certified performance
5. **Flight Data Monitoring Reports**: Historical data from operations

---

## Validation and Testing

### Recommended Validation Process

1. **Visual Inspection**: Review phase detection plots
2. **Spot Checks**: Manually verify 10-20 random samples
3. **Edge Cases**: Test with unusual flight profiles
4. **Cross-Validation**: Compare with pilot logs or other systems

### Quality Metrics

- **Phase Accuracy**: >95% for standard flights
- **Transition Accuracy**: ±5 seconds for phase transitions
- **False Positives**: <2% spurious phase detections

### Tuning Tips

If detection is inaccurate:

1. **Too many taxi detections**: Increase `taxi_speed`
2. **Missed takeoff**: Lower `takeoff_speed`
3. **Cruise oscillation**: Increase `cruise_vs_threshold`
4. **Late approach detection**: Increase `approach_altitude`
5. **Early landing detection**: Decrease `landing_rollout_alt`

---

## Compliance Notes

### Flight Data Monitoring (FDM)

This system's phase definitions align with:
- ICAO Annex 6 requirements
- FAA AC 120-82 guidelines
- EASA Part-ORO regulations
- IATA FDM best practices

### Safety Reporting

Detected phases can be used for:
- Safety event classification
- Exceedance monitoring
- Trend analysis
- Risk assessment

### Data Privacy

Flight data may contain sensitive information:
- Follow operator's data handling policies
- Comply with GDPR/local privacy laws
- Anonymize data when sharing
- Secure storage and transmission

---

## Support and Updates

### Getting Help

- Check documentation: `README.md`, `QUICKSTART.md`
- Review examples: `example_usage.py`
- Aviation research: `FLIGHT_PHASES_RESEARCH.md`

### Contributing

To contribute new aircraft profiles or improvements:
1. Validate thresholds with actual flight data
2. Document source of threshold values
3. Test with multiple flights of that aircraft type
4. Submit with example validation results

---

*Last Updated: October 2025*
*Version: 2.0*
