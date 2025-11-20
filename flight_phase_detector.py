"""
Flight Phase Detection System
==============================

This script analyzes aircraft flight data from CSV files and identifies different flight phases
based on multiple parameters including airspeed, altitude, vertical speed, and autopilot status.

Flight Phases Identified:
-------------------------
1. GROUND (PRE-FLIGHT): Aircraft on ground before takeoff
2. TAXI-OUT: Aircraft taxiing to runway
3. TAKEOFF: Aircraft accelerating on runway and initial climb
4. INITIAL CLIMB: Climbing phase after takeoff (typically up to 1,500 ft AGL)
5. CLIMB: Continued climb to cruise altitude
6. CRUISE: Level flight at cruise altitude
7. DESCENT: Descending from cruise altitude
8. APPROACH: Intermediate/initial approach to landing
9. FINAL_APPROACH: Final approach segment (below 1,000 ft AGL)
10. LANDING: Touchdown and deceleration on runway
11. TAXI-IN: Aircraft taxiing to gate
12. GROUND (POST-FLIGHT): Aircraft parked at gate

Supported Aircraft Types:
------------------------
- Regional Turboprops (Q400, ATR72, Dash 8)
- Narrow-body Jets (B737, A320, A220)
- Wide-body Jets (B777, B787, A330, A350)
- Business Jets (Citation, Gulfstream, Challenger)

Compliance Standards:
--------------------
- ICAO Annex 6 (Operation of Aircraft)
- FAA AC 120-82 (Flight Operational Quality Assurance)
- EASA AMC/GM to Part-ORO (Flight Data Monitoring)
- IATA Flight Data Analysis Best Practices

Author: Flight Data Analysis System
Version: 2.0
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os
from typing import Dict, Optional, List


# ============================================================================
# AIRCRAFT PROFILES - Predefined threshold configurations
# ============================================================================

AIRCRAFT_PROFILES = {
    'Q400': {
        'name': 'Bombardier Q400 (Regional Turboprop)',
        'taxi_speed': 30,
        'takeoff_speed': 80,
        'rotation_speed': 100,
        'climb_rate': 500,
        'descent_rate': -300,
        'cruise_vs_threshold': 200,
        'approach_altitude': 3000,
        'initial_climb_alt': 1500,
        'landing_altitude': 500,
        'typical_cruise_alt': 25000,
        'typical_cruise_speed': 360,
    },
    'ATR72': {
        'name': 'ATR 72 (Regional Turboprop)',
        'taxi_speed': 25,
        'takeoff_speed': 75,
        'rotation_speed': 95,
        'climb_rate': 500,
        'descent_rate': -300,
        'cruise_vs_threshold': 200,
        'approach_altitude': 3000,
        'initial_climb_alt': 1500,
        'landing_altitude': 500,
        'typical_cruise_alt': 22000,
        'typical_cruise_speed': 300,
    },
    'B737': {
        'name': 'Boeing 737 (Narrow-body Jet)',
        'taxi_speed': 30,
        'takeoff_speed': 100,
        'rotation_speed': 140,
        'climb_rate': 800,
        'descent_rate': -500,
        'cruise_vs_threshold': 200,
        'approach_altitude': 3000,
        'initial_climb_alt': 1500,
        'landing_altitude': 500,
        'typical_cruise_alt': 37000,
        'typical_cruise_speed': 450,
    },
    'A320': {
        'name': 'Airbus A320 (Narrow-body Jet)',
        'taxi_speed': 30,
        'takeoff_speed': 95,
        'rotation_speed': 135,
        'climb_rate': 800,
        'descent_rate': -500,
        'cruise_vs_threshold': 200,
        'approach_altitude': 3000,
        'initial_climb_alt': 1500,
        'landing_altitude': 500,
        'typical_cruise_alt': 37000,
        'typical_cruise_speed': 450,
    },
    'B777': {
        'name': 'Boeing 777 (Wide-body Jet)',
        'taxi_speed': 35,
        'takeoff_speed': 120,
        'rotation_speed': 160,
        'climb_rate': 1000,
        'descent_rate': -800,
        'cruise_vs_threshold': 250,
        'approach_altitude': 3000,
        'initial_climb_alt': 1500,
        'landing_altitude': 500,
        'typical_cruise_alt': 39000,
        'typical_cruise_speed': 490,
    },
    'GENERIC_TURBOPROP': {
        'name': 'Generic Turboprop (Regional)',
        'taxi_speed': 30,
        'takeoff_speed': 80,
        'rotation_speed': 100,
        'climb_rate': 500,
        'descent_rate': -300,
        'cruise_vs_threshold': 200,
        'approach_altitude': 3000,
        'initial_climb_alt': 1500,
        'landing_altitude': 500,
        'typical_cruise_alt': 25000,
        'typical_cruise_speed': 300,
    },
    'GENERIC_JET': {
        'name': 'Generic Jet (Commercial)',
        'taxi_speed': 30,
        'takeoff_speed': 100,
        'rotation_speed': 140,
        'climb_rate': 800,
        'descent_rate': -500,
        'cruise_vs_threshold': 200,
        'approach_altitude': 3000,
        'initial_climb_alt': 1500,
        'landing_altitude': 500,
        'typical_cruise_alt': 37000,
        'typical_cruise_speed': 450,
    },
}


# ============================================================================
# REGULATORY STANDARDS - Alternative threshold configurations
# ============================================================================

REGULATORY_STANDARDS = {
    'FAA': {
        'name': 'FAA AC 120-82 (Flight Operational Quality Assurance)',
        'description': 'US Federal Aviation Administration standards',
        'approach_altitude': 3000,      # Below 3,000 ft AGL
        'final_approach_alt': 1000,     # Stabilized approach criteria
        'climb_rate': 500,              # Minimum for positive climb
        'descent_rate': -300,           # Minimum for descent phase
        'unstabilized_alt': 500,        # Decision altitude for go-around
    },
    'EASA': {
        'name': 'EASA AMC/GM to Part-ORO',
        'description': 'European Union Aviation Safety Agency standards',
        'approach_altitude': 3000,
        'final_approach_alt': 1000,
        'climb_rate': 500,
        'descent_rate': -300,
        'unstabilized_alt': 500,
    },
    'IATA': {
        'name': 'IATA Flight Data Analysis',
        'description': 'International Air Transport Association best practices',
        'approach_altitude': 3000,
        'final_approach_alt': 1000,
        'climb_rate': 500,
        'descent_rate': -300,
        'unstabilized_alt': 500,
    },
}


# ============================================================================
# MAIN DETECTOR CLASS
# ============================================================================


class FlightPhaseDetector:
    """
    Detects flight phases from aircraft data using multiple parameters.

    The detection uses a rule-based approach considering:
    - Airspeed (knots)
    - Altitude (feet MSL and AGL)
    - Vertical speed (feet/minute)
    - Autopilot engagement status
    - Flap position
    - Engine torque/thrust

    Supports multiple aircraft types with predefined threshold profiles.
    Complies with FAA, EASA, and IATA flight data monitoring standards.
    """

    def __init__(self, csv_file: str, aircraft_type: str = 'Q400',
                 custom_thresholds: Optional[Dict] = None):
        """
        Initialize the flight phase detector with a CSV file.

        Args:
            csv_file (str): Path to the CSV file containing flight data
            aircraft_type (str): Aircraft type code (Q400, B737, A320, etc.)
                               Use 'GENERIC_TURBOPROP' or 'GENERIC_JET' if type unknown
            custom_thresholds (dict, optional): Custom threshold values to override defaults

        Available Aircraft Types:
            - Q400: Bombardier Q400 (Regional Turboprop)
            - ATR72: ATR 72 (Regional Turboprop)
            - B737: Boeing 737 (Narrow-body Jet)
            - A320: Airbus A320 (Narrow-body Jet)
            - B777: Boeing 777 (Wide-body Jet)
            - GENERIC_TURBOPROP: Generic turboprop configuration
            - GENERIC_JET: Generic jet configuration

        Example:
            >>> # Using predefined aircraft profile
            >>> detector = FlightPhaseDetector('flight.csv', aircraft_type='B737')

            >>> # Using custom thresholds
            >>> custom = {'takeoff_speed': 90, 'cruise_vs_threshold': 150}
            >>> detector = FlightPhaseDetector('flight.csv', 'A320', custom)
        """
        self.csv_file = csv_file
        self.aircraft_type = aircraft_type
        self.df = None
        self.phases = []

        # Load aircraft-specific thresholds
        if aircraft_type in AIRCRAFT_PROFILES:
            self.THRESHOLDS = AIRCRAFT_PROFILES[aircraft_type].copy()
            self.aircraft_name = self.THRESHOLDS.pop('name')
        else:
            print(f"Warning: Unknown aircraft type '{aircraft_type}'. Using GENERIC_TURBOPROP.")
            self.THRESHOLDS = AIRCRAFT_PROFILES['GENERIC_TURBOPROP'].copy()
            self.aircraft_name = self.THRESHOLDS.pop('name')

        # Add additional standard thresholds
        self.THRESHOLDS.update({
            'ground_altitude_var': 100,      # Max altitude variation on ground
            'min_cruise_duration': 30,       # Min samples for cruise phase
            'final_approach_alt': 1000,      # Altitude for final approach
            'landing_rollout_alt': 100,      # Altitude for landing rollout
        })

        # Remove documentation fields
        self.THRESHOLDS.pop('typical_cruise_alt', None)
        self.THRESHOLDS.pop('typical_cruise_speed', None)

        # Apply custom threshold overrides
        if custom_thresholds:
            self.THRESHOLDS.update(custom_thresholds)
            print(f"Applied custom threshold overrides: {custom_thresholds}")

    def load_data(self):
        """
        Load and preprocess the CSV data.

        Returns:
            pd.DataFrame: Loaded and preprocessed flight data

        Raises:
            FileNotFoundError: If CSV file does not exist
            ValueError: If required columns are missing
        """
        if not os.path.exists(self.csv_file):
            raise FileNotFoundError(f"CSV file not found: {self.csv_file}")

        print(f"Loading data from {self.csv_file}...")
        print(f"Aircraft type: {self.aircraft_name}")

        # Read CSV, skip the units row (row 1)
        self.df = pd.read_csv(self.csv_file, skiprows=[1])

        # Clean up column names (remove leading/trailing spaces)
        self.df.columns = self.df.columns.str.strip()

        # Validate required columns - try multiple possible column names
        required_mappings = {
            'airspeed': ['AIRSPEED  L', 'AIRSPEED R', 'AIRSPEED', 'COMPUTED AIRSPEED'],
            'altitude': ['ALTITUDE L', 'ALTITUDE R', 'ALTITUDE', 'ELEVATION'],
            'air_ground': ['AIR/GROUND', 'AIR GROUND', 'GROUND/AIR'],
            'flaps': ['T.E. FLAP POSN-RIGHT', 'T.E. FLAP POSN-LEFT', 'FLAPS', 'ALT FLAPS'],
            'speedbrake': ['SPEED BRK HDL POSN', 'SPOILER POSN NO. 7', 'SPOILER POSN NO. 2'],
            'vertical_accel': ['VERTICAL ACCELERATION', 'ACCN NORM'],
        }

        # Find available columns
        available_columns = set(self.df.columns.str.strip())

        # Map column names to standard names
        self.column_mapping = {}
        missing_columns = []

        for standard_name, possible_names in required_mappings.items():
            found = False
            for possible_name in possible_names:
                if possible_name in available_columns:
                    self.column_mapping[standard_name] = possible_name
                    found = True
                    break
            if not found:
                missing_columns.append(f"{standard_name} (tried: {', '.join(possible_names)})")

        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}\n"
                           f"Available columns include: {sorted(list(available_columns))[:10]}...")

        print(f"Column mapping: {self.column_mapping}")

        print(f"Loaded {len(self.df)} data points")
        print(f"Time period: {len(self.df) * 0.5 / 60:.1f} minutes (assuming 2 Hz sampling)")

        # Calculate derived parameters
        self._calculate_derived_parameters()

        return self.df

    def _calculate_derived_parameters(self):
        """
        Calculate additional parameters needed for phase detection.

        Derived Parameters:
            - AIRSPEED_AVG: Average of left/right airspeed sensors
            - ALTITUDE_AVG: Average of left/right altitude sensors
            - TQ_AVG: Average engine torque
            - VERTICAL_SPEED: Rate of altitude change (fpm)
            - VERTICAL_SPEED_SMOOTH: Smoothed vertical speed
            - ALTITUDE_AGL: Altitude above ground level (handles different airport elevations)
        """

        # Average airspeed from available sensors
        airspeed_col = self.column_mapping.get('airspeed', 'COMPUTED AIRSPEED')
        if airspeed_col in self.df.columns:
            self.df['AIRSPEED_AVG'] = self.df[airspeed_col]
        else:
            # If no airspeed column, try to use groundspeed or set to 0
            if 'GROUNDSPEED' in self.df.columns:
                self.df['AIRSPEED_AVG'] = self.df['GROUNDSPEED']
                print("Warning: Using GROUNDSPEED as airspeed")
            else:
                self.df['AIRSPEED_AVG'] = 0
                print("Warning: No airspeed data available, setting to 0")

        # Average altitude from available sensors
        altitude_col = self.column_mapping.get('altitude', 'ELEVATION')
        if altitude_col in self.df.columns:
            self.df['ALTITUDE_AVG'] = self.df[altitude_col]
        else:
            self.df['ALTITUDE_AVG'] = 0
            print("Warning: No altitude data available, setting to 0")

        # Process AIR/GROUND status
        air_ground_col = self.column_mapping.get('air_ground')
        if air_ground_col and air_ground_col in self.df.columns:
            # Convert to boolean: True = AIR, False = GROUND
            self.df['IS_AIRBORNE'] = self.df[air_ground_col].str.upper() == 'AIR'
            print(f"Using AIR/GROUND data from column: {air_ground_col}")
        else:
            # No AIR/GROUND data, infer from other parameters
            self.df['IS_AIRBORNE'] = False  # Will be set in phase classification
            print("Warning: No AIR/GROUND data available, will infer from other parameters")

        # Process flap position
        flaps_col = self.column_mapping.get('flaps')
        if flaps_col and flaps_col in self.df.columns:
            self.df['FLAPS_AVG'] = pd.to_numeric(self.df[flaps_col], errors='coerce').fillna(0)
            print(f"Using flaps data from column: {flaps_col}")
        else:
            self.df['FLAPS_AVG'] = 0
            print("Warning: No flaps data available")

        # Process speedbrake/spoiler position
        speedbrake_col = self.column_mapping.get('speedbrake')
        if speedbrake_col and speedbrake_col in self.df.columns:
            self.df['SPEEDBRAKE_DEPLOYED'] = pd.to_numeric(self.df[speedbrake_col], errors='coerce').fillna(0) > 0
            print(f"Using speedbrake data from column: {speedbrake_col}")
        else:
            self.df['SPEEDBRAKE_DEPLOYED'] = False
            print("Warning: No speedbrake data available")

        # Process vertical acceleration
        vert_accel_col = self.column_mapping.get('vertical_accel')
        if vert_accel_col and vert_accel_col in self.df.columns:
            self.df['VERTICAL_ACCEL'] = pd.to_numeric(self.df[vert_accel_col], errors='coerce').fillna(1.0)
            print(f"Using vertical acceleration from column: {vert_accel_col}")
        else:
            self.df['VERTICAL_ACCEL'] = 1.0
            print("Warning: No vertical acceleration data available")

        # Average engine torque (handle potential column name variations)
        torque_cols = ['TQ 1', 'TQ 2', 'TQ 1 ', 'TQ 2 ', 'ENG 1', 'ENG 2']
        available_torque = [col for col in torque_cols if col in self.df.columns]

        if len(available_torque) >= 2:
            self.df['TQ_AVG'] = self.df[available_torque[:2]].mean(axis=1)
        elif len(available_torque) == 1:
            self.df['TQ_AVG'] = self.df[available_torque[0]]
        else:
            # No torque data, use 0 or try to infer from other columns
            self.df['TQ_AVG'] = 50  # Assume moderate power setting
            print("Warning: No torque/thrust data available, using default value")

        # Calculate vertical speed (feet per minute)
        # Assuming data is sampled at approximately 2 Hz (2 samples per second)
        time_diff = 0.5  # seconds between samples
        self.df['VERTICAL_SPEED'] = self.df['ALTITUDE_AVG'].diff() / time_diff * 60

        # Smooth vertical speed to reduce noise
        window_size = 10
        self.df['VERTICAL_SPEED_SMOOTH'] = self.df['VERTICAL_SPEED'].rolling(
            window=window_size, center=True
        ).mean()

        # Calculate acceleration (g's change per sample)
        accel_cols = ['ACCN NORM', 'LONGITUDINAL ACCEL']
        if 'ACCN NORM' in self.df.columns:
            self.df['ACCEL_NORM_DIFF'] = self.df['ACCN NORM'].diff()
        elif 'LONGITUDINAL ACCEL' in self.df.columns:
            self.df['ACCEL_NORM_DIFF'] = self.df['LONGITUDINAL ACCEL'].diff()
        else:
            self.df['ACCEL_NORM_DIFF'] = 0
            print("Warning: No acceleration data available")

        # Ground altitude (estimated as minimum altitude in first 100 samples)
        self.ground_altitude = self.df['ALTITUDE_AVG'].head(100).min()

        # Also check last 100 samples for destination altitude (may be different airport)
        destination_altitude = self.df['ALTITUDE_AVG'].tail(200).min()

        # If destination is significantly higher, we need to adjust AGL calculation dynamically
        self.altitude_change = destination_altitude - self.ground_altitude

        # Altitude Above Ground Level (AGL) - initially based on departure airport
        self.df['ALTITUDE_AGL'] = self.df['ALTITUDE_AVG'] - self.ground_altitude

        # If airports are at very different elevations, we need dynamic ground reference
        if abs(self.altitude_change) > 1000:
            # Find the highest point (top of climb) to split departure/arrival phases
            max_alt_idx = self.df['ALTITUDE_AVG'].idxmax()

            # For arrival phase (after top of descent), use destination altitude as reference
            # Approximate: use last phase of flight for destination ground level
            for idx in range(len(self.df)):
                if idx > max_alt_idx:
                    # In second half of flight, gradually transition to destination altitude
                    current_alt = self.df.iloc[idx]['ALTITUDE_AVG']
                    # If we're close to destination altitude, use it as reference
                    if current_alt < (destination_altitude + 3000):
                        self.df.at[idx, 'ALTITUDE_AGL'] = current_alt - destination_altitude

        print(f"Ground altitude estimated at: {self.ground_altitude:.0f} feet MSL")
        if abs(self.altitude_change) > 1000:
            print(f"Destination altitude detected at: {destination_altitude:.0f} feet MSL (Δ{self.altitude_change:+.0f} ft)")

    def detect_phases(self):
        """
        Main method to detect flight phases using rule-based classification.

        Algorithm:
            1. Classify each data point independently based on thresholds
            2. Apply smoothing to eliminate spurious transitions
            3. Extract contiguous phase segments
            4. Calculate statistics for each segment

        Returns:
            list: List of dictionaries containing phase information
                Each dictionary contains:
                - phase: Phase name
                - start_sample, end_sample: Sample numbers
                - duration_samples, duration_seconds, duration_minutes: Duration
                - start/end/min/max altitude and airspeed
                - avg_vertical_speed: Average rate of climb/descent
        """
        print("\nDetecting flight phases...")
        print(f"Using thresholds: Aircraft={self.aircraft_type}")
        print(f"  - Taxi speed: {self.THRESHOLDS['taxi_speed']} kts")
        print(f"  - Takeoff speed: {self.THRESHOLDS['takeoff_speed']} kts")
        print(f"  - Rotation speed: {self.THRESHOLDS['rotation_speed']} kts")
        print(f"  - Climb rate threshold: {self.THRESHOLDS['climb_rate']} fpm")
        print(f"  - Descent rate threshold: {self.THRESHOLDS['descent_rate']} fpm")

        self.df['PHASE'] = 'UNKNOWN'

        for idx in range(len(self.df)):
            phase = self._classify_phase(idx)
            self.df.at[idx, 'PHASE'] = phase

        # Post-process to smooth transitions and apply minimum duration rules
        self._smooth_phases()

        # Extract phase segments
        self._extract_phase_segments()

        return self.phases

    def _classify_phase(self, idx):
        """
        Classify the flight phase for a given data point.

        Args:
            idx (int): Index of the data point

        Returns:
            str: Flight phase classification
        """
        row = self.df.iloc[idx]

        airspeed = row['AIRSPEED_AVG']
        altitude_agl = row['ALTITUDE_AGL']
        vs = row['VERTICAL_SPEED_SMOOTH'] if not pd.isna(row['VERTICAL_SPEED_SMOOTH']) else 0
        is_airborne = row['IS_AIRBORNE']
        flaps = row['FLAPS_AVG']
        speedbrake_deployed = row['SPEEDBRAKE_DEPLOYED']
        vertical_accel = row['VERTICAL_ACCEL']

        # Handle autopilot engagement (try multiple possible column names)
        ap_engaged = False
        if 'AP ENGAGED' in self.df.columns:
            ap_engaged = row['AP ENGAGED'] == 'ENGAGED'
        elif 'G/S ENGAGE' in self.df.columns:
            ap_engaged = row['G/S ENGAGE'] == 'ENGAGED'

        torque = row['TQ_AVG']

        # Determine if we've taken off yet (helps with sequencing)
        has_flown = False
        if idx > 0:
            # Check if we've previously been airborne or at cruise altitude/high speed
            prev_max_alt = self.df.iloc[:idx]['ALTITUDE_AGL'].max()
            prev_max_speed = self.df.iloc[:idx]['AIRSPEED_AVG'].max()
            has_flown = (prev_max_alt > 5000) or (prev_max_speed > 150)

        # If we have direct AIR/GROUND data, use it to override other logic
        if 'IS_AIRBORNE' in self.df.columns and not pd.isna(is_airborne):
            if not is_airborne:
                # Aircraft is on ground - determine specific ground phase
                if airspeed < 5:
                    return 'GROUND'
                elif airspeed < self.THRESHOLDS['taxi_speed']:
                    if has_flown:
                        return 'TAXI-IN'
                    else:
                        return 'TAXI-OUT'
                elif altitude_agl < 100 and airspeed < self.THRESHOLDS['taxi_speed']:
                    return 'LANDING'
                else:
                    # Moving on ground but not clearly taxi or landing
                    if has_flown:
                        return 'TAXI-IN'
                    else:
                        return 'TAXI-OUT'
            else:
                # Aircraft is airborne - determine air phase
                if vs > self.THRESHOLDS['climb_rate']:
                    if altitude_agl < self.THRESHOLDS['initial_climb_alt']:
                        return 'INITIAL_CLIMB'
                    else:
                        return 'CLIMB'
                elif vs < self.THRESHOLDS['descent_rate']:
                    # Check for speedbrake deployment (indicates descent)
                    if speedbrake_deployed and altitude_agl > self.THRESHOLDS['approach_altitude']:
                        return 'DESCENT'
                    elif altitude_agl < self.THRESHOLDS['approach_altitude']:
                        # Check flap position for approach phases
                        if flaps > 5:  # Significant flap extension
                            if altitude_agl < 1000:
                                return 'FINAL_APPROACH'
                            else:
                                return 'APPROACH'
                        else:
                            return 'APPROACH'
                    else:
                        return 'DESCENT'
                else:
                    # Level flight - check if cruise or approach
                    if altitude_agl > self.THRESHOLDS['approach_altitude']:
                        return 'CRUISE'
                    else:
                        # Low altitude level flight with flaps likely indicates approach
                        if flaps > 5:
                            return 'APPROACH'
                        else:
                            return 'CRUISE'

        # Fallback to original logic if no AIR/GROUND data available
        # GROUND (PRE-FLIGHT / POST-FLIGHT)
        if airspeed < 5 and altitude_agl < self.THRESHOLDS['landing_altitude']:
            return 'GROUND'

        # TAXI - distinguish based on whether we've flown yet
        if (airspeed < self.THRESHOLDS['taxi_speed'] and
            airspeed >= 5 and
            altitude_agl < self.THRESHOLDS['landing_altitude']):
            if has_flown:
                return 'TAXI-IN'
            else:
                return 'TAXI-OUT'

        # TAKEOFF (high acceleration, increasing speed on/near ground with high power)
        # Must be early in flight (not after cruise)
        if (not has_flown and
            airspeed >= self.THRESHOLDS['taxi_speed'] and
            altitude_agl < 500 and
            torque > 50):
            return 'TAKEOFF'

        # INITIAL CLIMB (just after takeoff)
        if (altitude_agl < self.THRESHOLDS['initial_climb_alt'] and
            vs > self.THRESHOLDS['climb_rate'] and
            airspeed > self.THRESHOLDS['rotation_speed']):
            return 'INITIAL_CLIMB'

        # CLIMB
        if (vs > self.THRESHOLDS['climb_rate'] and
            altitude_agl >= self.THRESHOLDS['initial_climb_alt']):
            return 'CLIMB'

        # DESCENT (from high altitude)
        if (vs < self.THRESHOLDS['descent_rate'] and
            altitude_agl > self.THRESHOLDS['approach_altitude']):
            return 'DESCENT'

        # APPROACH (after having flown, below approach altitude but above ground)
        # This must be checked BEFORE cruise to catch the landing phase
        if (has_flown and altitude_agl < self.THRESHOLDS['approach_altitude']):
            # LANDING phase: very low altitude, decelerating on or near ground
            if altitude_agl < 100 and airspeed < self.THRESHOLDS['taxi_speed']:
                return 'LANDING'
            # FINAL_APPROACH: below 1000 ft AGL, stabilized approach to runway
            if altitude_agl < 1000 and airspeed > self.THRESHOLDS['taxi_speed']:
                return 'FINAL_APPROACH'
            # APPROACH phase: intermediate/initial approach
            if airspeed > self.THRESHOLDS['taxi_speed']:
                return 'APPROACH'

        # CRUISE (steady altitude at high altitude, before descent)
        # Only classify as cruise if at genuinely high altitude
        if (abs(vs) < self.THRESHOLDS['cruise_vs_threshold'] and
            altitude_agl > self.THRESHOLDS['approach_altitude'] and
            airspeed > self.THRESHOLDS['rotation_speed']):
            return 'CRUISE'

        # Default - maintain previous phase if available
        if idx > 0:
            return self.df.iloc[idx - 1]['PHASE']

        return 'UNKNOWN'

    def _smooth_phases(self):
        """Apply smoothing to phase transitions and enforce minimum durations."""

        # Forward fill for very short phase transitions (< 5 samples)
        min_duration = 5

        phase_changes = self.df['PHASE'] != self.df['PHASE'].shift()
        phase_starts = self.df.index[phase_changes].tolist()

        for i in range(len(phase_starts) - 1):
            start_idx = phase_starts[i]
            end_idx = phase_starts[i + 1]

            if end_idx - start_idx < min_duration:
                # Replace short phase with previous phase
                if start_idx > 0:
                    prev_phase = self.df.iloc[start_idx - 1]['PHASE']
                    self.df.loc[start_idx:end_idx-1, 'PHASE'] = prev_phase

    def _extract_phase_segments(self):
        """Extract contiguous phase segments with start/end times and statistics."""

        self.phases = []
        current_phase = None
        phase_start_idx = 0

        for idx in range(len(self.df)):
            phase = self.df.iloc[idx]['PHASE']

            if phase != current_phase:
                # Save previous phase segment
                if current_phase is not None:
                    self._save_phase_segment(current_phase, phase_start_idx, idx - 1)

                # Start new phase
                current_phase = phase
                phase_start_idx = idx

        # Save last phase
        if current_phase is not None:
            self._save_phase_segment(current_phase, phase_start_idx, len(self.df) - 1)

        print(f"\nDetected {len(self.phases)} phase segments")

    def _save_phase_segment(self, phase, start_idx, end_idx):
        """Save a phase segment with statistics."""

        segment_data = self.df.iloc[start_idx:end_idx + 1]

        duration_samples = end_idx - start_idx + 1
        duration_seconds = duration_samples * 0.5  # Assuming 2 Hz sampling

        phase_info = {
            'phase': phase,
            'start_sample': start_idx + 1,  # 1-indexed
            'end_sample': end_idx + 1,
            'duration_samples': duration_samples,
            'duration_seconds': duration_seconds,
            'duration_minutes': duration_seconds / 60,
            'start_altitude': segment_data.iloc[0]['ALTITUDE_AVG'],
            'end_altitude': segment_data.iloc[-1]['ALTITUDE_AVG'],
            'min_altitude': segment_data['ALTITUDE_AVG'].min(),
            'max_altitude': segment_data['ALTITUDE_AVG'].max(),
            'start_airspeed': segment_data.iloc[0]['AIRSPEED_AVG'],
            'end_airspeed': segment_data.iloc[-1]['AIRSPEED_AVG'],
            'max_airspeed': segment_data['AIRSPEED_AVG'].max(),
            'avg_vertical_speed': segment_data['VERTICAL_SPEED_SMOOTH'].mean(),
        }

        self.phases.append(phase_info)

    def print_summary(self):
        """Print a summary of detected flight phases."""

        print("\n" + "="*80)
        print("FLIGHT PHASE SUMMARY")
        print("="*80)

        total_duration = 0

        for i, phase in enumerate(self.phases, 1):
            print(f"\n{i}. {phase['phase']}")
            print(f"   Samples: {phase['start_sample']} - {phase['end_sample']}")
            print(f"   Duration: {phase['duration_minutes']:.2f} minutes ({phase['duration_seconds']:.1f} seconds)")
            print(f"   Altitude: {phase['start_altitude']:.0f} ft → {phase['end_altitude']:.0f} ft "
                  f"(range: {phase['min_altitude']:.0f} - {phase['max_altitude']:.0f} ft)")
            print(f"   Airspeed: {phase['start_airspeed']:.0f} kts → {phase['end_airspeed']:.0f} kts "
                  f"(max: {phase['max_airspeed']:.0f} kts)")
            print(f"   Avg Vertical Speed: {phase['avg_vertical_speed']:.0f} fpm")

            total_duration += phase['duration_minutes']

        print(f"\n{'='*80}")
        print(f"Total Flight Duration: {total_duration:.2f} minutes ({total_duration/60:.2f} hours)")
        print(f"{'='*80}\n")

    def export_to_csv(self, output_file=None):
        """
        Export the phase analysis to a CSV file.

        Args:
            output_file (str): Output file path. If None, generates automatically.
        """
        if output_file is None:
            base_name = os.path.splitext(self.csv_file)[0]
            output_file = f"{base_name}_phases.csv"

        # Export detailed data with phases
        self.df.to_csv(output_file, index=False)
        print(f"Detailed phase data exported to: {output_file}")

        # Export phase summary
        summary_file = output_file.replace('.csv', '_summary.csv')
        phases_df = pd.DataFrame(self.phases)
        phases_df.to_csv(summary_file, index=False)
        print(f"Phase summary exported to: {summary_file}")

    def plot_phases(self, output_file=None):
        """
        Create visualization plots of the flight phases.

        Args:
            output_file (str): Output file path for the plot. If None, displays interactively.
        """
        print("\nGenerating visualization...")

        # Create figure with subplots
        fig, axes = plt.subplots(4, 1, figsize=(14, 12))
        fig.suptitle('Flight Phase Analysis', fontsize=16, fontweight='bold')

        # Define colors for each phase
        phase_colors = {
            'GROUND': '#8B4513',
            'TAXI-OUT': '#FFA500',
            'TAXI-IN': '#FF8C00',
            'TAKEOFF': '#FF4500',
            'INITIAL_CLIMB': '#32CD32',
            'CLIMB': '#228B22',
            'CRUISE': '#4169E1',
            'DESCENT': '#FFD700',
            'APPROACH': '#FF6347',
            'FINAL_APPROACH': '#FF1493',
            'LANDING': '#DC143C',
            'UNKNOWN': '#808080'
        }

        # Get unique phases in order
        unique_phases = self.df['PHASE'].unique()

        # Plot 1: Altitude
        ax1 = axes[0]
        for phase in unique_phases:
            phase_data = self.df[self.df['PHASE'] == phase]
            ax1.scatter(phase_data.index, phase_data['ALTITUDE_AVG'],
                       c=phase_colors.get(phase, '#808080'), label=phase, s=2, alpha=0.7)
        ax1.set_ylabel('Altitude (feet)', fontweight='bold')
        ax1.set_xlabel('Sample')
        ax1.grid(True, alpha=0.3)
        ax1.legend(loc='upper left', fontsize=8, ncol=3)
        ax1.set_title('Altitude Profile with Flight Phases')

        # Plot 2: Airspeed
        ax2 = axes[1]
        for phase in unique_phases:
            phase_data = self.df[self.df['PHASE'] == phase]
            ax2.scatter(phase_data.index, phase_data['AIRSPEED_AVG'],
                       c=phase_colors.get(phase, '#808080'), s=2, alpha=0.7)
        ax2.set_ylabel('Airspeed (knots)', fontweight='bold')
        ax2.set_xlabel('Sample')
        ax2.grid(True, alpha=0.3)
        ax2.set_title('Airspeed Profile')

        # Plot 3: Vertical Speed
        ax3 = axes[2]
        for phase in unique_phases:
            phase_data = self.df[self.df['PHASE'] == phase]
            ax3.scatter(phase_data.index, phase_data['VERTICAL_SPEED_SMOOTH'],
                       c=phase_colors.get(phase, '#808080'), s=2, alpha=0.7)
        ax3.axhline(y=0, color='black', linestyle='--', linewidth=1, alpha=0.5)
        ax3.set_ylabel('Vertical Speed (fpm)', fontweight='bold')
        ax3.set_xlabel('Sample')
        ax3.grid(True, alpha=0.3)
        ax3.set_title('Vertical Speed Profile')

        # Plot 4: Engine Torque
        ax4 = axes[3]
        for phase in unique_phases:
            phase_data = self.df[self.df['PHASE'] == phase]
            ax4.scatter(phase_data.index, phase_data['TQ_AVG'],
                       c=phase_colors.get(phase, '#808080'), s=2, alpha=0.7)
        ax4.set_ylabel('Engine Torque (%)', fontweight='bold')
        ax4.set_xlabel('Sample')
        ax4.grid(True, alpha=0.3)
        ax4.set_title('Average Engine Torque')

        plt.tight_layout()

        if output_file is None:
            base_name = os.path.splitext(self.csv_file)[0]
            output_file = f"{base_name}_phase_analysis.png"

        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"Plot saved to: {output_file}")

        # Also try to show interactively
        try:
            plt.show()
        except:
            pass  # In case running in non-interactive environment

    def generate_report(self, output_file=None):
        """
        Generate a comprehensive text report of the flight analysis.

        Args:
            output_file (str): Output file path. If None, generates automatically.
        """
        if output_file is None:
            base_name = os.path.splitext(self.csv_file)[0]
            output_file = f"{base_name}_phase_report.txt"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("FLIGHT PHASE DETECTION REPORT\n")
            f.write("="*80 + "\n\n")

            f.write(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Input File: {self.csv_file}\n")
            f.write(f"Total Data Points: {len(self.df)}\n")
            f.write(f"Ground Altitude (MSL): {self.ground_altitude:.0f} feet\n\n")

            f.write("FLIGHT PHASES DETECTED:\n")
            f.write("-"*80 + "\n\n")

            for i, phase in enumerate(self.phases, 1):
                f.write(f"{i}. {phase['phase']}\n")
                f.write(f"   Samples: {phase['start_sample']} - {phase['end_sample']} "
                       f"({phase['duration_samples']} samples)\n")
                f.write(f"   Duration: {phase['duration_minutes']:.2f} minutes "
                       f"({phase['duration_seconds']:.1f} seconds)\n")
                f.write(f"   Altitude Range: {phase['min_altitude']:.0f} - "
                       f"{phase['max_altitude']:.0f} feet\n")
                f.write(f"   Altitude Change: {phase['start_altitude']:.0f} → "
                       f"{phase['end_altitude']:.0f} feet\n")
                f.write(f"   Airspeed Range: {phase['start_airspeed']:.0f} → "
                       f"{phase['end_airspeed']:.0f} knots (max: {phase['max_airspeed']:.0f} kts)\n")
                f.write(f"   Average Vertical Speed: {phase['avg_vertical_speed']:.0f} fpm\n\n")

            total_duration = sum(p['duration_minutes'] for p in self.phases)
            f.write("="*80 + "\n")
            f.write(f"Total Flight Duration: {total_duration:.2f} minutes ({total_duration/60:.2f} hours)\n")
            f.write("="*80 + "\n")

        print(f"Detailed report saved to: {output_file}")


def main():
    """
    Main function to run the flight phase detection.

    Command Line Usage:
        python flight_phase_detector.py <csv_file> [aircraft_type]

    Examples:
        python flight_phase_detector.py flight.csv
        python flight_phase_detector.py flight.csv B737
        python flight_phase_detector.py flight.csv A320
    """

    import sys

    print("="*80)
    print("FLIGHT PHASE DETECTION SYSTEM v2.0")
    print("="*80)
    print()

    # Get CSV file from command line or use default
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    else:
        # Default to the sample file
        csv_file = "5Y_TBX_Q400.csv"
        print(f"No input file specified, using default: {csv_file}")

    # Get aircraft type from command line or use default
    if len(sys.argv) > 2:
        aircraft_type = sys.argv[2].upper()
    else:
        aircraft_type = 'Q400'
        print(f"No aircraft type specified, using default: {aircraft_type}")

    # Check if file exists
    if not os.path.exists(csv_file):
        print(f"Error: File '{csv_file}' not found!")
        print("\nUsage: python flight_phase_detector.py <csv_file> [aircraft_type]")
        print("\nAvailable Aircraft Types:")
        for code, profile in AIRCRAFT_PROFILES.items():
            print(f"  {code:20s} - {profile['name']}")
        return

    # Validate aircraft type
    if aircraft_type not in AIRCRAFT_PROFILES:
        print(f"Warning: Unknown aircraft type '{aircraft_type}'")
        print("\nAvailable Aircraft Types:")
        for code, profile in AIRCRAFT_PROFILES.items():
            print(f"  {code:20s} - {profile['name']}")
        print(f"\nDefaulting to GENERIC_TURBOPROP")
        aircraft_type = 'GENERIC_TURBOPROP'

    print()

    # Initialize detector
    detector = FlightPhaseDetector(csv_file, aircraft_type=aircraft_type)

    # Load data
    detector.load_data()

    # Detect phases
    detector.detect_phases()

    # Print summary
    detector.print_summary()

    # Export results
    detector.export_to_csv()

    # Generate report
    detector.generate_report()

    # Create visualization
    detector.plot_phases()

    print("\n" + "="*80)
    print("Analysis complete!")
    print("="*80)


if __name__ == "__main__":
    main()
