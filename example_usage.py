"""
Quick Start Example for Flight Phase Detection
==============================================

This file demonstrates various ways to use the flight phase detector,
including aircraft-specific profiles and custom configurations.
"""

from flight_phase_detector import FlightPhaseDetector
import os


def quick_analysis(csv_file, aircraft_type='Q400'):
    """
    Perform a quick flight phase analysis on a CSV file.
    
    Args:
        csv_file (str): Path to the flight data CSV file
        aircraft_type (str): Aircraft type profile to use (Q400, B737, A320, etc.)
    """
    
    print("="*60)
    print("QUICK FLIGHT PHASE ANALYSIS")
    print("="*60)
    print()
    
    # Check if file exists
    if not os.path.exists(csv_file):
        print(f"Error: File '{csv_file}' not found!")
        return
    
    # Create detector instance with aircraft type
    print(f"Analyzing: {csv_file}")
    print(f"Aircraft Type: {aircraft_type}\n")
    detector = FlightPhaseDetector(csv_file, aircraft_type=aircraft_type)
    
    # Load data
    print("Step 1: Loading data...")
    detector.load_data()
    print("✓ Data loaded successfully\n")
    
    # Detect phases
    print("Step 2: Detecting flight phases...")
    phases = detector.detect_phases()
    print(f"✓ Detected {len(phases)} phase segments\n")
    
    # Print summary
    print("Step 3: Generating summary...")
    detector.print_summary()
    
    # Export results
    print("\nStep 4: Exporting results...")
    detector.export_to_csv()
    print("✓ CSV files exported\n")
    
    # Generate report
    print("Step 5: Generating report...")
    detector.generate_report()
    print("✓ Report generated\n")
    
    # Create plots
    print("Step 6: Creating visualizations...")
    detector.plot_phases()
    print("✓ Plots saved\n")
    
    print("="*60)
    print("ANALYSIS COMPLETE!")
    print("="*60)
    
    # List output files
    base_name = os.path.splitext(csv_file)[0]
    print("\nOutput files created:")
    print(f"  1. {base_name}_phases.csv - Detailed data with phases")
    print(f"  2. {base_name}_phases_summary.csv - Phase summary table")
    print(f"  3. {base_name}_phase_report.txt - Comprehensive text report")
    print(f"  4. {base_name}_phase_analysis.png - Visualization plots")
    print()


def compare_flights(csv_files):
    """
    Compare multiple flights and print basic statistics.
    
    Args:
        csv_files (list): List of CSV file paths
    """
    
    print("="*60)
    print("FLIGHT COMPARISON")
    print("="*60)
    print()
    
    results = []
    
    for csv_file in csv_files:
        if not os.path.exists(csv_file):
            print(f"Warning: Skipping '{csv_file}' - file not found")
            continue
        
        detector = FlightPhaseDetector(csv_file)
        detector.load_data()
        detector.detect_phases()
        
        # Collect statistics
        total_duration = sum(p['duration_minutes'] for p in detector.phases)
        max_altitude = max(p['max_altitude'] for p in detector.phases)
        max_speed = max(p['max_airspeed'] for p in detector.phases)
        
        results.append({
            'file': csv_file,
            'duration': total_duration,
            'max_altitude': max_altitude,
            'max_speed': max_speed,
            'phases': len(detector.phases)
        })
    
    # Print comparison table
    print(f"{'File':<30} {'Duration':<12} {'Max Alt':<12} {'Max Speed':<12} {'Phases':<8}")
    print("-"*76)
    
    for r in results:
        print(f"{os.path.basename(r['file']):<30} "
              f"{r['duration']:>8.1f} min  "
              f"{r['max_altitude']:>8.0f} ft  "
              f"{r['max_speed']:>8.0f} kts  "
              f"{r['phases']:>6}")
    
    print()


