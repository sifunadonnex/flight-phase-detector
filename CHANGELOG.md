# Changelog

All notable changes to the Flight Phase Detection System.

## [2.0.0] - 2025

### Added - Multi-Aircraft Support
- **7 Predefined Aircraft Profiles**: Q400, ATR72, B737, A320, B777, GENERIC_TURBOPROP, GENERIC_JET
- **Aircraft-Specific Thresholds**: Optimized speed, rate, and altitude thresholds for each aircraft type
- **Command-Line Aircraft Selection**: `python flight_phase_detector.py <file> <aircraft_type>`
- **Custom Threshold Override**: Can start with a profile and override specific thresholds
- **AIRCRAFT_CONFIGURATIONS.md**: Comprehensive documentation of all aircraft profiles
- **REGULATORY_STANDARDS Dictionary**: FAA, EASA, IATA standards configuration

### Added - Enhanced Flight Phases
- **FINAL_APPROACH Phase**: Separate phase for stabilized approach below 1,000 ft AGL
- Now detects 12 distinct phases (previously 11)

### Fixed - Critical Issues
- **Phase Sequencing Bug**: Fixed "landing after taxi-out" issue with has_flown flag
- **Destination Altitude Handling**: Dynamic ground altitude calculation for airports at different elevations
- **Phase Detection Order**: Reordered logic to check APPROACH/LANDING before CRUISE

### Enhanced - Detection Algorithm
- **Dynamic Ground Altitude**: Automatically detects destination airport altitude from final samples
- **has_flown Flag**: Distinguishes departure vs arrival ground/taxi phases
- **Improved Phase Logic**: More robust classification preventing illogical transitions

### Enhanced - Documentation
- Updated README.md with aircraft profile usage
- Updated QUICKSTART.md with aircraft type selection examples
- Updated example_usage.py to demonstrate multi-aircraft features
- New AIRCRAFT_CONFIGURATIONS.md with detailed threshold tables
- Updated PROJECT_SUMMARY.md with v2.0 features

### Enhanced - User Experience
- Display aircraft type name on startup
- Show available aircraft types if invalid type provided
- Better error messages for file/column validation
- Display aircraft-specific thresholds in console output

---

## [1.0.0] - Initial Release

### Added
- Initial flight phase detection system
- Support for 11 flight phases
- CSV data processing
- Multiple output formats (CSV, TXT, PNG)
- Basic threshold configuration
- Comprehensive documentation

### Features
- Multi-parameter analysis (airspeed, altitude, vertical speed, torque)
- Signal smoothing and noise filtering
- Automatic ground altitude detection
- Phase transition smoothing
- Color-coded visualizations
- Text reports with statistics

### Documentation
- README.md - Complete user guide
- FLIGHT_PHASES_RESEARCH.md - Aviation research
- QUICKSTART.md - Quick start guide
- example_usage.py - Usage examples

---

## Version Numbering

- **Major version (X.0.0)**: Breaking changes or major feature additions
- **Minor version (1.X.0)**: New features, backward compatible
- **Patch version (1.0.X)**: Bug fixes, minor improvements

---

## Upgrade Notes

### From 1.0 to 2.0

**Breaking Changes:**
- `FlightPhaseDetector.__init__()` now accepts `aircraft_type` parameter (defaults to 'Q400' for backward compatibility)
- FINAL_APPROACH is now a separate phase (may affect phase counting in existing scripts)

**Recommended Migration:**
```python
# Old (v1.0)
detector = FlightPhaseDetector('flight.csv')

# New (v2.0) - Still works, uses Q400 by default
detector = FlightPhaseDetector('flight.csv')

# New (v2.0) - Recommended: Specify aircraft type explicitly
detector = FlightPhaseDetector('flight.csv', aircraft_type='Q400')
```

**Benefits of Upgrading:**
1. More accurate detection with aircraft-specific thresholds
2. Fixed critical bugs (destination altitude, phase sequencing)
3. FINAL_APPROACH phase for stabilized approach analysis
4. Better documentation and examples
5. Easier customization with aircraft profiles

---

## Future Roadmap

### Planned Features
- [ ] Additional aircraft types (A350, B787, regional jets)
- [ ] Helicopter flight profiles
- [ ] Real-time analysis mode
- [ ] Machine learning-based phase detection
- [ ] Integration with flight planning systems
- [ ] API for cloud-based analysis
- [ ] Web-based visualization dashboard
- [ ] Mobile app for quick analysis

### Under Consideration
- [ ] Support for additional data formats (Parquet, HDF5)
- [ ] Anomaly detection within phases
- [ ] Performance benchmarking against flight plan
- [ ] Fuel efficiency analysis by phase
- [ ] Weather integration
- [ ] Automated report generation to PDF

---

## Contributors

- Initial development and v1.0 release
- v2.0 multi-aircraft support and enhancements

---

## License

MIT License - See LICENSE file for details
