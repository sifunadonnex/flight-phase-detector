# Flight Phases - Comprehensive Research

## Table of Contents
1. [Introduction](#introduction)
2. [Standard Flight Phases](#standard-flight-phases)
3. [Aviation Industry Standards](#aviation-industry-standards)
4. [Parameters Used for Detection](#parameters-used-for-detection)
5. [Safety and Risk Considerations](#safety-and-risk-considerations)
6. [Aircraft-Specific Variations](#aircraft-specific-variations)
7. [References](#references)

---

## Introduction

Flight phase identification is crucial for:
- **Flight Safety Analysis**: Different phases have different risk profiles
- **Flight Data Monitoring (FDM)**: Required by aviation regulators
- **Accident Investigation**: Understanding the sequence of events
- **Performance Analysis**: Fuel efficiency, engine health monitoring
- **Pilot Training**: Understanding normal flight profiles
- **Maintenance Planning**: Component wear varies by phase

Aviation authorities worldwide (FAA, EASA, ICAO) require systematic flight data analysis, with phase identification being a fundamental component.

---

## Standard Flight Phases

### 1. PRE-FLIGHT / GROUND (Before Departure)

**Definition**: Aircraft stationary at gate or parking position before flight operations begin.

**Characteristics**:
- **Airspeed**: 0 knots
- **Altitude**: Field elevation (constant)
- **Engine State**: Off, starting, or at idle
- **Systems**: APU may be running, systems check in progress

**Key Activities**:
- Pre-flight inspection
- Loading passengers/cargo
- System checks
- Engine start procedures

**Duration**: Variable (typically 10-60 minutes before departure)

**Safety Considerations**: Ground handling, refueling operations

---

### 2. TAXI-OUT

**Definition**: Aircraft moving under its own power from gate to runway.

**Characteristics**:
- **Airspeed**: 0-30 knots (typically 10-20 knots)
- **Altitude**: Field elevation ±10 feet
- **Engine Torque/N1**: Low (15-40%)
- **Brakes**: Frequently applied
- **Steering**: Using nose wheel steering

**Key Activities**:
- Following taxiway routes
- Pre-takeoff checklists
- Communication with ground control
- Queue at runway holding point

**Typical Duration**: 5-20 minutes (highly variable based on airport size/congestion)

**Parameters for Detection**:
- Ground speed: 5-30 knots
- Altitude variation: < 50 feet
- Engine power: Low but above idle
- Wheel rotation: Active

**Safety Considerations**: 
- Runway incursions
- Taxiway navigation
- Other ground traffic

---

### 3. TAKEOFF

**Definition**: The critical phase from start of takeoff roll to initial climb.

**Sub-phases**:
1. **Takeoff Roll**: Acceleration on runway
2. **Rotation**: Nose wheel lifts off
3. **Liftoff**: Main wheels leave ground
4. **Initial Acceleration**: Climb with gear/flaps still extended

**Characteristics**:
- **Airspeed**: 
  - Start: 0 knots
  - V1 (decision speed): ~80-120 knots depending on aircraft
  - VR (rotation): ~90-140 knots
  - V2 (takeoff safety speed): ~100-150 knots
- **Altitude**: Ground level to ~50 feet
- **Engine Power**: Maximum takeoff thrust (100% or near 100%)
- **Acceleration**: High longitudinal acceleration (0.2-0.4g)
- **Pitch Angle**: Increases rapidly (10-15 degrees)
- **Flaps**: Extended (takeoff configuration)

**Critical Speeds** (example for mid-size aircraft):
- **V1**: ~135 knots - Decision speed (cannot abort after)
- **VR**: ~140 knots - Rotation speed
- **V2**: ~145 knots - Takeoff safety speed

**Typical Duration**: 30-60 seconds from brake release to 35 feet AGL

**Parameters for Detection**:
- Rapid airspeed increase (>2 knots/second)
- Altitude: < 100 feet AGL
- Engine torque/N1: >90%
- High normal acceleration (as weight transfers from wheels)
- Landing gear: Extended then retracting

**Safety Considerations**:
- **Most critical phase**: Engine failure during takeoff
- Runway length requirements
- Obstacle clearance
- Weather (wind, visibility)
- Bird strikes

**Regulations**:
- FAR 25.107 (Takeoff Speeds)
- EASA CS-25 requirements

---

### 4. INITIAL CLIMB

**Definition**: The climb from lift-off to approximately 1,500 feet AGL.

**Characteristics**:
- **Altitude**: 0-1,500 feet AGL
- **Airspeed**: Accelerating from V2 to climb speed (~150-250 knots)
- **Vertical Speed**: High (1,000-3,000 fpm)
- **Engine Power**: Maximum continuous or takeoff thrust
- **Pitch Angle**: 10-20 degrees
- **Flaps**: Extended, then retracting progressively
- **Landing Gear**: Retracting

**Key Activities**:
- Positive rate of climb - gear up
- Flap retraction schedule
- Acceleration to climb speed
- Following departure procedures (SID)

**Typical Duration**: 2-5 minutes

**Parameters for Detection**:
- Altitude: 0-1,500 feet AGL
- Vertical speed: >500 fpm
- Airspeed: >V2 and increasing
- Flap position: Transitioning from takeoff to clean
- Positive climb gradient

**Safety Considerations**:
- **Second most critical phase**
- Engine failure: Limited options for return
- Terrain/obstacle avoidance
- Noise abatement procedures
- ATC coordination

**Aviation Standards**:
- FAR 25.111 (Takeoff Path)
- Minimum climb gradient: 2.4% (one engine out)

---

### 5. CLIMB

**Definition**: Sustained climb from initial climb altitude to cruise altitude.

**Characteristics**:
- **Altitude**: From 1,500 feet AGL to cruise altitude (typically 20,000-45,000 feet)
- **Airspeed**: Climb schedule (IAS or Mach)
  - Lower altitudes: 250 knots IAS (below 10,000 ft in most countries)
  - Higher altitudes: ~280-320 knots IAS or M0.74-0.78
- **Vertical Speed**: 1,000-3,000 fpm (decreasing with altitude)
- **Engine Power**: Climb thrust (80-95% N1)
- **Pitch Angle**: 5-15 degrees (decreasing with altitude)
- **Flaps/Gear**: Clean configuration
- **Autopilot**: Usually engaged

**Key Activities**:
- Following flight plan route
- Step climbs (if applicable)
- Communication with ATC
- Passenger service begins

**Typical Duration**: 10-30 minutes

**Parameters for Detection**:
- Altitude: Steadily increasing, > 1,500 ft AGL
- Vertical speed: >500 fpm
- Airspeed: Relatively constant for altitude
- Autopilot: Often engaged
- Engine power: Climb setting

**Transition to Cruise**:
- Top of climb (TOC)
- Level-off at cruise altitude
- Vertical speed approaches zero

**Safety Considerations**:
- Terrain clearance
- Traffic separation
- Weather avoidance
- System monitoring

---

### 6. CRUISE

**Definition**: Level flight at optimum altitude for the flight segment.

**Characteristics**:
- **Altitude**: Constant (typically ±200 feet)
  - Short haul: 20,000-35,000 feet
  - Long haul: 35,000-43,000 feet
- **Airspeed**: 
  - Turboprops: 250-350 knots IAS
  - Jets: M0.74-0.85 (typically M0.78)
- **Vertical Speed**: ±100-200 fpm (essentially zero)
- **Engine Power**: Cruise thrust (optimized for fuel efficiency)
- **Autopilot**: Engaged
- **Flight Director**: Following flight plan

**Sub-types**:
- **Cruise-climb**: Gradual altitude increase as weight decreases
- **Step-climb**: Discrete altitude increases
- **Level cruise**: Constant altitude

**Typical Duration**: 
- Short haul: 30 minutes - 2 hours
- Medium haul: 2-6 hours  
- Long haul: 6-16 hours

**Parameters for Detection**:
- Altitude: Constant (standard deviation < 200 feet)
- Vertical speed: |VS| < 200 fpm
- Airspeed: Constant
- Autopilot: Engaged
- Power setting: Cruise

**Optimal Performance**:
- **ECON Speed**: Economic cruise speed (best cost index)
- **LRC**: Long Range Cruise (99% of max range, faster)
- **MRC**: Maximum Range Cruise (best fuel efficiency)

**Safety Considerations**:
- Routine monitoring phase
- Turbulence
- Weather deviations
- Fuel management
- ETOPS compliance (for twin-engine over water)

---

### 7. DESCENT

**Definition**: Controlled descent from cruise altitude to approach altitude.

**Sub-phases**:
1. **Cruise Descent**: From cruise to ~10,000 feet
2. **Arrival**: Following STAR (Standard Terminal Arrival Route)

**Characteristics**:
- **Altitude**: Decreasing from cruise to ~3,000-5,000 feet
- **Vertical Speed**: -300 to -2,500 fpm (typically -1,500 to -2,000 fpm)
- **Airspeed**: 
  - Initial: Cruise speed reducing
  - Lower: 250 knots below 10,000 feet (most jurisdictions)
- **Engine Power**: Reduced (sometimes idle)
- **Autopilot**: Usually engaged
- **Spoilers/Speed brakes**: May be deployed

**Descent Types**:
- **Idle Descent**: Most fuel efficient
- **Continuous Descent Approach (CDA)**: Environmentally preferred
- **Step Descent**: Discrete altitude decreases

**Typical Duration**: 15-30 minutes

**Parameters for Detection**:
- Altitude: Steadily decreasing, >3,000 feet AGL
- Vertical speed: < -300 fpm
- Airspeed: Controlled, decreasing
- Engine power: Reduced

**Descent Planning**:
- **Top of Descent (TOD)**: Point to begin descent
- **Rule of Thumb**: 3:1 ratio (3 nm per 1,000 feet altitude loss)
- Example: Descend from 35,000 ft over 105 nm distance

**Safety Considerations**:
- Pressurization changes (passenger comfort)
- Terrain awareness (TAWS)
- Traffic conflicts
- Weather (icing conditions)

---

### 8. APPROACH

**Definition**: The phase of flight from initial approach fix to landing threshold.

**Sub-phases**:
1. **Initial Approach**: Joining approach pattern
2. **Intermediate Approach**: Aligning with runway
3. **Final Approach**: Last segment to landing

**Characteristics**:
- **Altitude**: Decreasing from ~3,000 to 50 feet AGL
- **Airspeed**: Reducing to approach speed (Vapp)
  - Turboprops: 100-140 knots
  - Jets: 130-160 knots
- **Vertical Speed**: -500 to -1,000 fpm on final
- **Descent Angle**: Typically 3 degrees on final
- **Flaps**: Progressively extending (approach then landing configuration)
- **Landing Gear**: Extended
- **Autopilot**: May be engaged (coupled approach) or manual

**Approach Types**:
- **Visual Approach**: Pilot sees runway, flies visually
- **ILS (Instrument Landing System)**: Precision approach (most common)
- **RNAV/GPS**: Satellite-based precision
- **Non-Precision**: VOR, NDB approaches

**Stabilized Approach Criteria** (typically by 1,000 ft or 500 ft AGL):
- On correct flight path
- Airspeed: Vapp ±5 knots
- Descent rate: ≤1,000 fpm
- Landing configuration (gear down, flaps)
- Thrust at appropriate setting

**Typical Duration**: 5-10 minutes

**Parameters for Detection**:
- Altitude: 500-3,000 feet AGL, decreasing
- Vertical speed: -300 to -1,000 fpm
- Airspeed: Decreasing toward Vapp
- Flaps: Extended (>15 degrees)
- Gear: Down
- Localizer/Glideslope: Captured (if ILS)

**Key Altitudes**:
- **Decision Height (DH)**: Minimum altitude for precision approach
- **Minimum Descent Altitude (MDA)**: For non-precision approaches

**Safety Considerations**:
- **Critical phase for accidents**
- Unstabilized approach → Go-around
- Weather minimums (visibility, ceiling)
- Windshear/microburst
- Runway alignment
- CFIT (Controlled Flight Into Terrain) risk

---

### 9. LANDING

**Definition**: The final phase from crossing runway threshold to full stop on runway.

**Sub-phases**:
1. **Threshold Crossing**: 50 feet AGL
2. **Flare**: Pitch up to reduce descent rate
3. **Touchdown**: Main wheels contact runway
4. **Rollout**: Deceleration to taxi speed

**Characteristics**:
- **Altitude**: 50 feet to ground level
- **Airspeed**: 
  - Threshold: Vapp (approach speed)
  - Touchdown: Vref (reference speed) ~1.3 × Vstall
  - Rollout: Decreasing rapidly
- **Vertical Speed**: 
  - Before flare: -500 to -800 fpm
  - At touchdown: -100 to -300 fpm (target <200 fpm)
- **Pitch Angle**: Increases during flare (7-10 degrees)
- **Deceleration**: High (braking + reverse thrust)
- **Flaps**: Full landing configuration
- **Spoilers**: Deploy automatically on touchdown

**Landing Distances**:
- **Threshold**: Runway threshold
- **Touchdown Zone**: First 3,000 feet of runway
- **Landing Distance Available (LDA)**: Total usable runway

**Typical Duration**: 30-90 seconds from threshold to taxi speed

**Parameters for Detection**:
- Altitude: <50 feet AGL, rapidly decreasing
- Airspeed: Vref to taxi speed
- High deceleration (negative longitudinal acceleration)
- Spoiler deployment
- Reverse thrust (high N1 with negative thrust)
- Normal acceleration spike at touchdown

**Key Events**:
1. **50 ft call**: "Fifty"
2. **30 ft call**: "Thirty"
3. **Flare**: Pilot input to raise nose
4. **Main gear touchdown**: Weight on wheels
5. **Nose gear touchdown**: ~5-10 seconds later
6. **Reverse thrust**: Applied (if available)
7. **Autobrake**: Engaged or manual braking
8. **60 knots call**: Approaching taxi speed
9. **Runway exit**: Turn off onto taxiway

**Safety Considerations**:
- **Critical phase**
- Hard landing (>2.0g vertical acceleration)
- Long landing (beyond touchdown zone)
- Crosswind landing
- Runway condition (wet, contaminated)
- Runway excursion risk
- Go-around decision (if unstabilized)

**Performance Requirements**:
- FAR 25.125 (Landing distances)
- Runway must be ≥60% longer than calculated landing distance

---

### 10. TAXI-IN

**Definition**: Movement from runway exit to parking position.

**Characteristics**:
- **Airspeed**: 0-30 knots (ground speed)
- **Altitude**: Field elevation
- **Engine Power**: Low (idle to taxi thrust)
- **Flaps**: Retracting to up position
- **After-landing checklist**: Completed

**Key Activities**:
- Following taxi route to gate
- After-landing checks
- Communication with ground control
- APU start (if needed)

**Typical Duration**: 5-20 minutes

**Parameters for Detection**:
- Ground speed: 5-30 knots
- Altitude: Constant (field elevation ±20 feet)
- Engine power: Low
- Position in flight: After landing phase

**Safety Considerations**:
- Taxiway navigation
- Ground traffic
- Reduced visibility from cockpit

---

### 11. POST-FLIGHT / GROUND (After Arrival)

**Definition**: Aircraft stationary at gate after flight completion.

**Characteristics**:
- **Airspeed**: 0 knots
- **Altitude**: Gate elevation (constant)
- **Engines**: Shutting down or shut down
- **APU**: May start for ground power

**Key Activities**:
- Engine shutdown
- Passenger deplaning
- Post-flight inspection
- Refueling/servicing

**Duration**: Variable

**Parameters for Detection**:
- Ground speed: 0 knots
- Altitude: Constant
- Position: After taxi-in phase
- Engine parameters: Decreasing to zero

---

## Aviation Industry Standards

### ICAO (International Civil Aviation Organization)

**Annex 6 - Operation of Aircraft**:
- Part I: Commercial Air Transport - Aeroplanes
- Requires systematic flight data analysis
- Flight phase identification for safety monitoring

### FAA (Federal Aviation Administration)

**AC 120-82 - Flight Operational Quality Assurance**:
- Defines standard flight phases
- Specifies parameters for each phase
- Event detection requirements

**FAR Part 25** (Airworthiness Standards):
- 25.107: Takeoff speeds and distances
- 25.111: Takeoff path
- 25.125: Landing distances
- 25.143: Controllability and maneuverability

### EASA (European Union Aviation Safety Agency)

**AMC/GM to Part-ORO**:
- Flight Data Monitoring (FDM) requirements
- Phase-specific event detection
- Safety performance indicators

### IATA (International Air Transport Association)

**Flight Data Analysis Recommendations**:
- Standardized phase definitions
- Event exceedance thresholds
- Best practices for FDM programs

---

## Parameters Used for Detection

### Primary Parameters

1. **Airspeed (IAS - Indicated Air Speed)**
   - **Units**: Knots
   - **Sensor**: Pitot-static system
   - **Accuracy**: ±2-5 knots
   - **Update Rate**: 1-8 Hz
   - **Usage**: Primary discriminator for most phases

2. **Altitude**
   - **Types**: 
     - MSL (Mean Sea Level) - from barometric altimeter
     - AGL (Above Ground Level) - calculated or radio altimeter
   - **Units**: Feet
   - **Accuracy**: ±50 feet (barometric), ±2 feet (radio alt)
   - **Usage**: Critical for all phase detection

3. **Vertical Speed (Rate of Climb/Descent)**
   - **Units**: Feet per minute (fpm)
   - **Derived**: From altitude change over time
   - **Smoothing**: Often filtered to reduce noise
   - **Usage**: Distinguishes climb/cruise/descent

4. **Ground Speed**
   - **Units**: Knots
   - **Source**: GPS or calculated from IAS + wind
   - **Usage**: Ground operations (taxi phases)

### Secondary Parameters

5. **Engine Parameters**
   - **N1/N2**: Fan/core speed (% RPM)
   - **Torque**: For turboprops (%)
   - **EPR**: Engine Pressure Ratio
   - **Fuel Flow**: Rate of fuel consumption
   - **Usage**: Power setting indication

6. **Autopilot Status**
   - **Values**: Engaged/Disengaged
   - **Usage**: Typically engaged in cruise/climb/descent

7. **Flight Control Positions**
   - **Flap Position**: Degrees or setting (0, 1, 5, 15, 30, etc.)
   - **Spoiler Position**: Degrees
   - **Usage**: Configuration for approach/landing

8. **Landing Gear**
   - **Status**: Up, Down, In Transit
   - **Weight on Wheels**: Boolean
   - **Usage**: Ground vs. airborne discrimination

9. **Acceleration**
   - **Normal (Vertical)**: g-force perpendicular to aircraft floor
   - **Longitudinal**: Forward/aft acceleration
   - **Lateral**: Side-to-side acceleration
   - **Usage**: Detecting takeoff, landing, turns

10. **Radio Altimeter**
    - **Range**: 0-2,500 feet AGL
    - **Accuracy**: ±2 feet
    - **Usage**: Precision altitude during approach/landing

### Time-Based Parameters

11. **Time Stamps**
    - **GPS Time**: UTC time from satellite
    - **Sample Time**: Relative time in recording
    - **Usage**: Duration calculations, sequencing

### Position Parameters

12. **GPS Position**
    - **Latitude/Longitude**: Degrees
    - **Accuracy**: ±10 meters
    - **Usage**: On-ground vs. airborne, taxi routing

13. **Heading**
    - **Magnetic Heading**: Degrees (0-360)
    - **Usage**: Runway alignment, navigation

---

## Safety and Risk Considerations

### Accident Statistics by Phase

According to Boeing Statistical Summary and IATA data:

| Phase | % of Flight Time | % of Fatal Accidents |
|-------|------------------|---------------------|
| Taxi | 1% | <1% |
| Takeoff | 1% | 14% |
| Initial Climb | 1% | 13% |
| Climb | 14% | 11% |
| Cruise | 57% | 10% |
| Descent | 13% | 3% |
| Approach | 12% | 29% |
| Landing | 1% | 20% |

**Key Insights**:
- **80% of accidents occur during 4% of flight time** (takeoff, initial climb, approach, landing)
- **Approach and landing** are the highest risk phases
- **Cruise** is safest despite longest duration

### Critical Phases

**Takeoff and Initial Climb**:
- Engine failure scenarios
- Bird strike risk
- Limited maneuvering options
- High workload

**Approach and Landing**:
- Weather impacts (visibility, wind)
- Runway excursion risk
- CFIT (Controlled Flight Into Terrain)
- Unstabilized approach

### Flight Data Monitoring (FDM)

**Purpose**: Proactive safety through data analysis

**Phase-Specific Events Monitored**:
- **Takeoff**: Excessive rotation, tail strike, V-speed exceedance
- **Climb**: Rate of climb deviation, speed exceedance
- **Cruise**: Altitude deviation, overspeed
- **Descent**: Excessive descent rate, speed brake use
- **Approach**: Unstabilized approach, glideslope deviation
- **Landing**: Hard landing (>2.0g), long landing

---

## Aircraft-Specific Variations

### Commercial Jets (Boeing 737, Airbus A320, etc.)

**Typical Values**:
- Cruise Altitude: 35,000-41,000 feet
- Cruise Speed: M0.78-0.82
- Approach Speed: 130-150 knots
- Climb Rate: 1,500-3,000 fpm

**Autopilot**: Engaged shortly after takeoff, disengaged before landing

### Regional Turboprops (Q400, ATR 72, etc.)

**Typical Values**:
- Cruise Altitude: 20,000-27,000 feet
- Cruise Speed: 250-360 knots
- Approach Speed: 100-130 knots
- Climb Rate: 1,000-2,500 fpm

**Engine Parameter**: Torque (%) instead of N1

### Business Jets

**Characteristics**:
- Higher cruise altitudes (41,000-51,000 feet)
- Faster cruise speeds (M0.80-0.90)
- Shorter field performance
- More agile climb/descent

### Cargo Aircraft

**Differences**:
- Higher operating weights
- Different performance profiles
- May operate at night primarily
- Different loading configurations

---

## Detection Algorithms

### Rule-Based Approach (Used in This Tool)

**Advantages**:
- Interpretable
- Based on aviation knowledge
- No training data required
- Fast execution

**Disadvantages**:
- Requires threshold tuning
- May have edge cases
- Aircraft-type specific

**Implementation**:
```python
if airspeed < 5 and altitude_agl < 500:
    phase = "GROUND"
elif vertical_speed > 500 and altitude_agl < 1500:
    phase = "INITIAL_CLIMB"
# ... more rules
```

### Machine Learning Approaches

**Methods**:
- Hidden Markov Models (HMM)
- Random Forests
- Neural Networks (LSTM for temporal patterns)
- Support Vector Machines (SVM)

**Advantages**:
- Can learn from data
- May capture complex patterns
- Adaptable to different aircraft

**Disadvantages**:
- Requires labeled training data
- "Black box" behavior
- Computationally intensive

### Hybrid Approaches

Combining rule-based with ML for best results:
- Rules for clear-cut cases
- ML for ambiguous transitions
- Rule-based validation of ML output

---

## Validation and Accuracy

### Ground Truth

**Sources**:
- Manual coding by flight analysts
- Pilot input (flight phase logs)
- ATC records
- Video recordings

### Accuracy Metrics

**Confusion Matrix**: Phase-by-phase accuracy

**Temporal Accuracy**:
- Transition point detection (±5 seconds)
- Phase duration estimation

**Typical Performance**:
- Rule-based: 93-97% accuracy
- ML-based: 95-99% accuracy
- Hybrid: 97-99% accuracy

---

## Future Directions

### Real-Time Detection

- Streaming data from aircraft
- On-board phase detection
- Real-time safety alerts

### Predictive Analytics

- Anomaly detection within phases
- Predictive maintenance
- Fuel optimization

### Integration

- Flight management systems
- Electronic Flight Bag (EFB)
- ATC systems

### Automation

- Autonomous flight operations
- Urban Air Mobility (UAM)
- Unmanned Aircraft Systems (UAS)

---

## References

### Regulatory Documents

1. **ICAO Annex 6** - Operation of Aircraft
2. **FAA AC 120-82** - Flight Operational Quality Assurance
3. **EASA AMC/GM to Part-ORO** - Flight Data Monitoring
4. **FAR Part 25** - Airworthiness Standards: Transport Category Airplanes

### Industry Publications

5. **IATA Flight Data Analysis Best Practices**
6. **Boeing Statistical Summary of Commercial Jet Airplane Accidents**
7. **Airbus Safety Magazine**
8. **Flight Safety Foundation - ALAR (Approach and Landing Accident Reduction)**

### Academic Research

9. Li, L., et al. (2019). "Flight Phase Identification Using Machine Learning." *Journal of Air Transport Management*
10. Matthews, B., et al. (2013). "Automatic Flight-Tracking Surveillance Information System." *IEEE Transactions on Intelligent Transportation Systems*
11. Janakiraman, V. (2016). "Explaining Aviation Safety Incidents Using Deep Temporal Multiple Instance Learning." *KDD*

### Aircraft Flight Manuals

12. **Bombardier Q400 Flight Crew Operating Manual**
13. **Boeing 737 Flight Crew Training Manual**
14. **Airbus A320 Flight Crew Operating Manual**

### Online Resources

15. **SKYbrary** - Aviation Safety Database (https://skybrary.aero)
16. **FAA Safety** (https://www.faa.gov/about/safety)
17. **EASA** (https://www.easa.europa.eu)

---

## Glossary

- **AGL**: Above Ground Level
- **ATC**: Air Traffic Control
- **CFIT**: Controlled Flight Into Terrain
- **DH**: Decision Height
- **ECON**: Economy (cruise speed)
- **ETOPS**: Extended-range Twin-engine Operations
- **FDM**: Flight Data Monitoring
- **FDR**: Flight Data Recorder
- **IAS**: Indicated Air Speed
- **ILS**: Instrument Landing System
- **LDA**: Landing Distance Available
- **LRC**: Long Range Cruise
- **MDA**: Minimum Descent Altitude
- **MSL**: Mean Sea Level
- **N1/N2**: Engine shaft speeds
- **RNAV**: Area Navigation
- **SID**: Standard Instrument Departure
- **STAR**: Standard Terminal Arrival Route
- **TAWS**: Terrain Awareness and Warning System
- **TOC**: Top of Climb
- **TOD**: Top of Descent
- **V1**: Decision Speed (takeoff)
- **V2**: Takeoff Safety Speed
- **Vapp**: Approach Speed
- **Vref**: Reference Landing Speed
- **VR**: Rotation Speed

---

*This document provides comprehensive research on flight phases for aviation analysis and software development purposes.*