if __name__ == "__main__":
    # Example 1: Analyze a single flight with default (Q400) profile
    print("Example 1: Single Flight Analysis (Q400 Profile)")
    print("-"*60)
    quick_analysis("5Y_TBX_Q400.csv", aircraft_type='Q400')
    
    # Example 2: Using different aircraft profiles
    print("\n\nExample 2: Aircraft Profile Selection")
    print("-"*60)
    
    # Turboprop analysis
    print("\nAnalyzing with Q400 profile:")
    detector_q400 = FlightPhaseDetector("5Y_TBX_Q400.csv", aircraft_type='Q400')
    detector_q400.load_data()
    phases_q400 = detector_q400.detect_phases()
    print(f"✓ Detected {len(phases_q400)} phase segments with Q400 profile")
    
    # Jet analysis (hypothetical)
    print("\nExample of B737 profile usage:")
    print("detector = FlightPhaseDetector('737_flight.csv', aircraft_type='B737')")
    print("detector.load_data()")
    print("phases = detector.detect_phases()")
    
    print("\nExample of A320 profile usage:")
    print("detector = FlightPhaseDetector('a320_flight.csv', aircraft_type='A320')")
    
    print("\nAvailable aircraft types:")
    print("  - Q400 (Regional Turboprop)")
    print("  - ATR72 (Regional Turboprop)")
    print("  - B737 (Narrow-Body Jet)")
    print("  - A320 (Narrow-Body Jet)")
    print("  - B777 (Wide-Body Jet)")
    print("  - GENERIC_TURBOPROP (Generic)")
    print("  - GENERIC_JET (Generic)")
    
    # Example 3: Custom threshold analysis
    print("\n\nExample 3: Custom Threshold Analysis")
    print("-"*60)
    
    # Start with B737 profile and customize
    custom_thresholds = {
        'cruise_vs_threshold': 150,    # Stricter cruise definition
        'takeoff_speed': 95,            # Adjust for specific conditions
        'approach_altitude': 2500,      # Different airport procedures
    }
    
    print("Using B737 profile with custom threshold overrides:")
    print(f"  cruise_vs_threshold: {custom_thresholds['cruise_vs_threshold']} fpm")
    print(f"  takeoff_speed: {custom_thresholds['takeoff_speed']} knots")
    print(f"  approach_altitude: {custom_thresholds['approach_altitude']} ft AGL")
    
    detector = FlightPhaseDetector("5Y_TBX_Q400.csv", 'Q400', custom_thresholds)
    detector.load_data()
    detector.detect_phases()
    print("✓ Analysis complete with custom thresholds")
    
    # Example 4: Access phase data programmatically
    print("\n\nExample 4: Programmatic Access to Phase Data")
    print("-"*60)
    detector = FlightPhaseDetector("5Y_TBX_Q400.csv", aircraft_type='Q400')
    detector.load_data()
    phases = detector.detect_phases()
    
    # Find the cruise phase
    cruise_phases = [p for p in phases if p['phase'] == 'CRUISE']
    if cruise_phases:
        print(f"\nFound {len(cruise_phases)} cruise segment(s):")
        for i, cruise in enumerate(cruise_phases, 1):
            print(f"\n  Cruise Segment {i}:")
            print(f"    Duration: {cruise['duration_minutes']:.1f} minutes")
            print(f"    Altitude: {cruise['max_altitude']:.0f} feet")
            print(f"    Speed: {cruise['max_airspeed']:.0f} knots")
    
    # Find takeoff phase
    takeoff_phases = [p for p in phases if p['phase'] == 'TAKEOFF']
    if takeoff_phases:
        takeoff = takeoff_phases[0]
        print(f"\nTakeoff Phase Details:")
        print(f"  Duration: {takeoff['duration_seconds']:.1f} seconds")
        print(f"  Speed at liftoff: {takeoff['end_airspeed']:.0f} knots")
        print(f"  Altitude gain: {takeoff['end_altitude'] - takeoff['start_altitude']:.0f} ft")
    
    # Find final approach
    final_approach = [p for p in phases if p['phase'] == 'FINAL_APPROACH']
    if final_approach:
        fa = final_approach[0]
        print(f"\nFinal Approach Phase Details:")
        print(f"  Duration: {fa['duration_minutes']:.2f} minutes")
        print(f"  Starting altitude: {fa['start_altitude']:.0f} ft")
        print(f"  Descent rate: {fa['avg_vertical_speed']:.0f} fpm")
    
    # Example 5: Compare different aircraft configurations
    print("\n\nExample 5: Understanding Aircraft Profiles")
    print("-"*60)
    
    print("\nThreshold comparison between aircraft types:")
    print(f"{'Parameter':<25} {'Q400':<12} {'B737':<12} {'B777':<12}")
    print("-"*61)
    
    # Sample threshold comparisons (you can expand this)
    params = [
        ('Takeoff Speed', '80 kts', '100 kts', '120 kts'),
        ('Rotation Speed', '100 kts', '140 kts', '160 kts'),
        ('Climb Rate', '500 fpm', '800 fpm', '1000 fpm'),
        ('Typical Cruise Alt', '25,000 ft', '37,000 ft', '39,000 ft'),
        ('Typical Cruise Speed', '360 kts', '450 kts', '490 kts'),
    ]
    
    for param, q400, b737, b777 in params:
        print(f"{param:<25} {q400:<12} {b737:<12} {b777:<12}")
    
    print("\nFor complete threshold tables, see AIRCRAFT_CONFIGURATIONS.md")
    
    print("\n" + "="*60)
    print("All examples completed!")
    print("="*60)
    print("\nNext steps:")
    print("  1. Try analyzing your own flight data")
    print("  2. Select the appropriate aircraft profile")
    print("  3. Customize thresholds if needed")
    print("  4. Review AIRCRAFT_CONFIGURATIONS.md for detailed settings")

